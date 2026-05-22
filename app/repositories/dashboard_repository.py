from uuid import UUID

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dashboard import Dashboard


class DashboardRepository:

    @staticmethod
    async def create_dashboard(
        db: AsyncSession,
        dashboard: Dashboard
    ):

        db.add(dashboard)

        await db.commit()

        await db.refresh(dashboard)

        return dashboard

    @staticmethod
    async def get_dashboards(
        db: AsyncSession,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Dashboard).where(
                Dashboard.organization_id == organization_id
            )
        )

        return result.scalars().all()

    @staticmethod
    async def get_dashboard(
        db: AsyncSession,
        dashboard_id: UUID,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Dashboard).where(
                Dashboard.id == dashboard_id,
                Dashboard.organization_id == organization_id
            )
        )

        return result.scalar_one_or_none()