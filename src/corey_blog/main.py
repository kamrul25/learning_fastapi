from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

# Mount static files route
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "October 19, 2026"
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better",
        "date_posted": "October 19, 2026"
    },
]

@app.get("/")
@app.get("/posts")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="home.html", 
        context={"posts": posts, "title": "Home"}
    )

@app.get("/api/posts")
async def get_posts():
    return posts