from sqlalchemy import Table, Column, Integer, ForeignKey
from db.connection import Base

car_garage = Table(
    'car_garage', Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id')),
    Column('garage_id', Integer, ForeignKey('garages.id'))
)