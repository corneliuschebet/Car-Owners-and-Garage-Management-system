from db.connection import Session
from models.owner import Owner

def register_owner(name, email, phone):
    session = Session()
    owner = Owner(name=name, email=email, phone_number=phone)
    session.add(owner)
    session.commit()
    print(f"Owner {name} registered.")