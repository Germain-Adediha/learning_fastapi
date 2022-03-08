"""
The same way we can declare  more validdtionss and metadata for query parameters with QUERY (Query),
we can declaree the same type of validations and metadata for path parameters with PATH (Path)
"""
from fastapi import FastAPI,Path,Query
from typing import Optional

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id:int = Path(...,
                           title="The id of the item to get"),
        q: Optional[str] = Query(None,alias="item_query")
):
    result={
        "Item_id":item_id
    }
    if q:
        result.update({
            "q":q
        })
    return result


@app.get("/items2/{item_id}")
async def read_items2(
        q:str,
        item_id : int = Path(...,
                             title="The id of the item to get")
):
    result =    {
        "item_id":item_id
    }
    if q:
        result.update({
            "q":q
        })
    return  result


# keyword arguments kwargs , greater than or equal(ge) , greater than(gt) and less than(lt)

@app.get("/items3/{item_id}")
async def read_items3(
      *,
       item_id : int = Path(...,
                             title="The id of the item to get", ge=100),
        q: float = Query(...,
                        gt =0, lt=100.5)

):
    result = {
        "item_id":item_id
    }
    if q:
        result.update({
            "q":q
        })
    return  result


