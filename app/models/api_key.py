from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class APIKey(BaseModel):

    __tablename__ = "api_keys"

    key: Mapped[str] = mapped_column(
        String(500),
        unique=True,
        index=True
    )

    name: Mapped[str]

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id")
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )