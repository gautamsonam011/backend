from uuid import UUID

from pydantic import BaseModel


class EventCreate(BaseModel):

    event_name: str

    event_type: str

    source: str

    properties: dict


class EventResponse(BaseModel):

    id: UUID

    event_name: str

    event_type: str

    source: str

    properties: dict

    organization_id: UUID

    class Config:

        from_attributes = Trues