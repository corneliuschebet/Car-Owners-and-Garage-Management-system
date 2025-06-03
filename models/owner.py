from sqlalchemy import Column, Integer, String
from models.base import Base

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    def __repr__(self):
        return f"<Owner(id={self.id}, name='{self.name}', phone='{self.phone}')>"
