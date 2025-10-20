from fastapi import APIRouter, Request
from util.template_util import criar_templates
from fastapi.responses import HTMLResponse
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger

router = APIRouter()
templates = criar_templates("templates")

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
    ) 
