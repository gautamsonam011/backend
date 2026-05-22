from fastapi import APIRouter


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.post("/")
async def create_report():

    return {
        "message": "Report scheduled"
    }


@router.get("/")
async def get_reports():

    return {
        "message": "Reports list"
    }