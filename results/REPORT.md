# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-11-24** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

## 🎓 졸업 심사

전당에 오른 뒤 **실제로 새로 쌓인 시세**로 매기는 시험이에요. 기준: 전진 60일 이상 · 그 기간에 +10% 넘는 상승장 포함 · 실제 거래 10회 이상(4코인 합) · 같은 기간 단순 보유보다 나은 수익 · 코인별 최대 낙폭 -20% 이내 · 튼튼함 심사 통과.

**졸업한 전략: 아직 없음**

졸업에 가장 가까운 전략:

| ID | 전진 기간 | 상승장 경험 | 실제 거래 | 보유 대비 | 최대 낙폭 | 튼튼함 | 통과 |
|---|---|---|---|---|---|---|---|
| `20fa805145` | ⬜ 48일 | ✅ 11% | ✅ 10회 | ✅ +29.6%p | ✅ -6% | ✅ 통과 | 5/6 |
| `cdcac84052` | ⬜ 46일 | ✅ 11% | ✅ 18회 | ✅ +27.0%p | ✅ -7% | ✅ 통과 | 5/6 |
| `7ba6000391` | ⬜ 46일 | ✅ 11% | ✅ 11회 | ✅ +29.8%p | ✅ -7% | ✅ 통과 | 5/6 |
| `cba03c6a1a` | ⬜ 46일 | ✅ 11% | ✅ 12회 | ✅ +26.6%p | ✅ -9% | ✅ 통과 | 5/6 |
| `fd1c453679` | ⬜ 45일 | ✅ 11% | ✅ 14회 | ✅ +24.0%p | ✅ -9% | ✅ 통과 | 5/6 |
| `08a39b7267` | ⬜ 45일 | ✅ 11% | ✅ 10회 | ✅ +24.0%p | ✅ -10% | ✅ 통과 | 5/6 |
| `d7fb6c9904` | ⬜ 44일 | ✅ 11% | ✅ 13회 | ✅ +25.0%p | ✅ -9% | ✅ 통과 | 5/6 |
| `f7e00c6fe8` | ⬜ 48일 | ✅ 11% | ⬜ 0회 | ✅ +33.1%p | ✅ 0% | ✅ 통과 | 4/6 |

## 📡 지금 보유 신호

