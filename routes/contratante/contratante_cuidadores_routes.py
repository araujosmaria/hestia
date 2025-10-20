from fastapi import APIRouter, Request
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from util.template_util import criar_templates

router = APIRouter()
templates = criar_templates("templates")

# ======================
# LISTAR CUIDADORES
# ======================
@router.get("/contratante/cuidadores")
async def get_listar_cuidadores(request: Request):
    # Aqui você buscaria os cuidadores no banco
    cuidadores_fake = [
        {"id": 1, "nome": "Ana", "especialidade": "Cuidados com idosos", "nota": 5},
        {"id": 2, "nome": "Carlos", "especialidade": "Enfermagem domiciliar", "nota": 4},
        {"id": 3, "nome": "Fernanda", "especialidade": "Acompanhamento hospitalar", "nota": 5},
    ]
    return templates.TemplateResponse(
        "contratante/perfil_cuidadores.html",
        {"request": request, "cuidadores": cuidadores_fake}
    )

# ======================
# PERFIL DO CUIDADOR
# ======================
@router.get("/contratante/cuidadores/{id}")
async def get_perfil_cuidador(request: Request, id: int):
    # Aqui você buscaria os detalhes do cuidador no banco
    cuidador_fake = {
        "id": id,
        "nome": "Ana",
        "especialidade": "Cuidados com idosos",
        "nota": 5,
        "descricao": "Mais de 10 anos de experiência cuidando de idosos com carinho e paciência."
    }
    return templates.TemplateResponse(
        "contratante/perfil_cuidadores.html",
        {"request": request, "cuidador": cuidador_fake}
    )