from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init_db import init_db
from routes.order_routes import order_router
from routes.order_item_routes import order_item_router
from routes.order_status_websocket import order_status_ws_router
from routes.order_status_routes import order_status_router
from os import getenv
import dotenv

dotenv.load_dotenv()

init_db()

app = FastAPI()

origins = getenv('CORS_ALLOWED_ORIGINS', ['http://localhost:3000']).split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_router)
app.include_router(order_item_router)
app.include_router(order_status_ws_router)
app.include_router(order_status_router)
