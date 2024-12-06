from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base

# כתובת מסד הנתונים עבור SQLite
DATABASE_URL = "sqlite:///./my_data.db"

# יצירת ה-Engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# יצירת ה-Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)