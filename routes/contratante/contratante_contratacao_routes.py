from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/contratacoes")
async def get_listar_contratacoes():
    return templates.TemplateResponse("contratante/listar_contratacoes.html", {"request": {}})

@router.get("/contratante/contratacoes/avaliar/{id}")
async def get_avaliar_contratacao(id: int):
    return templates.TemplateResponse("contratante/avaliar_contratacao.html", {"request": {}, "contratacao_id": id})

@router.post("/contratante/contratacoes/avaliar")
async def post_avaliar_contratacao(id: int, nota: int, comentario: str):
    return templates.TemplateResponse("contratante/listar_contratacoes.html", {"request": {}, "mensagem": "Contratação avaliada com sucesso!"})
