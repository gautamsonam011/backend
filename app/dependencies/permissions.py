from fastapi import Depends
from fastapi import HTTPException

from app.dependencies.auth import get_current_user

from app.models.user import User


def require_roles(allowed_roles: list[str]):

    async def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role not in allowed_roles:

            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return current_user

    return role_checker