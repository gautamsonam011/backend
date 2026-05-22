from pydantic import BaseModel


class AlertCreate(BaseModel):

    name: str

    metric_name: str

    operator: str

    threshold: float


class AlertResponse(BaseModel):

    id: str

    name: str

    metric_name: str

    threshold: float

    class Config:
        from_attributes = True