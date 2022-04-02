from sqlalchemy.orm import relationship

from  .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer ,primary_key=True)
    email = Column(String , unique = True)
    hashed_password =Column(String)
    is_active =  Column(Boolean, default=True)

    items = relationship("Item",back_populates ="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer , primary_key= True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates ="items")
