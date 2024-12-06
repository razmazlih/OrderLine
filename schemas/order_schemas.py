from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from schemas.order_item_schemas import OrderItemResponseSchema


class OrderCreateSchema(BaseModel):
    user_id: int
    restaurant_id: int


class OrderSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    restaurant_id: int
    total_price: float
    ordered_at: datetime
    items: list[OrderItemResponseSchema]

    class Config:
        orm_mode = True


class OrderUpdateSchema(BaseModel):
    user_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    total_price: Optional[float] = None

    class Config:
        orm_mode = True
