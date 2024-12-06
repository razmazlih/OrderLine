from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models.order_model import OrderModel
from schemas.order_schemas import OrderCreateSchema, OrderSchema, OrderUpdateSchema

order_router = APIRouter(prefix="/orders", tags=["Order"])


# יצירת הזמנה חדשה
@order_router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    db_order = OrderModel(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        total_price=order.total_price,
        ordered_at=datetime.now(),
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# שליפת כל ההזמנות
@order_router.get("/", response_model=list[OrderSchema])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).offset(skip).limit(limit).all()
    return orders


# שליפת הזמנה לפי ID
@order_router.get("/{order_id}", response_model=OrderSchema)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# עדכון הזמנה
@order_router.put("/{order_id}", response_model=OrderSchema)
def update_order(
    order_id: int, order_update: OrderUpdateSchema, db: Session = Depends(get_db)
):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order_update.dict(exclude_unset=True).items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return order


# מחיקת הזמנה
@order_router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}
