from sqlalchemy.ext.asyncio import AsyncSession

from app.models.report import Report

from app.schemas.report import ReportCreate

from app.repositories.report_repository import (
    ReportRepository
)


class ReportService:

    @staticmethod
    async def create_report(
        db: AsyncSession,
        payload: ReportCreate,
        organization_id: str
    ):

        report = Report(
            name=payload.name,
            frequency=payload.frequency,
            file_url="generated_report.pdf",
            organization_id=organization_id,
            dashboard_id=None
        )

        return await ReportRepository.create_report(
            db,
            report
        )