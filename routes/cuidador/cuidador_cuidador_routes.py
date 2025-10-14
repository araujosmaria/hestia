from fastapi import APIRouter, Request, Form, File, UploadFile, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import os
import secrets
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo
from data.usuario import usuario_repo
from util.auth_decorator import obter_usuario_logado, esta_logado, criar_sessao, requer_autenticacao
from io import BytesIO
from PIL import Image, ImageDraw, ImageOps


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cuidador/home_cuidador")
async def get_home_cuidador(request: Request, mensagem: str = None):
    # Obter usuário logado
    user = obter_usuario_logado(request)
    
    # Se não houver usuário logado, redirecionar para login
    if not user:
        return RedirectResponse("/login", status_code=303)
    
    # Verificar se o perfil é realmente de cuidador (opcional, mas recomendado)
    if user.get("perfil") != "cuidador":
        return RedirectResponse("/login", status_code=303)

    # Renderizar template com dados
    return templates.TemplateResponse(
        "cuidador/home_cuidador.html",
        {
            "request": request,
            "mensagem": mensagem,
            "user": user,
            "oportunidades_novas": 0,
            "solicitacoes_pendentes": 0,
            "avaliacao_media": 0.0,
            "trabalhos_concluidos": 0,
            "ganhos_mes": "0,00"
        }
    )


# ======================
# ALTERAR SENHA (GET)
# ======================
@router.get("/cuidador/alterar_senha")
@requer_autenticacao()
async def get_alterar_senha(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "cuidador/alterar_senha.html",
        {"request": request}
    )

# ======================
# ALTERAR SENHA (POST)
# ======================
@router.post("/cuidador/alterar_senha")
@requer_autenticacao()
async def post_alterar_senha(
    request: Request,
    senha_atual: str = Form(...),
    nova_senha: str = Form(...),
    confirmar_senha: str = Form(...),
    usuario_logado: dict = None
):
    if nova_senha != confirmar_senha:
        mensagem = "As senhas não coincidem!"
        return templates.TemplateResponse(
            "cuidador/alterar_senha.html",
            {"request": request, "mensagem": mensagem}
        )
    response = RedirectResponse(url="/cuidador/home_cuidador", status_code=303)
    return response

# ======================
# ABERTURA DE CHAMADOS (GET)
# ======================
@router.get("/cuidador/chamados/abrir")
@requer_autenticacao()
async def get_abertura_chamados(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "abertura_chamados.html",
        {"request": request}
    )

# ======================
# ABERTURA DE CHAMADOS (POST)
# ======================
@router.post("/cuidador/chamados/abrir")
@requer_autenticacao()
async def post_abertura_chamados(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(...),
    usuario_logado: dict = None
):
    mensagem = f"Chamado '{titulo}' aberto com sucesso!"
    return templates.TemplateResponse(
        "abertura_chamados.html",
        {"request": request, "mensagem": mensagem}
    )

# ======================
# LISTAR CHAMADOS ABERTOS
# ======================
@router.get("/cuidador/chamados/abertos")
@requer_autenticacao()
async def get_chamados_abertos(request: Request, usuario_logado: dict = None):
    chamados_fake = [
        {"id": 1, "titulo": "Problema no acesso", "status": "Em análise"},
        {"id": 2, "titulo": "Erro ao atualizar perfil", "status": "Aberto"}
    ]
    return templates.TemplateResponse(
        "chamados_abertos.html",
        {"request": request, "chamados": chamados_fake}
    )