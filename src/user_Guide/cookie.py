
from typing import Annotated
from fastapi import Cookie, FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

@app.get("/items/")
async def read_items(
    ads_id: Annotated[str | None, Cookie()] = None,
    session_id: Annotated[str | None, Cookie()] = None,
    fatebook_tracker: Annotated[str | None, Cookie()] = None,
    googall_tracker: Annotated[str | None, Cookie()] = None
):
    return {
        "ads_id": ads_id,
        "session_id": session_id,
        "fatebook_tracker": fatebook_tracker,
        "googall_tracker": googall_tracker
    }


@app.get("/headers/")
async def read_header(
    user_agent: Annotated[str | None, Header()] = None
):
    return {"User-Agent": user_agent}


@app.get("/multiples/")
async def read_header_multiple(
    x_token: Annotated[list[str] | None, Header()] = None
):
    return {"X-Token values": x_token}
