from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR AVALIAÇÕES RECEBIDAS
# ======================
@router.get("/contratante/avaliacoes_recebidas")
async def get_avaliacoes_recebidas(request: Request):
    avaliacoes_fake = [
        {"id": 1, "cuidador": "Ana", "nota": 5, "comentario": "Contratante muito atencioso e organizado."},
        {"id": 2, "cuidador": "Carlos", "nota": 4, "comentario": "Boa experiência, tudo ocorreu bem."},
        {"id": 3, "cuidador": "Fernanda", "nota": 3, "comentario": "Poderia ter comunicado melhor alguns detalhes."}
    ]
    return templates.TemplateResponse(
        "contratante/avaliacoes_recebidas.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )

# ======================
# DETALHE DE UMA AVALIAÇÃO
# ======================
@router.get("/contratante/avaliacoes_recebidas/{id}")
async def get_detalhe_avaliacao_recebida(request: Request, id: int):
    avaliacao_fake = {
        "id": id,
        "cuidador": "Ana",
        "nota": 5,
        "comentario": "Contratante muito atencioso e organizado.",
        "data": "20/08/2025"
    }
    return templates.TemplateResponse(
        "contratante/avaliacoes_recebidas.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )
