# There are many situtaions in which I need to report an error to a client that is using my API

# I could need to tell the client that:
# The client doesn't have enough privileges for that operation.
# The client doesn't have access to that resource.
# The item the client was trying to access doesn't exist.
# etc.

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo":"The Fo wirestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error":"There goes my error"})
    return {"item": items[item_id]}

