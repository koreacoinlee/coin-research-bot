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
import threading
import time
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import backtest as bt
from . import data as dataio
from . import gates
from . import hof as H
from . import report
from .strategy import crossover, describe, key, mutate, random_strategy
from .util import atomic_write_json, atomic_write_text, read_json

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


def fetch_with_deadline(market: str, cfg: dict):
    """새 시세 받기를 별도 스레드에서 돌리고, 제한 시간을 넘기면 포기한다.
    (DNS 조회처럼 urlopen 의 timeout 이 적용되지 않는 곳에서 멈추는 경우까지 막기 위함)"""
    box = {}

    def work():
        try:
            box["df"] = dataio.load(market, cfg["interval"], cfg["max_bars"], refresh=True)
        except Exception as e:  # noqa: BLE001
            box["err"] = e

    th = threading.Thread(target=work, daemon=True)
    th.start()
    th.join(cfg.get("fetch_timeout_s", 180))
    if th.is_alive():
        raise TimeoutError(f"{cfg.get('fetch_timeout_s', 180)}초 안에 응답 없음")
    if "err" in box:
        raise box["err"]
    return box["df"]


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
        df = None
        if not cfg.get("offline"):
            # 업비트 응답이 없거나 네트워크가 멈춰도 연구 전체가 날아가지 않게 시간 제한을 두고,
            # 실패하면 저장돼 있던 시세로 계속 진행한다 (전진 성과만 그 회차에 갱신되지 않음).
            try:
                df = fetch_with_deadline(m, cfg)
            except Exception as e:
                log.append(f"- ⚠️ {m} 새 시세 받기 실패 → 저장된 시세로 진행 ({type(e).__name__}: {str(e)[:80]})")
        if df is None:
            try:
                df = dataio.load(m, cfg["interval"], cfg["max_bars"], refresh=False)
            except Exception as e:
                log.append(f"- ⚠️ {m} 저장된 시세도 읽지 못함: {e}")
                continue
        for w in dataio.check(df, cfg["interval"]):
            log.append(f"- ⚠️ {m} 데이터 점검: {w}")
        if len(df) > 300:
            frames[m] = df
    if not frames:
        raise SystemExit("데이터를 하나도 받지 못했습니다.")
    last = max(df["time"].max() for df in frames.values())
    log.append(f"- 데이터: {', '.join(frames)} · {cfg['interval']} · 마지막 봉 {last:%Y-%m-%d %H:%M} UTC")

    ev = Evaluator(frames, cfg)
    hof_path = RES / "hall_of_fame.json"
    hof = read_json(hof_path, [])

    # 2) 기존 명예의 전당 재평가 (데이터가 늘었으므로)
    for h in hof:
        h["eval"] = ev.evaluate(h["strategy"])
        h["forward"] = H.forward_metrics(frames, h["strategy"], h["since_bar"], cfg["interval"])

    # 튼튼함 심사 도입 전에 들어온 전략은 한 번 소급 심사한다 (결과는 졸업 조건에 쓰임)
    if hof:
        bh_per0 = gates.bh_valid_sharpes(frames, cfg["interval"])
        legacy = [h for h in hof if "robustness" not in h or h["robustness"] is None]
        for h in legacy:
            h["robustness"] = gates.robustness(frames, h["strategy"], cfg, bh_per0, random.Random(h["id"]))
        if legacy:
            ok = sum(h["robustness"]["passed"] for h in legacy)
            log.append(f"- 기존 전략 튼튼함 소급 심사: {len(legacy)}개 중 {ok}개 통과")

    # 3) 진화 — 기존 상위 전략을 씨앗으로
    seeds = [h["strategy"] for h in sorted(hof, key=lambda h: h["eval"]["fitness"], reverse=True)]
    budget = cfg["minutes"] * 60 - (time.time() - t_start) - 60
    ranked = evolve(ev, seeds, cfg, max(budget, 30), log)

    # 4) 검증 구간 심사 → 명예의 전당 입성
    # 하루 입성 한도는 실행 횟수와 무관하게 '날짜' 기준으로 센다 (하루 여러 번 돌아도 과하게 늘지 않게)
    state_path = RES / "state.json"
    state = read_json(state_path, {})
    admitted = state.setdefault("admitted", {})
    quota = max(0, cfg["max_new_per_day"] - admitted.get(today, 0))
    known = {key(h["strategy"]) for h in hof}
    added = []
    bh_per = gates.bh_valid_sharpes(frames, cfg["interval"])
    bh_valid = float(np.median(list(bh_per.values())))
    rng = random.Random()
    robust_tried, robust_fail = 0, {}
    def ret_vec(s):  # 학습+검증 구간 수익률을 이어 붙인 벡터 (시험 구간은 보지 않음)
        return np.concatenate([bt.run(df, s)[: int(len(df) * 0.8)] for df in frames.values()])

    accepted_vecs = [ret_vec(h["strategy"]) for h in hof]
    # 입성 심사는 후보가 많으면 오래 걸릴 수 있어 시간 상한을 둔다 (작업 제한 55분 안에 끝나도록)
    admit_deadline = time.time() + cfg.get("admission_max_s", 300)
    for k, res in ranked[: cfg["candidates_checked"]] if quota else []:
        if time.time() > admit_deadline:
            log.append("- 입성 심사 시간 상한 도달 → 나머지 후보는 다음 회차로")
            break
        if k in known or res.get("fitness", -99) < cfg["min_fitness"]:
            continue
        v = res["valid"]
        if v["sharpe"] < cfg["min_valid_sharpe"] or v["trades"] < cfg["min_trades_valid"]:
            continue
        # 검증 구간에서 '그냥 들고 있기'보다 확실히 나아야 함 (상승장·하락장 모두 공정하게 비교)
        if v["sharpe"] < bh_valid + cfg["min_valid_excess"]:
            continue
        # 이미 있는 전략과 거의 똑같이 움직이면 중복으로 보고 건너뜀
        vec = ret_vec(ev.strats[k])
        if vec.std() == 0 or any(np.corrcoef(vec, w)[0, 1] > cfg["max_corr"] for w in accepted_vecs if w.std() > 0):
            continue
        # 튼튼함 심사 (이웃 파라미터 / 비용 3배 / 코인 일관성). 비싸서 한 번 실행에 시도 횟수 제한.
        if robust_tried >= cfg["robustness"]["max_checks"]:
            break
        robust_tried += 1
        rb = gates.robustness(frames, ev.strats[k], cfg, bh_per, rng)
        if not rb["passed"]:
            for f in rb["fail"]:
                robust_fail[f] = robust_fail.get(f, 0) + 1
            continue
        res["robustness"] = rb
        accepted_vecs.append(vec)
        added.append(k)
        if len(added) >= quota:
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
                "robustness": ev.evaluate(s).get("robustness"),
                "forward": None,
            }
        )
    fails =", ".join(f"{k} {v}" for k, v in robust_fail.items())
    log.append(f"- 튼튼함 심사: {robust_tried}개 시도 → {len(added)}개 통과" + (f" (탈락 사유: {fails})" if fails else ""))

    # 5) 정리: 퇴출 규칙은 hof.prune 참고
    hof, retired, added = H.prune(hof, added, cfg)
    admitted[today] = admitted.get(today, 0) + len(added)
    state["admitted"] = dict(sorted(admitted.items())[-30:])
    log.append(f"- 새로 명예의 전당 입성: {len(added)}개 (오늘 누적 {admitted[today]}/{cfg['max_new_per_day']}, 검증 구간 B&H 샤프 {bh_valid:.2f})")
    if retired:
        log.append(f"- 퇴출: {', '.join(h['id'] for h in retired)}")

    # 졸업 심사: 처음 통과한 날을 기록 (이후 기준에서 벗어나면 리포트에 '보류'로 표시)
    grads = state.setdefault("graduated", {})
    new_grads = []
    for h in hof:
        h["rank_score"] = H.rank_score(h, cfg)
        h["graduation"] = H.graduation(h, cfg)
        if h["graduation"]["passed"] and h["id"] not in grads:
            grads[h["id"]] = today
            new_grads.append(h["id"])
    if new_grads:
        log.append(f"- 🎓 졸업: {', '.join(new_grads)}")

    atomic_write_json(hof_path, hof)
    atomic_write_json(state_path, state)

    # 6) 보고서
    summary = report.write(hof, frames, cfg, log, today, added, state, new_grads)
    log.append(f"- 소요 {(time.time() - t_start) / 60:.1f}분")
    jp = RES / "journal.md"
    prev = jp.read_text(encoding="utf-8") if jp.exists() else "# 연구 일지\n"
    head, _, rest = prev.partition("\n")
    atomic_write_text(jp, head + "\n\n" + "\n".join(log) + "\n" + rest)
    report.notify(summary)
    print("\n".join(log))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        raise
