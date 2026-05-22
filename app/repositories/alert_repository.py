from uuid import UUID

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.alert import Alert


class AlertRepository:

    @staticmethod
    async def create_alert(
        db: AsyncSession,
        alert: Alert
    ):

        db.add(alert)

        await db.commit()

        await db.refresh(alert)

        return alert

    @staticmethod
    async def get_active_alerts(
        db: AsyncSession,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Alert).where(
                Alert.organization_id == organization_id,
                Alert.is_active.is_(True)
            )
        )

        return result.scalars().all()

    @staticmethod
    async def get_alert(
        db: AsyncSession,
        alert_id: UUID,
        organization_id: UUID
    ):

        result = await db.execute(
            select(Alert).where(
                Alert.id == alert_id,
                Alert.organization_id == organization_id
            )
        )

        return result.scalar_one_or_none()