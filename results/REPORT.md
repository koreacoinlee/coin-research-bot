# 🤖 코인 전략 연구 리포트

마지막 업데이트: **2026-10-08** · 대상: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 봉: 4h

> 학습(앞 60%)으로만 진화 → 검증(다음 20%)으로 입성 심사 → 시험(마지막 20%)은 보고만. '전진'은 전당에 오른 뒤 실제로 새로 쌓인 데이터에서의 성과입니다.

## 오늘
- 데이터: KRW-BTC, KRW-ETH, KRW-XRP, KRW-SOL · 4h · 마지막 봉 2026-10-07 08:00 UTC
- 1171세대 진화, 전략 57,627개 평가
- 새로 명예의 전당 입성: 3개 (검증 구간 B&H 샤프 1.36)

## 명예의 전당

| # | ID | 발견일 | 학습 샤프 | 검증 샤프 | 시험 샤프 | 시험 CAGR | 시험 MDD | 전진 수익 | 전략 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `20fa805145` 🆕 | 2026-10-08 | 1.88 | 2.17 | 0.94 | +14.9% | -18.9% | - | 진입: macd_pos(f=16, s=21, sig=7) AND volume_spike(n=37, mult=3.51) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 2 | `f00b4a37e3` 🆕 | 2026-10-08 | 2.07 | 1.95 | 0.56 | +11.6% | -29.2% | - | 진입: donchian_break(n=66) AND price_above_ma(n=197, kind=sma) AND volume_spike(n=44, mult=1.334) | 청산: price_below_ma(n=55, kind=sma) OR ma_cross_down(fast=8, slow=102, kind=sma) | 익절 27.3% |
| 3 | `f7e00c6fe8` 🆕 | 2026-10-08 | 1.86 | 2.10 | 1.21 | +22.2% | -22.0% | - | 진입: donchian_break(n=71) AND price_above_ma(n=197, kind=sma) | 청산: price_below_ma(n=22, kind=ema) | 손절 19.1% / 익절 27.3% / 트레일링 24.5% |

비교 기준(단순 보유) 샤프 — 학습 0.96 · 검증 1.36 · 시험 -0.37

![top equity](top_equity.png)

샤프·CAGR·MDD는 여러 코인의 중앙값, 수수료 0.05% + 슬리피지 0.05% 반영.
백테스트 성과는 미래 수익을 보장하지 않습니다. 실거래 전에 '전진' 성과가 충분히 쌓였는지 확인하세요.