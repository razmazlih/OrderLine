from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models.order_item_model import OrderItemModel
from schemas.order_item_schemas import (
    OrderItemResponseSchema,
    OrderItemCreateSchema,
    UpdateOrderItemSchema,
)


order_item_router = APIRouter(prefix="/order-item", tags=["OrderItems"])


@order_item_router.get("/{order_id}/", response_model=list[OrderItemResponseSchema])
def read_order_items_by_order(
    order_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    order_items = (
        db.query(OrderItemModel).filter(OrderItemModel.order_id == order_id).all()
    )
    if not order_items:
        raise HTTPException(status_code=404, detail="Order items not found")
    return order_items


@order_item_router.post("/", response_model=OrderItemResponseSchema)
def create_order(order_item: OrderItemCreateSchema, db: Session = Depends(get_db)):
    new_order_item = OrderItemModel(**order_item.model_dump())
    db.add(new_order_item)
    db.commit()
    db.refresh(new_order_item)
    return new_order_item


@order_item_router.put("/{order_item_id}/", response_model=OrderItemResponseSchema)
def update_order(
    order_item_id: int,
    order_item_update: UpdateOrderItemSchema,
    db: Session = Depends(get_db),
):
    """
    Update the quantity of an existing order item and return the full order item details.
    """
    existing_order_item = (
        db.query(OrderItemModel).filter(OrderItemModel.id == order_item_id).first()
    )

    if not existing_order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    if order_item_update.quantity is not None:
        existing_order_item.quantity = order_item_update.quantity

    if order_item_update.price is not None:
        existing_order_item.price = order_item_update.price

    db.commit()
    db.refresh(existing_order_item)

    return existing_order_item


@order_item_router.delete("/{order_item_id}/")
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    existing_order_item = (
        db.query(OrderItemModel).filter(OrderItemModel.id == order_item_id).first()
    )

    if not existing_order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    db.delete(existing_order_item)
    db.commit()

    return {"message": "Deleted successfully"}
