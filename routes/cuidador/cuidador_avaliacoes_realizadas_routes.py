from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.avaliacao.avaliacao_model import Avaliacao
from data.avaliacao import avaliacao_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cuidador/avaliacoes-realizadas")
async def listar_avaliacoes_realizadas():
    avaliacoes = avaliacao_repo.obter_realizadas_por_cuidador()
    return templates.TemplateResponse("cuidador/listar_avaliacoes_realizadas.html", {"request": {}, "avaliacoes": avaliacoes})

@router.get("/cuidador/avaliacoes-realizadas/alterar/{id}")
async def get_alterar_avaliacao(id: int):
    avaliacao = avaliacao_repo.obter_por_id(id)
    return templates.TemplateResponse("cuidador/alterar_avaliacao.html", {"request": {}, "avaliacao": avaliacao})

@router.post("/cuidador/avaliacoes-realizadas/alterar")
async def post_alterar_avaliacao(id: int, nota: int, comentario: str):
    if avaliacao_repo.atualizar(id, nota, comentario):
        return templates.TemplateResponse("cuidador/listar_avaliacoes_realizadas.html", {"request": {}, "mensagem": "Avaliação alterada com sucesso!"})
    return templates.TemplateResponse("cuidador/alterar_avaliacao.html", {"request": {}, "mensagem": "Erro ao alterar avaliação."})

@router.get("/cuidador/avaliacoes-realizadas/excluir/{id}")
async def excluir_avaliacao(id: int):
    if avaliacao_repo.excluir(id):
        return templates.TemplateResponse("cuidador/listar_avaliacoes_realizadas.html", {"request": {}, "mensagem": "Avaliação excluída com sucesso!"})
    return templates.TemplateResponse("cuidador/listar_avaliacoes_realizadas.html", {"request": {}, "mensagem": "Erro ao excluir avaliação."})
