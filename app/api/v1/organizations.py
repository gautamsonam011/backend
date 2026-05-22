from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse
)

from app.models.organization import Organization


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.post(
    "/",
    response_model=OrganizationResponse
)
async def create_organization(
    payload: OrganizationCreate,
    db: AsyncSession = Depends(get_db)
):

    organization = Organization(
        name=payload.name,
        slug=payload.name.lower().replace(" ", "-"),
        owner_id=None
    )

    db.add(organization)

    await db.commit()

    await db.refresh(organization)

    return organization


@router.get(
    "/",
    response_model=list[OrganizationResponse]
)
async def get_organizations(
    db: AsyncSession = Depends(get_db)
):

    from sqlalchemy import select

    result = await db.execute(
        select(Organization)
    )

    organizations = result.scalars().all()

    return organizations