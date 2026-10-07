"""매일 1회 실행되는 연구 루프.

데이터를 3구간으로 나눠 과최적화를 막는다:
  학습(train, 앞 60%)  → 유전 알고리즘이 이 구간 성과로만 진화
  검증(valid, 다음 20%) → 명예의 전당 입성 심사
  시험(test, 마지막 20%) → 순위 매기기에 쓰지 않고 보고만 함
그리고 전당에 오른 날 이후의 '전진 성과(forward)'를 매일 추적한다 — 진짜 미래 데이터.
"""
from __future__ import annotations

import json
import random
import time
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import backtest as bt
from . import data as dataio
from . import report
from .strategy import crossover, describe, key, mutate, random_strategy

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results"
KST = timezone(timedelta(hours=9))


def load_config():
    return json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def split(df):
    n = len(df)
    a, b = int(n * 0.6), int(n * 0.8)
    return df.iloc[:a], df.iloc[a:b], df.iloc[b:]


class Evaluator:
    def __init__(self, frames: dict[str, pd.DataFrame], cfg: dict):
        self.frames, self.cfg, self.iv = frames, cfg, cfg["interval"]
        self.cache: dict[str, dict] = {}
        self.strats: dict[str, dict] = {}

    def _segments(self, s):
        """전체 구간을 한 번 돌린 뒤 수익률을 구간별로 잘라 쓴다 (지표 워밍업 공유)."""
        out = {}
        for m, df in self.frames.items():
            r = bt.run(df, s)
            n = len(r)
            a, b = int(n * 0.6), int(n * 0.8)
            out[m] = {"train": r[:a], "valid": r[a:b], "test": r[b:], "all": r}
        return out

    def evaluate(self, s) -> dict:
        k = key(s)
        self.strats.setdefault(k, s)
        if k in self.cache:
            return self.cache[k]
        try:
            seg = self._segments(s)
        except Exception:
            res = {"fitness": -99}
            self.cache[k] = res
            return res
        res = {}
        for part in ("train", "valid", "test"):
            per = {m: bt.metrics(seg[m][part], self.iv) for m in seg}
            res[part] = {
                "sharpe": float(np.median([x["sharpe"] for x in per.values()])),
                "cagr": float(np.median([x["cagr"] for x in per.values()])),
                "mdd": float(np.median([x["mdd"] for x in per.values()])),
                "trades": int(np.sum([x["trades"] for x in per.values()])),
                "exposure": float(np.mean([x["exposure"] for x in per.values()])),
                "per_market": per,
            }
        tr = res["train"]
        min_tr = self.cfg["min_trades_train"] * len(self.frames)
        # 적합도: 여러 코인에서의 중앙 샤프. 거래가 너무 적거나 낙폭이 크면 벌점.
        worst = min(x["sharpe"] for x in tr["per_market"].values())
        fit = 0.7 * tr["sharpe"] + 0.3 * worst
        if tr["trades"] < min_tr:
            fit -= 2.0 * (1 - tr["trades"] / min_tr)
        if tr["mdd"] < -0.5:
            fit -= (abs(tr["mdd"]) - 0.5) * 3
        # 복잡도 벌점 (조건이 많을수록 과최적화 위험)
        fit -= 0.03 * (len(s["entry"]) + len(s["exit"]))
        res["fitness"] = float(fit)
        self.cache[k] = res
        return res


