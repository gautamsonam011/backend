from sqlalchemy.ext.asyncio import AsyncSession

from app.models.alert import Alert

from app.schemas.alert import AlertCreate

from app.repositories.alert_repository import (
    AlertRepository
)


class AlertService:

    @staticmethod
    async def create_alert(
        db: AsyncSession,
        payload: AlertCreate,
        organization_id: str
    ):

        alert = Alert(
            name=payload.name,
            metric_name=payload.metric_name,
            operator=payload.operator,
            threshold=payload.threshold,
            organization_id=organization_id
        )

        return await AlertRepository.create_alert(
            db,
            alert
        )