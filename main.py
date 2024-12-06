from fastapi import FastAPI
from database import engine
from models.order_model import Base
from routes.order_routes import router as order_router

# יצירת בסיס הנתונים
Base.metadata.create_all(bind=engine)

app = FastAPI()

# רישום הראוטר
app.include_router(order_router)