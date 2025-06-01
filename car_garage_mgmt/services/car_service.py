from db.connection import Session
from models.car import Car

def add_car(owner_id, make, model, year, vin):
    session = Session()
    car = Car(owner_id=owner_id, make=make, model=model, year=year, vin=vin)
    session.add(car)
    session.commit()
    print(f"Car {make} {model} added.")