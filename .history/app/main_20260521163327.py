
from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.events import router as events_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.alerts import router as alerts_router

app = FastAPI(title="InsightFlow Analytics")

app.include_router(auth_router)
app.include_router(events_router)
app.include_router(dashboard_router)
app.include_router(alerts_router)

@app.get("/")
async def root():
    return {"message": "InsightFlow Running"}
