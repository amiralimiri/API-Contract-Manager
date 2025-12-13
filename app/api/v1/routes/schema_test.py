from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.services.test_service import run_contract_test

router = APIRouter()


class SampleRequest(BaseModel):
    sample_request: dict


@router.post("/schemas/{id}/test")
async def run_test(
    id: int, payload: SampleRequest, session: AsyncSession = Depends(get_session)
):
    result = await run_contract_test(session, id, payload.sample_request)
    if result is None:
        raise HTTPException(status_code=404, detail="Schema not found")
    return result
