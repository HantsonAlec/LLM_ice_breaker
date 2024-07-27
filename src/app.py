import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.ice_breaker import ice_breaker_with

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static/css", StaticFiles(directory="css"), name="static")


class IceBreakerResponse(BaseModel):
    summary: str
    facts: list[str]
    profile_pic_url: str


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/process")
def process(name: str = Form(...)) -> IceBreakerResponse:
    person_summary, profile_pic = ice_breaker_with(name=name)
    return IceBreakerResponse(
        summary=person_summary.summary,
        facts=person_summary.facts,
        profile_pic_url=profile_pic,
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
