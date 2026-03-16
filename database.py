from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL DIRECTA - como en la guía página 4
DB_URL = f"mysql://root:IomHTqBUYCZfUQnlmbFwsNGXxXXAmTfx@centerbeam.proxy.rlwy.net:13371/railway"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()