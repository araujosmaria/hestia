from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.chat import chat_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cuidador/chats")
async def listar_chats():
    chats = chat_repo.obter_por_cuidador()
    return templates.TemplateResponse("cuidador/listar_chats.html", {"request": {}, "chats": chats})

@router.get("/cuidador/chats/{id}")
async def chat_com_contratante(id: int):
    mensagens = chat_repo.obter_mensagens(id)
    return templates.TemplateResponse("cuidador/chat_contratante.html", {"request": {}, "mensagens": mensagens})
