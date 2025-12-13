from sqlalchemy.ext.asyncio import AsyncSession


async def create_mock_for_schema(
    session: AsyncSession, schema_id: int
) -> str | None:  # pragma: no cover - placeholder implementation
    # اینجا می‌توانید یک سرویس ساده که یک مسیر mock تولید کند یا لینک به mock-server ایجاد کند
    # برای شروع، لینک فرضی برمی‌گردانیم.
    return f"https://mock.example.com/schemas/{schema_id}/endpoint"
