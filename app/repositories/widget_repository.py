from uuid import UUID

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.widget import Widget


class WidgetRepository:

    @staticmethod
    async def create_widget(
        db: AsyncSession,
        widget: Widget
    ):

        db.add(widget)

        await db.commit()

        await db.refresh(widget)

        return widget

    @staticmethod
    async def get_widgets(
        db: AsyncSession,
        dashboard_id: UUID
    ):

        result = await db.execute(
            select(Widget).where(
                Widget.dashboard_id == dashboard_id
            )
        )

        return result.scalars().all()