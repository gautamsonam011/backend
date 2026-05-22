
from sqlalchemy import Column, Integer, String, JSON
from app.core.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    event_name = Column(String)
    properties = Column(JSON)
