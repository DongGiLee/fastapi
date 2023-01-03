from fastapi import FastAPI, Query, Path
from typing import Union
from pydantic import Required

app = FastAPI()

@app.get(
    path="/",
    description="Step 2, Request Body"
)
async def main():
    return {"Hello":"World"}

@app.get(
    path='/items/{item_id}',
    description="Path Import"
)
async def read_items(
    item_id: int = Path(title="ID of the item of get", default=Required),
    q: Union[str, None] = Query(default=None, alias="item-query")
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})

    return results

@app.get(
    path='/items2/{item_id}',
    description="Path , Parameter sorting"
)
async def sorting1(
    q: str,
    item_id: int = Path(title="ID of the item of get", default=Required)
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})

    return results

@app.get(
    path='/items3/{item_id}',
    description="Path , Parameter sorting2 ,* "
)
async def sorting2(
    *,
    item_id: int = Path(title="ID of the item of get", default=Required),
    q: str
):
    results = {"item_id":item_id}

    if q:
        results.update({"q":q})

    return results

@app.get(
    path='/integer/{integer}',
    description="숫자 비교, gt,ge le,lt"
)
async def integercomparison(
    *,
    integer: int = Path(title="ID of the item of get",
                        gt=0,
                        le=100
                        ),
    q: Union[str,None] = None,
    size: float = Query(gt=0, lt=10.5)
):
    results = {"item_id":integer, "size":size}

    if q:
        results.update({"q":q})

    return results
