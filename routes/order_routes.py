from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models.order_model import OrderModel
from schemas.order_schemas import FullOrderSchema, OrderCreateSchema, OrderSchema, OrderUpdateSchema

order_router = APIRouter(prefix="/orders", tags=["Order"])


@order_router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    db_order = OrderModel(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        ordered_at=datetime.now(),
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@order_router.get("/", response_model=list[OrderSchema])
def read_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).filter(OrderModel.user_id == user_id).all()
    return orders


@order_router.get("/{order_id}/", response_model=FullOrderSchema)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@order_router.put("/{order_id}/", response_model=OrderSchema)
def update_order(
    order_id: int, order_update: OrderUpdateSchema, db: Session = Depends(get_db)
):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order_update.model_dump(exclude_unset=True).items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return order


@order_router.delete("/{order_id}/")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}
