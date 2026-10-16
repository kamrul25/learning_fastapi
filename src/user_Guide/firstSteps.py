from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

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

#Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id} 


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message":"Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
