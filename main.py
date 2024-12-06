from fastapi import FastAPI
from database import engine
from init_db import init_db
from models import Base
from routes.order_routes import order_router
from routes.order_item_routes import order_item_router

# יצירת בסיס הנתונים
init_db()

app = FastAPI()

# רישום הראוטר
app.include_router(order_router)
app.include_router(order_item_router)

