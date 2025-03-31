from fastapi import APIRouter
from backend.app.api.routes import posts
from backend.app.api.endpoints import webhook  # 👈 Tilføjet webhook import

# Main API router
api_router = APIRouter()

# Include all modular routers
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(webhook.router, prefix="/api/v1/webhook", tags=["webhook"])  # 👈 Tilføjet webhook-router