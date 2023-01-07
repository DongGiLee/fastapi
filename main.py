from fastapi import FastAPI, Query, Path, Body
from typing import Union
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.2,
                "tax": 3.2,
            }
        }
class Item2(BaseModel):
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(default=None, example= "A very nice Item")
    price: float = Field(example=30.5)
    tax: Union[float, None] = Field(default=None, example=3.1)
@app.get(
    path="/",
    description="Step 2, Declare Request Example Data"
)
async def main():
    return {"Hello":"World"}

@app.put(
    path="/items/{item_id}"
)
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.put(
    path="/items2/{item_id}"
)
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results

@app.put(
    path='/items3/{item_id}',
    description="body example"
)
async def body_example(
        item_id: int,
        item: Item = Body(
            example={
                "name": "Boo",
                "description":"Body Example",
                "price": 24.4,
                "tax": 2.1
            }
        )
):
    results = {"item_id":item_id, "item": item}

    return results
@app.put(
    path='/items4/{item_id}',
    description="body examples"
)
async def body_examples(
        item_id: int,
        item: Item = Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            }
        )
):
    results = {"item_id":item_id, "item": item}

    return results



