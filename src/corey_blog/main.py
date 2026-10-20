# from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Calculate path to 'templates' relative to main.py
# BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory="templates")

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

@app.get("/")
@app.get("/posts")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/api/psots")
async def get_posts():
    return posts