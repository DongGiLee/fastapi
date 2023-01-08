from typing import Union, List, Any
from fastapi import FastAPI, Header
from pydantic import BaseModel, EmailStr
# Email Validator : email-validator or pydantic[email]
app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr   # 라이브러리 설치 필요
    full_name: Union[str, None] = None
class UserOut(BaseModel):
    username: str
    email: EmailStr   # 라이브러리 설치 필요
    full_name: Union[str, None] = None

class BaseUser(BaseModel):
    username: str
    email: EmailStr   # 라이브러리 설치 필요
    full_name: Union[str, None] = None

class UserIn2(BaseUser):
    password: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

items2 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

@app.post(
    path="/items/",
    description="create Item"
)
async def create_item(item: Item) -> Item:
    return item

@app.get(
    path="/items/",
    description="read Item"
)
async def read_item() -> List[Item]:
    return [
        Item(name="Protal Gun", price=42.0),
        Item(name="Plumbus", price=32.0)
    ]

@app.post(
    path="/items2/",
    response_model=Item,
    description="response model"
)
async def response_model_create_items(item: Item) -> Any:
    return item

@app.get(
    path="/items2/",
    response_model=List[Item],
    description="response model"
)
async def response_model_read_items() -> Any:
    return [
        {"name":"Portal Gun", "price": 43.6},
        {"name": "Plumbus", "price": 23.6}
    ]

@app.post(
    path='/user/',
    description="동일한 입력 데이터 반환"
)
async def create_user(user: UserIn) -> UserIn:
    return user

@app.post(
    path='/user2/',
    description="password 프로퍼티만 제외하고 출력",
    response_model=UserOut
)
async def create_user2(user: UserIn) -> Any:
    return user

@app.post(
    path='/user3/',
    description="반환유형 및 데이터 필터링",
    response_model=UserOut
)
async def create_user2(user: UserIn) -> Any:
    return user

@app.get(
    path="/items3/{item_id}",
    response_model=Item,
    description="기본값은 응답에 포함되지 않고 실제로 설정된 값만 포함됩니다.",
    response_model_exclude_unset=True
)
async def encoding_params(item_id: str):
    return items[item_id]

@app.get(
    path="/items4/{item_id}/name",
    description="응답 모델을 정의후 비공개 데이터가 필터링 되도록함",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items2[item_id]

@app.get(
    path="/items4/{item_id}/public",
    description="명시적으로 설정한 값만 반환",
    response_model=Item,
    response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items2[item_id]