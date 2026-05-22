from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.report import (
    ReportCreate,
    ReportResponse
)

from app.services.report_service import (
    ReportService
)


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.post(
    "/",
    response_model=ReportResponse
)
async def create_report(
    payload: ReportCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    report = await ReportService.create_report(
        db,
        payload,
        current_user.organization_id
    )

    return report


@router.get(
    "/",
    response_model=list[ReportResponse]
)
async def get_reports(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    reports = await ReportService.get_reports(
        db,
        current_user.organization_id
    )

    return reports