from sqlalchemy import select
from sqlalchemy import desc

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import Event


class EventRepository:

    @staticmethod
    async def create_event(
        db: AsyncSession,
        event: Event
    ):

        db.add(event)

        await db.commit()

        await db.refresh(event)

        return event

    @staticmethod
    async def bulk_create(
        db: AsyncSession,
        events: list[Event]
    ):

        db.add_all(events)

        await db.commit()

        return events

    @staticmethod
    async def get_events(
        db: AsyncSession,
        organization_id: str,
        limit: int = 100
    ):

        result = await db.execute(
            select(Event)
            .where(
                Event.organization_id == organization_id
            )
            .order_by(
                desc(Event.created_at)
            )
            .limit(limit)
        )

        return result.scalars().all()