"""결과 보고서(results/REPORT.md + 차트)와 선택적 텔레그램 알림."""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

from . import backtest as bt
from .util import atomic_write_text

RES = Path(__file__).resolve().parent.parent / "results"


def _pct(x):
    return f"{x * 100:+.1f}%"


def _chart(hof, frames, cfg):
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return None
    if not hof:
        return None
    m = cfg["markets"][0] if cfg["markets"][0] in frames else next(iter(frames))
    df = frames[m]
    fig, ax = plt.subplots(figsize=(10, 5), dpi=110)
    bh = np.cumprod(1 + df["close"].pct_change().fillna(0).to_numpy())
    ax.plot(df["time"], bh, color="#999", lw=1.2, label="Buy & Hold")
    for h in hof[:3]:
        eq = np.cumprod(1 + bt.run(df, h["strategy"]))
        ax.plot(df["time"], eq, lw=1.4, label=f"#{h['id']}")
    n = len(df)
    for frac, lab in ((0.6, "valid"), (0.8, "test")):
        ax.axvline(df["time"].iloc[int(n * frac)], color="#c44", ls="--", lw=0.8)
        ax.text(df["time"].iloc[int(n * frac)], ax.get_ylim()[1], f" {lab}", color="#c44", va="top", fontsize=8)
    ax.set_yscale("log")
    ax.set_title(f"Top strategies on {m} ({cfg['interval']}) — log equity")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    out = RES / "top_equity.png"
    fig.savefig(out)
    plt.close(fig)
    return out.name


COIN = lambda m: m.split("-")[-1]


def _fwd_cell(f):
    if not f:
        return "-"
    state = "관망 " if f.get("exposure", 1) == 0 else ""
    return f"{state}{_pct(f['total'])} / 보유 {_pct(f['bh'])} ({f['days']:.0f}일)"


def _now_cell(f):
    if not f:
        return "-"
    return "·".join(COIN(m) for m in f.get("holding", [])) or "관망"


