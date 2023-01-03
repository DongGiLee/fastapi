from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.get(
    path="/",
    description="Step 2, Request Body"
)
async def main():
    return {"Hello":"World"}

@app.put(
    path="/items/{item_id}",
    description="Request Body + Path + Query String"
)
async def create_item(item_id : int, item: Item, q: Union[str, None] = None):

    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q":q})

    return result