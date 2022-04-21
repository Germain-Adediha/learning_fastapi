from fastapi import FastAPI
from typing import Optional, List, Union
from pydantic import BaseModel,  EmailStr

app = FastAPI()

items ={
    "Iphone":{
        "name":"Iphone",
        "price": 20.2,
    },
    "samsung":{
        "name":"SamsungX",
        "price": 20.3,
    }
}


class Item(BaseModel):
    name:str
    description :Optional[str]=None
    price :float
    tax : Optional[float] = None
    tags : Optional[List[str]] = []


class UserIn(BaseModel):
    user_name:str
    user_email:EmailStr
    user_pwd: str


class UserOut(BaseModel):
    user_name:str
    user_email:EmailStr


@app.post("/item/", response_model =Item)
async def create_item(item: Item):
    return item


@app.post("/user/",response_model= UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/name", response_model= Item,response_model_include=["name","description"])
async def read_item_name(item_id : str):
    return items[item_id]


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


new_items= {
    "item1":{
        "description":"the first item",
        "type": "car"
    },
    "item2":{
        "description":"The second item",
        "type":"plane"
    }
}


@app.get("/new_items/{id}", response_model= Union[PlaneItem, CarItem])
async def read_new_item(id :str):
    return new_items[id]





"""
Use the path operation decorator's parameter #response_model# to define response models and especially to ensure private data is filtered out.
Use #response_model_exclude_unset to return only the values explicitly set.
"""


