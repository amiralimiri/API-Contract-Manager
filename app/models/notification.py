from datetime import datetime
from typing import Any, Optional

from sqlmodel import Field, SQLModel

from .schema import Schema


class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    schema_id: int = Field(foreign_key="schema.id")
    event_type: str
    payload: dict[str, Any]
    sent_at: datetime = Field(default_factory=datetime.utcnow)
