from fastapi import APIRouter


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.post("/")
async def create_organization():

    return {
        "message": "Organization created"
    }


@router.get("/")
async def get_organizations():

    return {
        "message": "Organizations list"
    }