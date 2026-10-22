from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

# Group everything into one body payload
class UpdatePayload(BaseModel):
    item: Item | None = None
    user: User | None = None
    importance: int | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    payload: UpdatePayload | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if payload:
        if payload.item:
            results.update({"item": payload.item})
        if payload.user:
            results.update({"user": payload.user})
        if payload.importance is not None:
            results.update({"importance": payload.importance})
    return results