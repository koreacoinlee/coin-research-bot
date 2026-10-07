"""시세 데이터 수집 (업비트 공개 API, 키 불필요).

data/{market}_{interval}.csv 에 캐시하고, 매일 새 캔들만 이어 붙인다.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
UPBIT = "https://api.upbit.com/v1/candles"

# interval 이름 -> 업비트 엔드포인트
INTERVALS = {
    "1d": "days",
    "4h": "minutes/240",
    "1h": "minutes/60",
}


def _get(url: str, params: dict) -> list:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{q}", headers={"Accept": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read())
        except Exception as e:  # 429 등은 잠시 쉬었다 재시도
            if attempt == 4:
                raise
            time.sleep(1.5 * (attempt + 1))
    return []


def fetch_upbit(market: str, interval: str, max_bars: int, since: pd.Timestamp | None = None,
                before: pd.Timestamp | None = None) -> pd.DataFrame:
    """최신부터(또는 before 시점부터) 과거로 200개씩 페이지를 넘기며 수집."""
    url = f"{UPBIT}/{INTERVALS[interval]}"
    rows, to = [], (before.strftime("%Y-%m-%d %H:%M:%S") if before is not None else None)
    while len(rows) < max_bars:
        params = {"market": market, "count": 200}
        if to:
            params["to"] = to
        batch = _get(url, params)
        if not batch:
            break
        rows.extend(batch)
        oldest = batch[-1]["candle_date_time_utc"]
        if since is not None and pd.Timestamp(oldest) <= since:
            break
        to = oldest.replace("T", " ")
        time.sleep(0.12)  # 초당 요청 제한 준수
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(
        {
            "time": pd.to_datetime([r["candle_date_time_utc"] for r in rows]),
            "open": [r["opening_price"] for r in rows],
            "high": [r["high_price"] for r in rows],
            "low": [r["low_price"] for r in rows],
            "close": [r["trade_price"] for r in rows],
            "volume": [r["candle_acc_trade_volume"] for r in rows],
        }
    )
    return df.drop_duplicates("time").sort_values("time").reset_index(drop=True)


def load(market: str, interval: str, max_bars: int = 4000, refresh: bool = True) -> pd.DataFrame:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / f"{market}_{interval}.csv"
    old = pd.read_csv(path, parse_dates=["time"]) if path.exists() else pd.DataFrame()
    if refresh:
        since = old["time"].max() if len(old) else None
        new = fetch_upbit(market, interval, max_bars if since is None else 1000, since)
        df = pd.concat([old, new]).drop_duplicates("time", keep="last") if len(old) else new
        # 과거 데이터가 목표보다 짧으면 더 오래된 구간을 채운다 (상장일까지)
        if len(old) and len(df) < max_bars and not (DATA_DIR / f".{market}_{interval}.complete").exists():
            back = fetch_upbit(market, interval, max_bars - len(df), before=df["time"].min())
            if len(back) < max_bars - len(df):  # 상장일에 닿음 → 다음부터 시도 안 함
                (DATA_DIR / f".{market}_{interval}.complete").touch()
            df = pd.concat([back, df]).drop_duplicates("time", keep="last")
        # 아직 마감되지 않은 마지막 캔들은 버린다 (미래 정보 누출 방지)
        now = pd.Timestamp(datetime.now(timezone.utc)).tz_localize(None)
        step = {"1d": pd.Timedelta(days=1), "4h": pd.Timedelta(hours=4), "1h": pd.Timedelta(hours=1)}[interval]
        df = df[df["time"] + step <= now]
        df = df.sort_values("time").tail(max_bars).reset_index(drop=True)
        df.to_csv(path, index=False)
        return df
    return old
