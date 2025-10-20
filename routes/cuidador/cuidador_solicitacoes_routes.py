from fastapi import APIRouter, Request
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from util.template_util import criar_templates

router = APIRouter()
templates = criar_templates("templates")

# ======================
# LISTAR SOLICITAÇÕES DE CONTRATAÇÃO
# ======================
@router.get("/cuidador/solicitacoes_contratacao")
async def listar_solicitacoes_contratacao(request: Request):
    solicitacoes = [
        {"id": 1, "nome": "Solicitação 1", "status": "Pendente"},
        {"id": 2, "nome": "Solicitação 2", "status": "Confirmada"},
        {"id": 3, "nome": "Solicitação 3", "status": "Pendente"}
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
    # Dados diferentes por ID
    solicitacoes_db = {
        1: {
            "id": 1,
            "nome": "Solicitação 1",
            "status": "Pendente",
            "data": "2025-08-27",
            "hora": "14:00h",
            "servico": "Cuidado com idoso",
            "observacoes": "Paciente prefere horário da tarde."
        },
        2: {
            "id": 2,
            "nome": "Solicitação 2",
            "status": "Confirmada",
            "data": "2025-09-01",
            "hora": "09:30h",
            "servico": "Acompanhamento em consulta",
            "observacoes": "Paciente com dificuldade de locomoção. Confirmar transporte."
        },
        3: {
            "id": 3,
            "nome": "Solicitação 3",
            "status": "Pendente",
            "data": "2025-09-05",
            "hora": "15:45h",
            "servico": "Administração de medicamentos",
            "observacoes": "Atenção aos horários de antibióticos."
        }
    }

    solicitacao = solicitacoes_db.get(solicitacao_id)

    if not solicitacao:
        return templates.TemplateResponse(
            "cuidador/erro.html",
            {"request": request, "mensagem": f"Solicitação {solicitacao_id} não encontrada."}
        )

    return templates.TemplateResponse(
        "cuidador/detalhes_solicitacao.html",
        {"request": request, "solicitacao": solicitacao}
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
