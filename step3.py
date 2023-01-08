from typing import Union, List
from fastapi import FastAPI, Header

app = FastAPI()

@app.get(
    path="/items/",
    description="Header,"
)
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}

@app.get(
    path="/under_score/",
    description="Header - convert_underscores=False: 언더스코어 하이픈 자동변환 비활성화"
)
async def underscore(
        strange_header: Union[str, None] = Header(default=None, convert_underscores=False)
):
    return {"strange_header":strange_header}


@app.get(
    path="/duplicateheader/",
    description="Header - 중복 헤더 "
)
async def duplicate_header(
        x_token: Union[List[str], None] = Header(default=None)
):
    return {"X-Token values":x_token}


