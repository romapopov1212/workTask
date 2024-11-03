

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Car(Base):
    __tablename__ = "Cars"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    model = Column(String, nullable=False)
    descriptions = Column(String, nullable=False)
    price = Column(Integer, nullable=False)



class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, unique=True)
    username = Column(Text, unique=True)
    password_hash = Column(Text)

class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    price = Column(Integer, nullable=False)