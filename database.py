from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv


DATABASE_USERNAME= getenv("DATABASE_USERNAME", "database-name")
DATABASE_PASSWORD=getenv("DATABASE_PASSWORD", "password")
DATABASE_NAME=getenv("DATABASE_NAME", "db-name")
DATABASE_HOST=getenv("DATABASE_HOST", "localhost")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
