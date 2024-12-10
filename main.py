from fastapi import FastAPI
from database import engine
from init_db import init_db
from models import Base
from routes.order_routes import order_router
from routes.order_item_routes import order_item_router
from routes.order_status_websocket import order_status_ws_router
from routes.order_status_routes import order_status_router

init_db()

app = FastAPI()

app.include_router(order_router)
app.include_router(order_item_router)
app.include_router(order_status_ws_router)
app.include_router(order_status_router)
