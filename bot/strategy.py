"""전략 '유전자' 정의 — 지표 조건 블록을 조합해 매매법을 만든다.

전략 = {
  "entry": [조건, ...], "entry_mode": "and"|"or",
  "exit":  [조건, ...] (하나라도 참이면 청산),
  "stop": 손절 비율 | None, "take": 익절 비율 | None, "trail": 트레일링 비율 | None,
}
조건 = {"type": ..., 파라미터...}
"""
from __future__ import annotations

import copy
import hashlib
import json
import random

import numpy as np
import pandas as pd

# ---------------------------------------------------------------- 지표

def sma(s, n):
    return s.rolling(n).mean()


def ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def rsi(s, n):
    d = s.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def atr(df, n):
    pc = df["close"].shift()
    tr = pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()


# ---------------------------------------------------------------- 조건 블록
# 각 블록: (파라미터 생성기, 신호 계산 함수). 신호는 해당 봉 '종가 시점'에 알 수 있는 정보만 쓴다.

def _ma(kind):
    return ema if kind == "ema" else sma


BLOCKS = {
    # 추세 추종
    "ma_cross_up": (
        lambda: {"fast": random.randint(3, 50), "slow": random.randint(20, 200), "kind": random.choice(["sma", "ema"])},
        lambda df, p: _ma(p["kind"])(df.close, p["fast"]) > _ma(p["kind"])(df.close, max(p["slow"], p["fast"] + 2)),
    ),
    "price_above_ma": (
        lambda: {"n": random.randint(10, 200), "kind": random.choice(["sma", "ema"])},
        lambda df, p: df.close > _ma(p["kind"])(df.close, p["n"]),
    ),
    "donchian_break": (
        lambda: {"n": random.randint(10, 100)},
        lambda df, p: df.close > df.high.rolling(p["n"]).max().shift(1),
    ),
    "momentum_pos": (
        lambda: {"n": random.randint(5, 120), "th": round(random.uniform(0.0, 0.3), 3)},
        lambda df, p: df.close.pct_change(p["n"]) > p["th"],
    ),
    "macd_pos": (
        lambda: {"f": random.randint(5, 20), "s": random.randint(21, 60), "sig": random.randint(5, 15)},
        lambda df, p: (lambda m: m > ema(m, p["sig"]))(ema(df.close, p["f"]) - ema(df.close, p["s"])),
    ),
    # 역추세 / 평균회귀
    "rsi_below": (
        lambda: {"n": random.randint(2, 30), "th": random.randint(10, 45)},
        lambda df, p: rsi(df.close, p["n"]) < p["th"],
    ),
    "bb_lower_touch": (
        lambda: {"n": random.randint(10, 60), "k": round(random.uniform(1.0, 3.0), 2)},
        lambda df, p: df.close < sma(df.close, p["n"]) - p["k"] * df.close.rolling(p["n"]).std(),
    ),
    "drawdown_from_high": (
        lambda: {"n": random.randint(5, 60), "th": round(random.uniform(0.05, 0.4), 3)},
        lambda df, p: df.close < df.high.rolling(p["n"]).max() * (1 - p["th"]),
    ),
    # 필터
    "volume_spike": (
        lambda: {"n": random.randint(10, 60), "mult": round(random.uniform(1.2, 4.0), 2)},
        lambda df, p: df.volume > p["mult"] * df.volume.rolling(p["n"]).mean(),
    ),
    "low_volatility": (
        lambda: {"n": random.randint(10, 60), "q": round(random.uniform(0.2, 0.7), 2)},
        lambda df, p: (lambda a: a < a.rolling(200, min_periods=50).quantile(p["q"]))(atr(df, p["n"]) / df.close),
    ),
}

