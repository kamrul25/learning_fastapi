from fastapi import FastAPI

app = FastAPI()

@FastAPI().get("/")
async def root():
    return {"message": "Hello World"}