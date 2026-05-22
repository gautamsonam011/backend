from fastapi import APIRouter


router = APIRouter(
    prefix="/dashboards",
    tags=["Dashboards"]
)


@router.post("/")
async def create_dashboard():

    return {
        "message": "Dashboard created"
    }


@router.get("/")
async def get_dashboards():

    return {
        "message": "Dashboards list"
    }


@router.get("/{dashboard_id}")
async def get_dashboard(
    dashboard_id: str
):

    return {
        "dashboard_id": dashboard_id
    }