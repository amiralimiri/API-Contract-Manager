from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.services.mock_service import create_mock_for_schema

router = APIRouter()


@router.get("/schemas/{id}/mock")
async def get_mock(id: int, session: AsyncSession = Depends(get_session)):
    url = await create_mock_for_schema(session, id)
    if not url:
        raise HTTPException(status_code=404, detail="Schema not found")
    return {"mock_url": url}
