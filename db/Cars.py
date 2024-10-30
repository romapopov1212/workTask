from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Car(Base):
    car_id = Column(Integer, primary_key=True),
    name = Column(String, nullable=False),
    descriptions = Column(String, nullable=False),
    price = Column(Integer, nullable=False),