#  There are some cases where I might need to convert a data type to something compatible with JSON.

#  For that using jsonable_encoder() function

from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

app = FastAPI()

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

# In this example, it would convert the Pydantic model to a dict, and the datetime to a str.

# The result of calling it is something that can be encoded with the Python standard json.dumps().

# It doesn't return a large str containing the data in JSON format (as a string). It returns a Python standard data structure (e.g. a dict) with values and sub-values that are all compatible with JSON.