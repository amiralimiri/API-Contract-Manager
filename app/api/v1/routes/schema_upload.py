from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.session import get_session
from app.services.schema_service import create_schema

router = APIRouter()


@router.post("/schemas/upload")
async def upload_schema(
    name: str,
    schema_file: UploadFile = File(...),
    session: AsyncSession = Depends(get_session),
):
    content = await schema_file.read()
    try:
        sc = await create_schema(session, name, content, uploaded_by=1)
        return {"status": "ok", "schema_id": sc.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
