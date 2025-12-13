from fastapi import APIRouter

from .schema_diff import router as schema_diff_router
from .schema_mock import router as schema_mock_router
from .schema_test import router as schema_test_router
from .schema_upload import router as schema_upload_router

router = APIRouter(prefix="/api/v1")

router.include_router(schema_upload_router, tags=["schemas"])
router.include_router(schema_diff_router, tags=["schemas"])
router.include_router(schema_test_router, tags=["schemas"])
router.include_router(schema_mock_router, tags=["schemas"])
