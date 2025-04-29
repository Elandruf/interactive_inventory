from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)  # id es autoincremental
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean, default=True)