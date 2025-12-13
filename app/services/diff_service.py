from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.schema import Schema
from app.models.schema_version import SchemaVersion
from app.utils.diff_tools import json_diff
from app.utils.file_handler import load_schema_body_from_version


async def get_diff_for_schema(session: AsyncSession, schema: Schema) -> str:
    query = (
        select(SchemaVersion)
        .where(SchemaVersion.schema_id == schema.id)
        .order_by(SchemaVersion.version_number.desc())
    )
    result = await session.exec(query)
    versions = result.all()

    if len(versions) < 2:
        return "No previous version to diff"

    latest, previous = versions[0], versions[1]
    latest_body = await load_schema_body_from_version(latest)
    previous_body = await load_schema_body_from_version(previous)

    if latest_body is None or previous_body is None:
        return "Schema body is missing for one of the versions"

    return json_diff(latest_body, previous_body)
