from database import engine
from models.base import Base


def init_db():
    Base.metadata.create_all(bind=engine)
