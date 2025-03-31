from fastapi import APIRouter

api_router = APIRouter()

from app.api.endpoints import webhook
api_router.include_router(webhook.router, prefix="/api/v1/webhook", tags=["webhook"])