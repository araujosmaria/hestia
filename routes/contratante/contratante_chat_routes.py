from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/chats")
async def get_listar_chats():
    return templates.TemplateResponse("contratante/listar_chats.html", {"request": {}})
