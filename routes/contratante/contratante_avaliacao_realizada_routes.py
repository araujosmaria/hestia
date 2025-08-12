from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/avaliacoes-realizadas")
async def get_listar_avaliacoes_realizadas():
    return templates.TemplateResponse("contratante/listar_avaliacoes_realizadas.html", {"request": {}})

@router.get("/contratante/avaliacoes-realizadas/alterar/{id}")
async def get_alterar_avaliacao(id: int):
    return templates.TemplateResponse("contratante/alterar_avaliacao.html", {"request": {}, "avaliacao_id": id})

@router.post("/contratante/avaliacoes-realizadas/alterar")
async def post_alterar_avaliacao(id: int, nota: int, comentario: str):
    return templates.TemplateResponse("contratante/listar_avaliacoes_realizadas.html", {"request": {}, "mensagem": "Avaliação alterada com sucesso!"})

@router.get("/contratante/avaliacoes-realizadas/excluir/{id}")
async def get_excluir_avaliacao(id: int):
    return templates.TemplateResponse("contratante/listar_avaliacoes_realizadas.html", {"request": {}, "mensagem": "Avaliação excluída com sucesso!"})
