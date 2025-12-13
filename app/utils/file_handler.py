import json
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import aiofiles

from app.core.config import settings

if TYPE_CHECKING:  # pragma: no cover - used only for type checking
    from app.models.schema_version import SchemaVersion


UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def save_uploaded_schema(file_bytes: bytes, filename: str) -> str:
    target = UPLOAD_DIR / filename
    async with aiofiles.open(target, "wb") as f:
        await f.write(file_bytes)
    return str(target)


async def load_schema_body_from_version(
    version: "SchemaVersion",
) -> Optional[dict]:
    """Return the in-memory JSON body for a schema version.

    Prefers the stored ``schema_body`` column and falls back to reading the
    version's JSON file from disk when necessary.
    """

    if version.schema_body is not None:
        return version.schema_body

    path = Path(version.file_path)
    if not path.exists():
        return None

    async with aiofiles.open(path, "r") as f:
        return json.loads(await f.read())
