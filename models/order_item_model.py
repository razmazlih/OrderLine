from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import validates
from models.base import Base
from sqlalchemy import CheckConstraint


class OrderItemModel(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    menu_item_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("quantity >= 0", name="check_quantity_positive"),
        CheckConstraint("price >= 0", name="check_price_positive"),
    )

    @validates("quantity")
    def validate_quantity(self, key, value):
        if value < 0:
            raise ValueError("Quantity must be greater than or equal to 0")
        return value

    @validates("price")
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price must be greater than or equal to 0")
        return value