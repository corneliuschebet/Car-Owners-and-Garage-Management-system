from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base
from .relationships import car_garage

class Garage(Base):
    __tablename__ = 'garages'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    cars = relationship('Car', secondary=car_garage, back_populates='garages')