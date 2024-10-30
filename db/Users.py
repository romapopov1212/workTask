from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "Users",
    user_id = Column(Integer, primary_key=True),
    name = Column(String, nullable=False),
    surname = Column(String, nullable=False),
    email = Column(String, nullable=False),
    hashed_password = Column(String, nullable=False),
