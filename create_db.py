from db.connection import engine
from models.base import Base
from models.owner import Owner
from models.car import Car
from models.garage import Garage
import models.relationships  # important to import to register the association table

def create_database():
    print("Creating database and tables...")
    Base.metadata.create_all(engine)
    print("Database setup complete.")

if __name__ == "__main__":
    create_database()
