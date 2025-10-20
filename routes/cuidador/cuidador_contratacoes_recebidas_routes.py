from fastapi import APIRouter, Request, Form
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from util.template_util import criar_templates

router = APIRouter()
templates = criar_templates("templates")

# ======================
# LISTAR CONTRATAÇÕES RECEBIDAS
# ======================
@router.get("/cuidador/contratacoes")
async def get_contratacoes_recebidas(request: Request):
    # Aqui você buscaria as contratações no banco
    contratacoes_fake = [
        {"id": 1, "cliente": "Pedro", "servico": "Acompanhamento", "status": "Pendente"},
        {"id": 2, "cliente": "Ana", "servico": "Cuidados Noturnos", "status": "Confirmado"}
    ]
    return templates.TemplateResponse(
        "contratações_recebidas.html",
        {"request": request, "contratacoes": contratacoes_fake}
    )

# ======================
# AVALIAR UMA CONTRATAÇÃO (GET)
# ======================
@router.get("/cuidador/contratacoes/avaliar/{id}")
async def get_avaliar_contratacao(request: Request, id: int):
    contratacao_fake = {"id": id, "cliente": "Pedro", "servico": "Acompanhamento"}
    return templates.TemplateResponse(
        "avaliação_contratação.html",
        {"request": request, "contratacao": contratacao_fake}
    )

# ======================
# AVALIAR UMA CONTRATAÇÃO (POST)
# ======================
@router.post("/cuidador/contratacoes/avaliar")
async def post_avaliar_contratacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    # Aqui você salvaria a avaliação no banco
    return templates.TemplateResponse(
        "contratações_recebidas.html",
        {"request": request, "mensagem": f"Avaliação da contratação {id} salva com sucesso!"}
    )