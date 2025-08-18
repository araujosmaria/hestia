# from fastapi import APIRouter
# from fastapi.templating import Jinja2Templates
# from data.solicitacao import solicitacao_repo

# router = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @router.get("/cuidador/solicitacoes")
# async def listar_solicitacoes():
#     solicitacoes = solicitacao_repo.obter_por_cuidador()
#     return templates.TemplateResponse("cuidador/listar_solicitacoes.html", {"request": {}, "solicitacoes": solicitacoes})

# @router.get("/cuidador/solicitacoes/{id}")
# async def detalhes_solicitacao(id: int):
#     solicitacao = solicitacao_repo.obter_por_id(id)
#     return templates.TemplateResponse("cuidador/detalhes_solicitacao.html", {"request": {}, "solicitacao": solicitacao})
