"""핵심 규칙 자동 점검. 매 연구 실행 전에 돌고, 하나라도 실패하면 그 회차 연구를 건너뛴다.

    python -m tests.test_core
"""
from __future__ import annotations

import copy
import random
import sys
import traceback

import numpy as np
import pandas as pd

from bot import backtest as bt
from bot import gates
from bot import hof as H
from bot.strategy import BLOCKS, EXIT_BLOCKS, random_strategy

CFG = {
    "interval": "4h", "hof_size": 5, "forward_min_bars": 42, "retire_forward_mdd": -0.35,
    "graduation": {"min_days": 60, "min_upleg": 0.10, "min_trades": 10, "min_excess": 0.0, "max_mdd": -0.20},
    "robustness": {"neighbors": 2, "neighbor_scale": 0.15, "neighbor_min_excess": 0.25, "cost_mult": 3,
                   "min_coin_share": 0.75, "max_checks": 5},
}


def synth(n=1500, seed=0):
    rng = np.random.default_rng(seed)
    drift = np.repeat(rng.normal(0, 0.004, n // 150 + 1), 150)[:n]
    c = 1e6 * np.exp(np.cumsum(drift + rng.normal(0, 0.02, n)))
    o = np.r_[c[0], c[:-1]]
    h = np.maximum(o, c) * (1 + abs(rng.normal(0, 0.008, n)))
    l = np.minimum(o, c) * (1 - abs(rng.normal(0, 0.008, n)))
    t = pd.date_range("2024-01-01", periods=n, freq="4h")
    return pd.DataFrame(dict(time=t, open=o, high=h, low=l, close=c, volume=rng.lognormal(10, 0.6, n)))


# ------------------------------------------------------------ 백테스트

def test_no_lookahead_every_block():
    """미래 봉을 잘라내도 과거 수익률이 바뀌지 않아야 한다 (모든 지표 블록 각각)."""
    df = synth()
    random.seed(1)
    cuts = [700, 1000, 1300]
    for table, slot in ((BLOCKS, "entry"), (EXIT_BLOCKS, "exit")):
        for name, (gen, _) in table.items():
            for _ in range(3):
                s = random_strategy()
                s[slot] = [{"type": name, **gen()}]
                full = bt.run(df, s)
                for k in cuts:
                    part = bt.run(df.iloc[:k].reset_index(drop=True), s)
                    assert np.allclose(full[:k], part, equal_nan=True), f"{name} 블록이 미래 정보를 봄 (cut={k})"


def test_signals_ignore_future_bars():
    """k번째 봉 이후 가격을 엉뚱한 값으로 바꿔도, k-1 봉까지의 신호는 그대로여야 한다.
    (잘라내기만 하면 '딱 한 봉 앞'을 훔쳐보는 실수를 못 잡는다 → 미래를 뒤섞어서 확인)"""
    from bot.strategy import signal
    df = synth(seed=5)
    rng = np.random.default_rng(5)
    random.seed(5)
    for k in (600, 900, 1200):
        fake = df.copy()
        for col in ("open", "high", "low", "close", "volume"):
            fake.loc[k:, col] = fake[col].iloc[k:].to_numpy() * rng.uniform(0.5, 1.5, len(df) - k)
        fake["high"] = fake[["open", "high", "low", "close"]].max(axis=1)
        fake["low"] = fake[["open", "high", "low", "close"]].min(axis=1)
        for table in (BLOCKS, EXIT_BLOCKS):
            for name, (gen, fn) in table.items():
                if fn is None:
                    continue
                for _ in range(3):
                    c = {"type": name, **gen()}
                    a, b = signal(df, c, table), signal(fake, c, table)
                    assert (a[:k] == b[:k]).all(), f"{name} 블록이 미래 봉을 봄 (k={k}, {c})"


def test_gap_down_fills_at_open():
    # 손절가 90 인데 시가가 85 로 갭하락 → 85 에 체결돼야 한다 (90 으로 체결하면 낙관적 오류)
    t = pd.date_range("2024-01-01", periods=6, freq="4h")
    df = pd.DataFrame(dict(time=t, open=[100, 100, 100, 85, 85, 85], high=[101, 101, 101, 86, 86, 86],
                           low=[99, 99, 99, 80, 84, 84], close=[100, 100, 100, 85, 85, 85], volume=[1] * 6))
    s = {"entry": [{"type": "momentum_pos", "n": 1, "th": -1.0}], "entry_mode": "and",
         "exit": [{"type": "bars_held", "n": 50}], "stop": 0.10, "take": None, "trail": None}
    eq = np.prod(1 + bt.run(df, s, cost=0.0)[:4])
    assert abs(eq - 0.85) < 1e-9, f"갭하락 손절 체결가 오류: {eq}"


def test_cost_monotonic():
    df = synth(seed=2)
    random.seed(2)
    for _ in range(20):
        s = random_strategy()
        lo = np.prod(1 + bt.run(df, s, cost=0.0005))
        hi = np.prod(1 + bt.run(df, s, cost=0.003))
        assert hi <= lo + 1e-12, "비용을 올렸는데 수익이 늘어남"


def test_stop_fills_at_stop_price():
    # 100 에 진입 → 다음 봉 저가 80 → 손절 10% 면 90 근처(비용 반영)에서 청산돼야 한다
    t = pd.date_range("2024-01-01", periods=6, freq="4h")
    df = pd.DataFrame(dict(time=t, open=[100, 100, 100, 99, 95, 95], high=[101, 101, 101, 100, 96, 96],
                           low=[99, 99, 99, 80, 94, 94], close=[100, 100, 100, 95, 95, 95], volume=[1] * 6))
    s = {"entry": [{"type": "momentum_pos", "n": 1, "th": -1.0}], "entry_mode": "and",
         "exit": [{"type": "bars_held", "n": 50}], "stop": 0.10, "take": None, "trail": None}
    r, pos = bt.run(df, s, cost=0.0, with_pos=True)
    eq = np.prod(1 + r[:4])
    assert abs(eq - 0.90) < 1e-9, f"손절 체결가 오류: {eq}"
    assert not pos[3], "손절 후에도 보유로 표시됨"


def test_trades_counted_with_reentry():
    rets = np.array([0, .01, .01, -.01, .02, 0, 0])
    pos = np.array([0, 1, 1, 0, 1, 0, 0], bool)  # 3번째 봉에서 청산, 4번째에 재진입
    assert bt.metrics(rets, "4h", pos=pos)["trades"] == 2


# ------------------------------------------------------------ 전진 성과

def test_forward_metrics_bh_and_upleg():
    t = pd.date_range("2024-01-01", periods=10, freq="4h")
    close = np.array([100, 100, 100, 100, 90, 80, 88, 100, 96, 96], float)
    df = pd.DataFrame(dict(time=t, open=close, high=close, low=close, close=close, volume=1.0))
    never = {"entry": [{"type": "momentum_pos", "n": 1, "th": 9.0}], "entry_mode": "and",
             "exit": [{"type": "bars_held", "n": 5}], "stop": None, "take": None, "trail": None}
    f = H.forward_metrics({"X": df}, never, str(t[3]), "4h")
    assert abs(f["bh"] - (96 / 100 - 1)) < 1e-12
    assert abs(f["upleg"] - (100 / 80 - 1)) < 1e-12, f["upleg"]
    assert f["total"] == 0 and f["trades"] == 0 and f["holding"] == []
    assert abs(f["excess"] - 0.04) < 1e-12


# ------------------------------------------------------------ 전당 자리 관리

def entry(i, score, bars=None, mdd=0.0, excess=0.0):
    e = {"train": {"sharpe": score}, "valid": {"sharpe": score}}
    f = None if bars is None else {"bars": bars, "excess": excess, "mdd": mdd}
    return {"id": i, "eval": e, "forward": f}


def test_protected_entries_never_evicted():
    """이번 주 버그 재현: 검증을 막 마친 좋은 전략이, 보호 중인 전략들 때문에 밀려나면 안 된다."""
    hof = [entry("old_good1", 2.0, 50, excess=0.05), entry("old_good2", 1.9, 45, excess=0.05),
           entry("young1", 1.0, 10), entry("young2", 1.0, 20), entry("young3", 1.0, 30),
           entry("new1", 1.5), entry("new2", 1.4)]
    keep, retired, added = H.prune(hof, ["new1", "new2"], CFG)
    ids = {h["id"] for h in keep}
    assert {"old_good1", "old_good2", "young1", "young2", "young3"} <= ids, ids
    assert added == [] and retired == [], (added, retired)


def test_newcomer_beats_weak_matured():
    hof = [entry("old_weak", 0.2, 50, excess=-0.1), entry("y1", 1, 10), entry("y2", 1, 10),
           entry("y3", 1, 10), entry("y4", 1, 10), entry("new", 2.0)]
    keep, retired, added = H.prune(hof, ["new"], CFG)
    assert [h["id"] for h in retired] == ["old_weak"] and added == ["new"]


def test_drawdown_retirement_only_after_maturity():
    hof = [entry("bad_mature", 3, 50, mdd=-0.5), entry("bad_young", 3, 10, mdd=-0.5)]
    keep, retired, _ = H.prune(hof, [], CFG)
    assert [h["id"] for h in retired] == ["bad_mature"]
    assert [h["id"] for h in keep] == ["bad_young"]


# ------------------------------------------------------------ 졸업 / 튼튼함

def test_graduation():
    ok = {"forward": {"days": 61, "upleg": 0.12, "trades": 12, "excess": 0.03, "worst_mdd": -0.15},
          "robustness": {"passed": True}}
    assert H.graduation(ok, CFG)["passed"]
    for k, v in (("days", 59), ("upleg", 0.05), ("trades", 9), ("excess", -0.01), ("worst_mdd", -0.25)):
        bad = copy.deepcopy(ok)
        bad["forward"][k] = v
        g = H.graduation(bad, CFG)
        assert not g["passed"] and g["n_ok"] == 5, (k, g)
    weak = copy.deepcopy(ok)
    weak["robustness"] = {"passed": False}
    assert not H.graduation(weak, CFG)["passed"]
    assert not H.graduation({"forward": None}, CFG)["passed"]


def test_perturb_keeps_types_and_bounds():
    rng = random.Random(3)
    random.seed(3)
    for _ in range(50):
        s = random_strategy()
        p = gates.perturb(s, 0.15, rng)
        for g in ("entry", "exit"):
            for a, b in zip(s[g], p[g]):
                assert a["type"] == b["type"]
                for k in a:
                    if k == "type":
                        continue
                    assert type(a[k]) is type(b[k]), (k, a[k], b[k])
                    if isinstance(a[k], int) and not isinstance(a[k], bool):
                        assert b[k] >= 2
        assert (s["stop"] is None) == (p["stop"] is None)


def test_robustness_runs():
    frames = {f"C{i}": synth(1200, seed=10 + i) for i in range(4)}
    random.seed(4)
    bh = gates.bh_valid_sharpes(frames, "4h")
    r = gates.robustness(frames, random_strategy(), CFG, bh, random.Random(4))
    assert set(r) >= {"passed", "fail", "coins_beating_bh"}


def test_fetch_failure_falls_back_to_cache():
    """업비트가 멈추거나 오류를 내도, 시간 안에 포기하고 저장된 시세로 진행해야 한다."""
    import time as _t
    from bot import research as R
    cfg = {"interval": "4h", "max_bars": 100, "fetch_timeout_s": 1}
    orig = R.dataio.load
    try:
        R.dataio.load = lambda *a, **k: _t.sleep(30)        # 응답 없음
        t0 = _t.time()
        try:
            R.fetch_with_deadline("KRW-X", cfg)
            raise AssertionError("멈춘 요청이 예외 없이 끝남")
        except TimeoutError:
            pass
        assert _t.time() - t0 < 5, "제한 시간을 넘겨서도 기다림"

        def boom(*a, **k):
            raise OSError("network down")
        R.dataio.load = boom
        try:
            R.fetch_with_deadline("KRW-X", cfg)
            raise AssertionError("오류가 전달되지 않음")
        except OSError:
            pass
    finally:
        R.dataio.load = orig


def main():
    tests = [(n, f) for n, f in globals().items() if n.startswith("test_") and callable(f)]
    failed = 0
    for n, f in tests:
        try:
            f()
            print(f"✅ {n}")
        except Exception:
            failed += 1
            print(f"❌ {n}")
            traceback.print_exc()
    print(f"\n{len(tests) - failed}/{len(tests)} 통과")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
