from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author":"Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "October 19, 2026"
    },
    {
        "id": 2,
        "author":"Jane Doe",
        "title": "FPython is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPi makes it ever better",
        "date_posted": "October 19, 2026"
    },
]


@app.get("/home")
async def home():
    return posts