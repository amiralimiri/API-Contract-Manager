from datetime import datetime

from pydantic import BaseModel


class SchemaVersionBase(BaseModel):
    version_number: int
    file_path: str
    diff_summary: str | None = None


class SchemaVersionCreate(SchemaVersionBase):
    schema_id: int


class SchemaVersionResponse(SchemaVersionBase):
    version_id: int
    schema_id: int
    created_at: datetime

    class Config:
        from_attributes = True
