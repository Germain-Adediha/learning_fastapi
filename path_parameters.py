from fastapi import FastAPI
from enum import   Enum


class ModelName(str,Enum):
    germain = "germain"
    koffi = "koffi"
    jokebed = "jokebed"


app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}


@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user_id":user_id}


@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
            if model_name == ModelName.koffi:
                return {"model_name":model_name, "message":"learning fastapi"}
            if model_name.value == "germain":
                return {"model_name":model_name, "message": "build a RESTful API"}
            return {"model_name":model_name,"message":"Happy learning"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
   return file_path
