from uuid import UUID

from pydantic import BaseModel


class WidgetCreate(BaseModel):

    title: str

    widget_type: str

    query: str

    config: dict


class WidgetResponse(BaseModel):

    id: UUID

    title: str

    widget_type: str

    query: str

    config: dict

    dashboard_id: UUID

    class Config:

        from_attributes = True