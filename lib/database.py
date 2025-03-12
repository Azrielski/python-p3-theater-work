from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///moringa_theater.db"  # SQLite database file

engine = create_engine(DATABASE_URL, echo=True)  # Echo for debugging
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
