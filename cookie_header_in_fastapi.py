from fastapi import FastAPI, Cookie ,  Header , Query
from typing import Optional


app = FastAPI()

@app.get("/items/")
async def read_items(ads_id:Optional[str] = Cookie(None)):
    return {
        "ads_id":ads_id
    }


@app.get("/")
async def read_items2(user_agent: Optional[str] = Header(None, convert_underscores=False)):
        return {
            "user_agent":user_agent
        }


