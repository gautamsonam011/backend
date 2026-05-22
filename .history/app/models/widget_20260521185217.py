from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Widget(BaseModel):

    __tablename__ = "widgets"

    title: Mapped[str]

    widget_type: Mapped[str]

    query: Mapped[str]

    config: Mapped[dict] = mapped_column(
        JSON
    )

    dashboard_id: Mapped[str] = mapped_column(
        ForeignKey("dashboards.id")
    )

    dashboard = relationship(
        "Dashboard",
        back_populates="widgets"
    )