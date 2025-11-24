from datetime import datetime
from typing import Any

from pydantic import BaseModel


class NotificationBase(BaseModel):
    event_type: str
    payload: dict[str, Any]


class NotificationCreate(NotificationBase):
    schema_id: int


class NotificationResponse(NotificationBase):
    id: int
    schema_id: int
    sent_at: datetime

    class Config:
        from_attributes = True
