from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Car(Base):
    __tablename__ = "Cars"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    descriptions = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)