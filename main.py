from fastapi import FastAPI, Query
from typing import Union, List
from pydantic import Required

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

@app.get(
    path="/items2",
    description="Query Validation Regex"
)
async def read_item2(q : Union[str, None] = Query(default= None, min_length=3,max_length=50, regex="^fixedquery$")):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/items3",
    description="Query Validation Default"
)
async def read_item3(q : str = Query(default= "fixedquery", min_length=3,max_length=50)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/items4",
    description="Query Validation Required"
)
async def read_item4(q : str = Query(min_length=3, max_length=50)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/items5/",
    description="Query Validation Required를 명시적으로 선언할때 쓰임, default: ..."
)
async def read_item5(q : str = Query(default=..., min_length=3)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/items6/",
    description="Query Validation None과 required를 명시적으로 선언"
)
async def read_item6(q : Union[str, None] = Query(default=..., min_length=3)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/items7/",
    description="Query Validation Required - Pydantic"
)
async def read_item7(q : Union[str, None] = Query(default=Required, min_length=3)):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}

    if q:
        results.update({"q": q})

    return results

@app.get(
    path="/multiquery/",
    description="Query parameter list / multiple values"
)
async def multiquery(q: Union[List[str], None] = Query(default=["Foo","Bar"] )):

    query_items = {"q": q}

    return query_items

@app.get(
    path="/multiquery2/",
    description="Query parameter list / multiple values 2"
)
async def multiquery2(q: list = Query(default=[])):

    query_items = {"q": q}

    return query_items


@app.get(
    path="/metadata/",
    description="Meta data title, description, ..."
)
async def metadata(q: Union[str, None] = Query(
    default=None,
    title="metadata Title",
    description="metadata Description"
)):

    query_items = {"q": q}

    return query_items
@app.get(
    path="/metadata2/",
    description="Meta data alias, deprecated..."
)
async def metadata(q: Union[str, None] = Query(
    default=None,
    alias="item-query",
    deprecated=True
)):

    query_items = {"q": q}

    return query_items


@app.get(
    path="/hidden/",
    description="Open API에서 hidden, include_in_schema"
)
async def hidden(hidden_query: Union[str, None] = Query(
    default=None,
    include_in_schema=False
)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


