from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Dashboard(BaseModel):

    __tablename__ = "dashboards"

    name: Mapped[str]

    description: Mapped[str]

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )

    organization = relationship(
        "Organization",
        back_populates="dashboards"
    )

    widgets = relationship(
        "Widget",
        back_populates="dashboard"
    )