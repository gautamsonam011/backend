from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Notification(BaseModel):

    __tablename__ = "notifications"

    title: Mapped[str]

    message: Mapped[str]

    channel: Mapped[str]

    status: Mapped[str]

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )