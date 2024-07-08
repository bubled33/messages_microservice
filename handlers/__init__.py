from fastapi import APIRouter

from .base import router as base_router

router = APIRouter(prefix='/api')
router.include_router(base_router)
