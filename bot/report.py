"""결과 보고서(results/REPORT.md + 차트)와 선택적 텔레그램 알림."""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

from . import backtest as bt

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


def write(hof, frames, cfg, log, today, added) -> str:
    chart = _chart(hof, frames, cfg)
    lines = [
        "# 🤖 코인 전략 연구 리포트",
        "",
        f"마지막 업데이트: **{today}** · 대상: {', '.join(frames)} · 봉: {cfg['interval']}",
        "",
        "> 학습(앞 60%)으로만 진화 → 검증(다음 20%)으로 입성 심사 → 시험(마지막 20%)은 보고만. "
        "'전진'은 전당에 오른 뒤 실제로 새로 쌓인 데이터에서의 성과입니다.",
        "",
        "## 오늘",
        *log[1:],
        "",
        "## 명예의 전당",
        "",
        "| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 | 전략 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, h in enumerate(hof, 1):
        e, f = h["eval"], h.get("forward")
        fwd = f"{_pct(f['total'])} ({f['bars']}봉)" if f else "-"
        new = " 🆕" if h["id"] in added else ""
        lines.append(
            f"| {i} | `{h['id']}`{new} | {h['found']} | {e['train']['sharpe']:.2f} | {e['valid']['sharpe']:.2f} | "
            f"{e['test']['sharpe']:.2f} | {_pct(e['test']['cagr'])} | {_pct(e['test']['mdd'])} | {fwd} | {h['desc']} |"
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
    lines += [
        "",
        f"비교 기준(단순 보유) 샤프 — 학습 {bh['train']:.2f} · 검증 {bh['valid']:.2f} · 시험 {bh['test']:.2f}",
        "",
    ]
    if chart:
        lines += [f"![top equity]({chart})", ""]
    lines += [
        "샤프·CAGR·MDD는 여러 코인의 중앙값, 수수료 0.05% + 슬리피지 0.05% 반영.",
        "백테스트 성과는 미래 수익을 보장하지 않습니다. 실거래 전에 '전진' 성과가 충분히 쌓였는지 확인하세요.",
    ]
    (RES / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")

    top = hof[0] if hof else None
    msg = [f"🤖 코인 연구 {today}", *[l.lstrip("- ") for l in log[1:]]]
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
