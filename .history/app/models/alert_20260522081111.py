from uuid import UUID

from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Alert(BaseModel):

    __tablename__ = "alerts"

    name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    metric_name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    operator: Mapped[str] = mapped_column(
        String(50)
    )

    threshold: Mapped[float] = mapped_column(
        Float
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id"),
        index=True
    )