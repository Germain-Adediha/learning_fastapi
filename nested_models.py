from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Item(BaseModel):
    name : str
    description:  Optional[str] = None
    price : float
    tax:Optional[float] = None
    tags :list = []


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