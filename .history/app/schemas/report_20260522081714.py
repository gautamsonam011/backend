from uuid import UUID

from pydantic import BaseModel


class ReportCreate(BaseModel):

    name: str

    frequency: str

    dashboard_id: UUID


class ReportResponse(BaseModel):

    id: UUID

    name: str

    frequency: str

    file_url: str

    dashboard_id: UUID

    organization_id: UUID

    class Config:

        from_attributes = True