from pydantic import BaseModel

from app.utils.enums import WidgetType


class WidgetCreate(BaseModel):

    title: str

    widget_type: WidgetType

    query: str

    config: dict