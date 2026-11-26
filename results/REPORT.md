# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-11-26** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

## 🎓 졸업 심사

전당에 오른 뒤 **실제로 새로 쌓인 시세**로 매기는 시험이에요. 기준: 전진 60일 이상 · 그 기간에 +10% 넘는 상승장 포함 · 실제 거래 10회 이상(4코인 합) · 같은 기간 단순 보유보다 나은 수익 · 코인별 최대 낙폭 -20% 이내 · 튼튼함 심사 통과.

**졸업한 전략: 아직 없음**

졸업에 가장 가까운 전략:

| ID | 전진 기간 | 상승장 경험 | 실제 거래 | 보유 대비 | 최대 낙폭 | 튼튼함 | 통과 |
|---|---|---|---|---|---|---|---|
| `20fa805145` | ⬜ 50일 | ✅ 11% | ✅ 10회 | ✅ +30.4%p | ✅ -6% | ✅ 통과 | 5/6 |
| `cdcac84052` | ⬜ 49일 | ✅ 11% | ✅ 18회 | ✅ +27.8%p | ✅ -7% | ✅ 통과 | 5/6 |
| `7ba6000391` | ⬜ 48일 | ✅ 11% | ✅ 11회 | ✅ +30.6%p | ✅ -7% | ✅ 통과 | 5/6 |
| `cba03c6a1a` | ⬜ 48일 | ✅ 11% | ✅ 12회 | ✅ +27.4%p | ✅ -9% | ✅ 통과 | 5/6 |
| `fd1c453679` | ⬜ 48일 | ✅ 11% | ✅ 14회 | ✅ +24.8%p | ✅ -9% | ✅ 통과 | 5/6 |
| `08a39b7267` | ⬜ 48일 | ✅ 11% | ✅ 10회 | ✅ +24.5%p | ✅ -11% | ✅ 통과 | 5/6 |
| `d7fb6c9904` | ⬜ 47일 | ✅ 11% | ✅ 13회 | ✅ +25.7%p | ✅ -9% | ✅ 통과 | 5/6 |
| `f7e00c6fe8` | ⬜ 50일 | ✅ 11% | ⬜ 0회 | ✅ +33.8%p | ✅ 0% | ✅ 통과 | 4/6 |

## 📡 지금 보유 신호

