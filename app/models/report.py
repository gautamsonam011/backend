from uuid import UUID

from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Report(BaseModel):

    __tablename__ = "reports"

    name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    frequency: Mapped[str] = mapped_column(
        String(100)
    )

    file_url: Mapped[str] = mapped_column(
        String(1000)
    )

    dashboard_id: Mapped[UUID] = mapped_column(
        ForeignKey("dashboards.id"),
        index=True
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id"),
        index=True
    )