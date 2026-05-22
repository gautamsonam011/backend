from uuid import UUID

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
        organization_id: UUID
    ):

        report = Report(
            name=payload.name,
            frequency=payload.frequency,
            file_url="generated_report.pdf",
            organization_id=organization_id,
            dashboard_id=payload.dashboard_id
        )

        return await ReportRepository.create_report(
            db,
            report
        )

    @staticmethod
    async def get_reports(
        db: AsyncSession,
        organization_id: UUID
    ):

        return await ReportRepository.get_reports(
            db,
            organization_id
        )