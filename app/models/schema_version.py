from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class SchemaVersion(Base):
    __tablename__ = "schema_versions"

    version_id = Column(Integer, primary_key=True, index=True)

    schema_id = Column(Integer, ForeignKey("schemas.id"), nullable=False)

    version_number = Column(Integer, nullable=False)
    file_path = Column(String, nullable=False)
    diff_summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    schema = relationship("Schema", back_populates="versions")
