from uuid import UUID

from pydantic import BaseModel


class OrganizationCreate(BaseModel):

    name: str


class OrganizationResponse(BaseModel):

    id: UUID

    name: str

    slug: str

    class Config:

        from_attributes = True