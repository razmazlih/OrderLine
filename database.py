from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv


POSTGRES_USER= getenv("POSTGRES_USER", "database-name")
POSTGRES_PASSWORD=getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB=getenv("POSTGRES_DB", "db-name")
POSTGRES_HOST=getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT=getenv("POSTGRES_PORT", 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
