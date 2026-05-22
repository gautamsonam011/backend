from uuid import UUID

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.report import Report


class ReportRepository:

    @staticmethod
    async def create_report(
        db: AsyncSession,
        report: Report
    ):

        db.add(report)

        await db.commit()

        await db.refresh(report)

        return report

    @staticmethod
    async def get_reports(
        db: AsyncSession,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Report).where(
                Report.organization_id == organization_id
            )
        )

        return result.scalars().all()

    @staticmethod
    async def get_report(
        db: AsyncSession,
        report_id: UUID,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Report).where(
                Report.id == report_id,
                Report.organization_id == organization_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_dashboard_reports(
        db: AsyncSession,
        dashboard_id: UUID,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Report).where(
                Report.dashboard_id == dashboard_id,
                Report.organization_id == organization_id
            )
        )

        return result.scalars().all()