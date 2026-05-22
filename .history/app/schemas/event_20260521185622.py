from pydantic import BaseModel


class EventCreate(BaseModel):

    event_name: str

    event_type: str

    source: str

    properties: dict


class EventResponse(BaseModel):

    id: str

    event_name: str

    class Config:
        from_attributes = True