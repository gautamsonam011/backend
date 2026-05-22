from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.dashboard import (
    DashboardCreate,
    DashboardResponse
)

from app.services.dashboard_service import (
    DashboardService
)


router = APIRouter(
    prefix="/dashboards",
    tags=["Dashboards"]
)


@router.post(
    "/",
    response_model=DashboardResponse
)
async def create_dashboard(
    payload: DashboardCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    dashboard = await DashboardService.create_dashboard(
        db,
        payload,
        current_user.organization_id
    )

    return dashboard


@router.get(
    "/",
    response_model=list[DashboardResponse]
)
async def get_dashboards(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    dashboards = await DashboardService.get_dashboards(
        db,
        current_user.organization_id
    )

    return dashboards


@router.get(
    "/{dashboard_id}",
    response_model=DashboardResponse
)
async def get_dashboard(
    dashboard_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    dashboard = await DashboardService.get_dashboard(
        db,
        dashboard_id,
        current_user.organization_id
    )

    if not dashboard:

        raise HTTPException(
            status_code=404,
            detail="Dashboard not found"
        )

    return dashboard