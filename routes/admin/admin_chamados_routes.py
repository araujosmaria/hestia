from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Listar todos os chamados
@router.get("/admin/chamados")
async def get_listar_chamados():
    return templates.TemplateResponse("admin/chamados.html", {"request": {}})

# Página para responder um chamado específico
@router.get("/admin/chamados/responder/{id}")
async def get_responder_chamado(id: int):
    return templates.TemplateResponse("admin/responder_chamado.html", {"request": {}, "chamado_id": id})

# Submeter a resposta de um chamado
@router.post("/admin/chamados/responder")
async def post_responder_chamado(id: int, resposta: str):
    return templates.TemplateResponse("admin/chamados.html", {"request": {}, "mensagem": "Chamado respondido com sucesso!"})
