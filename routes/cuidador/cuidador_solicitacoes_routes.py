from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR SOLICITAÇÕES DE CONTRATAÇÃO
# ======================
@router.get("/cuidador/solicitacoes_contratacao")
async def listar_solicitacoes_contratacao(request: Request):
    solicitacoes = [
        {"id": 1, "nome": "Solicitação 1", "status": "Pendente"},
        {"id": 2, "nome": "Solicitação 2", "status": "Confirmada"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitacoes_contratacao.html",   # tela de contratação
        {"request": request, "solicitacoes": solicitacoes}
    )


# ======================
# DETALHES DE SOLICITAÇÃO
# ======================
@router.get("/cuidador/solicitacoes/{solicitacao_id}")
async def get_detalhes_solicitacao(request: Request, solicitacao_id: int):
    # Aqui você buscaria os detalhes no banco pelo ID
    solicitacao_fake = {
        "id": solicitacao_id,
        "nome": f"Solicitação {solicitacao_id}",
        "status": "Pendente" if solicitacao_id % 2 != 0 else "Confirmada",
        "data": "2025-08-27",
        "hora": "14:00",
        "servico": "Cuidado com idoso",
        "observacoes": "Paciente prefere horário da tarde."
    }
    return templates.TemplateResponse(
        "cuidador/detalhes_solicitacao.html",
        {"request": request, "solicitacao": solicitacao_fake}
    )

# ======================
# LISTAR SOLICITAÇÕES DE VERIFICAÇÃO
# ======================
@router.get("/cuidador/solicitacao_verificacao")
async def listar_solicitacao_verificacao(request: Request):
    verificacoes = [
        {"id": 1, "descricao": "Verificação pendente"},
        {"id": 2, "descricao": "Verificação concluída"}
    ]
    return templates.TemplateResponse(
        "cuidador/solicitacao_verificacao.html",   # tela de verificações
        {"request": request, "verificacoes": verificacoes}
    )

# ======================
# DETALHE DE UMA SOLICITAÇÃO DE VERIFICAÇÃO
# ======================
@router.get("/cuidador/solicitacoes_verificacao/{id}")
async def detalhes_solicitacao_verificacao(request: Request, id: int):
    verificacao = {
        "id": id,
        "descricao": f"Detalhes da verificação {id}"
    }
    return templates.TemplateResponse(
        "cuidador/detalhes_verificacao.html",   # tela de detalhes da verificação
        {"request": request, "verificacao": verificacao}
    )
