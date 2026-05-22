from pydantic import BaseModel


class ReportCreate(BaseModel):

    name: str

    frequency: str


class ReportResponse(BaseModel):

    id: str

    name: str

    frequency: str

    file_url: str

    class Config:
        from_attributes = True