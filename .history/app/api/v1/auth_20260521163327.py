
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login():
    return {"token": "sample-token"}

@router.post("/signup")
async def signup():
    return {"message": "User created"}
