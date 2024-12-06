from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from models.base import Base


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    restaurant_id = Column(Integer, nullable=False, index=True)
    ordered_at = Column(DateTime, default=None)
    items = relationship("OrderItemModel", backref="order", cascade="all, delete-orphan")

    @hybrid_property
    def total_price(self):
        return sum(item.price * item.quantity for item in self.items)