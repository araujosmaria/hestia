from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/avaliacoes")
async def get_listar_avaliacoes():
    return templates.TemplateResponse("admin/listar_avaliacoes.html", {"request": {}})

@router.get("/admin/avaliacoes/moderar/{id}")
async def get_moderar_avaliacao(id: int):
    return templates.TemplateResponse("admin/moderar_avaliacao.html", {"request": {}, "avaliacao_id": id})

@router.post("/admin/avaliacoes/moderar")
async def post_moderar_avaliacao(id: int, aprovado: bool):
    return templates.TemplateResponse("admin/listar_avaliacoes.html", {"request": {}, "mensagem": "Avaliação moderada com sucesso!"})
