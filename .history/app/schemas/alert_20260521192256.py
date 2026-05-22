from pydantic import BaseModel


class AlertCreate(BaseModel):

    name: str

    metric_name: str

    operator: str

    threshold: float