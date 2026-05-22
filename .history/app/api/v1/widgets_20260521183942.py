from fastapi import APIRouter


router = APIRouter(
    prefix="/widgets",
    tags=["Widgets"]
)


@router.post("/")
async def create_widget():

    return {
        "message": "Widget created"
    }


@router.get("/")
async def get_widgets():

    return {
        "message": "Widgets list"
    }