# 🤖 코인 전략 자동 연구 봇

매일 아침 9시 15분(한국시간)에 GitHub 서버에서 자동으로 실행됩니다. **내 컴퓨터는 꺼져 있어도 됩니다.**

매일 하는 일:
1. 업비트에서 BTC·ETH·XRP·SOL 4시간봉 시세를 받아 이어 붙임 (API 키 불필요)
2. 지표 조건 블록(이동평균, 돌파, RSI, 볼린저, 모멘텀, 거래량 등)을 조합해 **새 매매법을 수천~수만 개 생성**
3. 유전 알고리즘으로 좋은 전략끼리 교배·변이시키며 25분간 진화 — 어제까지 찾은 상위 전략이 씨앗이 되므로 날마다 연구가 이어짐
4. 과최적화 방지 심사를 통과한 전략만 "명예의 전당"에 등록
5. 전당 전략은 등록일 이후 새로 쌓이는 실제 데이터로 **전진 성과를 매일 추적**, 망가지면 퇴출
6. `results/REPORT.md`, `results/journal.md`, 차트를 저장소에 커밋 (선택: 텔레그램 알림)

## 과최적화 방지 장치

| 장치 | 내용 |
|---|---|
| 데이터 3분할 | 학습 60%로만 진화 → 검증 20%로 입성 심사 → 시험 20%는 보고만 |
| 여러 코인 동시 평가 | 4개 코인 성과의 중앙값 + 최악 코인 성과로 점수 → 한 코인에만 맞춘 전략 탈락 |
| 학습↔검증 격차 | 검증 샤프가 학습의 40% 미만이면 탈락 |
| 최소 거래 수 / 복잡도 벌점 | 우연히 몇 번 맞은 전략, 조건이 과하게 많은 전략 불리 |
| 중복 제거 | 기존 전략과 수익률 상관 0.85 이상이면 등록 안 함 |
| 전진 추적 | 발견 이후 진짜 미래 데이터 성과로 순위 반영·퇴출 |
| 체결 가정 | 종가 신호 → 다음 봉 시가 체결, 수수료 0.05% + 슬리피지 0.05%, 같은 봉 손절·익절이면 손절 우선 |

## 설치 (10분, 한 번만)

1. [github.com](https://github.com) 가입 후 **New repository** → 이름 예: `coin-research-bot`
   - **Public**이면 Actions 무료 무제한, Private이면 월 2,000분 무료(이 봇은 월 약 900분 사용)
2. 이 폴더의 파일을 전부 업로드 (저장소 페이지 → *Add file → Upload files* 로 드래그해도 됨. `.github` 폴더 포함 필수 — 숨김 폴더라 안 보이면 아래 참고)
3. 저장소 **Settings → Actions → General → Workflow permissions** 에서 **Read and write permissions** 선택 후 Save
4. **Actions** 탭 → `daily-research` → **Run workflow** 로 첫 실행 (첫날은 과거 데이터 수집 때문에 몇 분 더 걸림)
5. 끝나면 `results/REPORT.md` 를 열어 결과 확인. 이후로는 매일 자동 실행

> 웹 업로드에서 `.github` 폴더가 빠졌다면: 저장소에서 *Add file → Create new file*, 파일명에 `.github/workflows/daily-research.yml` 입력 후 해당 파일 내용을 붙여넣기.

### 텔레그램 알림 (선택)
1. 텔레그램에서 `@BotFather` → `/newbot` → 토큰 받기
2. 만든 봇에게 아무 메시지 보낸 뒤 `https://api.telegram.org/bot<토큰>/getUpdates` 에서 `chat.id` 확인
3. 저장소 **Settings → Secrets and variables → Actions** 에 `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID` 추가

## 설정 바꾸기 — `config.json`

| 키 | 의미 |
|---|---|
| `markets` | 업비트 마켓 코드 목록 (예: `"KRW-DOGE"`) |
| `interval` | `1d`, `4h`, `1h` |
| `minutes` | 하루 연구 시간(분). 늘리면 더 많이 탐색 (job 제한 45분) |
| `population` | 세대당 전략 수 |
| `min_valid_sharpe` | 전당 입성 최소 검증 샤프 — 높일수록 깐깐 |
| `hof_size` | 전당 최대 인원 |
| `retire_forward_mdd` | 전진 성과 낙폭이 이보다 나빠지면 퇴출 |

새 지표 블록을 추가하려면 `bot/strategy.py`의 `BLOCKS`(진입) / `EXIT_BLOCKS`(청산)에 한 줄씩 넣으면 자동으로 탐색 대상에 포함됩니다.

## 내 컴퓨터에서 돌려보기

```bash
pip install -r requirements.txt
python -m bot.research
```

## 주의

이 봇은 **연구·백테스트 전용**이며 실제 주문을 내지 않습니다. 백테스트에서 좋았던 전략도 실전에서는 실패하는 경우가 흔합니다. 실거래를 고민한다면 최소 몇 주 이상 '전진 수익'이 쌓인 전략만, 소액으로 검토하세요.
