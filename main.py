from fastapi import FastAPI
from database import engine
from models import Base

# יצירת בסיס הנתונים
Base.metadata.create_all(bind=engine)

app = FastAPI()
