from fastapi import FastAPI, Query, Path, Body
from typing import Union, List, Set, Dict
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []    # 3.9 이상 list[str]
    tags2: Set[str] = set()
    image: Union[Image, None] = None
    images: Union[List[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    item: List[Item]

@app.get(
    path="/",
    description="Step 2, Request Body Nested Models"
)
async def main():
    return {"Hello":"World"}

@app.post(
    path='/offers/'
)
async def create_offer(offer: Offer):
    return offer

@app.post(
    path='/images/multiple/'
)
async def create_multiple_images(images: List[Image]):
    return images


@app.post('/index-weights/')
async def create_index_weights(weights: Dict[int, float]):
    return weights