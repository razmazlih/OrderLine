from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv

import dotenv

dotenv.load_dotenv()


POSTGRES_USER= getenv("POSTGRES_USER", "razmaz")
POSTGRES_PASSWORD=getenv("POSTGRES_PASSWORD", "razmaz123")
POSTGRES_DB=getenv("POSTGRES_DB", "orderline-db")
POSTGRES_HOST=getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT=getenv("POSTGRES_PORT", 5432)

if getenv('TEST_DATABASE') != 'True':
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
