from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/administradores/cadastrar")
async def get_cadastrar_administrador():
    return templates.TemplateResponse("admin/cadastrar_administrador.html", {"request": {}})

@router.post("/admin/administradores/cadastrar")
async def post_cadastrar_administrador(nome: str, email: str, senha: str):
    return templates.TemplateResponse("admin/listar_administradores.html", {"request": {}, "mensagem": "Administrador cadastrado com sucesso!"})

@router.get("/admin/administradores/excluir/{id}")
async def get_excluir_administrador(id: int):
    return templates.TemplateResponse("admin/listar_administradores.html", {"request": {}, "mensagem": "Administrador excluído com sucesso!"})
