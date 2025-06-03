from models.garage import Garage
from db.connection import SessionLocal

def create_garage(name, location, contact_number=None):
    session = SessionLocal()
    garage = Garage(name=name, location=location, contact_number=contact_number)
    session.add(garage)
    session.commit()
    session.refresh(garage)
    session.close()
    return garage

def get_all_garages():
    session = SessionLocal()
    garages = session.query(Garage).all()
    session.close()
    return garages

def get_garage_by_id(garage_id):
    session = SessionLocal()
    garage = session.query(Garage).filter_by(id=garage_id).first()
    session.close()
    return garage

def update_garage(garage_id, name=None, location=None, contact_number=None):
    session = SessionLocal()
    garage = session.query(Garage).filter_by(id=garage_id).first()
    if not garage:
        session.close()
        return None
    if name:
        garage.name = name
    if location:
        garage.location = location
    if contact_number:
        garage.contact_number = contact_number
    session.commit()
    session.refresh(garage)
    session.close()
    return garage

def delete_garage(garage_id):
    session = SessionLocal()
    garage = session.query(Garage).filter_by(id=garage_id).first()
    if garage:
        session.delete(garage)
        session.commit()
    session.close()
    return garage
