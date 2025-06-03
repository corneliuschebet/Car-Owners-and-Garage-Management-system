from models.owner import Owner
from db.connection import SessionLocal

def create_owner(name, phone, email=None):
    session = SessionLocal()
    owner = Owner(name=name, phone=phone, email=email)
    session.add(owner)
    session.commit()
    session.refresh(owner)
    session.close()
    return owner

def get_all_owners():
    session = SessionLocal()
    owners = session.query(Owner).all()
    session.close()
    return owners

def get_owner_by_id(owner_id):
    session = SessionLocal()
    owner = session.query(Owner).filter_by(id=owner_id).first()
    session.close()
    return owner

def update_owner(owner_id, name=None, phone=None, email=None):
    session = SessionLocal()
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if not owner:
        session.close()
        return None
    if name:
        owner.name = name
    if phone:
        owner.phone = phone
    if email:
        owner.email = email
    session.commit()
    session.refresh(owner)
    session.close()
    return owner

def delete_owner(owner_id):
    session = SessionLocal()
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if owner:
        session.delete(owner)
        session.commit()
    session.close()
    return owner
