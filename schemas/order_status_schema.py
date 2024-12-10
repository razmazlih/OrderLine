from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StatusCreateSchema(BaseModel):
    order_id: int
    status: str


class StatusShowSchema(BaseModel):
    id: int
    order_id: int
    status: str
    updated_at: datetime
