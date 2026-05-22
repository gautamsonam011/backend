from uuid import UUID

from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Index

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Event(BaseModel):

    __tablename__ = "events"

    event_name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    event_type: Mapped[str] = mapped_column(
        String(255)
    )

    source: Mapped[str] = mapped_column(
        String(255)
    )

    properties: Mapped[dict] = mapped_column(
        JSON
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id"),
        index=True
    )

    organization = relationship(
        "Organization",
        back_populates="events"
    )

    __table_args__ = (
        Index(
            "idx_event_org_created",
            "organization_id",
            "created_at"
        ),
    )