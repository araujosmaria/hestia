from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR AVALIAÇÕES RECEBIDAS
# ======================
@router.get("/cuidador/avaliacoes_recebidas")
async def get_avaliacoes_recebidas(request: Request):
    # Aqui você buscaria no banco as avaliações recebidas pelo cuidador
    avaliacoes_fake = [
        {"id": 1, "contratante": "Carlos", "nota": 5, "comentario": "Excelente cuidador, muito atencioso!"},
        {"id": 2, "contratante": "Ana", "nota": 4, "comentario": "Bom trabalho, recomendo."},
        {"id": 3, "contratante": "Marcos", "nota": 3, "comentario": "Poderia melhorar a pontualidade."}
    ]
    return templates.TemplateResponse(
        "avaliacoes_recebidas.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )
