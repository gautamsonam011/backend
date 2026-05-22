from fastapi import FastAPI

from app.core.config import settings

from app.core.middleware import register_middleware

from app.api.v1.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME
)

register_middleware(app)

app.include_router(
    health_router,
    prefix="/api/v1"
)


@app.get("/")
async def root():

    return {
        "message": "Realtime Analytics Platform Running"
    }