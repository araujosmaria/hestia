from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter() 

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_login(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login")
async def get_login(request: Request): 
    return templates.TemplateResponse("login.html", {"request": request})