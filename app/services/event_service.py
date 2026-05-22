from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import Event

from app.schemas.event import EventCreate

from app.repositories.event_repository import (
    EventRepository
)


class EventService:

    @staticmethod
    async def ingest_event(
        db: AsyncSession,
        payload: EventCreate,
        organization_id: UUID
    ):

        event = Event(
            event_name=payload.event_name,
            event_type=payload.event_type,
            source=payload.source,
            properties=payload.properties,
            organization_id=organization_id
        )

        return await EventRepository.create_event(
            db,
            event
        )

    @staticmethod
    async def get_events(
        db: AsyncSession,
        organization_id: UUID
    ):

        return await EventRepository.get_events(
            db,
            organization_id
        )