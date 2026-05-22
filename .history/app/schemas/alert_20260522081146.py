from uuid import UUID

from pydantic import BaseModel


class AlertCreate(BaseModel):

    name: str

    metric_name: str

    operator: str

    threshold: float


class AlertResponse(BaseModel):

    id: UUID

    name: str

    metric_name: str

    operator: str

    threshold: float

    is_active: bool

    organization_id: UUID

    class Config:

        from_attributes = True