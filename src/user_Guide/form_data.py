# When I need to receive from fields instead of JSON, I can use Form

from typing import Annotated
from fastapi import FastAPI, Form, status

app = FastAPI()

@app.post("/login/", status_code=status.HTTP_201_CREATED)
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()], subscribe: Annotated[bool, Form()] = False):
     return {"username":username, "password":password, "subscribe":subscribe}