from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel , Field


app = FastAPI()

class Element(BaseModel):
    name:str
    description : Optional[str] = Field(
        None, title="Description of the element",
        max_length=500,
    )
    price : float = Field(...,gt =0 , description="The price of the element must be greater than zero")
    tax : float



@app.get("/elements/{element_id}")
async def update_element (elm_id:int ,
           element: Element = Body(...,embed=True)):
    result = {
        "elm_id":elm_id,
        "element": Element
    }
    return result
