from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.services.schema_service import create_schema

router = APIRouter()


class SchemaUploadResponse(BaseModel):
    status: str
    schema_id: int


@router.post("/schemas/upload", response_model=SchemaUploadResponse, status_code=201)
async def upload_schema(
    name: str = Form(...),
    schema_file: UploadFile = File(...),
    session: AsyncSession = Depends(get_session),
):
    content = await schema_file.read()

    try:
        schema = await create_schema(session, name, content, uploaded_by=1)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - safety net for unexpected errors
        raise HTTPException(status_code=500, detail="Failed to upload schema") from exc

    return {"status": "ok", "schema_id": schema.id}
