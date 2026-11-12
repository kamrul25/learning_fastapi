# There are many situtaions in which I need to report an error to a client that is using my API

# I could need to tell the client that:
# The client doesn't have enough privileges for that operation.
# The client doesn't have access to that resource.
# The item the client was trying to access doesn't exist.
# etc.

from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

items = {"foo":"The Fo wirestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error":"There goes my error"})
    return {"item": items[item_id]}


# Custom Headers
@app.get("/items_header/{item_id}")
async def read_item_header(item_id):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error":"There goes my error"}
        )
    return {"item": items[item_id]}

# Instasll Custom exception handlers
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    def __init__(self, name: str) :
         self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request:Request, exc:UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message":f"Oops!{exc.name} did something. There goes a rainbow..."}
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}