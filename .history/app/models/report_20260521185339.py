from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Report(BaseModel):

    __tablename__ = "reports"

    name: Mapped[str]

    frequency: Mapped[str]

    file_url: Mapped[str]

    dashboard_id: Mapped[str] = mapped_column(
        ForeignKey("dashboards.id")
    )

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )