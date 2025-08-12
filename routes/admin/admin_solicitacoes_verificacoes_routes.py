from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/solicitacoes")
async def get_listar_solicitacoes():
    return templates.TemplateResponse("admin/listar_solicitacoes.html", {"request": {}})

@router.get("/admin/solicitacoes/analisar/{id}")
async def get_analisar_solicitacao(id: int):
    return templates.TemplateResponse("admin/analisar_solicitacao.html", {"request": {}, "solicitacao_id": id})

@router.post("/admin/solicitacoes/analisar")
async def post_analisar_solicitacao(id: int, aprovado: bool):
    return templates.TemplateResponse("admin/listar_solicitacoes.html", {"request": {}, "mensagem": "Solicitação analisada com sucesso!"})
