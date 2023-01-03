from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get(
    path="/models/{model_name}",
    description="Enum "
)
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get(
    path="/",
    description="Fast API Study"
)
async def main():
    return {"Hello":"World"}
@app.get(
    path='/users/{user_id}',
    description="순서 확인용 아래 순위로"
)
async def read_user_me(user_id: int):
    return {"user_id": user_id}

@app.get(
    path='/users/me',
    description="순서 확인용 위 순위로"
)
async def read_user_me():
    return {"user_id": "current user: Me!"}


@app.get(
    path="/items/{itme_id}",
    description="선택적 매개변수"
)
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "q": q}

@app.put(
    path="/items/{itme_id}",
    description="Update Item"
)
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get(
    path="/files/{file_path:path}",
    description="path에 직접 지정"
)
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get(
    path= "/db/read_item",
    description= "DB에서 Read"
)
async def db_read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get(
    path= "/users/{user_id}/items/{item_id}",
    description= "매개변수의 순서"
)
async def read_user_item(
        user_id:int,
        item_id: str,
        q: Union[str, None] = None,
        short: bool = False
):
    item = {"item_id":item_id, "owner_id":user_id}
    if q:
        item.update({"q":q})
    if short:
        item.update(
            {"description" : "설명부분입니다."}
        )
    return item
