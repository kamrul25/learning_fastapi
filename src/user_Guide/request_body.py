# A request body is data sent by the client to your API. A response body is the data your API sends to the client.

from typing import Annotated, Any
from fastapi import FastAPI, Query
from pydantic import BaseModel # Pydantic's BaseModel

# Creating Data Model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): #declare it as a parameter like "item: Item"
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Request Body + path + query parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q":q})
    return result

# Additonal Validation of Query
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q is not None:
        results["q"] = q
    return results