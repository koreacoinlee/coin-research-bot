"""파일 입출력 보조.

결과 JSON 을 쓰는 도중 실행이 끊기면 반쯤 쓴 파일이 남아 다음 실행이 계속 실패할 수 있다.
임시 파일에 다 쓴 뒤 한 번에 바꿔치기(os.replace)해서 그런 일이 없게 한다.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def atomic_write_text(path: Path, text: str):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def atomic_write_json(path: Path, obj):
    atomic_write_text(path, json.dumps(obj, ensure_ascii=False, indent=1, default=float))


def read_json(path: Path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))
