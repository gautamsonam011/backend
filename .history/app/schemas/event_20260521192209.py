from pydantic import BaseModel

from app.utils.enums import EventSource


class EventCreate(BaseModel):

    event_name: str

    event_type: str

    source: EventSource

    properties: dict