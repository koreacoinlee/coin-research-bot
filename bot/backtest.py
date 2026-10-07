"""롱 온리 백테스트 엔진.

- 신호는 t봉 종가에 확정 → t+1봉 시가에 체결 (미래 정보 누출 없음)
- 손절/익절/트레일링은 봉 내부 고가·저가로 판정, 같은 봉에서 둘 다 닿으면 손절 우선(보수적)
- 수수료 + 슬리피지를 매수/매도 양쪽에 부과
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .strategy import BLOCKS, EXIT_BLOCKS, signal

FEE = 0.0005      # 업비트 KRW 마켓 0.05%
SLIPPAGE = 0.0005  # 보수적 가정
BARS_PER_YEAR = {"1d": 365, "4h": 365 * 6, "1h": 365 * 24}


def run(df: pd.DataFrame, s: dict) -> np.ndarray:
    """봉별 전략 수익률 배열을 돌려준다."""
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    n = len(df)

    ent = [signal(df, x, BLOCKS) for x in s["entry"]]
    entry = np.logical_and.reduce(ent) if s["entry_mode"] == "and" else np.logical_or.reduce(ent)
    hold_limit = None
    ex_sigs = []
    for x in s["exit"]:
        if x["type"] == "bars_held":
            hold_limit = x["n"]
        else:
            ex_sigs.append(signal(df, x, EXIT_BLOCKS))
    exit_sig = np.logical_or.reduce(ex_sigs) if ex_sigs else np.zeros(n, bool)

    cost = FEE + SLIPPAGE
    rets = np.zeros(n)
    in_pos, entry_px, peak, held = False, 0.0, 0.0, 0
    stop, take, trail = s["stop"], s["take"], s["trail"]

    for t in range(1, n):
        if in_pos:
            held += 1
            prev = c[t - 1]
            exit_px = None
            # 봉 내부 리스크 청산
            stops = []
            if stop:
                stops.append(entry_px * (1 - stop))
            if trail:
                stops.append(peak * (1 - trail))
            if stops:
                sp = max(stops)
                if l[t] <= sp:
                    exit_px = min(o[t], sp)  # 갭하락이면 시가에 체결
            if exit_px is None and take and h[t] >= entry_px * (1 + take):
                exit_px = max(o[t], entry_px * (1 + take))
            if exit_px is not None:
                rets[t] = (exit_px * (1 - cost)) / prev - 1
                in_pos = False
                continue
            # 전봉 종가 신호에 의한 청산 → 이번 봉 시가 체결
            if exit_sig[t - 1] or (hold_limit and held > hold_limit):
                rets[t] = (o[t] * (1 - cost)) / prev - 1
                in_pos = False
                continue
            rets[t] = c[t] / prev - 1
            peak = max(peak, h[t])
        elif entry[t - 1]:
            entry_px = o[t] * (1 + cost)
            peak = o[t]
            held = 0
            in_pos = True
            rets[t] = c[t] / entry_px - 1
            # 진입 봉에서 바로 손절 닿는 경우
            if stop and l[t] <= entry_px * (1 - stop):
                rets[t] = (entry_px * (1 - stop) * (1 - cost)) / entry_px - 1
                in_pos = False
    return rets


def metrics(rets: np.ndarray, interval: str) -> dict:
    eq = np.cumprod(1 + rets)
    years = max(len(rets) / BARS_PER_YEAR[interval], 1e-9)
    total = eq[-1] - 1
    cagr = eq[-1] ** (1 / years) - 1 if eq[-1] > 0 else -1.0
    sd = rets.std()
    sharpe = rets.mean() / sd * np.sqrt(BARS_PER_YEAR[interval]) if sd > 0 else 0.0
    dd = (eq / np.maximum.accumulate(eq) - 1).min()
    active = rets != 0
    # 거래 횟수: 포지션 구간의 시작 수
    trades = int(np.sum(active[1:] & ~active[:-1]) + active[0])
    return {
        "total": float(total),
        "cagr": float(cagr),
        "sharpe": float(sharpe),
        "mdd": float(dd),
        "trades": trades,
        "exposure": float(active.mean()),
    }


def buy_hold(df: pd.DataFrame, interval: str) -> dict:
    r = df["close"].pct_change().fillna(0).to_numpy()
    return metrics(r, interval)