전당 전략 45개 중 현재 코인을 들고 있는 전략: **SOL 5개 · XRP 3개 · BTC 2개 · ETH 2개**

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-11-23 20:00 UTC
- 980세대 진화, 전략 56,318개 평가
- 1156세대 진화, 전략 113,368개 평가
- 튼튼함 심사: 7개 시도 → 3개 통과 (탈락 사유: 코인일관성 4, 이웃파라미터 1, 비용3배 2)
- 새로 명예의 전당 입성: 3개 (오늘 누적 3/3, 검증 구간 B&H 샤프 0.78)
- 퇴출: 44f7a03cc5, a9462e61b4, 04479044b1

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 / 같은 기간 보유 | 지금 | 전략 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `f7e00c6fe8` | 2026-10-08 | 1.88 | 1.97 | 1.06 | +19.2% | -22.0% | 관망 +0.0% / 보유 -33.1% (48일) | 관망 | 진입: donchian_break(n=71) AND price_above_ma(n=197, kind=sma) | 청산: price_below_ma(n=22, kind=ema) | 손절 19.1% / 익절 27.3% / 트레일링 24.5% |
| 2 | `f00b4a37e3` | 2026-10-08 | 2.03 | 1.77 | 0.72 | +13.4% | -29.2% | 관망 +0.0% / 보유 -33.1% (48일) | 관망 | 진입: donchian_break(n=66) AND price_above_ma(n=197, kind=sma) AND volume_spike(n=44, mult=1.334) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 3 | `20fa805145` | 2026-10-08 | 1.88 | 2.03 | 0.72 | +10.2% | -18.9% | -3.5% / 보유 -33.1% (48일) | 관망 | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=37, mult=3.51) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 4 | `3e0a3dbb31` | 2026-10-11 | 2.09 | 2.04 | 0.66 | +9.2% | -16.1% | -4.6% / 보유 -31.3% (44일) | 관망 | 진입: volume_spike(n=26, mult=3.63) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 5 | `7ba6000391` | 2026-10-09 | 1.81 | 2.00 | 0.67 | +14.8% | -15.9% | -1.6% / 보유 -31.4% (46일) | 관망 | 진입: donchian_break(n=26) | 청산: price_below_ma(n=15, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.1% / 트레일링 21.4% |
| 6 | `cba03c6a1a` | 2026-10-09 | 1.77 | 2.33 | 0.44 | +7.6% | -19.4% | -4.8% / 보유 -31.4% (46일) | 관망 | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=32, mult=3.51) | 청산: ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 7 | `5ade91c3ae` | 2026-10-13 | 1.79 | 1.92 | 1.24 | +24.2% | -12.1% | 관망 +0.0% / 보유 -30.2% (42일) | 관망 | 진입: volume_spike(n=34, mult=3.53) AND donchian_break(n=83) | 청산: price_below_ma(n=139, kind=ema) OR donchian_low_break(n=18) | 손절 9.5% / 익절 32.2% |
| 8 | `ae82267119` | 2026-10-09 | 1.84 | 1.82 | 0.72 | +10.2% | -17.9% | 관망 +0.0% / 보유 -30.6% (46일) | 관망 | 진입: price_above_ma(n=169, kind=ema) AND volume_spike(n=35, mult=3.62) | 청산: price_below_ma(n=56, kind=sma) | 익절 38.6% |
| 9 | `6f3685817a` | 2026-10-10 | 1.87 | 1.59 | 0.64 | +9.7% | -16.9% | 관망 +0.0% / 보유 -31.1% (44일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) AND ma_cross_up(fast=13, slow=154, kind=sma) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 30.7% |
| 10 | `4f7cd897f0` | 2026-10-10 | 2.26 | 1.72 | 0.43 | +7.1% | -23.9% | -5.5% / 보유 -31.0% (45일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 11 | `cdcac84052` | 2026-10-09 | 1.78 | 1.99 | 0.18 | +4.1% | -21.9% | -4.8% / 보유 -31.8% (46일) | 관망 | 진입: price_above_ma(n=26, kind=ema) AND volume_spike(n=28, mult=2.52) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=99, kind=sma) | 손절 14.3% / 익절 27.3% / 트레일링 21.4% |
| 12 | `b12dd3fbc7` | 2026-10-09 | 1.78 | 1.74 | 0.50 | +6.8% | -30.1% | -2.6% / 보유 -31.8% (46일) | SOL | 진입: donchian_break(n=52) | 청산: price_below_ma(n=42, kind=sma) OR donchian_low_break(n=53) | 익절 33.6% |
| 13 | `114ad67d25` | 2026-10-11 | 1.98 | 1.83 | 0.14 | +0.7% | -27.4% | -5.1% / 보유 -31.3% (44일) | 관망 | 진입: volume_spike(n=20, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=142, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 14 | `d7fb6c9904` | 2026-10-11 | 1.93 | 1.99 | 0.15 | +0.9% | -27.2% | -6.3% / 보유 -31.3% (44일) | 관망 | 진입: volume_spike(n=15, mult=2.369) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) | 익절 41.1% |
| 15 | `2439726ead` | 2026-10-08 | 1.65 | 2.06 | 0.19 | +2.2% | -23.7% | -5.9% / 보유 -32.8% (47일) | 관망 | 진입: donchian_break(n=12) AND volume_spike(n=24, mult=2.89) | 청산: price_below_ma(n=116, kind=sma) |
| 16 | `fd1c453679` | 2026-10-10 | 2.01 | 1.97 | 0.35 | +5.7% | -23.3% | -6.6% / 보유 -30.6% (45일) | 관망 | 진입: volume_spike(n=20, mult=1.54) AND volume_spike(n=15, mult=2.715) AND price_above_ma(n=16, kind=sma) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=78, kind=sma) | 익절 27.3% |
| 17 | `6335aeebf2` | 2026-10-10 | 2.01 | 1.78 | 0.29 | +4.0% | -23.9% | -5.5% / 보유 -31.1% (44일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=5, slow=109, kind=sma) OR price_below_ma(n=135, kind=ema) |
| 18 | `4ca2bafdac` | 2026-10-27 | 1.47 | 2.39 | 0.65 | +11.1% | -18.9% | 관망 +0.0% / 보유 -24.9% (28일) | 관망 | 진입: donchian_break(n=86) OR drawdown_from_high(n=21, th=0.19) | 청산: donchian_low_break(n=27) OR price_below_ma(n=30, kind=ema) | 익절 6.2% |
| 19 | `88b03c3bd9` | 2026-10-09 | 1.82 | 1.51 | -0.08 | -2.6% | -23.4% | -1.2% / 보유 -31.4% (46일) | 관망 | 진입: low_volatility(n=43, q=0.24) AND donchian_break(n=16) | 청산: price_below_ma(n=39, kind=ema) | 손절 12.0% / 익절 27.3% |
| 20 | `43ba22956d` | 2026-11-23 | 2.30 | 1.41 | 0.30 | +5.8% | -19.6% | 관망 +0.0% / 보유 +1.1% (1일) | 관망 | 진입: macd_pos(f=3, s=29, sig=16) AND ma_cross_up(fast=36, slow=112, kind=ema) AND ma_cross_up(fast=5, slow=23, kind=ema) | 청산: donchian_low_break(n=9) OR rsi_above(n=25, th=79) OR bars_held(n=21) | 익절 30.4% |
| 21 | `030e70f004` | 2026-10-10 | 2.05 | 1.58 | -0.01 | -1.8% | -20.9% | -4.2% / 보유 -31.1% (44일) | 관망 | 진입: volume_spike(n=15, mult=3.025) AND momentum_pos(n=17, th=0.01) | 청산: price_below_ma(n=57, kind=sma) OR ma_cross_down(fast=47, slow=239, kind=sma) OR donchian_low_break(n=46) | 익절 29.1% |
| 22 | `fa158e2ae7` | 2026-11-21 | 1.89 | 1.73 | 0.05 | -1.2% | -20.8% | -1.2% / 보유 +3.0% (3일) | XRP | 진입: volume_spike(n=19, mult=3.625) AND price_above_ma(n=18, kind=sma) | 청산: bars_held(n=38) OR donchian_low_break(n=21) | 손절 29.2% / 익절 30.0% / 트레일링 26.3% |
| 23 | `ed518e2f80` | 2026-10-11 | 1.95 | 1.72 | 0.26 | +3.6% | -22.1% | -5.8% / 보유 -31.3% (44일) | 관망 | 진입: volume_spike(n=12, mult=3.069) AND momentum_pos(n=17, th=0.01) | 청산: ma_cross_down(fast=5, slow=108, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 20.4% / 익절 29.1% |
| 24 | `848c7af378` | 2026-11-20 | 1.69 | 1.80 | 0.57 | +9.0% | -21.8% | 관망 +0.0% / 보유 -1.2% (4일) | 관망 | 진입: price_above_ma(n=76, kind=sma) AND macd_pos(f=7, s=26, sig=7) AND low_volatility(n=44, q=0.5) | 청산: price_below_ma(n=22, kind=ema) | 익절 28.0% / 트레일링 27.7% |
| 25 | `08a39b7267` | 2026-10-10 | 1.98 | 1.67 | 0.13 | +0.9% | -21.2% | -6.6% / 보유 -30.6% (45일) | SOL | 진입: macd_pos(f=14, s=21, sig=7) AND volume_spike(n=29, mult=3.51) | 청산: price_below_ma(n=51, kind=sma) | 익절 60.8% |
| 26 | `51e55b9c84` | 2026-10-26 | 1.53 | 2.04 | 1.52 | +17.8% | -6.8% | -1.1% / 보유 -25.6% (29일) | SOL | 진입: volume_spike(n=14, mult=3.68) AND donchian_break(n=51) | 청산: bars_held(n=35) | 손절 12.9% / 익절 40.4% / 트레일링 26.8% |
| 27 | `84fcd77045` | 2026-10-12 | 1.41 | 1.83 | 0.22 | +2.1% | -12.2% | -3.9% / 보유 -31.4% (43일) | 관망 | 진입: volume_spike(n=15, mult=3.069) AND momentum_pos(n=17, th=0.01) AND volume_spike(n=10, mult=2.61) | 청산: bars_held(n=12) OR ma_cross_down(fast=6, slow=109, kind=sma) | 손절 28.0% / 익절 29.1% / 트레일링 28.7% |
| 28 | `481633c95e` 🆕 | 2026-11-24 | 2.03 | 1.32 | 0.11 | +0.1% | -19.0% | - | - | 진입: macd_pos(f=23, s=54, sig=12) AND volume_spike(n=19, mult=3.152) AND price_above_ma(n=232, kind=ema) | 청산: price_below_ma(n=56, kind=sma) OR ma_cross_down(fast=51, slow=150, kind=sma) | 익절 46.7% / 트레일링 9.4% |
| 29 | `3504da9518` | 2026-11-20 | 1.19 | 2.16 | 1.21 | +15.9% | -12.0% | 관망 +0.0% / 보유 -1.9% (4일) | 관망 | 진입: donchian_break(n=90) AND volume_spike(n=55, mult=3.84) | 청산: bars_held(n=40) | 손절 4.6% |
| 30 | `c1fa33b98e` | 2026-11-21 | 1.76 | 1.57 | 1.02 | +14.8% | -17.5% | 관망 +0.0% / 보유 +3.0% (3일) | 관망 | 진입: volume_spike(n=26, mult=3.619) AND low_volatility(n=45, q=0.64) | 청산: price_below_ma(n=55, kind=sma) | 손절 22.7% / 익절 30.0% |
| 31 | `3ec1452b69` | 2026-11-21 | 1.77 | 1.51 | 0.75 | +13.7% | -21.2% | 관망 +0.0% / 보유 +3.0% (3일) | 관망 | 진입: low_volatility(n=36, q=0.56) AND momentum_pos(n=17, th=0.008) AND volume_spike(n=10, mult=2.599) | 청산: price_below_ma(n=58, kind=sma) OR ma_cross_down(fast=6, slow=107, kind=sma) OR price_below_ma(n=135, kind=ema) | 손절 21.3% / 익절 29.1% |
| 32 | `404256e1c1` 🆕 | 2026-11-24 | 1.63 | 1.64 | 0.73 | +13.1% | -16.8% | - | - | 진입: macd_pos(f=17, s=34, sig=6) AND volume_spike(n=44, mult=1.39) AND ma_cross_up(fast=47, slow=187, kind=ema) | 청산: bars_held(n=13) OR price_below_ma(n=17, kind=ema) |
| 33 | `c2aebfdff3` | 2026-11-19 | 1.36 | 1.91 | 0.34 | +4.2% | -18.0% | 관망 +0.0% / 보유 -2.4% (5일) | 관망 | 진입: price_above_ma(n=117, kind=sma) AND volume_spike(n=11, mult=3.41) | 청산: price_below_ma(n=119, kind=sma) OR bars_held(n=39) | 손절 10.9% |
| 34 | `5b8f9bc24f` | 2026-11-18 | 1.33 | 1.94 | 0.59 | +10.5% | -16.0% | 관망 +0.0% / 보유 -3.8% (6일) | 관망 | 진입: donchian_break(n=90) OR drawdown_from_high(n=23, th=0.168) | 청산: price_below_ma(n=18, kind=sma) OR bars_held(n=38) |
| 35 | `f1611a53cb` | 2026-11-23 | 1.56 | 1.65 | -0.34 | -9.1% | -33.8% | -3.8% / 보유 +1.1% (1일) | BTC·ETH·XRP·SOL | 진입: macd_pos(f=3, s=29, sig=15) AND volume_spike(n=10, mult=1.78) | 청산: price_below_ma(n=16, kind=sma) OR rsi_above(n=25, th=79) | 익절 25.6% |
| 36 | `4414a03b38` | 2026-11-19 | 1.60 | 1.57 | 0.08 | -0.7% | -23.8% | -2.6% / 보유 -2.4% (5일) | 관망 | 진입: volume_spike(n=57, mult=3.68) AND macd_pos(f=10, s=50, sig=6) | 청산: ma_cross_down(fast=20, slow=88, kind=ema) | 트레일링 10.0% |
| 37 | `1c5674c6d8` | 2026-11-19 | 1.65 | 1.50 | 0.60 | +11.2% | -15.0% | 관망 +0.0% / 보유 -2.4% (5일) | 관망 | 진입: donchian_break(n=36) AND low_volatility(n=17, q=0.55) | 청산: price_below_ma(n=22, kind=ema) |
| 38 | `efc7382834` | 2026-11-23 | 1.60 | 1.49 | 0.88 | +16.2% | -14.6% | 관망 +0.0% / 보유 +1.1% (1일) | 관망 | 진입: low_volatility(n=31, q=0.43) AND donchian_break(n=30) AND ma_cross_up(fast=23, slow=138, kind=sma) | 청산: price_below_ma(n=70, kind=sma) OR price_below_ma(n=33, kind=ema) | 트레일링 27.4% |
| 39 | `c8693cdfa2` 🆕 | 2026-11-24 | 1.74 | 1.33 | 0.21 | +2.1% | -15.8% | - | - | 진입: macd_pos(f=21, s=26, sig=12) AND volume_spike(n=20, mult=3.173) AND donchian_break(n=58) | 청산: price_below_ma(n=58, kind=sma) OR ma_cross_down(fast=51, slow=150, kind=sma) OR donchian_low_break(n=19) | 익절 46.7% / 트레일링 20.7% |
| 40 | `88108241f6` | 2026-11-22 | 1.69 | 1.36 | 0.95 | +16.9% | -20.3% | 관망 +0.0% / 보유 +1.1% (2일) | 관망 | 진입: donchian_break(n=27) AND low_volatility(n=59, q=0.29) | 청산: ma_cross_down(fast=39, slow=61, kind=ema) OR price_below_ma(n=54, kind=sma) | 손절 16.0% / 익절 52.7% |
| 41 | `427e33e785` | 2026-11-22 | 1.49 | 1.40 | 0.52 | +11.7% | -26.5% | -3.8% / 보유 +1.1% (2일) | BTC·ETH·XRP·SOL | 진입: volume_spike(n=37, mult=2.16) AND macd_pos(f=7, s=44, sig=15) | 청산: bars_held(n=20) OR price_below_ma(n=22, kind=sma) | 익절 7.9% / 트레일링 17.2% |
| 42 | `4d4d21ab4f` | 2026-11-22 | 1.17 | 1.62 | 1.00 | +17.7% | -16.5% | 관망 +0.0% / 보유 +1.1% (2일) | 관망 | 진입: donchian_break(n=86) AND volume_spike(n=53, mult=2.4) | 청산: donchian_low_break(n=23) | 손절 3.9% / 익절 29.7% / 트레일링 19.1% |
| 43 | `600be275ef` | 2026-11-15 | 2.02 | 1.64 | 0.29 | +3.9% | -20.6% | 관망 +0.0% / 보유 -5.5% (9일) | 관망 | 진입: donchian_break(n=18) AND ma_cross_up(fast=3, slow=205, kind=ema) AND low_volatility(n=33, q=0.5) | 청산: price_below_ma(n=16, kind=sma) OR bars_held(n=49) | 손절 19.1% / 익절 59.3% / 트레일링 38.5% |
| 44 | `d6558d3b8c` | 2026-11-14 | 1.45 | 2.02 | 0.69 | +11.9% | -17.6% | 관망 +0.0% / 보유 -7.1% (10일) | 관망 | 진입: momentum_pos(n=78, th=0.049) AND volume_spike(n=52, mult=3.98) | 청산: ma_cross_down(fast=15, slow=99, kind=sma) OR bars_held(n=43) | 손절 6.8% / 익절 28.9% |
| 45 | `52be14e05e` | 2026-11-17 | 1.64 | 1.67 | 0.62 | +11.9% | -23.1% | 관망 +0.0% / 보유 -3.0% (7일) | 관망 | 진입: volume_spike(n=30, mult=2.42) AND low_volatility(n=36, q=0.26) | 청산: price_below_ma(n=29, kind=ema) | 손절 17.1% |

비교 기준(단순 보유) 샤프 — 학습 0.96 · 검증 0.78 · 시험 -1.03

![top equity](top_equity.png)

<details><summary>📖 규칙 설명</summary>

**데이터 나누기** — 과거 시세를 학습(앞 60%) · 검증(다음 20%) · 시험(마지막 20%)으로 나눠요. 전략은 학습 구간 성적으로만 진화하고, 검증 구간으로 입성을 심사해요. 시험 구간은 참고로 보여주기만 해요.

**입성 심사** — ① 검증 구간 샤프가 단순 보유보다 0.5 이상 높을 것 ② 기존 전당 전략과 수익 흐름이 비슷하지 않을 것(상관 0.7 이하) ③ 튼튼함 심사: 숫자 파라미터를 ±15% 흔든 변형 6개도 대체로 좋을 것, 거래 비용이 3배여도 단순 보유보다 나을 것, 4개 코인 중 3개 이상에서 단순 보유보다 나을 것. 하루 최대 3개.

**자리 관리** — 전당은 45자리. 입성 후 42봉(7일) 동안은 보호돼요. 자리가 차면, 보호 기간이 끝난 전략과 신입 중 점수가 가장 낮은 것이 나가요. 보호 기간 뒤 낙폭이 -35%보다 나빠지면 퇴출돼요.

**점수** — 학습·검증 샤프 평균에, 보호 기간이 끝난 전략은 '같은 기간 단순 보유 대비 초과 수익'을 더해요. 하락장에서 현금으로 피한 것도 실력으로 인정돼요.

**체결 가정** — 봉 마감 신호 → 다음 봉 시가 체결, 수수료 0.05% + 슬리피지 0.05%(한쪽), 같은 봉에서 손절·익절이 둘 다 닿으면 손절로 처리. 샤프·CAGR·MDD는 4개 코인의 중앙값.

</details>

백테스트와 졸업은 미래 수익을 보장하지 않습니다. 이 리포트는 투자 권유가 아니에요.