EXIT_BLOCKS = {
    "price_below_ma": (
        lambda: {"n": random.randint(5, 150), "kind": random.choice(["sma", "ema"])},
        lambda df, p: df.close < _ma(p["kind"])(df.close, p["n"]),
    ),
    "ma_cross_down": (
        lambda: {"fast": random.randint(3, 50), "slow": random.randint(20, 200), "kind": random.choice(["sma", "ema"])},
        lambda df, p: _ma(p["kind"])(df.close, p["fast"]) < _ma(p["kind"])(df.close, max(p["slow"], p["fast"] + 2)),
    ),
    "donchian_low_break": (
        lambda: {"n": random.randint(5, 60)},
        lambda df, p: df.close < df.low.rolling(p["n"]).min().shift(1),
    ),
    "rsi_above": (
        lambda: {"n": random.randint(2, 30), "th": random.randint(55, 90)},
        lambda df, p: rsi(df.close, p["n"]) > p["th"],
    ),
    "bars_held": (  # 시간 청산 — backtest 에서 특별 처리
        lambda: {"n": random.randint(2, 60)},
        None,
    ),
}


def signal(df, cond, table):
    _, fn = table[cond["type"]]
    return fn(df, cond).fillna(False).to_numpy(dtype=bool)


# ---------------------------------------------------------------- 생성 / 변이 / 교배

def _new_cond(table):
    t = random.choice(list(table))
    return {"type": t, **table[t][0]()}


def random_strategy():
    return {
        "entry": [_new_cond(BLOCKS) for _ in range(random.choice([1, 1, 2, 2, 3]))],
        "entry_mode": random.choice(["and", "and", "or"]),
        "exit": [_new_cond(EXIT_BLOCKS) for _ in range(random.choice([1, 1, 2]))],
        "stop": random.choice([None, round(random.uniform(0.02, 0.2), 3)]),
        "take": random.choice([None, None, round(random.uniform(0.05, 0.6), 3)]),
        "trail": random.choice([None, None, round(random.uniform(0.05, 0.3), 3)]),
    }


def _jitter(v):
    if isinstance(v, bool) or isinstance(v, str):
        return v
    if isinstance(v, int):
        return max(2, int(round(v * random.uniform(0.7, 1.3) + random.choice([-1, 0, 1]))))
    return round(max(0.0, v * random.uniform(0.75, 1.25)), 3)


def mutate(s):
    s = copy.deepcopy(s)
    r = random.random()
    if r < 0.5:  # 파라미터 미세조정
        group = random.choice(["entry", "exit"])
        c = random.choice(s[group])
        keys = [k for k in c if k != "type"]
        if keys:
            k = random.choice(keys)
            c[k] = _jitter(c[k])
    elif r < 0.65:  # 조건 교체
        group, table = random.choice([("entry", BLOCKS), ("exit", EXIT_BLOCKS)])
        s[group][random.randrange(len(s[group]))] = _new_cond(table)
    elif r < 0.75:  # 조건 추가/삭제
        group, table = random.choice([("entry", BLOCKS), ("exit", EXIT_BLOCKS)])
        if len(s[group]) > 1 and random.random() < 0.5:
            s[group].pop(random.randrange(len(s[group])))
        elif len(s[group]) < 3:
            s[group].append(_new_cond(table))
    elif r < 0.82:
        s["entry_mode"] = "or" if s["entry_mode"] == "and" else "and"
    else:  # 리스크 관리 변경
        k = random.choice(["stop", "take", "trail"])
        if s[k] is None:
            s[k] = round(random.uniform(0.02, 0.3), 3)
        elif random.random() < 0.3:
            s[k] = None
        else:
            s[k] = _jitter(s[k])
    return s


def crossover(a, b):
    c = copy.deepcopy(a)
    c["entry"] = copy.deepcopy(random.choice([a, b])["entry"])
    c["exit"] = copy.deepcopy(random.choice([a, b])["exit"])
    for k in ("stop", "take", "trail", "entry_mode"):
        c[k] = random.choice([a, b])[k]
    return c


def key(s) -> str:
    return hashlib.sha1(json.dumps(s, sort_keys=True).encode()).hexdigest()[:10]


def describe(s) -> str:
    def fmt(c):
        args = ", ".join(f"{k}={v}" for k, v in c.items() if k != "type")
        return f"{c['type']}({args})"

    j = f" {s['entry_mode'].upper()} "
    parts = [f"진입: {j.join(fmt(c) for c in s['entry'])}", f"청산: {' OR '.join(fmt(c) for c in s['exit'])}"]
    risk = [f"{n} {s[k]*100:.1f}%" for k, n in (("stop", "손절"), ("take", "익절"), ("trail", "트레일링")) if s[k]]
    if risk:
        parts.append(" / ".join(risk))
    return " | ".join(parts)
