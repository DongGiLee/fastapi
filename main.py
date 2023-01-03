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
    path= "/items",
    description= "매개변수 BaseModel 확인"
)
async def create_item(item: Item):
    return item