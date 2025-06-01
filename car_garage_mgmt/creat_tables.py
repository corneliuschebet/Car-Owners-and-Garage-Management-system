# create_tables.py
from db.connection import Base, engine
from models.owner import Owner
from models.car import Car
from models.garage import Garage
# Import other models if needed

def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
