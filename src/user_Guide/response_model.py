from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    decription: str | None=None
    price: float
    tax: float | None=None
    tags: list[str] = []


@app.post("/")
async def create_items(item: Item) -> Item:
    return item

@app.get("/items'/")
async def read_items() -> list[Item]:
    return [
        Item(name="Kamrul", price=52.00),
        Item(name="Hasan" ,price = 32.00),
    ]