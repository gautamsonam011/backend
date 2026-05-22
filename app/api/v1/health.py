from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import engine


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health_check():

    database_status = "healthy"

    try:

        async with engine.begin() as connection:

            await connection.execute(
                text("SELECT 1")
            )

    except Exception:

        database_status = "unhealthy"

    return {
        "status": "healthy",
        "service": "Realtime Analytics Platform",
        "timestamp": datetime.utcnow(),
        "database": database_status,
        "version": "1.0.0"
    }