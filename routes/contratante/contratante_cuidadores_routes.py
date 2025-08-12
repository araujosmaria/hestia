from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/cuidadores")
async def get_listar_cuidadores():
    return templates.TemplateResponse("contratante/listar_cuidadores.html", {"request": {}})

@router.get("/contratante/cuidadores/detalhes/{id}")
async def get_detalhes_cuidador(id: int):
    return templates.TemplateResponse("contratante/detalhes_cuidador.html", {"request": {}, "cuidador_id": id})

@router.get("/contratante/cuidadores/chat/{id}")
async def get_chat_cuidador(id: int):
    return templates.TemplateResponse("contratante/chat_cuidador.html", {"request": {}, "cuidador_id": id})

@router.post("/contratante/cuidadores/solicitar-contratacao")
async def post_solicitar_contratacao(cuidador_id: int, detalhes: str):
    return templates.TemplateResponse("contratante/listar_cuidadores.html", {"request": {}, "mensagem": "Solicitação de contratação enviada com sucesso!"})
