# create_db.py

from models import Base, engine
import models.owner
import models.car
import models.garage
import models.relationships

Base.metadata.create_all(engine)
print("✅ Database tables created.")
