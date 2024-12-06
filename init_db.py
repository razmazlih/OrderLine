from database import engine
from models import Base

def init_db():
    for base in Base:
        base.metadata.create_all(bind=engine)