from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class Organization(BaseModel):

    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    slug: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    owner_id: Mapped[str | None] = mapped_column(
    nullable=True)

    users = relationship(
        "User",
        back_populates="organization"
    )

    dashboards = relationship(
        "Dashboard",
        back_populates="organization"
    )

    events = relationship(
        "Event",
        back_populates="organization"
    )