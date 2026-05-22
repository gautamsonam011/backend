from uuid import UUID

from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Dashboard(BaseModel):

    __tablename__ = "dashboards"

    name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id"),
        index=True
    )

    organization = relationship(
        "Organization",
        back_populates="dashboards"
    )

    widgets = relationship(
        "Widget",
        back_populates="dashboard",
        cascade="all, delete-orphan"
    )