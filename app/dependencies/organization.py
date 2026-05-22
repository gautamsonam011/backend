from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.organization import Organization
from app.models.user import User


async def get_current_organization(
    organization_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = await db.execute(
        select(Organization).where(
            Organization.id == organization_id
        )
    )

    organization = result.scalar_one_or_none()

    if not organization:

        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )
   
    # Multi-tenant isolation check

    if organization.owner_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return organization