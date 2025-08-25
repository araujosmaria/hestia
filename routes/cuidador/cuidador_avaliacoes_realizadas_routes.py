from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR AVALIAÇÕES REALIZADAS
# ======================
@router.get("/cuidador/avaliacoes_realizadas")
async def get_avaliacoes_realizadas(request: Request):
    # Aqui você buscaria no banco as avaliações feitas pelo cuidador
    avaliacoes_fake = [
        {"id": 1, "contratante": "João", "nota": 5, "comentario": "Muito bom trabalhar com ele."},
        {"id": 2, "contratante": "Maria", "nota": 4, "comentario": "Experiência positiva."}
    ]
    return templates.TemplateResponse(
        "avaliacoes_realizadas.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )

# ======================
# ALTERAR AVALIAÇÃO (GET)
# ======================
@router.get("/cuidador/avaliacoes_realizadas/alterar/{id}")
async def get_alterar_avaliacao(request: Request, id: int):
    avaliacao_fake = {"id": id, "contratante": "João", "nota": 5, "comentario": "Muito bom trabalhar com ele."}
    return templates.TemplateResponse(
        "alteração_avaliação.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )

# ======================
# ALTERAR AVALIAÇÃO (POST)
# ======================
@router.post("/cuidador/avaliacoes_realizadas/alterar")
async def post_alterar_avaliacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    # Aqui entraria a lógica para atualizar no banco
    mensagem = f"Avaliação {id} alterada com sucesso!"
    return templates.TemplateResponse(
        "avaliacoes_realizadas.html",
        {"request": request, "mensagem": mensagem}
    )

# ======================
# EXCLUIR AVALIAÇÃO (GET)
# ======================
@router.get("/cuidador/avaliacoes_realizadas/excluir/{id}")
async def get_excluir_avaliacao(request: Request, id: int):
    avaliacao_fake = {"id": id, "contratante": "João", "nota": 5, "comentario": "Muito bom trabalhar com ele."}
    return templates.TemplateResponse(
        "exclusão_avaliação.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )

# ======================
# EXCLUIR AVALIAÇÃO (POST)
# ======================
@router.post("/cuidador/avaliacoes_realizadas/excluir")
async def post_excluir_avaliacao(
    request: Request,
    id: int = Form(...)
):
    # Aqui entraria a lógica para excluir no banco
    mensagem = f"Avaliação {id} excluída com sucesso!"
    return templates.TemplateResponse(
        "avaliacoes_realizadas.html",
        {"request": request, "mensagem": mensagem}
    )