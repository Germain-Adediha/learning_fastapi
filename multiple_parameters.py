from fastapi import FastAPI, Path, Body

from pydantic import BaseModel

from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price :float
    tax : Optional[float] = None


class User(BaseModel):

    username : str
    user_id: int
    user_full_name:str




@app.put("/items/{item_id}")
async def update_item (
        # all the following parameters should be called as kwargs .Even if they don't have a default value
        item_id:int = Path(...,title="The id of the item to update",ge =1,le = 1000),
        q: Optional[str] = None,
        item:Optional[Item]=None
):
    result = {
        "item_id" : item_id
    }
    if q :
        result.update({
            "q":q
        })
    if item:
        result.update({
            "item":item
        })
    return result


@app.put("/items2/{user_id}")
async def update_user_info(
        item_id: int,
        item: Item,
        user: User,
        importance : int = Body(...) # if we declare it as is , because it is a singular value, FASTAPI will assume that it is a query param.that's why we instruct it to treat it as another body key (using body)
):
    result = {
        "item_id":item_id,
        "item_description": item,
        "user_info":user,
        "importance":importance

    }
    return result



