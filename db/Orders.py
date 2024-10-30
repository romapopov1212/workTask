from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'Orders',
    order_id = Column(Integer, primary_key=True),
    user_id = Column(Integer, primary_key=True),
    price = Column(Integer, nullable=False),

