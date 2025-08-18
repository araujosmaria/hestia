# from fastapi import APIRouter
# from fastapi.templating import Jinja2Templates
# from data.contratacao import contratacao_repo

# router = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @router.get("/cuidador/contratacoes-recebidas")
# async def listar_contratacoes_recebidas():
#     contratacoes = contratacao_repo.obter_por_cuidador()
#     return templates.TemplateResponse("cuidador/listar_contratacoes_recebidas.html", {"request": {}, "contratacoes": contratacoes})

# @router.get("/cuidador/contratacoes-recebidas/avaliar/{id}")
# async def get_avaliar_contratacao(id: int):
#     contratacao = contratacao_repo.obter_por_id(id)
#     return templates.TemplateResponse("cuidador/avaliar_contratacao.html", {"request": {}, "contratacao": contratacao})

# @router.post("/cuidador/contratacoes-recebidas/avaliar")
# async def post_avaliar_contratacao(id: int, nota: int, comentario: str):
#     if contratacao_repo.avaliar(id, nota, comentario):
#         return templates.TemplateResponse("cuidador/listar_contratacoes_recebidas.html", {"request": {}, "mensagem": "Avaliação registrada com sucesso!"})
#     return templates.TemplateResponse("cuidador/avaliar_contratacao.html", {"request": {}, "mensagem": "Erro ao registrar avaliação."})
