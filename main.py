from fastapi import FastAPI, Query
from typing import Union


app = FastAPI()

@app.get(
    path="/",
    description="Step 2, Request Body"
)
async def main():
    return {"Hello":"World"}

@app.get(
    path="/items",
    description="Query Validation"
)
async def read_item(q : Union[str, None] = Query(default= None, min_length=3,max_length=50)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results
