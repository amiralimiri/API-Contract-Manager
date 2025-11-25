from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.session import get_session
from app.models.schema import Schema
from app.services.diff_service import get_diff_for_schema

router = APIRouter()


@router.get("/schemas/{id}/diff")
async def diff_schema(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Schema).where(Schema.id == id))
    schema = result.one_or_none()
    if not schema:
        raise HTTPException(status_code=404, detail="Schema not found")
    diff = await get_diff_for_schema(session, schema)
    return {"diff_summary": diff}
