from fastapi import APIRouter


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


@router.post("/")
async def create_alert():

    return {
        "message": "Alert created"
    }


@router.get("/")
async def get_alerts():

    return {
        "message": "Alerts list"
    }