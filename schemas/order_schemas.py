from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderCreateSchema(BaseModel):
    user_id: int
    restaurant_id: int
    total_price: float = 0.0


class OrderSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    restaurant_id: int
    total_price: float
    ordered_at: datetime

    class Config:
        orm_mode = True


class OrderUpdateSchema(BaseModel):
    user_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    total_price: Optional[float] = None

    class Config:
        orm_mode = True
