from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from schemas.order_item_schemas import OrderItemResponseSchema
from schemas.order_status_schema import StatusShowSchema


class OrderCreateSchema(BaseModel):
    user_id: int
    restaurant_id: int

class SmallStatusSchema(BaseModel):
    status: str

class OrderSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    restaurant_id: int
    total_price: float
    ordered_at: datetime
    status: List[SmallStatusSchema]

    class Config:
        orm_mode = True

class FullOrderSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    restaurant_id: int
    total_price: float
    ordered_at: datetime
    items: List[OrderItemResponseSchema]
    status: List[StatusShowSchema]


class OrderUpdateSchema(BaseModel):
    user_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    total_price: Optional[float] = None

    class Config:
        orm_mode = True
