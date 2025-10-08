from fastapi import APIRouter, Request, UploadFile, File, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from data.cliente import cliente_repo
from util.auth_decorator import criar_sessao, requer_autenticacao
import os
import secrets
from io import BytesIO
from PIL import Image, ImageDraw


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contratante/home_contratante")
async def get_home_contratante(request: Request):
    id_usuario = 1
    return RedirectResponse(
        url=f"/contratante/home_contratante?mensagem=Senha+alterada+com+sucesso",
        status_code=303
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
