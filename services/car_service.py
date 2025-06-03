from models.car import Car
from models.owner import Owner
from models.garage import Garage
from db.connection import SessionLocal

def create_car(make, model, year, license_plate, owner_id):
    session = SessionLocal()
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if not owner:
        session.close()
        return None
    car = Car(make=make, model=model, year=year, license_plate=license_plate, owner=owner)
    session.add(car)
    session.commit()
    session.refresh(car)
    session.close()
    return car

def get_all_cars():
    session = SessionLocal()
    cars = session.query(Car).all()
    session.close()
    return cars

def get_car_by_id(car_id):
    session = SessionLocal()
    car = session.query(Car).filter_by(id=car_id).first()
    session.close()
    return car

def update_car(car_id, make=None, model=None, year=None, license_plate=None):
    session = SessionLocal()
    car = session.query(Car).filter_by(id=car_id).first()
    if not car:
        session.close()
        return None
    if make:
        car.make = make
    if model:
        car.model = model
    if year:
        car.year = year
    if license_plate:
        car.license_plate = license_plate
    session.commit()
    session.refresh(car)
    session.close()
    return car

def delete_car(car_id):
    session = SessionLocal()
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        session.delete(car)
        session.commit()
    session.close()
    return car

def link_car_to_garage(car_id, garage_id):
    session = SessionLocal()
    car = session.query(Car).filter_by(id=car_id).first()
    garage = session.query(Garage).filter_by(id=garage_id).first()
    if car and garage:
        car.garages.append(garage)
        session.commit()
    session.close()
    return car
