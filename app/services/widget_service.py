from uuid import UUID

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.widget import Widget

from app.schemas.widget import WidgetCreate

from app.repositories.widget_repository import (
    WidgetRepository
)

from app.repositories.dashboard_repository import (
    DashboardRepository
)


class WidgetService:

    @staticmethod
    async def create_widget(
        db: AsyncSession,
        payload: WidgetCreate,
        dashboard_id: UUID,
        organization_id: UUID
    ):

        dashboard = await DashboardRepository.get_dashboard(
            db,
            dashboard_id,
            organization_id
        )

        if not dashboard:

            raise HTTPException(
                status_code=404,
                detail="Dashboard not found"
            )

        widget = Widget(
            title=payload.title,
            widget_type=payload.widget_type,
            query=payload.query,
            config=payload.config,
            dashboard_id=dashboard_id
        )

        return await WidgetRepository.create_widget(
            db,
            widget
        )

    @staticmethod
    async def get_widgets(
        db: AsyncSession,
        dashboard_id: UUID,
        organization_id: UUID
    ):

        dashboard = await DashboardRepository.get_dashboard(
            db,
            dashboard_id,
            organization_id
        )

        if not dashboard:

            raise HTTPException(
                status_code=404,
                detail="Dashboard not found"
            )

        return await WidgetRepository.get_widgets(
            db,
            dashboard_id
        )