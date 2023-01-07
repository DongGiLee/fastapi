from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

@app.get("/")
async def main():
    return "Fast API Study Base"