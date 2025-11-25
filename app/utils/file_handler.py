import os
from pathlib import Path

from app.core.config import settings

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def save_uploaded_schema(file_bytes: bytes, filename: str) -> str:
    target = UPLOAD_DIR / filename
    with open(target, "wb") as f:
        f.write(file_bytes)
    return str(target)
