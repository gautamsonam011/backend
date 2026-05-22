from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dashboard import Dashboard

from app.schemas.dashboard import DashboardCreate

from app.repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    async def create_dashboard(
        db: AsyncSession,
        payload: DashboardCreate,
        organization_id: str
    ):

        dashboard = Dashboard(
            name=payload.name,
            description=payload.description,
            organization_id=organization_id
        )

        return await DashboardRepository.create_dashboard(
            db,
            dashboard
        )

    @staticmethod
    async def get_dashboards(
        db: AsyncSession,
        organization_id: str
    ):

        return await DashboardRepository.get_dashboards(
            db,
            organization_id
        )