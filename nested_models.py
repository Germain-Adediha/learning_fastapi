from fastapi import FastAPI, Query
from pydantic import BaseModel, HttpUrl
from typing import Optional, List


app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name : str
    description:  Optional[str] = None
    price : Optional[float] = Query(None ,gt=0,lt=10000)
    tax:Optional[float] = None
    tags :list[str] = []
    tags2 : set[str] = set()
    image: Optional[List[Image]] = None # pydantic models can be also used as subtypes of list , set  etc...


class Offer(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    item:List[Item]




@app.put("/items/{item_id}")
async def update_item(
        item_id:int ,
        item: Item
):
    result ={
        "item_id":item_id,
        "Item": item
    }
    return result


@app.post("/offers/")
async def create_offer(offer : Offer):
    return offer


@app.post("/images/multiples/")
async def create_multiple_images(images : list[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights:dict[int,float]):
    return weights