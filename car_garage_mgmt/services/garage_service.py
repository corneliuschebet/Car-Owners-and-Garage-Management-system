from db.connection import Session
from models.garage import Garage

def add_garage(name, location, capacity):
    session = Session()
    garage = Garage(name=name, location=location, capacity=capacity)
    session.add(garage)
    session.commit()
    print(f"Garage {name} added.")
