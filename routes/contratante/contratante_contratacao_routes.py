from typing import Optional
from fastapi import APIRouter, Request, Form
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from util.template_util import criar_templates

router = APIRouter()
templates = criar_templates("templates")

# ======================
# SOLICITAR CONTRATAÇÃO (GET)
# ======================
@router.get("/contratante/solicitar-contratacao")
async def get_solicitar_contratacao(request: Request, cuidador_id: Optional[int] = None):
    return templates.TemplateResponse(
        "contratante/solicitar_contratacao.html",
        {"request": request, "cuidador_id": cuidador_id}
    )

# ======================
# SOLICITAR CONTRATAÇÃO (POST)
# ======================
@router.post("/contratante/solicitar-contratacao")
async def post_solicitar_contratacao(
    request: Request,
    cuidador_id: int = Form(...),
    nome_projeto: str = Form(...),
    descricao: str = Form(...)
):
    mensagem = f"Solicitação do projeto '{nome_projeto}' enviada com sucesso para o cuidador {cuidador_id}!"
    return templates.TemplateResponse(
        "contratante/solicitar_contratacao.html",
        {"request": request, "mensagem": mensagem, "cuidador_id": cuidador_id}
    )


# ======================
# CONTRATAÇÕES REALIZADAS
# ======================
@router.get("/contratante/contratacoes-realizadas")
async def contratacoes_realizadas(request: Request):
    contratacoes_fake = [
        {"id": 1, "projeto": "Website", "contratado": "João", "status": "Concluído", "periodo": "01/08 a 10/08"},
        {"id": 2, "projeto": "App Mobile", "contratado": "Maria", "status": "Em andamento", "periodo": "05/08 a 20/08"}
    ]
    return templates.TemplateResponse(
        "contratante/contratacoes_realizadas.html",
        {"request": request, "contratacoes": contratacoes_fake}
    )

# ======================
# AVALIAR CONTRATAÇÃO (GET)
# ======================
@router.get("/contratante/avaliar_contratacao/{id}")
async def get_avaliar_contratacao(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/avaliar_contratacao.html",
        {"request": request, "contratacao_id": id}
    )

# ======================
# AVALIAR CONTRATAÇÃO (POST)
# ======================
@router.post("/contratante/avaliar_contratacao")
async def post_avaliar_contratacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    mensagem = f"Avaliação da contratação {id} enviada com sucesso!"
    return templates.TemplateResponse(
        "contratante/avaliar_contratacao.html",
        {"request": request, "contratacao_id": id, "mensagem": mensagem}
    )