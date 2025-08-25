from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ===========================
# SOLICITAR CONTRATAÇÃO
# ===========================
@router.get("/contratante/solicitar_contratacao")
async def get_solicitar_contratacao(request: Request):
    return templates.TemplateResponse(
        "contratante/solicitar_contratacao.html",
        {"request": request}
    )

@router.post("/contratante/solicitar_contratacao")
async def post_solicitar_contratacao(
    request: Request,
    cuidador_id: int = Form(...),
    data_inicio: str = Form(...),
    data_fim: str = Form(...),
    observacoes: str = Form(...)
):
    # lógica para salvar solicitação
    mensagem = "Solicitação de contratação enviada com sucesso!"
    return templates.TemplateResponse(
        "contratante/solicitar_contratacao.html",
        {"request": request, "mensagem": mensagem}
    )

# ===========================
# AVALIAÇÃO DA CONTRATAÇÃO
# ===========================
@router.get("/contratante/avaliar_contratacao/{id}")
async def get_avaliar_contratacao(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/avaliacao_contratacao.html",
        {"request": request, "contratacao_id": id}
    )

@router.post("/contratante/avaliar_contratacao")
async def post_avaliar_contratacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    # lógica de avaliação
    return templates.TemplateResponse(
        "contratante/avaliacao_contratacao.html",
        {"request": request, "mensagem": f"Avaliação da contratação {id} enviada com sucesso!"}
    )
# ===========================
# ALTERAR AVALIAÇÃO DA CONTRATAÇÃO
# ===========================
@router.get("/contratante/alterar_avaliacao/{id}")
async def get_alterar_avaliacao(request: Request, id: int):
    # Aqui você buscaria os dados da avaliação no banco para preencher o formulário
    avaliacao_fake = {
        "id": id,
        "nota": 4,
        "comentario": "Boa experiência, mas poderia melhorar a comunicação."
    }
    return templates.TemplateResponse(
        "contratante/alterar_avaliacao.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )

@router.post("/contratante/alterar_avaliacao")
async def post_alterar_avaliacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    # Aqui entraria a lógica para atualizar a avaliação no banco
    mensagem = f"Avaliação {id} atualizada com sucesso!"
    return templates.TemplateResponse(
        "contratante/alterar_avaliacao.html",
        {"request": request, "mensagem": mensagem}
    )


# ===========================
# CONTRATAÇÕES REALIZADAS
# ===========================
@router.get("/contratante/contratacoes_realizadas")
async def get_contratacoes_realizadas(request: Request):
    contratacoes_fake = [
        {"id": 1, "cuidador": "Carlos", "periodo": "01/09 - 10/09", "status": "Finalizada"},
        {"id": 2, "cuidador": "Ana", "periodo": "15/09 - 20/09", "status": "Em andamento"}
    ]
    return templates.TemplateResponse(
        "contratante/contratacoes_realizadas.html",
        {"request": request, "contratacoes": contratacoes_fake}
    )