전당 전략 45개 중 현재 코인을 들고 있는 전략: **SOL 1개**

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-11-26 08:00 UTC
- 1098세대 진화, 전략 55,572개 평가
- 1240세대 진화, 전략 110,157개 평가
- 튼튼함 심사: 0개 시도 → 0개 통과
- 새로 명예의 전당 입성: 0개 (오늘 누적 3/3, 검증 구간 B&H 샤프 0.72)

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 / 같은 기간 보유 | 지금 | 전략 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `f7e00c6fe8` | 2026-10-08 | 1.91 | 1.90 | 0.83 | +13.3% | -22.0% | 관망 +0.0% / 보유 -33.8% (50일) | 관망 | 진입: donchian_break(n=71) AND price_above_ma(n=197, kind=sma) | 청산: price_below_ma(n=22, kind=ema) | 손절 19.1% / 익절 27.3% / 트레일링 24.5% |
| 2 | `f00b4a37e3` | 2026-10-08 | 2.05 | 1.64 | 0.63 | +10.3% | -29.2% | 관망 +0.0% / 보유 -33.8% (50일) | 관망 | 진입: donchian_break(n=66) AND price_above_ma(n=197, kind=sma) AND volume_spike(n=44, mult=1.334) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 3 | `7ba6000391` | 2026-10-09 | 1.86 | 2.00 | 0.54 | +11.4% | -15.9% | -1.6% / 보유 -32.2% (48일) | 관망 | 진입: donchian_break(n=26) | 청산: price_below_ma(n=15, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.1% / 트레일링 21.4% |
| 4 | `3e0a3dbb31` | 2026-10-11 | 2.14 | 2.01 | 0.59 | +7.7% | -16.1% | -4.6% / 보유 -32.0% (47일) | 관망 | 진입: volume_spike(n=26, mult=3.63) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 5 | `20fa805145` | 2026-10-08 | 1.88 | 1.94 | 0.61 | +8.6% | -18.9% | -3.5% / 보유 -33.8% (50일) | 관망 | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=37, mult=3.51) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 6 | `cba03c6a1a` | 2026-10-09 | 1.79 | 2.29 | 0.38 | +5.5% | -19.4% | -4.8% / 보유 -32.2% (48일) | 관망 | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=32, mult=3.51) | 청산: ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 7 | `5ade91c3ae` | 2026-10-13 | 1.77 | 1.88 | 0.99 | +18.7% | -11.4% | 관망 +0.0% / 보유 -31.0% (45일) | 관망 | 진입: volume_spike(n=34, mult=3.53) AND donchian_break(n=83) | 청산: price_below_ma(n=139, kind=ema) OR donchian_low_break(n=18) | 손절 9.5% / 익절 32.2% |
| 8 | `ae82267119` | 2026-10-09 | 1.89 | 1.69 | 0.62 | +8.6% | -17.9% | 관망 +0.0% / 보유 -31.4% (49일) | 관망 | 진입: price_above_ma(n=169, kind=ema) AND volume_spike(n=35, mult=3.62) | 청산: price_below_ma(n=56, kind=sma) | 익절 38.6% |
| 9 | `6f3685817a` | 2026-10-10 | 1.87 | 1.56 | 0.46 | +6.6% | -16.9% | 관망 +0.0% / 보유 -31.8% (47일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) AND ma_cross_up(fast=13, slow=154, kind=sma) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 10 | `cdcac84052` | 2026-10-09 | 1.82 | 1.98 | 0.08 | +2.8% | -21.9% | -4.8% / 보유 -32.6% (49일) | 관망 | 진입: price_above_ma(n=26, kind=ema) AND volume_spike(n=28, mult=2.52) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=99, kind=sma) | 손절 14.3% / 익절 27.3% / 트레일링 21.4% |
| 11 | `4f7cd897f0` | 2026-10-10 | 2.28 | 1.65 | 0.37 | +5.7% | -23.9% | -5.5% / 보유 -31.8% (47일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 12 | `43ba22956d` | 2026-11-23 | 2.34 | 1.44 | 0.24 | +5.0% | -19.6% | 관망 +0.0% / 보유 -0.0% (4일) | 관망 | 진입: macd_pos(f=3, s=29, sig=16) AND ma_cross_up(fast=36, slow=112, kind=ema) AND ma_cross_up(fast=5, slow=23, kind=ema) | 청산: donchian_low_break(n=9) OR rsi_above(n=25, th=79) OR bars_held(n=21) | 익절 30.4% |
| 13 | `114ad67d25` | 2026-10-11 | 2.01 | 1.76 | 0.06 | -1.5% | -27.4% | -5.1% / 보유 -32.0% (47일) | 관망 | 진입: volume_spike(n=20, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=142, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 14 | `d7fb6c9904` | 2026-10-11 | 1.95 | 1.91 | 0.09 | -0.6% | -27.2% | -6.3% / 보유 -32.0% (47일) | 관망 | 진입: volume_spike(n=15, mult=2.369) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 41.1% |
| 15 | `2439726ead` | 2026-10-08 | 1.68 | 1.95 | 0.14 | +0.7% | -23.7% | -5.9% / 보유 -33.6% (50일) | 관망 | 진입: donchian_break(n=12) AND volume_spike(n=24, mult=2.89) | 청산: price_below_ma(n=116, kind=sma) |
| 16 | `b12dd3fbc7` | 2026-10-09 | 1.78 | 1.63 | 0.32 | +3.0% | -30.1% | -2.9% / 보유 -32.6% (49일) | 관망 | 진입: donchian_break(n=52) | 청산: price_below_ma(n=42, kind=sma) OR donchian_low_break(n=53) | 익절 33.6% |
| 17 | `fd1c453679` | 2026-10-10 | 2.05 | 1.84 | 0.23 | +2.9% | -23.3% | -6.6% / 보유 -31.4% (48일) | 관망 | 진입: volume_spike(n=20, mult=1.54) AND volume_spike(n=15, mult=2.715) AND price_above_ma(n=16, kind=sma) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=78, kind=sma) | 익절 27.3% |
| 18 | `4ca2bafdac` | 2026-10-27 | 1.52 | 2.26 | 0.59 | +9.5% | -18.9% | 관망 +0.0% / 보유 -25.8% (31일) | 관망 | 진입: donchian_break(n=86) OR drawdown_from_high(n=21, th=0.19) | 청산: donchian_low_break(n=27) OR price_below_ma(n=30, kind=ema) | 익절 6.2% |
| 19 | `88b03c3bd9` | 2026-10-09 | 1.82 | 1.45 | -0.16 | -3.8% | -23.4% | -1.2% / 보유 -32.2% (48일) | 관망 | 진입: low_volatility(n=43, q=0.24) AND donchian_break(n=16) | 청산: price_below_ma(n=39, kind=ema) | 손절 12.0% / 익절 27.3% |
| 20 | `6335aeebf2` | 2026-10-10 | 2.03 | 1.63 | 0.23 | +2.6% | -23.9% | -5.5% / 보유 -31.8% (47일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) |
| 21 | `fa158e2ae7` | 2026-11-21 | 1.93 | 1.56 | -0.14 | -4.0% | -20.1% | -2.2% / 보유 +1.9% (6일) | 관망 | 진입: volume_spike(n=19, mult=3.625) AND price_above_ma(n=18, kind=sma) | 청산: bars_held(n=38) OR donchian_low_break(n=21) | 손절 29.2% / 익절 30.0% / 트레일링 26.3% |
| 22 | `030e70f004` | 2026-10-10 | 2.05 | 1.41 | -0.09 | -3.2% | -20.9% | -4.2% / 보유 -31.8% (47일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=47, slow=239, kind=sma) OR donchian_low_break(n=46) | 익절 29.1% |
| 23 | `848c7af378` | 2026-11-20 | 1.71 | 1.66 | 0.47 | +7.4% | -21.8% | 관망 +0.0% / 보유 -2.3% (6일) | 관망 | 진입: price_above_ma(n=76, kind=sma) AND macd_pos(f=7, s=26, sig=7) AND low_volatility(n=44, q=0.5) | 청산: price_below_ma(n=22, kind=ema) | 익절 28.0% / 트레일링 27.7% |
| 24 | `ed518e2f80` | 2026-10-11 | 2.00 | 1.50 | 0.21 | +2.1% | -22.1% | -5.8% / 보유 -32.0% (47일) | 관망 | 진입: volume_spike(n=12, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: ma_cross_down(fast=5, slow=108, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 25 | `3504da9518` | 2026-11-20 | 1.20 | 2.12 | 0.98 | +12.6% | -11.2% | 관망 +0.0% / 보유 -3.0% (7일) | 관망 | 진입: donchian_break(n=90) AND volume_spike(n=55, mult=3.84) | 청산: bars_held(n=40) | 손절 4.6% |
| 26 | `c1fa33b98e` | 2026-11-21 | 1.80 | 1.49 | 0.95 | +13.1% | -17.5% | 관망 +0.0% / 보유 +1.9% (6일) | 관망 | 진입: volume_spike(n=26, mult=3.619) AND low_volatility(n=45, q=0.64) | 청산: price_below_ma(n=55, kind=sma) | 손절 22.7% / 익절 30.0% |
| 27 | `3ec1452b69` | 2026-11-21 | 1.76 | 1.53 | 0.69 | +12.1% | -21.2% | 관망 +0.0% / 보유 +1.9% (6일) | 관망 | 진입: low_volatility(n=36, q=0.56) AND momentum_pos(n=17, th=0.008) AND volume_spike(n=10, mult=2.599) | 청산: price_below_ma(n=58, kind=sma) OR ma_cross_down(fast=6, slow=107, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 21.3% / 익절 29.1% |
| 28 | `08a39b7267` | 2026-10-10 | 2.03 | 1.58 | 0.03 | -1.1% | -21.2% | -6.9% / 보유 -31.4% (48일) | 관망 | 진입: macd_pos(f=14, s=21, sig=7) AND volume_spike(n=29, mult=3.51) | 청산: price_below_ma(n=51, kind=sma) | 익절 60.8% |
| 29 | `84fcd77045` | 2026-10-12 | 1.43 | 1.76 | 0.20 | +1.8% | -12.2% | -3.9% / 보유 -32.2% (46일) | 관망 | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) AND volume_spike(n=10, mult=2.61) | 청산: bars_held(n=12) OR ma_cross_down(fast=6, slow=109, kind=sma) | 손절 28.0% / 익절 29.1% / 트레일링 28.7% |
| 30 | `481633c95e` | 2026-11-24 | 2.08 | 1.17 | -0.11 | -2.7% | -19.0% | 관망 +0.0% / 보유 -1.1% (2일) | 관망 | 진입: macd_pos(f=23, s=54, sig=12) AND volume_spike(n=19, mult=3.152) AND price_above_ma(n=232, kind=ema) | 청산: price_below_ma(n=56, kind=sma) OR ma_cross_down(fast=51, slow=150, kind=sma) | 익절 46.7% / 트레일링 9.4% |
| 31 | `404256e1c1` | 2026-11-24 | 1.69 | 1.52 | 0.64 | +12.0% | -16.4% | 관망 +0.0% / 보유 -1.1% (2일) | 관망 | 진입: macd_pos(f=17, s=34, sig=6) AND volume_spike(n=44, mult=1.39) AND ma_cross_up(fast=47, slow=187, kind=ema) | 청산: bars_held(n=13) OR price_below_ma(n=17, kind=ema) |
| 32 | `7efbcacdba` | 2026-11-26 | 1.64 | 1.49 | 0.09 | -0.2% | -17.2% | 관망 +0.0% / 보유 +0.8% (0일) | 관망 | 진입: price_above_ma(n=18, kind=sma) AND volume_spike(n=60, mult=3.45) | 청산: donchian_low_break(n=20) | 손절 4.0% / 익절 30.6% |
| 33 | `c8693cdfa2` | 2026-11-24 | 1.78 | 1.36 | -0.11 | -2.3% | -15.0% | 관망 +0.0% / 보유 -1.1% (2일) | 관망 | 진입: macd_pos(f=21, s=26, sig=12) AND volume_spike(n=20, mult=3.173) AND donchian_break(n=58) | 청산: price_below_ma(n=58, kind=sma) OR ma_cross_down(fast=51, slow=150, kind=sma) OR donchian_low_break(n=19) | 익절 46.7% / 트레일링 20.7% |
| 34 | `f1611a53cb` | 2026-11-23 | 1.60 | 1.48 | -0.43 | -10.5% | -34.1% | -5.1% / 보유 -0.0% (4일) | 관망 | 진입: macd_pos(f=3, s=29, sig=15) AND volume_spike(n=10, mult=1.78) | 청산: price_below_ma(n=16, kind=sma) OR rsi_above(n=25, th=79) | 익절 25.6% |
| 35 | `20158f4a24` | 2026-11-25 | 1.77 | 1.26 | 0.48 | +10.5% | -23.7% | 관망 +0.0% / 보유 +1.5% (2일) | 관망 | 진입: ma_cross_up(fast=38, slow=104, kind=ema) AND macd_pos(f=12, s=23, sig=10) AND rsi_below(n=2, th=40) | 청산: price_below_ma(n=56, kind=sma) OR rsi_above(n=11, th=88) OR bars_held(n=56) | 익절 27.1% |
| 36 | `efc7382834` | 2026-11-23 | 1.63 | 1.37 | 0.69 | +11.2% | -14.6% | 관망 +0.0% / 보유 -0.0% (4일) | 관망 | 진입: low_volatility(n=31, q=0.43) AND donchian_break(n=30) AND ma_cross_up(fast=23, slow=138, kind=sma) | 청산: price_below_ma(n=70, kind=sma) OR price_below_ma(n=33, kind=ema) | 트레일링 27.4% |
| 37 | `88108241f6` | 2026-11-22 | 1.75 | 1.25 | 0.85 | +13.6% | -20.3% | 관망 +0.0% / 보유 -0.0% (5일) | 관망 | 진입: donchian_break(n=27) AND low_volatility(n=59, q=0.29) | 청산: ma_cross_down(fast=39, slow=61, kind=ema) OR price_below_ma(n=54, kind=sma) | 손절 16.0% / 익절 52.7% |
| 38 | `51e55b9c84` | 2026-10-26 | 1.59 | 1.68 | 1.44 | +17.1% | -9.3% | -1.7% / 보유 -26.4% (32일) | SOL | 진입: volume_spike(n=14, mult=3.68) AND donchian_break(n=51) | 청산: bars_held(n=35) | 손절 12.9% / 익절 40.4% / 트레일링 26.8% |
| 39 | `38bbcc0f77` | 2026-11-25 | 1.59 | 1.36 | 0.02 | -2.8% | -15.9% | 관망 +0.0% / 보유 +1.5% (2일) | 관망 | 진입: macd_pos(f=12, s=23, sig=10) AND volume_spike(n=22, mult=3.98) | 청산: price_below_ma(n=56, kind=sma) OR rsi_above(n=11, th=88) OR bars_held(n=56) | 익절 27.1% |
| 40 | `427e33e785` | 2026-11-22 | 1.55 | 1.31 | 0.32 | +5.4% | -26.5% | -6.6% / 보유 -0.0% (5일) | 관망 | 진입: volume_spike(n=37, mult=2.16) AND macd_pos(f=7, s=44, sig=15) | 청산: bars_held(n=20) OR price_below_ma(n=22, kind=sma) | 익절 7.9% / 트레일링 17.2% |
| 41 | `e732e3a52d` | 2026-11-26 | 1.46 | 1.40 | 0.34 | +4.8% | -16.7% | 관망 +0.0% / 보유 +0.8% (0일) | 관망 | 진입: price_above_ma(n=153, kind=sma) AND volume_spike(n=17, mult=3.51) | 청산: donchian_low_break(n=8) | 손절 12.0% / 익절 30.8% |
| 42 | `b7368702af` | 2026-11-26 | 1.37 | 1.45 | 1.07 | +14.0% | -10.8% | 관망 +0.0% / 보유 +0.8% (0일) | 관망 | 진입: price_above_ma(n=46, kind=ema) AND volume_spike(n=18, mult=3.559) AND low_volatility(n=33, q=0.4) | 청산: price_below_ma(n=58, kind=sma) OR ma_cross_down(fast=5, slow=111, kind=sma) OR ma_cross_down(fast=12, slow=82, kind=ema) | 익절 30.1% |
| 43 | `4d4d21ab4f` | 2026-11-22 | 1.22 | 1.45 | 0.84 | +14.3% | -16.5% | 관망 +0.0% / 보유 -0.0% (5일) | 관망 | 진입: donchian_break(n=86) AND volume_spike(n=53, mult=2.4) | 청산: donchian_low_break(n=23) | 손절 3.9% / 익절 29.7% / 트레일링 19.1% |
| 44 | `063f69d8d7` | 2026-11-25 | 1.38 | 1.24 | 0.09 | -0.8% | -11.7% | 관망 +0.0% / 보유 +1.5% (2일) | 관망 | 진입: ma_cross_up(fast=38, slow=111, kind=ema) AND volume_spike(n=11, mult=3.52) AND momentum_pos(n=30, th=0.005) | 청산: price_below_ma(n=56, kind=sma) OR rsi_above(n=11, th=88) | 익절 26.3% |
| 45 | `5b8f9bc24f` | 2026-11-18 | 1.34 | 1.91 | 0.53 | +9.0% | -16.0% | 관망 +0.0% / 보유 -4.8% (8일) | 관망 | 진입: donchian_break(n=90) OR drawdown_from_high(n=23, th=0.168) | 청산: price_below_ma(n=18, kind=sma) OR bars_held(n=38) |

비교 기준(단순 보유) 샤프 — 학습 0.99 · 검증 0.72 · 시험 -1.02

![top equity](top_equity.png)

<details><summary>📖 규칙 설명</summary>

**데이터 나누기** — 과거 시세를 학습(앞 60%) · 검증(다음 20%) · 시험(마지막 20%)으로 나눠요. 전략은 학습 구간 성적으로만 진화하고, 검증 구간으로 입성을 심사해요. 시험 구간은 참고로 보여주기만 해요.

**입성 심사** — ① 검증 구간 샤프가 단순 보유보다 0.5 이상 높을 것 ② 기존 전당 전략과 수익 흐름이 비슷하지 않을 것(상관 0.7 이하) ③ 튼튼함 심사: 숫자 파라미터를 ±15% 흔든 변형 6개도 대체로 좋을 것, 거래 비용이 3배여도 단순 보유보다 나을 것, 4개 코인 중 3개 이상에서 단순 보유보다 나을 것. 하루 최대 3개.

**자리 관리** — 전당은 45자리. 입성 후 42봉(7일) 동안은 보호돼요. 자리가 차면, 보호 기간이 끝난 전략과 신입 중 점수가 가장 낮은 것이 나가요. 보호 기간 뒤 낙폭이 -35%보다 나빠지면 퇴출돼요.

**점수** — 학습·검증 샤프 평균에, 보호 기간이 끝난 전략은 '같은 기간 단순 보유 대비 초과 수익'을 더해요. 하락장에서 현금으로 피한 것도 실력으로 인정돼요.

**체결 가정** — 봉 마감 신호 → 다음 봉 시가 체결, 수수료 0.05% + 슬리피지 0.05%(한쪽), 같은 봉에서 손절·익절이 둘 다 닿으면 손절로 처리. 샤프·CAGR·MDD는 4개 코인의 중앙값.

</details>

백테스트와 졸업은 미래 수익을 보장하지 않습니다. 이 리포트는 투자 권유가 아니에요.