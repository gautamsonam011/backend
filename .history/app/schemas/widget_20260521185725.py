from pydantic import BaseModel


class WidgetCreate(BaseModel):

    title: str

    widget_type: str

    query: str

    config: dict


class WidgetResponse(BaseModel):

    id: str

    title: str

    widget_type: str

    class Config:
        from_attributes = True