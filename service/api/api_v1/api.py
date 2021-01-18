from fastapi import APIRouter

from .endpoints.hello import router as triage_router


router = APIRouter()
router.include_router(triage_router)
