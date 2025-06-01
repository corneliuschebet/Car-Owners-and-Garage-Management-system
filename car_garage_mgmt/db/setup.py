from models import *
from db.connection import Base, engine

Base.metadata.create_all(engine)
