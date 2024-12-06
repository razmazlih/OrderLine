from models.base import Base
from database import engine

def init_db():
    Base.metadata.create_all(bind=engine)