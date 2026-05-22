from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.alert import (
    AlertCreate,
    AlertResponse
)

from app.services.alert_service import (
    AlertService
)


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


@router.post(
    "/",
    response_model=AlertResponse
)
async def create_alert(
    payload: AlertCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    alert = await AlertService.create_alert(
        db,
        payload,
        current_user.organization_id
    )

    return alert


@router.get(
    "/",
    response_model=list[AlertResponse]
)
async def get_alerts(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    alerts = await AlertService.get_active_alerts(
        db,
        current_user.organization_id
    )

    return alerts