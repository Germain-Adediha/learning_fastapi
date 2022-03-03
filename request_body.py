from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name : str
    description : Optional[str]=None
    price: float
    tax :Optional[float]=None



app = FastAPI()


@app.post("/items/")
async def create_item(item:Item):
    item_dict= item.dict()
    item.tax = 3333
    if item.tax:
        new_price = item.price + item.tax
        item_dict.update({"new price":new_price})
    result = {"item_tax":item.tax,"item_new_price":new_price}
    return result


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id":item_id,**item.dict()}
    if q:
        result.update({ "q":q })
    return result

