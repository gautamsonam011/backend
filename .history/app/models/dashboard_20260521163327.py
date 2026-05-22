
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Dashboard(Base):
    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True)
    name = Column(String)
