# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-10-15** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

> 학습(앞 60%)으로만 진화 → 검증(다음 20%)으로 입성 심사 → 시험(마지막 20%)은 보고만. '전진'은 전당에 오른 뒤 실제로 새로 쌓인 데이터에서의 성과이고, 옆의 '보유'는 같은 기간 그냥 들고 있었을 때입니다. 전진 기록이 42봉 이상 쌓이기 전까지는 퇴출되지 않습니다.

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-10-14 16:00 UTC
- 1428세대 진화, 전략 66,983개 평가
- 새로 명예의 전당 입성: 3개 (오늘 누적 3/3, 검증 구간 B&H 샤프 1.25)
- 퇴출: f00b4a37e3, f7e00c6fe8, 20fa805145

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 | 전략 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `3e0a3dbb31` | 2026-10-11 | 2.07 | 2.41 | 0.94 | +13.9% | -16.1% | 관망 중 +0.0% / 보유 -4.3% (4.0일) | 진입: volume_spike(n=26, mult=3.63) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 2 | `d7fb6c9904` | 2026-10-11 | 1.90 | 2.32 | 0.44 | +6.5% | -27.9% | 관망 중 +0.0% / 보유 -4.3% (4.0일) | 진입: volume_spike(n=15, mult=2.369) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 41.1% |
| 3 | `114ad67d25` | 2026-10-11 | 1.96 | 2.26 | 0.54 | +11.0% | -27.4% | 관망 중 +0.0% / 보유 -4.3% (4.0일) | 진입: volume_spike(n=20, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=142, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 4 | `cba03c6a1a` | 2026-10-09 | 1.71 | 2.49 | 0.82 | +15.4% | -19.4% | +0.1% / 보유 -4.5% (5.7일) | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=32, mult=3.51) | 청산: ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 5 | `cdcac84052` | 2026-10-09 | 1.69 | 2.41 | 0.50 | +11.0% | -21.9% | +0.0% / 보유 -5.1% (6.3일) | 진입: price_above_ma(n=26, kind=ema) AND volume_spike(n=28, mult=2.52) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=99, kind=sma) | 손절 14.3% / 익절 27.3% / 트레일링 21.4% |
| 6 | `ae82267119` | 2026-10-09 | 1.72 | 2.37 | 0.72 | +11.1% | -17.9% | 관망 중 +0.0% / 보유 -3.3% (6.0일) | 진입: price_above_ma(n=169, kind=ema) AND volume_spike(n=35, mult=3.62) | 청산: price_below_ma(n=56, kind=sma) | 익절 38.6% |
| 7 | `6335aeebf2` | 2026-10-10 | 2.01 | 2.08 | 0.59 | +11.2% | -23.9% | 관망 중 +0.0% / 보유 -4.0% (4.3일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) |
| 8 | `fd1c453679` | 2026-10-10 | 1.98 | 2.08 | 0.60 | +12.2% | -24.8% | +0.1% / 보유 -3.3% (5.0일) | 진입: volume_spike(n=20, mult=1.54) AND volume_spike(n=15, mult=2.715) AND price_above_ma(n=16, kind=sma) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=78, kind=sma) | 익절 27.3% |
| 9 | `030e70f004` | 2026-10-10 | 2.07 | 1.99 | 0.15 | +1.1% | -20.4% | 관망 중 +0.0% / 보유 -4.0% (4.3일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=47, slow=239, kind=sma) OR donchian_low_break(n=46) | 익절 29.1% |
| 10 | `4f7cd897f0` | 2026-10-10 | 2.20 | 1.81 | 0.75 | +13.8% | -23.9% | 관망 중 +0.0% / 보유 -4.0% (4.7일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 11 | `7ba6000391` | 2026-10-09 | 1.74 | 2.17 | 0.77 | +16.2% | -15.6% | 관망 중 +0.0% / 보유 -4.5% (5.7일) | 진입: donchian_break(n=26) | 청산: price_below_ma(n=15, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.1% / 트레일링 21.4% |
| 12 | `88b03c3bd9` | 2026-10-09 | 1.77 | 2.14 | 0.11 | +0.5% | -23.4% | -0.3% / 보유 -4.5% (5.7일) | 진입: low_volatility(n=43, q=0.24) AND donchian_break(n=16) | 청산: price_below_ma(n=39, kind=ema) | 손절 12.0% / 익절 27.3% |
| 13 | `08a39b7267` | 2026-10-10 | 1.92 | 1.97 | 0.64 | +8.6% | -21.2% | 관망 중 +0.0% / 보유 -3.3% (5.0일) | 진입: macd_pos(f=14, s=21, sig=7) AND volume_spike(n=29, mult=3.51) | 청산: price_below_ma(n=51, kind=sma) | 익절 60.8% |
| 14 | `6f3685817a` | 2026-10-10 | 2.04 | 1.80 | 0.67 | +11.5% | -16.9% | 관망 중 +0.0% / 보유 -4.0% (4.3일) | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) AND ma_cross_up(fast=13, slow=154, kind=sma) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 15 | `2439726ead` | 2026-10-08 | 1.69 | 2.15 | 0.64 | +13.6% | -23.7% | 관망 중 +0.0% / 보유 -6.5% (6.8일) | 진입: donchian_break(n=12) AND volume_spike(n=24, mult=2.89) | 청산: price_below_ma(n=116, kind=sma) |
| 16 | `ed518e2f80` | 2026-10-11 | 2.01 | 1.81 | 0.56 | +10.1% | -22.1% | 관망 중 +0.0% / 보유 -4.3% (4.0일) | 진입: volume_spike(n=12, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: ma_cross_down(fast=5, slow=108, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 17 | `b12dd3fbc7` | 2026-10-09 | 1.70 | 1.99 | 0.65 | +11.8% | -30.1% | 관망 중 +0.0% / 보유 -5.1% (6.3일) | 진입: donchian_break(n=52) | 청산: price_below_ma(n=42, kind=sma) OR donchian_low_break(n=53) | 익절 33.6% |
| 18 | `5ade91c3ae` | 2026-10-13 | 1.76 | 1.84 | 1.47 | +30.2% | -12.1% | 관망 중 +0.0% / 보유 -2.8% (2.2일) | 진입: volume_spike(n=34, mult=3.53) AND donchian_break(n=83) | 청산: price_below_ma(n=139, kind=ema) OR donchian_low_break(n=18) | 손절 9.5% / 익절 32.2% |
| 19 | `0159cf6bdc` 🆕 | 2026-10-15 | 1.63 | 1.94 | 0.69 | +10.8% | -20.7% | - | 진입: volume_spike(n=29, mult=3.02) AND macd_pos(f=14, s=57, sig=10) AND donchian_break(n=16) | 청산: ma_cross_down(fast=6, slow=123, kind=sma) | 손절 15.2% / 익절 9.6% |
| 20 | `d64bf6417c` | 2026-10-11 | 1.64 | 1.84 | 0.26 | +7.3% | -28.4% | 관망 중 +0.0% / 보유 -3.4% (3.7일) | 진입: ma_cross_up(fast=38, slow=189, kind=sma) AND donchian_break(n=31) | 청산: bars_held(n=48) | 손절 10.4% / 익절 18.0% |
| 21 | `4fe2256c35` 🆕 | 2026-10-15 | 1.44 | 1.99 | 1.14 | +21.5% | -20.7% | - | 진입: low_volatility(n=54, q=0.58) AND donchian_break(n=36) | 청산: ma_cross_down(fast=7, slow=29, kind=ema) OR bars_held(n=35) | 손절 13.5% / 익절 46.6% / 트레일링 21.9% |
| 22 | `7746daa9c2` | 2026-10-12 | 1.53 | 1.82 | 0.61 | +16.3% | -20.9% | -0.4% / 보유 -4.4% (3.0일) | 진입: low_volatility(n=33, q=0.28) AND volume_spike(n=22, mult=2.3) | 청산: price_below_ma(n=64, kind=ema) OR donchian_low_break(n=38) |
| 23 | `84fcd77045` | 2026-10-12 | 1.43 | 1.88 | 0.52 | +5.2% | -12.2% | 관망 중 +0.0% / 보유 -4.4% (3.0일) | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) AND volume_spike(n=10, mult=2.61) | 청산: bars_held(n=12) OR ma_cross_down(fast=6, slow=109, kind=sma) | 손절 28.0% / 익절 29.1% / 트레일링 28.7% |
| 24 | `a0dbda8ff5` | 2026-10-11 | 1.45 | 1.86 | 0.75 | +10.5% | -13.0% | 관망 중 +0.0% / 보유 -3.4% (3.7일) | 진입: donchian_break(n=78) AND low_volatility(n=48, q=0.45) | 청산: price_below_ma(n=16, kind=sma) | 손절 17.2% / 익절 18.6% |
| 25 | `9b8b1a5627` | 2026-10-13 | 1.34 | 1.92 | 0.88 | +17.7% | -15.5% | 관망 중 +0.0% / 보유 -2.8% (2.2일) | 진입: volume_spike(n=43, mult=3.25) AND ma_cross_up(fast=6, slow=196, kind=sma) AND donchian_break(n=32) | 청산: price_below_ma(n=45, kind=ema) | 트레일링 11.9% |
| 26 | `f25d57d3ab` | 2026-10-11 | 1.42 | 1.79 | 0.93 | +15.5% | -18.8% | 관망 중 +0.0% / 보유 -3.4% (3.7일) | 진입: volume_spike(n=20, mult=3.064) AND momentum_pos(n=17, th=0.01) AND low_volatility(n=53, q=0.37) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 29.1% / 트레일링 27.2% |
| 27 | `ad5d089d4f` | 2026-10-14 | 1.29 | 1.89 | 0.57 | +11.1% | -18.2% | 관망 중 +0.0% / 보유 -2.4% (1.2일) | 진입: donchian_break(n=37) | 청산: bars_held(n=47) OR bars_held(n=4) | 트레일링 26.6% |
| 28 | `6e5115a679` | 2026-10-12 | 1.35 | 1.75 | 0.06 | -0.4% | -25.4% | -0.5% / 보유 -4.4% (3.0일) | 진입: volume_spike(n=53, mult=2.5) AND donchian_break(n=30) AND macd_pos(f=8, s=21, sig=10) | 청산: ma_cross_down(fast=44, slow=176, kind=ema) | 익절 44.7% / 트레일링 9.8% |
| 29 | `c69b0f0d84` 🆕 | 2026-10-15 | 1.29 | 1.80 | -0.14 | -5.3% | -24.9% | - | 진입: ma_cross_up(fast=46, slow=156, kind=sma) AND momentum_pos(n=103, th=0.034) AND macd_pos(f=10, s=22, sig=5) | 청산: price_below_ma(n=23, kind=ema) | 손절 11.1% / 트레일링 16.2% |
| 30 | `459b6429eb` | 2026-10-13 | 1.24 | 1.82 | 0.72 | +10.3% | -17.0% | 관망 중 +0.0% / 보유 -2.8% (2.2일) | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 4.8% |

비교 기준(단순 보유) 샤프 — 학습 0.93 · 검증 1.25 · 시험 -0.41

![top equity](top_equity.png)

샤프·CAGR·MDD는 여러 코인의 중앙값, 수수료 0.05% + 슬리피지 0.05% 반영.
백테스트 성과는 미래 수익을 보장하지 않습니다. 실거래 전에 '전진' 성과가 충분히 쌓였는지 확인하세요.