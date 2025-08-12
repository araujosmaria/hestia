from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from data.especialidade.especialidade_model import Especialidade
from data.especialidade import especialidade_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cuidador/especializacoes")
async def listar_especializacoes():
    especializacoes = especialidade_repo.obter_por_cuidador()
    return templates.TemplateResponse("cuidador/listar_especializacoes.html", {"request": {}, "especializacoes": especializacoes})

@router.get("/cuidador/especializacoes/cadastrar")
async def get_cadastrar_especializacao():
    return templates.TemplateResponse("cuidador/cadastrar_especializacao.html", {"request": {}})

@router.post("/cuidador/especializacoes/cadastrar")
async def post_cadastrar_especializacao(nome: str):
    if especialidade_repo.inserir(Especialidade(id=0, nome=nome)):
        return templates.TemplateResponse("cuidador/listar_especializacoes.html", {"request": {}, "mensagem": "Especialização cadastrada com sucesso!"})
    return templates.TemplateResponse("cuidador/cadastrar_especializacao.html", {"request": {}, "mensagem": "Erro ao cadastrar especialização."})

@router.get("/cuidador/especializacoes/alterar/{id}")
async def get_alterar_especializacao(id: int):
    especializacao = especialidade_repo.obter_por_id(id)
    return templates.TemplateResponse("cuidador/alterar_especializacao.html", {"request": {}, "especializacao": especializacao})

@router.post("/cuidador/especializacoes/alterar")
async def post_alterar_especializacao(id: int, nome: str):
    if especialidade_repo.atualizar(Especialidade(id=id, nome=nome)):
        return templates.TemplateResponse("cuidador/listar_especializacoes.html", {"request": {}, "mensagem": "Especialização alterada com sucesso!"})
    return templates.TemplateResponse("cuidador/alterar_especializacao.html", {"request": {}, "mensagem": "Erro ao alterar especialização."})

@router.get("/cuidador/especializacoes/excluir/{id}")
async def excluir_especializacao(id: int):
    if especialidade_repo.excluir(id):
        return templates.TemplateResponse("cuidador/listar_especializacoes.html", {"request": {}, "mensagem": "Especialização excluída com sucesso!"})
    return templates.TemplateResponse("cuidador/listar_especializacoes.html", {"request": {}, "mensagem": "Erro ao excluir especialização."})
