from fastapi import FastAPI
from  typing import Optional


app = FastAPI()

items_base =[
    {
        "item_name":"phone"
    },
    {
        "item_name":"laptop"
    },
    {
        "item_name":"charger"
    },
    {
        "item_name":"powerBank"
    }
]


@app.get("/items")
async def read_item(skip:int,limit:int):
    return items_base[skip:skip+limit]

# Optional parameter


@app.get("/r_item/{item_id}")
async def r_item(item_id:int, item_name:Optional[str]=None, short : bool = False):
    item= {"item_id":item_id}
    if item_name:
        item.update({"item_name":item_name})
    if not short:
        item.update({
            "description":"just a description"
        })

# Multiples paths


@app.get("/users/{user_id}/item/{item_id}")
async def read_user_item(user_id:int,item_id:int,item_name:Optional[str]=None,short:bool=False):
    item = { "item_id": item_id,"item_name":items_base[item_id],"owner_id":user_id}
    if item_name:
        item.update({"item_name":item_name})
    if not short:
        item.update({"description":"just a description"})
    return item

