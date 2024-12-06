from pydantic import BaseModel, field_validator
from typing import Optional, Required


class OrderItemCreateSchema(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    price: float

    @field_validator("quantity")
    def validate_quantity(cls, value):
        if value < 0:
            raise ValueError("Quantity must be greater than or equal to 0")
        return value

    @field_validator("price")
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("Price must be greater than or equal to 0")
        return value


class UpdateOrderItemSchema(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None


class OrderItemResponseSchema(BaseModel):
    id: Optional[int] = None
    order_id: int
    menu_item_id: int
    quantity: int
    price: float
