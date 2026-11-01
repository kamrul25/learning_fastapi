
from typing import Annotated
from fastapi import Cookie, FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

# Declare the header parameters that you need in a Pydantic model
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"} # forbid extra headers

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None=None
    x_tag: list[str] = []


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

# declare the parameter as Header
@app.get("/common/")
async def read_common_headers(headers: Annotated[CommonHeaders, Header()]):
    return headers
