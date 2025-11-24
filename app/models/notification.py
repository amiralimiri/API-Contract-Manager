from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String

from app.db.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    schema_id = Column(Integer, ForeignKey("schemas.id"), nullable=False)

    event_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
