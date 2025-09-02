from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR AVALIAÇÕES
# ======================
@router.get("/admin/avaliacoes")
async def get_listar_avaliacoes(request: Request):
    avaliacoes_fake = [
        {"id": 1, "usuario": "João", "nota": 5, "comentario": "Excelente!"},
        {"id": 2, "usuario": "Maria", "nota": 3, "comentario": "Bom, mas pode melhorar."}
    ]
    return templates.TemplateResponse(
        "administrador/avaliacoes.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )


# ======================
# MODERAR AVALIAÇÃO (GET)
# ======================
@router.get("/admin/avaliacoes/moderar/{id}")
async def get_moderar_avaliacao(request: Request, id: int):
    avaliacao_fake = {"id": id, "usuario": "João", "nota": 5, "comentario": "Excelente!"}
    return templates.TemplateResponse(
        "administrador/moderar_avaliacao.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )

# ======================
# MODERAR AVALIAÇÃO (POST)
# ======================
@router.post("/admin/avaliacoes/moderar")
async def post_moderar_avaliacao(
    request: Request,
    id: int = Form(...),
    aprovado: bool = Form(...)
):

    return templates.TemplateResponse(
        "administrador/avaliacoes.html",
        {"request": request, "mensagem": f"Avaliação {id} moderada com sucesso!"}
    )
