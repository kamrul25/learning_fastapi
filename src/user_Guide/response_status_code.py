# Response Status Code for each speific HTTP method get(), post(), put(), delete()
# Information and response don't have any body 100 - 199
# Successful 200 - 299
# Redirection 300 - 399 may or may not have body  except 304, "Not Modified"
# Client Error response 400 - 499
# Server Error 500 - 599

from fastapi import FastAPI , status
app = FastAPI()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# I don't need to memorize what each of these codes mean

@app.post("/status/", status_code=status.HTTP_201_CREATED)
async def create_status(name: str):
    return {name}