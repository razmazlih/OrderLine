from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models.order_status_model import OrderStatusModel
from routes.order_status_websocket import notify_order_status
from schemas.order_status_schema import StatusCreateSchema, StatusShowSchema

order_status_router = APIRouter(prefix="/order-status", tags=["OrderStatuses"])


@order_status_router.get("/{order_id}/", response_model=List[StatusShowSchema])
def read_statuses(order_id: int, db: Session = Depends(get_db)):
    order_statuses = (
        db.query(OrderStatusModel).filter(OrderStatusModel.order_id == order_id).all()
    )
    return order_statuses


@order_status_router.post("/", response_model=StatusShowSchema)
async def create_status_and_update_ws(
    order_status: StatusCreateSchema, db: Session = Depends(get_db)
):
    db_order_status = OrderStatusModel(
        order_id=order_status.order_id,
        status=order_status.status,
        updated_at=datetime.now(),
    )

    db.add(db_order_status)
    db.commit()
    db.refresh(db_order_status)

    await notify_order_status(db_order_status.order_id, db_order_status.status)

    return db_order_status
