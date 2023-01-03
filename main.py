from fastapi import FastAPI, Query, Path, Body
from typing import Union
from pydantic import BaseModel, Required

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.get(
    path="/",
    description="Step 2, Request Body"
)

async def main():
    return {"Hello":"World"}

@app.put(
    path="/items/{item_id}",
    description="Mix Path, Query Body Params"
)
async def update_item(
    *,
    item_id: int = Path(title="ID the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[str, None] = None
):
    result = {"item_id": item_id}
    if q:
        result.update({"q":q})
    if item:
        result.update({"item": item})
    return result

@app.put(
    path="/items2/{item_id}",
    description="Multiple body parameters"
)
async def update_item2(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}

    return results


@app.put(
    path="/body/{body_id}",
    description="Multiple body parameters"
)
async def update_item2(body_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": body_id, "item": item, "user": user, "importance": importance}

    return results

