"""명예의 전당 입성 전 '튼튼함' 심사.

하루에 10만 개 넘는 전략을 평가하고 그중 검증 구간 성적이 좋은 것을 고르면,
검증 구간에 '우연히' 잘 맞은 전략이 섞이기 쉽다(다중 검정 편향). 그래서 입성 전에 세 가지를 더 본다.

1. 이웃 파라미터: 숫자 파라미터를 ±15% 흔든 변형들도 대체로 잘 되는가?
   딱 그 숫자에서만 잘 되는 전략은 우연일 가능성이 크다.
2. 비용 3배: 수수료·슬리피지를 3배로 올려도 단순 보유보다 나은가?
   거래가 잦아 비용에 민감한 전략을 거른다.
3. 코인 일관성: 검증 구간에서 4개 코인 중 최소 3개에서 단순 보유보다 나은가?
   한두 코인 덕분에 중앙값만 좋아 보이는 전략을 거른다.
"""
from __future__ import annotations

import copy
import random

import numpy as np

from . import backtest as bt


def perturb(s: dict, scale: float, rng: random.Random) -> dict:
    """모든 숫자 파라미터를 동시에 ±scale 범위에서 흔든 변형."""
    s = copy.deepcopy(s)

    def jit(v):
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            return v
        f = 1 + rng.uniform(-scale, scale)
        if isinstance(v, int):
            return max(2, int(round(v * f)))
        return round(max(0.0, v * f), 4)

    for group in ("entry", "exit"):
        for c in s[group]:
            for k in list(c):
                if k != "type":
                    c[k] = jit(c[k])
    for k in ("stop", "take", "trail"):
        if s[k]:
            s[k] = jit(s[k])
    return s


def valid_sharpes(frames: dict, s: dict, interval: str, cost: float | None = None) -> dict:
    """코인별 검증 구간(60~80%) 샤프."""
    out = {}
    for m, df in frames.items():
        r = bt.run(df, s, cost=cost)
        n = len(r)
        out[m] = bt.metrics(r[int(n * 0.6): int(n * 0.8)], interval)["sharpe"]
    return out


def bh_valid_sharpes(frames: dict, interval: str) -> dict:
    out = {}
    for m, df in frames.items():
        n = len(df)
        out[m] = bt.buy_hold(df.iloc[int(n * 0.6): int(n * 0.8)], interval)["sharpe"]
    return out


def robustness(frames: dict, s: dict, cfg: dict, bh: dict, rng: random.Random) -> dict:
    """세 가지 심사 결과. passed 가 True 여야 입성."""
    g = cfg["robustness"]
    iv = cfg["interval"]
    bh_med = float(np.median(list(bh.values())))

    base = valid_sharpes(frames, s, iv)
    beats = sum(base[m] > bh[m] for m in frames)
    need = int(np.ceil(g["min_coin_share"] * len(frames)))
    coin_ok = beats >= need

    stress = float(np.median(list(valid_sharpes(frames, s, iv, cost=(bt.FEE + bt.SLIPPAGE) * g["cost_mult"]).values())))
    cost_ok = stress > bh_med

    nb = []
    for _ in range(g["neighbors"]):
        try:
            nb.append(float(np.median(list(valid_sharpes(frames, perturb(s, g["neighbor_scale"], rng), iv).values()))))
        except Exception:
            nb.append(-9.0)
    nb_med = float(np.median(nb))
    nb_ok = nb_med >= bh_med + g["neighbor_min_excess"]

    return {
        "passed": bool(coin_ok and cost_ok and nb_ok),
        "coins_beating_bh": f"{beats}/{len(frames)}",
        "cost_stress_sharpe": stress,
        "neighbor_median_sharpe": nb_med,
        "bh_valid_sharpe": bh_med,
        "fail": [n for n, ok in (("코인일관성", coin_ok), ("비용3배", cost_ok), ("이웃파라미터", nb_ok)) if not ok],
    }
