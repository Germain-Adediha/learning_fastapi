from sqlalchemy.orm import Session
import models, schemas
from fastapi import FastAPI


def get_user(my_db: Session, user_id:int):
    return my_db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(my_db : Session, email: str):
    return my_db.query(models.User).filter(models.User.email == email).first()


def get_users(my_db: Session, skip :int =0 , limit: int =100):
    return my_db.query(models.User).offset(skip).limit(limit).all()


def create_user(my_db: Session, user:schemas.UserCreate):
    hashed_password = user.password+ "h-pword"
    my_db_user = models.User(email = user.email, hashed_password = hashed_password)
    my_db.add(my_db_user)
    my_db.commit()
    my_db.refresh(my_db_user)

    return my_db_user


def get_items(my_db:Session, skip=0,limit=100):
    return my_db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(my_db : Session, item:schemas.Item, user_id:int):
    my_db_item = models.Item(**item.dict(),owner_id = user_id)
    my_db.add(my_db_item)
    my_db.commit()
    my_db.refresh()

    return my_db_item
