from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run

app = FastAPI()
templates = Jinja2Templates(directory="app/templates/")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).resolve().parent.parent / "app" / "static"),
    name="static"
)


@app.get("/")
def get(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/chupep.jpg")
async def chupep():
    return FileResponse("chupep.jpg")


run(app, host="localhost", port=1200)