def evolve(ev: Evaluator, seeds: list[dict], cfg: dict, budget_s: float, log: list[str]):
    pop_size = cfg["population"]
    pop = [x for x in seeds][: pop_size // 3]
    while len(pop) < pop_size:
        pop.append(random_strategy())
    start, gen, best_hist = time.time(), 0, []
    while time.time() - start < budget_s:
        scored = sorted(pop, key=lambda s: ev.evaluate(s)["fitness"], reverse=True)
        best_hist.append(ev.evaluate(scored[0])["fitness"])
        elite = scored[: max(4, pop_size // 8)]

        def pick():  # 토너먼트 선택
            return max(random.sample(scored[: pop_size // 2], 3), key=lambda s: ev.evaluate(s)["fitness"])

        nxt = list(elite)
        while len(nxt) < pop_size:
            r = random.random()
            if r < 0.15:
                nxt.append(random_strategy())  # 새로운 아이디어 주입
            elif r < 0.45:
                nxt.append(mutate(crossover(pick(), pick())))
            else:
                nxt.append(mutate(pick()))
        pop = nxt
        gen += 1
        # 정체되면 절반을 갈아엎어 다양성 확보
        if len(best_hist) >= 10 and best_hist[-1] - best_hist[-10] < 1e-6:
            pop = pop[: pop_size // 2] + [random_strategy() for _ in range(pop_size - pop_size // 2)]
            best_hist.clear()
    log.append(f"- {gen}세대 진화, 전략 {len(ev.cache):,}개 평가")
    return sorted(ev.cache.items(), key=lambda kv: kv[1]["fitness"], reverse=True)


def forward_metrics(ev: Evaluator, s: dict, since: str) -> dict | None:
    t0 = pd.Timestamp(since)
    per = {}
    for m, df in ev.frames.items():
        mask = (df["time"] > t0).to_numpy()
        if mask.sum() < 2:
            return None
        r = bt.run(df, s)[mask]
        per[m] = bt.metrics(r, ev.iv)
    return {
        "bars": int(mask.sum()),
        "total": float(np.mean([x["total"] for x in per.values()])),
        "mdd": float(np.median([x["mdd"] for x in per.values()])),
    }


def main():
    cfg = load_config()
    RES.mkdir(exist_ok=True)
    random.seed()
    today = datetime.now(KST).strftime("%Y-%m-%d")
    log = [f"## {today}"]
    t_start = time.time()

    # 1) 데이터 업데이트
    frames = {}
    for m in cfg["markets"]:
        try:
            df = dataio.load(m, cfg["interval"], cfg["max_bars"], refresh=not cfg.get("offline"))
            if len(df) > 300:
                frames[m] = df
        except Exception as e:
            log.append(f"- ⚠️ {m} 데이터 실패: {e}")
    if not frames:
        raise SystemExit("데이터를 하나도 받지 못했습니다.")
    last = max(df["time"].max() for df in frames.values())
    log.append(f"- 데이터: {', '.join(frames)} · {cfg['interval']} · 마지막 봉 {last:%Y-%m-%d %H:%M} UTC")

    ev = Evaluator(frames, cfg)
    hof_path = RES / "hall_of_fame.json"
    hof = json.loads(hof_path.read_text(encoding="utf-8")) if hof_path.exists() else []

    # 2) 기존 명예의 전당 재평가 (데이터가 하루 늘었으므로)
    for h in hof:
        h["eval"] = ev.evaluate(h["strategy"])
        h["forward"] = forward_metrics(ev, h["strategy"], h["since_bar"])

    # 3) 진화 — 기존 상위 전략을 씨앗으로
    seeds = [h["strategy"] for h in sorted(hof, key=lambda h: h["eval"]["fitness"], reverse=True)]
    budget = cfg["minutes"] * 60 - (time.time() - t_start) - 60
    ranked = evolve(ev, seeds, cfg, max(budget, 30), log)

    # 4) 검증 구간 심사 → 명예의 전당 입성
    known = {key(h["strategy"]) for h in hof}
    added = []
    bh_valid = np.median([bt.buy_hold(split(df)[1], cfg["interval"])["sharpe"] for df in frames.values()])
    def ret_vec(s):  # 학습+검증 구간 수익률을 이어 붙인 벡터 (시험 구간은 보지 않음)
        return np.concatenate([bt.run(df, s)[: int(len(df) * 0.8)] for df in frames.values()])

    accepted_vecs = [ret_vec(h["strategy"]) for h in hof]
    for k, res in ranked[: cfg["candidates_checked"]]:
        if k in known or res.get("fitness", -99) < cfg["min_fitness"]:
            continue
        v = res["valid"]
        if v["sharpe"] < cfg["min_valid_sharpe"] or v["trades"] < cfg["min_trades_valid"]:
            continue
        # 학습/검증 성과 차이가 너무 크면 과최적화로 간주
        if v["sharpe"] < 0.4 * res["train"]["sharpe"]:
            continue
        # 이미 있는 전략과 거의 똑같이 움직이면 중복으로 보고 건너뜀
        vec = ret_vec(ev.strats[k])
        if vec.std() == 0 or any(np.corrcoef(vec, w)[0, 1] > cfg["max_corr"] for w in accepted_vecs if w.std() > 0):
            continue
        accepted_vecs.append(vec)
        added.append(k)
        if len(added) >= cfg["max_new_per_day"]:
            break

    for k in added:
        s = ev.strats[k]
        hof.append(
            {
                "id": k,
                "found": today,
                "since_bar": str(last),
                "strategy": s,
                "desc": describe(s),
                "eval": ev.evaluate(s),
                "forward": None,
            }
        )
    log.append(f"- 새로 명예의 전당 입성: {len(added)}개 (검증 구간 B&H 샤프 {bh_valid:.2f})")

    # 5) 정리: 점수순 정렬, 최대 개수 유지. 전진 성과가 크게 망가진 전략은 퇴출.
    def rank_score(h):
        e = h["eval"]
        score = 0.5 * e["valid"]["sharpe"] + 0.5 * e["train"]["sharpe"]
        f = h.get("forward")
        if f and f["bars"] >= cfg["forward_min_bars"]:
            score += 0.5 * np.sign(f["total"]) * min(abs(f["total"]) * 5, 1)
        return score

    retired = [h for h in hof if h.get("forward") and h["forward"]["bars"] >= cfg["forward_min_bars"]
               and h["forward"]["mdd"] < cfg["retire_forward_mdd"]]
    hof = [h for h in hof if h not in retired]
    hof.sort(key=rank_score, reverse=True)
    if len(hof) > cfg["hof_size"]:
        retired += hof[cfg["hof_size"]:]
        hof = hof[: cfg["hof_size"]]
    if retired:
        log.append(f"- 퇴출: {', '.join(h['id'] for h in retired)}")
    for h in hof:
        h["rank_score"] = float(rank_score(h))

    hof_path.write_text(json.dumps(hof, ensure_ascii=False, indent=1, default=float), encoding="utf-8")

    # 6) 보고서
    summary = report.write(hof, frames, cfg, log, today, added)
    log.append(f"- 소요 {(time.time() - t_start) / 60:.1f}분")
    jp = RES / "journal.md"
    prev = jp.read_text(encoding="utf-8") if jp.exists() else "# 연구 일지\n"
    head, _, rest = prev.partition("\n")
    jp.write_text(head + "\n\n" + "\n".join(log) + "\n" + rest, encoding="utf-8")
    report.notify(summary)
    print("\n".join(log))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        raise
