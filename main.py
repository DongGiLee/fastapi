from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{itme_id}")
def read_item(itme_id: int, q: Union[str, None] = None):
    return {"item_id":itme_id, "q":q}