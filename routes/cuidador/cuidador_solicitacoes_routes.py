from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota para listar solicitações de contratação
@router.get("/cuidador/solicitacoes/contratacao")
async def listar_solicitacoes_contratacao(request: Request):
    # Aqui você pode chamar o repo para obter dados reais
    solicitacoes = [
        {"id": 1, "nome": "Solicitação 1", "status": "Pendente"},
        {"id": 2, "nome": "Solicitação 2", "status": "Confirmada"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitações_contratação.html",
        {"request": request, "solicitacoes": solicitacoes}
    )

# Rota para visualizar detalhes de uma solicitação
@router.get("/cuidador/solicitacoes/detalhes/{id}")
async def detalhes_solicitacao(request: Request, id: int):
    # Obter solicitação pelo ID (simulação)
    solicitacao = {"id": id, "nome": f"Solicitação {id}", "descricao": "Detalhes da solicitação"}
    return templates.TemplateResponse(
        "cuidador/detalhes_solicitação.html",
        {"request": request, "solicitacao": solicitacao}
    )

# Rota para visualizar solicitação de verificação
@router.get("/cuidador/solicitacoes/verificacao")
async def solicitacao_verificacao(request: Request):
    verificacoes = [
        {"id": 1, "descricao": "Verificação pendente"},
        {"id": 2, "descricao": "Verificação concluída"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitação_verificação.html",
        {"request": request, "verificacoes": verificacoes}
    )
