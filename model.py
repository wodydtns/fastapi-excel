from re import L
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class UserTable(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key, autoIncrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)


class User(BaseModel):
    id: int
    name: str
    age: int
