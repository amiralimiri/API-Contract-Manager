import json
from pathlib import Path

import aiofiles
from sqlalchemy import desc
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.schema import Schema
from app.models.schema_version import SchemaVersion
from app.utils.diff_tools import json_diff


async def get_diff_for_schema(session: AsyncSession, schema: Schema) -> str:
    query = (
        select(SchemaVersion)
        .where(SchemaVersion.schema_id == schema.id)
        .order_by(SchemaVersion.created_at.desc())
    )
    result = await session.exec(query)
    versions = result.all()

    if len(versions) < 2:
        return "No previous version to diff"
    latest = versions[0]
    previous = versions[1]

    for path in (latest.file_path, previous.file_path):
        if not Path(path).exists():
            return f"File not found: {path}"

    async with aiofiles.open(latest.file_path, "r") as f:
        a = json.loads(await f.read())

    async with aiofiles.open(previous.file_path, "r") as f:
        b = json.loads(await f.read())

    return json_diff(a, b)
