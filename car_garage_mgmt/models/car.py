from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db.connection import Base
from .relationships import car_garage

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    vin = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    owner = relationship('Owner', back_populates='cars')
    garages = relationship('Garage', secondary=car_garage, back_populates='cars')
