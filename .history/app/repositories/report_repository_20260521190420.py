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
        organization_id: str
    ):

        result = await db.execute(
            select(Report).where(
                Report.organization_id == organization_id
            )
        )

        return result.scalars().all()