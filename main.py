from fastapi import FastAPI, Query, Path, Body
from typing import Union
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None,
        title="The description of the item",
        max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.get(
    path="/",
    description="Step 2, Request Body Fields"
)
async def main():
    return {"Hello":"World"}

@app.put(
    path="/items/{item_id}",
    description="Body Field"
)
async def update_item(
        item_id: int,
        item: Item = Body(embed=True)
):
    results = { "item_id": item_id, "item": item}

    return results


