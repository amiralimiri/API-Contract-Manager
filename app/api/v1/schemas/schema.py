from datetime import datetime

from pydantic import BaseModel


class SchemaBase(BaseModel):
    name: str


class SchemaCreate(SchemaBase):
    uploaded_by: int


class SchemaResponse(SchemaBase):
    id: int
    current_version: int | None
    uploaded_by: int
    created_at: datetime

    class Config:
        from_attributes = True
