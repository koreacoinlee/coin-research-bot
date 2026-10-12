# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-10-13** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

> 학습(앞 60%)으로만 진화 → 검증(다음 20%)으로 입성 심사 → 시험(마지막 20%)은 보고만. '전진'은 전당에 오른 뒤 실제로 새로 쌓인 데이터에서의 성과이고, 옆의 '보유'는 같은 기간 그냥 들고 있었을 때입니다. 전진 기록이 42봉 이상 쌓이기 전까지는 퇴출되지 않습니다.

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-10-12 12:00 UTC
- 1337세대 진화, 전략 67,284개 평가
- 새로 명예의 전당 입성: 3개 (오늘 누적 3/3, 검증 구간 B&H 샤프 1.26)

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 | 전략 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `3e0a3dbb31` | 2026-10-11 | 2.08 | 2.36 | 0.94 | +13.9% | -16.1% | 관망 중 +0.0% / 보유 -1.6% (1.8일) | 진입: volume_spike(n=26, mult=3.63) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 2 | `114ad67d25` | 2026-10-11 | 1.97 | 2.26 | 0.54 | +11.0% | -27.4% | 관망 중 +0.0% / 보유 -1.6% (1.8일) | 진입: volume_spike(n=20, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=142, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 3 | `d7fb6c9904` | 2026-10-11 | 1.90 | 2.29 | 0.43 | +6.5% | -27.9% | 관망 중 +0.0% / 보유 -1.6% (1.8일) | 진입: volume_spike(n=15, mult=2.369) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 41.1% |
| 4 | `cba03c6a1a` | 2026-10-09 | 1.73 | 2.45 | 0.81 | +15.4% | -19.4% | 관망 중 +0.0% / 보유 -1.8% (3.5일) | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=32, mult=3.51) | 청산: ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 5 | `20fa805145` | 2026-10-08 | 1.85 | 2.32 | 0.94 | +14.9% | -18.9% | 관망 중 +0.0% / 보유 -4.2% (5.2일) | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=37, mult=3.51) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 6 | `6335aeebf2` | 2026-10-10 | 2.02 | 2.08 | 0.59 | +11.2% | -23.9% | 관망 중 +0.0% / 보유 -1.3% (2.2일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) |
| 7 | `cdcac84052` | 2026-10-09 | 1.70 | 2.38 | 0.50 | +10.9% | -21.9% | 관망 중 +0.0% / 보유 -2.4% (4.2일) | 진입: price_above_ma(n=26, kind=ema) AND volume_spike(n=28, mult=2.52) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=99, kind=sma) | 손절 14.3% / 익절 27.3% / 트레일링 21.4% |
| 8 | `fd1c453679` | 2026-10-10 | 1.98 | 2.08 | 0.59 | +11.9% | -24.8% | +0.0% / 보유 -0.6% (2.8일) | 진입: volume_spike(n=20, mult=1.54) AND volume_spike(n=15, mult=2.715) AND price_above_ma(n=16, kind=sma) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=78, kind=sma) | 익절 27.3% |
| 9 | `030e70f004` | 2026-10-10 | 2.07 | 1.99 | 0.15 | +1.1% | -20.4% | 관망 중 +0.0% / 보유 -1.3% (2.2일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=47, slow=239, kind=sma) OR donchian_low_break(n=46) | 익절 29.1% |
| 10 | `ae82267119` | 2026-10-09 | 1.73 | 2.33 | 0.72 | +11.1% | -17.9% | 관망 중 +0.0% / 보유 -0.6% (3.8일) | 진입: price_above_ma(n=169, kind=ema) AND volume_spike(n=35, mult=3.62) | 청산: price_below_ma(n=56, kind=sma) | 익절 38.6% |
| 11 | `4f7cd897f0` | 2026-10-10 | 2.21 | 1.81 | 0.75 | +13.8% | -23.9% | 관망 중 +0.0% / 보유 -1.2% (2.5일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 12 | `f7e00c6fe8` | 2026-10-08 | 1.86 | 2.10 | 1.21 | +22.2% | -22.0% | 관망 중 +0.0% / 보유 -4.2% (5.2일) | 진입: donchian_break(n=71) AND price_above_ma(n=197, kind=sma) | 청산: price_below_ma(n=22, kind=ema) | 손절 19.1% / 익절 27.3% / 트레일링 24.5% |
| 13 | `88b03c3bd9` | 2026-10-09 | 1.77 | 2.14 | 0.11 | +0.5% | -23.4% | -0.3% / 보유 -1.8% (3.5일) | 진입: low_volatility(n=43, q=0.24) AND donchian_break(n=16) | 청산: price_below_ma(n=39, kind=ema) | 손절 12.0% / 익절 27.3% |
| 14 | `f00b4a37e3` | 2026-10-08 | 1.99 | 1.92 | 0.64 | +12.8% | -29.2% | 관망 중 +0.0% / 보유 -4.2% (5.2일) | 진입: donchian_break(n=66) AND price_above_ma(n=197, kind=sma) AND volume_spike(n=44, mult=1.334) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 15 | `7ba6000391` | 2026-10-09 | 1.74 | 2.17 | 0.77 | +16.2% | -15.6% | 관망 중 +0.0% / 보유 -1.8% (3.5일) | 진입: donchian_break(n=26) | 청산: price_below_ma(n=15, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.1% / 트레일링 21.4% |
| 16 | `08a39b7267` | 2026-10-10 | 1.92 | 1.97 | 0.64 | +8.6% | -21.2% | 관망 중 +0.0% / 보유 -0.6% (2.8일) | 진입: macd_pos(f=14, s=21, sig=7) AND volume_spike(n=29, mult=3.51) | 청산: price_below_ma(n=51, kind=sma) | 익절 60.8% |
| 17 | `2439726ead` | 2026-10-08 | 1.70 | 2.13 | 0.61 | +13.6% | -23.7% | 관망 중 +0.0% / 보유 -3.9% (4.7일) | 진입: donchian_break(n=12) AND volume_spike(n=24, mult=2.89) | 청산: price_below_ma(n=116, kind=sma) |
| 18 | `6f3685817a` | 2026-10-10 | 2.06 | 1.75 | 0.67 | +11.5% | -16.9% | 관망 중 +0.0% / 보유 -1.3% (2.2일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) AND ma_cross_up(fast=13, slow=154, kind=sma) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 19 | `ed518e2f80` | 2026-10-11 | 2.01 | 1.76 | 0.56 | +10.2% | -22.1% | 관망 중 +0.0% / 보유 -1.6% (1.8일) | 진입: volume_spike(n=12, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: ma_cross_down(fast=5, slow=108, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 20 | `b12dd3fbc7` | 2026-10-09 | 1.70 | 2.01 | 0.65 | +11.8% | -30.1% | 관망 중 +0.0% / 보유 -2.4% (4.2일) | 진입: donchian_break(n=52) | 청산: price_below_ma(n=42, kind=sma) OR donchian_low_break(n=53) | 익절 33.6% |
| 21 | `5ade91c3ae` 🆕 | 2026-10-13 | 1.76 | 1.84 | 1.47 | +30.2% | -12.1% | - | 진입: volume_spike(n=34, mult=3.53) AND donchian_break(n=83) | 청산: price_below_ma(n=139, kind=ema) OR donchian_low_break(n=18) | 손절 9.5% / 익절 32.2% |
| 22 | `d64bf6417c` | 2026-10-11 | 1.63 | 1.79 | 0.26 | +7.3% | -28.4% | 관망 중 +0.0% / 보유 -0.7% (1.5일) | 진입: ma_cross_up(fast=38, slow=189, kind=sma) AND donchian_break(n=31) | 청산: bars_held(n=48) | 손절 10.4% / 익절 18.0% |
| 23 | `7746daa9c2` | 2026-10-12 | 1.53 | 1.84 | 0.62 | +16.7% | -20.9% | -0.2% / 보유 -1.7% (0.8일) | 진입: low_volatility(n=33, q=0.28) AND volume_spike(n=22, mult=2.3) | 청산: price_below_ma(n=64, kind=ema) OR donchian_low_break(n=38) |
| 24 | `a0dbda8ff5` | 2026-10-11 | 1.48 | 1.86 | 0.75 | +10.5% | -13.0% | 관망 중 +0.0% / 보유 -0.7% (1.5일) | 진입: donchian_break(n=78) AND low_volatility(n=48, q=0.45) | 청산: price_below_ma(n=16, kind=sma) | 손절 17.2% / 익절 18.6% |
| 25 | `84fcd77045` | 2026-10-12 | 1.43 | 1.88 | 0.52 | +5.2% | -12.2% | 관망 중 +0.0% / 보유 -1.7% (0.8일) | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) AND volume_spike(n=10, mult=2.61) | 청산: bars_held(n=12) OR ma_cross_down(fast=6, slow=109, kind=sma) | 손절 28.0% / 익절 29.1% / 트레일링 28.7% |
| 26 | `9b8b1a5627` 🆕 | 2026-10-13 | 1.35 | 1.87 | 0.88 | +17.7% | -15.5% | - | 진입: volume_spike(n=43, mult=3.25) AND ma_cross_up(fast=6, slow=196, kind=sma) AND donchian_break(n=32) | 청산: price_below_ma(n=45, kind=ema) | 트레일링 11.9% |
| 27 | `f25d57d3ab` | 2026-10-11 | 1.42 | 1.79 | 0.93 | +15.5% | -18.8% | 관망 중 +0.0% / 보유 -0.7% (1.5일) | 진입: volume_spike(n=20, mult=3.064) AND momentum_pos(n=17, th=0.01) AND low_volatility(n=53, q=0.37) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 29.1% / 트레일링 27.2% |
| 28 | `6e5115a679` | 2026-10-12 | 1.33 | 1.75 | 0.08 | -0.1% | -25.4% | -0.3% / 보유 -1.7% (0.8일) | 진입: volume_spike(n=53, mult=2.5) AND donchian_break(n=30) AND macd_pos(f=8, s=21, sig=10) | 청산: ma_cross_down(fast=44, slow=176, kind=ema) | 익절 44.7% / 트레일링 9.8% |
| 29 | `459b6429eb` 🆕 | 2026-10-13 | 1.25 | 1.82 | 0.72 | +10.3% | -17.0% | - | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 4.8% |

비교 기준(단순 보유) 샤프 — 학습 0.92 · 검증 1.26 · 시험 -0.37

![top equity](top_equity.png)

샤프·CAGR·MDD는 여러 코인의 중앙값, 수수료 0.05% + 슬리피지 0.05% 반영.
백테스트 성과는 미래 수익을 보장하지 않습니다. 실거래 전에 '전진' 성과가 충분히 쌓였는지 확인하세요.