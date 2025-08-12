from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/relatorios")
async def get_listar_relatorios():
    return templates.TemplateResponse("admin/listar_relatorios.html", {"request": {}})
