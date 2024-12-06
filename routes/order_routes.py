from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import Order as OrderModel
from schemas.order_schemas import OrderCreate, Order, OrderUpdate

router = APIRouter(prefix="/orders", tags=["Order"])

# יצירת הזמנה חדשה
@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
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
@router.get("/", response_model=list[Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).offset(skip).limit(limit).all()
    return orders

# שליפת הזמנה לפי ID
@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# עדכון הזמנה
@router.put("/{order_id}", response_model=Order)
def update_order(
    order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)
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
@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}