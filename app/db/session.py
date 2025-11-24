# app/db/session.py
from sqlmodel import Session, create_engine

from app.core.config import settings

# engine اصلی پروژه
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)


# session factory
def get_session():
    with Session(engine) as session:
        yield session
