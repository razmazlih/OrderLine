from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init_db import init_db
from routes.order_routes import order_router
from routes.order_item_routes import order_item_router
from routes.order_status_websocket import order_status_ws_router
from routes.order_status_routes import order_status_router

init_db()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

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
