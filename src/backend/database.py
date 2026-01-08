from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session
import os
from dotenv import load_dotenv
from .models import User, Todo  # Import your models here

load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

async def create_db_and_tables():
    """Create database tables"""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Dependency to get database session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()