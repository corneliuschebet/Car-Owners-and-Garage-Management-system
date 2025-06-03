from sqlalchemy import Column, Integer, String
from models.base import Base

class Garage(Base):
    __tablename__ = "garages"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    contact_number = Column(String, nullable=True)

    def __repr__(self):
        return f"<Garage(id={self.id}, name='{self.name}', location='{self.location}')>"
