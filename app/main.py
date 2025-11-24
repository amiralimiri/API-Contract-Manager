from fastapi import FastAPI

from app.api.v1.routes.schema_upload import router as schema_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG, version="0.0.1")

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "env": settings.ENV}

    app.include_router(schema_router)

    return app


app = create_app()
