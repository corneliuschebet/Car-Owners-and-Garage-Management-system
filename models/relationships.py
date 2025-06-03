from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.car import Car
from models.garage import Garage

# Association table between Cars and Garages
car_garage_association = Table(
    "car_garage",
    Base.metadata,
    Column("car_id", Integer, ForeignKey("cars.id")),
    Column("garage_id", Integer, ForeignKey("garages.id"))
)

# Extend Car and Garage with relationship properties
Car.garages = relationship(
    "Garage",
    secondary=car_garage_association,
    backref="cars"
)
