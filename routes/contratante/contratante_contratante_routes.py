from fastapi import APIRouter, Depends, Request, UploadFile, File, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pytest import Session
from data.cliente import cliente_repo
import os
import secrets
from io import BytesIO
from PIL import Image, ImageDraw
from util.auth_decorator import obter_usuario_logado
from fastapi.requests import Request


router = APIRouter()
# ajuste para sua função real

templates = Jinja2Templates(directory="templates")

# @router.get("/contratante/home_contratante")
# async def get_home_contratante(request: Request, mensagem: str | None = None):
#     # Pega o usuário da sessão
#     user = obter_usuario_logado(request)
#     print("Sessão atual:", request.session)  # debug
#     print("Usuário logado:", user.id)           # debug

#     # Se não tiver usuário logado, redireciona para login
#     if not user:
#         return RedirectResponse("/login", status_code=303)

#     # Converte dataclass/objeto para dict caso necessário
#     if not isinstance(user, dict):
#         user_dict = user.__dict__  # funciona para dataclasses
#     else:
#         user_dict = user

#     # Renderiza o template garantindo que user sempre exista
#     return templates.TemplateResponse(
#         "contratante/home_contratante.html",
#         {
#             "request": request,
#             "mensagem": mensagem or "",
#             "user": user_dict
#         }
#     )

@router.get("/contratante/home_contratante")
async def get_home_contratante(request: Request, mensagem: str | None = None):
    user = obter_usuario_logado(request)
    print("Sessão atual:", request.session)
    print("Usuário logado:", user.id if user else "Nenhum")

    if not user:
        return RedirectResponse("/login", status_code=303)

    user_dict = user.__dict__ if not isinstance(user, dict) else user
    return templates.TemplateResponse(
        "contratante/home_contratante.html",
        {"request": request, "mensagem": mensagem or "", "user": user_dict}
    )



# ======================
# ALTERAR SENHA CONTRATANTE
# ======================
@router.get("/contratante/alterar_senha/{id}")
async def get_alterar_senha(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/alterar_senha.html",
        {"request": request, "id": id}
    )

# ======================
# POST: processar alteração de senha
# ======================
@router.post("/contratante/alterar_senha")
async def post_alterar_senha(
    request: Request,
    id: int = Form(...),
    senha_atual: str = Form(...),
    nova_senha: str = Form(...),
    confirmar_senha: str = Form(...)
):
    if nova_senha != confirmar_senha:
        return templates.TemplateResponse(
            "contratante/alterar_senha.html",
            {
                "request": request,
                "id": id,
                "erro": "As senhas não coincidem."
            }
        )

    # Aqui faria a atualização da senha no banco de dados...

    return RedirectResponse(
        url="/contratante/home_contratante?mensagem=Senha+alterada+com+sucesso",
        status_code=303
    )
# ======================
# SOLICITAR VERIFICAÇÃO (GET)
# ======================
@router.get("/contratante/solicitar_verificacao/{id}")
async def get_solicitar_verificacao(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/solicitar_verificacao.html",
        {"request": request, "id": id}
    )

# ======================
# SOLICITAR VERIFICAÇÃO (POST)
# ======================
@router.post("/contratante/solicitar_verificacao/{id}")
async def post_solicitar_verificacao(
    request: Request,
    id: int,
    documento: str = Form(...)
):
    mensagem = "Verificação solicitada com sucesso!"
    return templates.TemplateResponse(
        "contratante/solicitar_verificacao.html",
        {"request": request, "id": id, "mensagem": mensagem}
    )


# ======================
# CHAMADOS (Abrir + Listar)
# ======================

# lista fake só para simular o banco de dados
chamados_fake = [
    {"id": 1, "titulo": "Erro no sistema", "status": "Aberto"},
    {"id": 2, "titulo": "Problema no pagamento", "status": "Resolvido"}
]

@router.get("/contratante/chamados")
async def get_chamados(request: Request):
    return templates.TemplateResponse(
        "contratante/chamados.html",
        {"request": request, "chamados": chamados_fake}
    )

@router.post("/contratante/chamados/abrir")
async def post_chamado(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(...)
):
    novo_id = len(chamados_fake) + 1
    chamados_fake.append({
        "id": novo_id,
        "titulo": titulo,
        "status": "Aberto"
    })

    # redireciona para a lista atualizada
    return RedirectResponse(url="/contratante/chamados", status_code=303)
