from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/relatorios", response_class=HTMLResponse)
async def get_listar_relatorios(request: Request):
    relatorios = [
        {"id": 1, "nome": "Maria Silva", "especialidade": "Cuidados com Alzheimer", "avaliacao": 4.8, "disponibilidade": "Segunda a Sexta"},
        {"id": 2, "nome": "João Pereira", "especialidade": "Cuidados gerais", "avaliacao": 4.5, "disponibilidade": "Fins de semana"},
        {"id": 3, "nome": "Ana Costa", "especialidade": "Cuidados com mobilidade reduzida", "avaliacao": 4.9, "disponibilidade": "Segunda a Domingo"},
    ]
    return templates.TemplateResponse(
        "administrador/relatorios.html",
        {"request": request, "relatorios": relatorios}
    )  # <-- SEM vírgula aqui
