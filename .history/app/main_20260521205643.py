from fastapi import FastAPI
import app.models
from app.core.config import settings
from app.core.middleware import register_middleware
from contextlib import asynccontextmanager

from app.core.database import engine

from app.models.base import Base

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.organizations import router as organizations_router
from app.api.v1.events import router as events_router
from app.api.v1.dashboards import router as dashboards_router
from app.api.v1.widgets import router as widgets_router
from app.api.v1.alerts import router as alerts_router
from app.api.v1.reports import router as reports_router
from app.api.v1.websocket import router as websocket_router
from app.api.v1.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME
)

register_middleware(app)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(organizations_router, prefix="/api/v1")
app.include_router(events_router, prefix="/api/v1")
app.include_router(dashboards_router, prefix="/api/v1")
app.include_router(widgets_router, prefix="/api/v1")
app.include_router(alerts_router, prefix="/api/v1")
app.include_router(reports_router, prefix="/api/v1")
app.include_router(websocket_router)
app.include_router(health_router, prefix="/api/v1")


@app.get("/")
async def root():

    return {
        "message": "Realtime Analytics Platform Running"
    }