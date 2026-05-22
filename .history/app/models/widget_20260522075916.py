from uuid import UUID

from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Widget(BaseModel):

    __tablename__ = "widgets"

    title: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    widget_type: Mapped[str] = mapped_column(
        String(100)
    )

    query: Mapped[str] = mapped_column(
        String(1000)
    )

    config: Mapped[dict] = mapped_column(
        JSON
    )

    dashboard_id: Mapped[UUID] = mapped_column(
        ForeignKey("dashboards.id"),
        index=True
    )

    dashboard = relationship(
        "Dashboard",
        back_populates="widgets"
    )