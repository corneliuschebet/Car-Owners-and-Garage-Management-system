from db.connection import SessionLocal
from models.owner import Owner
from models.car import Car
from models.garage import Garage
import models.relationships  # pour garantir que la table de relation est chargée

def seed():
    session = SessionLocal()

    # Propriétaires
    alice = Owner(name="Alice Johnson", phone="0700123456", email="alice@example.com")
    bob = Owner(name="Bob Smith", phone="0711223344", email="bob@example.com")
    
    # Voitures
    car1 = Car(make="Toyota", model="Corolla", year=2015, license_plate="KBY123A", owner=alice)
    car2 = Car(make="Honda", model="Civic", year=2018, license_plate="KBZ456B", owner=bob)

    # Garages
    garage1 = Garage(name="QuickFix Auto", location="Nairobi West", contact_number="0790112233")
    garage2 = Garage(name="City Garage", location="Westlands", contact_number="0788223344")

    # Liens voitures-garages
    car1.garages.append(garage1)
    car2.garages.extend([garage1, garage2])

    session.add_all([alice, bob, car1, car2, garage1, garage2])
    session.commit()
    session.close()

    print("✔️ Database seeded with sample data.")

if __name__ == "__main__":
    seed()
