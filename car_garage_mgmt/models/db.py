# models/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///car_garage.db")  # Make sure path matches project root
Session = sessionmaker(bind=engine)
