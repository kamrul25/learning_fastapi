from fastapi import FastAPI

app = FastAPI() # instance of FastAPI and main point of interaction to create all my API.

# @FastAPI().get("/")
@app.get("/")
async def root():
    return {"message": "Hello World"}

# I can also use the other operations
# @app.post("/post")
# @app.put("/put")
# @app.delete("/delete")

# And the more exotic ones
# @app.options("/options")
# @app.head("/head")
# @app.patch("/patch")
# @app.trace("/trace")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id":item_id}
