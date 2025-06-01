from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    cars = relationship('Car', back_populates='owner')