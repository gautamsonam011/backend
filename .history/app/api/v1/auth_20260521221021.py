from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.dependencies.auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import AuthService

from app.core.database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=TokenResponse
)
async def register(
    payload: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):

    return await AuthService.register(
        db,
        payload
    )


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db)
):

    return await AuthService.login(
        db,
        payload
    )


@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)):

    return {
        "message": "Logged out successfully"
    }