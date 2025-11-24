from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Schema(Base):
    __tablename__ = "schemas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # اشاره به آخرین نسخه
    current_version = Column(
        Integer, ForeignKey("schema_versions.version_id"), nullable=True
    )

    # چه کسی آپلود کرده
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # روابط
    uploader = relationship("User")
    versions = relationship("SchemaVersion", back_populates="schema")
