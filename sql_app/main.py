
from fastapi import FastAPI , Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency


def get_my_db():
    my_db= SessionLocal()
    try:
        yield my_db
    finally:
        my_db.close()


@app.post("/users/", response_model= schemas.User)
def create_user(user:schemas.UserCreate, my_db:Session = Depends(get_my_db)):
    db_user = crud.get_user_by_email(my_db, email = user.email)
    if db_user:
        raise HTTPException(status_code=400, detail ="email already registered")
    return crud.create_user(my_db = my_db)


@app.get("/users/", response_model= list[schemas.User])
def read_users(skip:int = 0 , limit:int=100, my_db: Session = Depends(get_my_db)):
    users = crud.get_users(my_db,skip= skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model = schemas.User)
def read_user(user_id:int, my_db: Session = Depends(get_my_db)):
    db_user = crud.get_user(my_db, user_id= user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail ="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id :int,
        item: schemas.ItemCreate,my_db: Session = Depends(get_my_db)
):
    return crud.create_user_item(my_db=my_db, item = item, user_id = user_id)


@app.get("/itens/", response_model=list[schemas.Item])
def read_items(skip :int =0, limit:int=100, my_db: Session = Depends(get_my_db)):
    items = crud.get_items(my_db,skip =skip,limit=limit)
    return items
