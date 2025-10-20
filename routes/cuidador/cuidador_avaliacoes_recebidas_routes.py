from fastapi import APIRouter, Request
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from util.template_util import criar_templates

router = APIRouter()
templates = criar_templates("templates")

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
        "cuidador/avaliacoes_recebidas.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )
