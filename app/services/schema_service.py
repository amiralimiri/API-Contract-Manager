import json
import os
from datetime import datetime

from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.schema import Schema
from app.models.schema_version import SchemaVersion
from app.utils.file_handler import save_uploaded_schema


async def create_schema(
    session: AsyncSession, name: str, file_bytes: bytes, uploaded_by: int
) -> Schema:
    # save file
    filename = f"{name}-{int(datetime.utcnow().timestamp())}.json"
    filepath = await save_uploaded_schema(file_bytes, filename)

    schema = Schema(name=name, uploaded_by=uploaded_by)
    session.add(schema)
    await session.flush()  # get id

    version = SchemaVersion(schema_id=schema.id, version_number=1, file_path=filepath)
    session.add(version)
    schema.current_version = version.version_id

    await session.commit()
    await session.refresh(schema)
    return schema
