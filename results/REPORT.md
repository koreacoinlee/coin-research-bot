# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-10-11** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

> 학습(앞 60%)으로만 진화 → 검증(다음 20%)으로 입성 심사 → 시험(마지막 20%)은 보고만. '전진'은 전당에 오른 뒤 실제로 새로 쌓인 데이터에서의 성과이고, 옆의 '보유'는 같은 기간 그냥 들고 있었을 때입니다. 전진 기록이 42봉 이상 쌓이기 전까지는 퇴출되지 않습니다.

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-10-11 00:00 UTC
- 2495세대 진화, 전략 121,167개 평가
- 새로 명예의 전당 입성: 3개 (오늘 누적 3/3, 검증 구간 B&H 샤프 1.24)

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 | 전략 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `3e0a3dbb31` | 2026-10-11 | 2.07 | 2.39 | 0.94 | +13.9% | -16.1% | 관망 중 +0.0% / 보유 -0.9% (0.3일) | 진입: volume_spike(n=26, mult=3.63) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 2 | `d7fb6c9904` | 2026-10-11 | 1.90 | 2.38 | 0.35 | +6.1% | -27.9% | 관망 중 +0.0% / 보유 -0.9% (0.3일) | 진입: volume_spike(n=15, mult=2.369) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 41.1% |
| 3 | `114ad67d25` | 2026-10-11 | 1.96 | 2.28 | 0.54 | +10.5% | -27.4% | 관망 중 +0.0% / 보유 -0.9% (0.3일) | 진입: volume_spike(n=20, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=142, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 4 | `cba03c6a1a` | 2026-10-09 | 1.72 | 2.47 | 0.81 | +14.5% | -19.4% | 관망 중 +0.0% / 보유 -1.1% (2.0일) | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=32, mult=3.51) | 청산: ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 5 | `20fa805145` | 2026-10-08 | 1.85 | 2.32 | 0.94 | +14.9% | -18.9% | 관망 중 +0.0% / 보유 -3.6% (3.7일) | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=37, mult=3.51) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 6 | `cdcac84052` | 2026-10-09 | 1.70 | 2.46 | 0.50 | +10.9% | -21.9% | 관망 중 +0.0% / 보유 -1.7% (2.7일) | 진입: price_above_ma(n=26, kind=ema) AND volume_spike(n=28, mult=2.52) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=99, kind=sma) | 손절 14.3% / 익절 27.3% / 트레일링 21.4% |
| 7 | `6335aeebf2` | 2026-10-10 | 2.01 | 2.08 | 0.59 | +11.2% | -23.9% | 관망 중 +0.0% / 보유 -0.6% (0.7일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) |
| 8 | `ae82267119` | 2026-10-09 | 1.72 | 2.35 | 0.72 | +11.1% | -17.9% | 관망 중 +0.0% / 보유 +0.1% (2.3일) | 진입: price_above_ma(n=169, kind=ema) AND volume_spike(n=35, mult=3.62) | 청산: price_below_ma(n=56, kind=sma) | 익절 38.6% |
| 9 | `fd1c453679` | 2026-10-10 | 1.98 | 2.08 | 0.51 | +9.6% | -24.8% | 관망 중 +0.0% / 보유 +0.1% (1.3일) | 진입: volume_spike(n=20, mult=1.54) AND volume_spike(n=15, mult=2.715) AND price_above_ma(n=16, kind=sma) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=78, kind=sma) | 익절 27.3% |
| 10 | `030e70f004` | 2026-10-10 | 2.07 | 1.99 | 0.15 | +1.1% | -20.4% | 관망 중 +0.0% / 보유 -0.6% (0.7일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=47, slow=239, kind=sma) OR donchian_low_break(n=46) | 익절 29.1% |
| 11 | `4f7cd897f0` | 2026-10-10 | 2.21 | 1.81 | 0.75 | +13.8% | -23.9% | 관망 중 +0.0% / 보유 -0.5% (1.0일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 12 | `f00b4a37e3` | 2026-10-08 | 1.99 | 2.03 | 0.56 | +11.6% | -29.2% | 관망 중 +0.0% / 보유 -3.6% (3.7일) | 진입: donchian_break(n=66) AND price_above_ma(n=197, kind=sma) AND volume_spike(n=44, mult=1.334) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 13 | `7ba6000391` | 2026-10-09 | 1.74 | 2.24 | 0.69 | +14.1% | -15.6% | 관망 중 +0.0% / 보유 -1.1% (2.0일) | 진입: donchian_break(n=26) | 청산: price_below_ma(n=15, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.1% / 트레일링 21.4% |
| 14 | `f7e00c6fe8` | 2026-10-08 | 1.86 | 2.10 | 1.21 | +22.2% | -22.0% | 관망 중 +0.0% / 보유 -3.6% (3.7일) | 진입: donchian_break(n=71) AND price_above_ma(n=197, kind=sma) | 청산: price_below_ma(n=22, kind=ema) | 손절 19.1% / 익절 27.3% / 트레일링 24.5% |
| 15 | `88b03c3bd9` | 2026-10-09 | 1.79 | 2.14 | 0.11 | +0.5% | -23.4% | 관망 중 +0.0% / 보유 -1.1% (2.0일) | 진입: low_volatility(n=43, q=0.24) AND donchian_break(n=16) | 청산: price_below_ma(n=39, kind=ema) | 손절 12.0% / 익절 27.3% |
| 16 | `08a39b7267` | 2026-10-10 | 1.92 | 1.97 | 0.64 | +8.6% | -21.2% | 관망 중 +0.0% / 보유 +0.1% (1.3일) | 진입: macd_pos(f=14, s=21, sig=7) AND volume_spike(n=29, mult=3.51) | 청산: price_below_ma(n=51, kind=sma) | 익절 60.8% |
| 17 | `2439726ead` | 2026-10-08 | 1.69 | 2.19 | 0.54 | +11.4% | -23.7% | 관망 중 +0.0% / 보유 -3.2% (3.2일) | 진입: donchian_break(n=12) AND volume_spike(n=24, mult=2.89) | 청산: price_below_ma(n=116, kind=sma) |
| 18 | `6f3685817a` | 2026-10-10 | 2.05 | 1.78 | 0.67 | +11.5% | -16.9% | 관망 중 +0.0% / 보유 -0.6% (0.7일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) AND ma_cross_up(fast=13, slow=154, kind=sma) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 19 | `ed518e2f80` | 2026-10-11 | 2.01 | 1.79 | 0.56 | +9.6% | -22.1% | 관망 중 +0.0% / 보유 -0.9% (0.3일) | 진입: volume_spike(n=12, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: ma_cross_down(fast=5, slow=108, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 20 | `b12dd3fbc7` | 2026-10-09 | 1.70 | 2.11 | 0.65 | +11.8% | -30.1% | 관망 중 +0.0% / 보유 -1.7% (2.7일) | 진입: donchian_break(n=52) | 청산: price_below_ma(n=42, kind=sma) OR donchian_low_break(n=53) | 익절 33.6% |
| 21 | `d64bf6417c` 🆕 | 2026-10-11 | 1.60 | 1.94 | 0.15 | +5.6% | -28.4% | - | 진입: ma_cross_up(fast=38, slow=189, kind=sma) AND donchian_break(n=31) | 청산: bars_held(n=48) | 손절 10.4% / 익절 18.0% |
| 22 | `a0dbda8ff5` 🆕 | 2026-10-11 | 1.48 | 1.97 | 0.70 | +8.7% | -13.0% | - | 진입: donchian_break(n=78) AND low_volatility(n=48, q=0.45) | 청산: price_below_ma(n=16, kind=sma) | 손절 17.2% / 익절 18.6% |
| 23 | `f25d57d3ab` 🆕 | 2026-10-11 | 1.42 | 1.79 | 0.93 | +15.5% | -18.8% | - | 진입: volume_spike(n=20, mult=3.064) AND momentum_pos(n=17, th=0.01) AND low_volatility(n=53, q=0.37) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 29.1% / 트레일링 27.2% |

비교 기준(단순 보유) 샤프 — 학습 0.93 · 검증 1.24 · 시험 -0.40

![top equity](top_equity.png)

샤프·CAGR·MDD는 여러 코인의 중앙값, 수수료 0.05% + 슬리피지 0.05% 반영.
백테스트 성과는 미래 수익을 보장하지 않습니다. 실거래 전에 '전진' 성과가 충분히 쌓였는지 확인하세요.