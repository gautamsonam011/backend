from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services.auth_service import AuthService

from app.core.database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    return await AuthService.register_user(
        db,
        user_data
    )