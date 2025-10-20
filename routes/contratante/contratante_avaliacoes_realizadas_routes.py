from fastapi import APIRouter, Request, Form
from util.template_util import criar_templates
from fastapi.responses import RedirectResponse
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger

router = APIRouter()
templates = criar_templates("templates")

# ==========================
# LISTAR AVALIAÇÕES REALIZADAS
# ==========================
@router.get("/contratante/avaliacoes_realizadas")
async def get_avaliacoes_realizadas(request: Request):
    avaliacoes_fake = [
        {"id": 1, "cuidador": "Ana", "nota": 5, "comentario": "Ótimo trabalho!"},
        {"id": 2, "cuidador": "Carlos", "nota": 4, "comentario": "Boa experiência."},
        {"id": 3, "cuidador": "Fernanda", "nota": 3, "comentario": "Poderia melhorar a comunicação."}
    ]
    return templates.TemplateResponse(
        "contratante/avaliacoes_realizadas.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )

# ==========================
# ALTERAR AVALIAÇÃO
# ==========================
@router.get("/contratante/alterar_avaliacao/{id}")
async def get_alterar_avaliacao(request: Request, id: int):
    avaliacao_fake = {
        "id": id,
        "nota": 4,
        "comentario": "Boa experiência, mas poderia melhorar a comunicação.",
        "cuidador": "Ana"
    }
    return templates.TemplateResponse(
        "contratante/alterar_avaliacao.html",
        {"request": request, "avaliacao": avaliacao_fake}
    )

@router.post("/contratante/alterar_avaliacao")
async def post_alterar_avaliacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):

    mensagem = f"Avaliação {id} atualizada com sucesso!"
    avaliacao_fake = {
        "id": id,
        "nota": nota,
        "comentario": comentario,
        "cuidador": "Ana"
    }
    return templates.TemplateResponse(
        "contratante/alterar_avaliacao.html",
        {"request": request, "avaliacao": avaliacao_fake, "mensagem": mensagem}
    )

# ==========================
# EXCLUIR AVALIAÇÃO
# ==========================
@router.get("/contratante/avaliacoes_realizadas/excluir")
async def get_excluir_avaliacao(request: Request, id: int):
    return RedirectResponse(url="/contratante/avaliacoes_realizadas", status_code=303)
