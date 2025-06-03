from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database URI
DATABASE_URL = "sqlite:///car_garage.db"

# Create engine and session factory
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
