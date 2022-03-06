from fastapi import FastAPI,Query
from typing import Optional , List


app = FastAPI()


@app.get("/item/")
async def read_item(item_id:int, item_name : str , description: Optional[str] = Query(None,
                                                                                      title="description string",
                                                                                      max_length=20,
                                                                                      min_length=10,
                                                                                      regex="^Germain",
                                                                                      description="description of the query",
                                                                                      alias="dscpt",
                                                                                      deprecated=True)):
    result ={
        "items":[
            {"item_id":item_id},
            {"item_name": item_name}
        ]
    }
    if description:
        result.update({"description":description})
    return result



# Query parameter list / multiple values

@app.get("/items/")
async def read_items(description : Optional[List[str]] = Query(None,regex="phone$")):
    items = {
        "description":description
    }
    return items


@app.get("/items3")
async def read_items3(item_name: List[str] = Query(["phones"])):
    result = {"item_name": item_name}
    return item_name



@app.get("/items4/")
async def excluding(hidden_querry : Optional[str] = Query(None, include_in_schema= False)):
    if hidden_querry:
        return {"hidden querry ": hidden_querry}
    else:
        return {"hidden_querry": "Not found"}
