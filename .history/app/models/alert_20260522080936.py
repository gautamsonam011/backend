from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Alert(BaseModel):

    __tablename__ = "alerts"

    name: Mapped[str]

    metric_name: Mapped[str]

    operator: Mapped[str]

    threshold: Mapped[float] = mapped_column(
        Float
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )