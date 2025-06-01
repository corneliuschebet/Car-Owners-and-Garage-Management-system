from models import Owner, Car, Garage
from db.connection import Session

session = Session()
owner = Owner(name='Alice', email='alice@email.com', phone_number='123-456')
session.add(owner)
session.commit()