from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.avaliacao import avaliacao_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cuidador/avaliacoes-recebidas")
async def listar_avaliacoes_recebidas():
    avaliacoes = avaliacao_repo.obter_recebidas_por_cuidador()
    return templates.TemplateResponse("cuidador/listar_avaliacoes_recebidas.html", {"request": {}, "avaliacoes": avaliacoes})
