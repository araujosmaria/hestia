from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR SOLICITAÇÕES DE CONTRATAÇÃO
# ======================
@router.get("/cuidador/solicitacoes_contratacao")
async def listar_solicitacoes_contratacao(request: Request):
    # Aqui você pode chamar o repo para obter dados reais
    solicitacoes = [
        {"id": 1, "nome": "Solicitação 1", "status": "Pendente"},
        {"id": 2, "nome": "Solicitação 2", "status": "Confirmada"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitacoes_contratacao.html",
        {"request": request, "solicitacoes": solicitacoes}
    )

# ======================
# VISUALIZAR DETALHES DE UMA SOLICITAÇÃO
# ======================
@router.get("/cuidador/cuidador_solicitacoes/detalhes")
async def detalhes_solicitacao(request: Request):
    # Exemplo: busca a solicitação "mais recente" ou do cuidador logado
    solicitacao = {"id": 1, "nome": "Solicitação 1", "descricao": "Detalhes da solicitação"}
    
    return templates.TemplateResponse(
        "cuidador/detalhes_solicitacao.html",
        {"request": request, "solicitacao": solicitacao}
    )

# ======================
# VISUALIZAR SOLICITAÇÕES DE VERIFICAÇÃO
# ======================
@router.get("/cuidador/solicitacoes/verificacao")
async def solicitacao_verificacao(request: Request):
    verificacoes = [
        {"id": 1, "descricao": "Verificação pendente"},
        {"id": 2, "descricao": "Verificação concluída"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitacao_verificacao.html",
        {"request": request, "verificacoes": verificacoes}
    )
