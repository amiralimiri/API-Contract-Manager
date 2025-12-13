import json
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schema import Schema
from app.models.schema_version import SchemaVersion
from app.utils.file_handler import save_uploaded_schema


async def create_schema(
    session: AsyncSession, name: str, file_bytes: bytes, uploaded_by: int | None
) -> Schema:
    """Persist a new schema and its first version.

    The uploaded JSON is validated before being saved to disk and stored in the
    ``schema_body`` column for quick access.
    """

    try:
        schema_body = json.loads(file_bytes.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError("Uploaded file is not valid JSON") from exc

    filename = f"{name}-{int(datetime.utcnow().timestamp())}.json"
    filepath = await save_uploaded_schema(file_bytes, filename)

    schema = Schema(name=name, uploaded_by=uploaded_by)
    session.add(schema)
    await session.flush()  # get id for FK

    version = SchemaVersion(
        schema_id=schema.id,
        version_number=1,
        file_path=filepath,
        schema_body=schema_body,
    )
    session.add(version)
    await session.flush()

    schema.current_version = version.version_id

    await session.commit()
    await session.refresh(schema)
    return schema
