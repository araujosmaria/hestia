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

@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


@router.get("/redefinir-senha")
async def get_redefinir_senha(request: Request):
    return templates.TemplateResponse("redefinir_senha.html", {"request": request})