from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/avaliacoes-recebidas")
async def get_listar_avaliacoes_recebidas():
    return templates.TemplateResponse("contratante/listar_avaliacoes_recebidas.html", {"request": {}})
