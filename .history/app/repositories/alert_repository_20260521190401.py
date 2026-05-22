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
        db: AsyncSession
    ):

        result = await db.execute(
            select(Alert).where(
                Alert.is_active == True
            )
        )

        return result.scalars().all()