"""명예의 전당 규칙: 점수, 전진 성과, 자리 관리, 졸업 심사.

research.py 에서 분리해 두어 tests/ 에서 규칙만 따로 검사할 수 있게 했다.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import backtest as bt

HOURS = {"1d": 24, "4h": 4, "1h": 1}


# ------------------------------------------------------------------ 전진 성과

def forward_metrics(frames: dict, s: dict, since: str, interval: str) -> dict | None:
    """전당 입성 시점(since) 이후 실제로 새로 쌓인 봉에서의 성과."""
    t0 = pd.Timestamp(since)
    per = {}
    for m, df in frames.items():
        mask = (df["time"] > t0).to_numpy()
        if mask.sum() < 2 or (~mask).sum() < 1:
            return None
        r, p = bt.run(df, s, with_pos=True)
        rm, pm = r[mask], p[mask]
        x = bt.metrics(rm, interval, pos=pm)
        close = df["close"].to_numpy()
        base = close[~mask][-1]                     # 입성 시점 종가
        path = np.r_[base, close[mask]]
        x["bh"] = float(path[-1] / base - 1)
        x["upleg"] = float(np.max(path / np.minimum.accumulate(path)) - 1)  # 기간 중 가장 큰 상승 폭
        x["holding"] = bool(p[-1])                   # 지금 보유 중인가
        per[m] = x
    bars = int(min(((df["time"] > t0).sum()) for df in frames.values()))
    total = float(np.mean([x["total"] for x in per.values()]))
    bh = float(np.mean([x["bh"] for x in per.values()]))
    return {
        "bars": bars,
        "days": bars * HOURS[interval] / 24,
        "total": total,
        "bh": bh,
        "excess": total - bh,
        "exposure": float(np.mean([x["exposure"] for x in per.values()])),
        "mdd": float(np.median([x["mdd"] for x in per.values()])),
        "worst_mdd": float(min(x["mdd"] for x in per.values())),
        "trades": int(sum(x["trades"] for x in per.values())),
        "upleg": float(np.median([x["upleg"] for x in per.values()])),
        "holding": [m for m, x in per.items() if x["holding"]],
    }


# ------------------------------------------------------------------ 점수 / 자리 관리

def matured(h: dict, cfg: dict) -> bool:
    f = h.get("forward")
    return bool(f and f["bars"] >= cfg["forward_min_bars"])


def rank_score(h: dict, cfg: dict) -> float:
    e = h["eval"]
    score = 0.5 * e["valid"]["sharpe"] + 0.5 * e["train"]["sharpe"]
    if matured(h, cfg):
        f = h["forward"]
        # 전진 성과는 '같은 기간 단순 보유 대비' (하락장에서 현금으로 피한 것도 실력으로 인정)
        score += float(np.sign(f["excess"]) * min(abs(f["excess"]) * 5, 1.5))
    return float(score)


def prune(hof: list[dict], added: list[str], cfg: dict) -> tuple[list[dict], list[dict], list[str]]:
    """퇴출 처리. (남은 전당, 퇴출된 것, 실제로 입성한 신입 id) 를 돌려준다.

    규칙
    - 전진 검증을 마친 뒤 낙폭이 기준보다 크면 퇴출.
    - 자리가 넘치면 '전진 검증을 마친 전략 + 이번 신입' 중 점수 최하위부터 내보낸다.
      전진 기록을 쌓는 중인 기존 전략은 보호 → 검증이 끝나기도 전에 밀려나지 않는다.
      신입은 검증을 마친 기존 전략 중 최약체보다 나아야 자리를 얻는다.
    """
    added = list(added)
    retired = [h for h in hof if matured(h, cfg) and h["forward"]["mdd"] < cfg["retire_forward_mdd"]]
    keep = [h for h in hof if h not in retired]
    while len(keep) > cfg["hof_size"]:
        pool = [h for h in keep if matured(h, cfg) or h["id"] in added] or keep
        worst = min(pool, key=lambda h: rank_score(h, cfg))
        keep.remove(worst)
        if worst["id"] in added:
            added.remove(worst["id"])
        else:
            retired.append(worst)
    keep.sort(key=lambda h: rank_score(h, cfg), reverse=True)
    return keep, retired, added


# ------------------------------------------------------------------ 졸업 심사

def graduation(h: dict, cfg: dict) -> dict:
    """실전 검증 기준 통과 여부. checks 는 (이름, 통과여부, 현재값, 기준) 목록."""
    g = cfg["graduation"]
    f = h.get("forward") or {}
    days = f.get("days", 0.0)
    checks = [
        ("전진 기간", days >= g["min_days"], f"{days:.0f}일", f"{g['min_days']}일↑"),
        ("상승장 경험", f.get("upleg", 0) >= g["min_upleg"], f"{f.get('upleg', 0) * 100:.0f}%", f"+{g['min_upleg'] * 100:.0f}%↑"),
        ("실제 거래", f.get("trades", 0) >= g["min_trades"], f"{f.get('trades', 0)}회", f"{g['min_trades']}회↑"),
        ("보유 대비", f.get("excess", -1) > g["min_excess"], f"{f.get('excess', 0) * 100:+.1f}%p", "+0%p 초과"),
        ("최대 낙폭", f.get("worst_mdd", -1) >= g["max_mdd"], f"{abs(f.get('worst_mdd', 0)) * -100:.0f}%".replace("-0%", "0%"), f"{g['max_mdd'] * 100:.0f}% 이내"),
        ("튼튼함 심사", bool((h.get("robustness") or {}).get("passed")),
         "통과" if (h.get("robustness") or {}).get("passed") else ("미통과" if h.get("robustness") else "미심사"), "통과"),
    ]
    return {"passed": all(ok for _, ok, _, _ in checks), "checks": checks, "n_ok": sum(ok for _, ok, _, _ in checks),
            "n_total": len(checks)}
