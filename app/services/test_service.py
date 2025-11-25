from jsonschema import ValidationError, validate
from sqlalchemy.future import select


async def run_contract_test(
    session, schema_id: int, sample_request: dict
) -> dict | None:
    """
    آخرین نسخه‌ی اسکیما را بارگذاری می‌کند و sample_request را با آن اعتبارسنجی می‌کند.
    در صورت معتبر بودن، نتیجهٔ موفقیت‌آمیز برمی‌گرداند.
    در صورت خطا، جزئیات خطا برمی‌گرداند.
    """

    # گرفتن آخرین نسخه از اسکیما
    from app.models.schema_version import SchemaVersion

    q = await session.exec(
        select(SchemaVersion)
        .where(SchemaVersion.schema_id == schema_id)
        .order_by(SchemaVersion.created_at.desc())  # اصلاح created_a
    )
    schema_version = q.first()

    if not schema_version:
        return {"success": False, "error": "Schema not found", "schema_id": schema_id}

    schema_body = schema_version.schema_body
    if not isinstance(schema_body, dict):
        return {
            "success": False,
            "error": "Schema body is invalid or not in dict form",
            "schema_id": schema_id,
        }

    # اعتبارسنجی JSON
    try:
        validate(instance=sample_request, schema=schema_body)
        return {
            "success": True,
            "message": "Request is valid",
            "schema_version": schema_version.version,
        }

    except ValidationError as e:
        return {
            "success": False,
            "error": "Validation error",
            "details": e.message,
            "path": list(e.absolute_path),
            "schema_version": schema_version.version,
        }
