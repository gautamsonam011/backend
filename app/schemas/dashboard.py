from uuid import UUID

from pydantic import BaseModel


class DashboardCreate(BaseModel):

    name: str

    description: str


class DashboardResponse(BaseModel):

    id: UUID

    name: str

    description: str

    class Config:

        from_attributes = True