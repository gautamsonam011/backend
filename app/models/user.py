from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class User(BaseModel):

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    hashed_password: Mapped[str]

    full_name: Mapped[str]

    role: Mapped[str]

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    organization = relationship(
        "Organization",
        back_populates="users"
    )