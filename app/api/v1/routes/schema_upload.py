from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/schema", tags=["Schema"])


@router.post("/upload")
async def upload_schema(file: UploadFile):
    return {"filename": file.filename}
