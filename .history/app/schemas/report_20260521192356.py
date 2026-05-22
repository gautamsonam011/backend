from pydantic import BaseModel

from app.utils.enums import ReportFrequency


class ReportCreate(BaseModel):

    name: str

    frequency: ReportFrequency