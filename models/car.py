from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)         # Marque (e.g. Toyota)
    model = Column(String, nullable=False)        # Modèle (e.g. Corolla)
    year = Column(Integer, nullable=False)        # Année de fabrication
    license_plate = Column(String, nullable=False, unique=True)  # Immatriculation
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)

    owner = relationship("Owner", backref="cars")

    def __repr__(self):
        return f"<Car(id={self.id}, make='{self.make}', model='{self.model}', license='{self.license_plate}')>"
