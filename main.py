from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def getting_started():
    return {"Getting started with " : " FastAPI "}


@app.get("/item/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}


