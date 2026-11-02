from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name: str
    decription: str | None=None
    price: float
    tax: float | None=None
    tags: list[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/")
async def create_items(item: Item) -> Item:
    return item

@app.post("/items/", response_model=Item)
async def create_item(item: Item)-> Any:
    return item

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user



@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name="Kamrul", price=52.00),
        Item(name="Hasan" ,price = 32.00),
    ]