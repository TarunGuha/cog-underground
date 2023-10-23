from fastapi import APIRouter
from app.services.torbot.routes.router import router as tor_router

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "test"}


@router.get("/health")
async def get_health():
    return {"status": "ok"}


router.include_router(tor_router)
