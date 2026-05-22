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
        organization_id: str
    ):

        result = await db.execute(
            select(Dashboard).where(
                Dashboard.organization_id == organization_id
            )
        )

        return result.scalars().all()