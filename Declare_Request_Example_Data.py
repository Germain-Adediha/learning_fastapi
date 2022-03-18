from fastapi import FastAPI ,Body
from typing import Optional
from pydantic import BaseModel , Field


app = FastAPI()

# Pydantic schema_extra
class Item(BaseModel):
    name : str
    description: Optional[str] = None
    price : float
    tax: Optional[float] = None

    class Config:
        schema_extra ={
            "example":{
                "name":"FASTAPI",
                "description":"A python framework",
                "price": 0,
                "tax":0,
            }
        }


# Field additional arguments
class Item2(BaseModel):
    name : str = Field(...,example="FASTAPI")
    description :Optional[str] = Field(...,example ="A python framework")
    price: float = Field(...,example = 0)
    tax : Optional[float] =Field(...,example = 0)



class Item3(BaseModel):
    name:str
    description:Optional[str]=None
    price :float
    tax : Optional[float] =None


@app.put("/item/{item_id}")
async def update_item(item_id:int, item:Item):
    result ={
        "item_id": item_id,
        "item": item
    }
    return result


@app.put("/item2/{item2_id}")
async def update_item2(item_id:int , item : Item2):
    result = {
        "item_id":item_id,
        "item" : item
    }
    return result


# We can pass the example of data expected in Body()
@app.put("/item3/{item3}")
async def update_item3(
        item_id:int,
        item: Item3= Body(..., example={
                "name":"FASTAPI",
                "description":"A python framework",
                "price": 0,
                "tax":0,
        })
):
    result = {
        "item_id": item_id,
        "item": item
    }
    return result


# Body with multiples examples ( Using dict with multiples examples each with extra information that will be added to OpenAPI too

@app.put("/item4/{item_id}")
async def update_item4(item_id:int, item:Item3 = Body(...,
                                                      examples={
                                                          "normal":{
                                                             "summary":"A normal example",
                                                             "description":"A **normal** item works correctly",
                                                              "value":{
                                                                  "name": "FASTAPI",
                                                                  "desciption": " A python framework",
                                                                  "price":0,
                                                                  "tax": 0.0
                                                              }
                                                         },
                                                          "converted":{
                                                              "summary":"An example with converted data",
                                                              "description":"fastapi can convert price 'string' to actual 'numbers' automatically",
                                                              "value":{
                                                                  "name": "FASTAPI",
                                                                  "description":"framework",
                                                                  "price": "0"
                                                              }
                                                          },
                                                          "invalid":{
                                                              "summary":"Invalid data is rejected as error",
                                                              "value":{
                                                                  "name":" FASTAPI",
                                                                  "price":"Zero"
                                                              }
                                                          }
                                                      })):
    result = {
        "item_id":item_id,
        "item": item
    }
    return result