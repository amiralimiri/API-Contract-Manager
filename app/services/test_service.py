from jsonschema import ValidationError, validate
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.schema_version import SchemaVersion
from app.utils.file_handler import load_schema_body_from_version


async def run_contract_test(
    session: AsyncSession, schema_id: int, sample_request: dict
) -> dict | None:
    """Validate a sample request body against the latest schema version."""

    q = await session.exec(
        select(SchemaVersion)
        .where(SchemaVersion.schema_id == schema_id)
        .order_by(SchemaVersion.version_number.desc())
    )
    schema_version = q.first()

    if not schema_version:
        return None

    schema_body = await load_schema_body_from_version(schema_version)
    if not isinstance(schema_body, dict):
        return {
            "success": False,
            "error": "Schema body is missing or invalid",
            "schema_id": schema_id,
        }

    try:
        validate(instance=sample_request, schema=schema_body)
        return {
            "success": True,
            "message": "Request is valid",
            "schema_version": schema_version.version_number,
        }

    except ValidationError as e:
        return {
            "success": False,
            "error": "Validation error",
            "details": e.message,
            "path": list(e.absolute_path),
            "schema_version": schema_version.version_number,
        }
