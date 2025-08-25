from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# VISUALIZAR AGENDA
# ======================
@router.get("/cuidador/agenda")
async def get_agenda(request: Request):
    # Aqui você buscaria a agenda no banco
    agenda_fake = [
        {"id": 1, "data": "2025-08-25", "hora": "09:00", "status": "Disponível"},
        {"id": 2, "data": "2025-08-26", "hora": "14:00", "status": "Ocupado"},
        {"id": 3, "data": "2025-08-27", "hora": "10:00", "status": "Disponível"}
    ]
    return templates.TemplateResponse(
        "agenda.html",
        {"request": request, "agenda": agenda_fake}
    )

# ======================
# CADASTRO DE DISPONIBILIDADE (GET)
# ======================
@router.get("/cuidador/agenda/cadastrar")
async def get_cadastro_disponibilidade(request: Request):
    return templates.TemplateResponse(
        "cadastro_disponibilidade.html",
        {"request": request}
    )

# ======================
# CADASTRO DE DISPONIBILIDADE (POST)
# ======================
@router.post("/cuidador/agenda/cadastrar")
async def post_cadastro_disponibilidade(
    request: Request,
    data: str = Form(...),
    hora: str = Form(...)
):
    # Aqui entraria a lógica de salvar no banco
    mensagem = f"Disponibilidade cadastrada: {data} às {hora}"
    return templates.TemplateResponse(
        "cadastro_disponibilidade.html",
        {"request": request, "mensagem": mensagem}
    )

# ======================
# REMOÇÃO DE DISPONIBILIDADE (GET)
# ======================
@router.get("/cuidador/agenda/remover/{id}")
async def get_remocao_disponibilidade(request: Request, id: int):
    disponibilidade_fake = {"id": id, "data": "2025-08-25", "hora": "09:00"}
    return templates.TemplateResponse(
        "remoção_disponibilidade.html",
        {"request": request, "disponibilidade": disponibilidade_fake}
    )

# ======================
# REMOÇÃO DE DISPONIBILIDADE (POST)
# ======================
@router.post("/cuidador/agenda/remover")
async def post_remocao_disponibilidade(
    request: Request,
    id: int = Form(...)
):
    # Aqui entraria a lógica de remover do banco
    mensagem = f"Disponibilidade {id} removida com sucesso!"
    return templates.TemplateResponse(
        "remoção_disponibilidade.html",
        {"request": request, "mensagem": mensagem}
    )