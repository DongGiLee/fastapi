from typing import Union
from fastapi import FastAPI, Body, Cookie

app = FastAPI()


@app.put(
    path="/items/",
    description="Cookie로 불러오지않은면 쿼리 매개변수로 해석됨"
)
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
