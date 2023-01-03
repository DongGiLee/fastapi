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

@app.post(
    path="/items",
    description="모델 사용"
)
async def create_item(item: Item):

    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})

    return item_dict