def write(hof, frames, cfg, log, today, added, state=None, new_grads=()) -> str:
    state = state or {}
    grads = state.get("graduated", {})
    chart = _chart(hof, frames, cfg)
    g = cfg["graduation"]
    lines = [
        "# 🤖 코인 전략 연구 리포트",
        "",
        f"마지막 업데이트: **{today}** · 대상: {', '.join(frames)} · 봉: {cfg['interval']}",
        "",
        "## 🎓 졸업 심사",
        "",
        f"전당에 오른 뒤 **실제로 새로 쌓인 시세**로 매기는 시험이에요. 기준: 전진 {g['min_days']}일 이상 · "
        f"그 기간에 +{g['min_upleg'] * 100:.0f}% 넘는 상승장 포함 · 실제 거래 {g['min_trades']}회 이상(4코인 합) · "
        f"같은 기간 단순 보유보다 나은 수익 · 코인별 최대 낙폭 {g['max_mdd'] * 100:.0f}% 이내 · 튼튼함 심사 통과.",
        "",
    ]
    passed = [h for h in hof if h.get("graduation", {}).get("passed")]
    lapsed = [i for i in grads if i not in {h["id"] for h in passed}]
    if passed:
        lines.append("**졸업한 전략:** " + ", ".join(f"`{h['id']}` ({grads.get(h['id'], today)} 졸업)" for h in passed))
    else:
        lines.append("**졸업한 전략: 아직 없음**")
    if lapsed:
        lines.append(f"  \n졸업 후 기준에서 벗어나 보류 중: {', '.join(f'`{i}`' for i in lapsed)}")
    lines += ["", "졸업에 가장 가까운 전략:", "",
              "| ID | 전진 기간 | 상승장 경험 | 실제 거래 | 보유 대비 | 최대 낙폭 | 튼튼함 | 통과 |",
              "|---|---|---|---|---|---|---|---|"]
    near = sorted(hof, key=lambda h: (h.get("graduation", {}).get("n_ok", 0), h.get("forward", {}) and h["forward"]["days"] or 0), reverse=True)[:8]
    for h in near:
        gr = h.get("graduation")
        if not gr:
            continue
        cells = [("✅ " if ok else "⬜ ") + cur for _, ok, cur, _ in gr["checks"]]
        lines.append(f"| `{h['id']}` | " + " | ".join(cells) + f" | {gr['n_ok']}/{gr['n_total']} |")

    # 지금 신호
    holding = {}
    for h in hof:
        for m in (h.get("forward") or {}).get("holding", []):
            holding[COIN(m)] = holding.get(COIN(m), 0) + 1
    sig = " · ".join(f"{c} {n}개" for c, n in sorted(holding.items(), key=lambda kv: -kv[1])) or "없음 (모든 전략 관망 중)"
    lines += ["", "## 📡 지금 보유 신호", "",
              f"전당 전략 {len(hof)}개 중 현재 코인을 들고 있는 전략: **{sig}**",
              "", "## 오늘", *log[1:], "",
              "## 명예의 전당", "",
              "| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 / 같은 기간 보유 | 지금 | 전략 |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, h in enumerate(hof, 1):
        e, f = h["eval"], h.get("forward")
        badge = " 🆕" if h["id"] in added else (" 🎓" if h.get("graduation", {}).get("passed") else "")
        lines.append(
            f"| {i} | `{h['id']}`{badge} | {h['found']} | {e['train']['sharpe']:.2f} | {e['valid']['sharpe']:.2f} | "
            f"{e['test']['sharpe']:.2f} | {_pct(e['test']['cagr'])} | {_pct(e['test']['mdd'])} | {_fwd_cell(f)} | {_now_cell(f)} | {h['desc']} |"
        )
    # 비교 기준
    bh = {}
    for part, idx in (("train", 0), ("valid", 1), ("test", 2)):
        vals = []
        for df in frames.values():
            n = len(df)
            cut = [(0, int(n * 0.6)), (int(n * 0.6), int(n * 0.8)), (int(n * 0.8), n)][idx]
            vals.append(bt.buy_hold(df.iloc[cut[0]:cut[1]], cfg["interval"])["sharpe"])
        bh[part] = float(np.median(vals))
    rb = cfg["robustness"]
    lines += [
        "",
        f"비교 기준(단순 보유) 샤프 — 학습 {bh['train']:.2f} · 검증 {bh['valid']:.2f} · 시험 {bh['test']:.2f}",
        "",
    ]
    if chart:
        lines += [f"![top equity]({chart})", ""]
    lines += [
        "<details><summary>📖 규칙 설명</summary>",
        "",
        "**데이터 나누기** — 과거 시세를 학습(앞 60%) · 검증(다음 20%) · 시험(마지막 20%)으로 나눠요. "
        "전략은 학습 구간 성적으로만 진화하고, 검증 구간으로 입성을 심사해요. 시험 구간은 참고로 보여주기만 해요.",
        "",
        "**입성 심사** — ① 검증 구간 샤프가 단순 보유보다 "
        f"{cfg['min_valid_excess']} 이상 높을 것 ② 기존 전당 전략과 수익 흐름이 비슷하지 않을 것(상관 {cfg['max_corr']} 이하) "
        f"③ 튼튼함 심사: 숫자 파라미터를 ±{rb['neighbor_scale'] * 100:.0f}% 흔든 변형 {rb['neighbors']}개도 대체로 좋을 것, "
        f"거래 비용이 {rb['cost_mult']}배여도 단순 보유보다 나을 것, 4개 코인 중 {int(np.ceil(rb['min_coin_share'] * len(frames)))}개 이상에서 단순 보유보다 나을 것. "
        f"하루 최대 {cfg['max_new_per_day']}개.",
        "",
        f"**자리 관리** — 전당은 {cfg['hof_size']}자리. 입성 후 {cfg['forward_min_bars']}봉"
        f"({cfg['forward_min_bars'] * {'1d': 24, '4h': 4, '1h': 1}[cfg['interval']] / 24:.0f}일) 동안은 보호돼요. "
        "자리가 차면, 보호 기간이 끝난 전략과 신입 중 점수가 가장 낮은 것이 나가요. "
        f"보호 기간 뒤 낙폭이 {cfg['retire_forward_mdd'] * 100:.0f}%보다 나빠지면 퇴출돼요.",
        "",
        "**점수** — 학습·검증 샤프 평균에, 보호 기간이 끝난 전략은 '같은 기간 단순 보유 대비 초과 수익'을 더해요. "
        "하락장에서 현금으로 피한 것도 실력으로 인정돼요.",
        "",
        "**체결 가정** — 봉 마감 신호 → 다음 봉 시가 체결, 수수료 0.05% + 슬리피지 0.05%(한쪽), "
        "같은 봉에서 손절·익절이 둘 다 닿으면 손절로 처리. 샤프·CAGR·MDD는 4개 코인의 중앙값.",
        "",
        "</details>",
        "",
        "백테스트와 졸업은 미래 수익을 보장하지 않습니다. 이 리포트는 투자 권유가 아니에요.",
    ]
    atomic_write_text(RES / "REPORT.md", "\n".join(lines))

    msg = [f"🤖 코인 연구 {today}", *[l.lstrip("- ") for l in log[1:]]]
    if new_grads:
        msg += ["", f"🎓 새 졸업 전략: {', '.join(new_grads)} — 리포트에서 근거를 확인하세요."]
    top = hof[0] if hof else None
    if top:
        e = top["eval"]
        msg += ["", f"1위 {top['id']}: 검증 샤프 {e['valid']['sharpe']:.2f}, 시험 샤프 {e['test']['sharpe']:.2f}", top["desc"]]
    return "\n".join(msg)


def notify(text: str):
    token, chat = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not (token and chat):
        return
    try:
        data = urllib.parse.urlencode({"chat_id": chat, "text": text[:4000]}).encode()
        urllib.request.urlopen(f"https://api.telegram.org/bot{token}/sendMessage", data=data, timeout=15)
    except Exception as e:
        print("텔레그램 전송 실패:", e)
