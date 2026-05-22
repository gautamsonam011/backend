from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.widget import (
    WidgetCreate,
    WidgetResponse
)

from app.services.widget_service import (
    WidgetService
)


router = APIRouter(
    prefix="/widgets",
    tags=["Widgets"]
)


@router.post(
    "/dashboard/{dashboard_id}",
    response_model=WidgetResponse
)
async def create_widget(
    dashboard_id: UUID,
    payload: WidgetCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    widget = await WidgetService.create_widget(
        db,
        payload,
        dashboard_id,
        current_user.organization_id
    )

    return widget


@router.get(
    "/dashboard/{dashboard_id}",
    response_model=list[WidgetResponse]
)
async def get_widgets(
    dashboard_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    widgets = await WidgetService.get_widgets(
        db,
        dashboard_id,
        current_user.organization_id
    )

    return widgets