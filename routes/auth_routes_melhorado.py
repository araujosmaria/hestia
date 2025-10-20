"""
Rotas de autenticação melhoradas com rate limiting, flash messages e recuperação de senha funcional.

INSTRUÇÕES DE USO:
1. Este arquivo contém versões melhoradas das rotas de autenticação
2. Você pode copiar as funções desejadas para public_routes.py
3. Ou substituir todo o sistema de auth por este arquivo

MELHORIAS IMPLEMENTADAS:
- Rate limiting em login, cadastro e recuperação de senha
- Flash messages para feedback ao usuário
- Recuperação de senha funcional com envio de email
- Validação de senha forte
- Logging de eventos de segurança
"""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import ValidationError

# Imports do sistema
from util.template_util import criar_templates
from util.auth_decorator import criar_sessao, destruir_sessao, obter_usuario_logado, esta_logado
from util.security import (
    criar_hash_senha,
    verificar_senha,
    gerar_token_redefinicao,
    obter_data_expiracao_token,
    validar_forca_senha
)
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso
from util.rate_limiter import SimpleRateLimiter
from util.email_service import email_service
from util.config import (
    RATE_LIMIT_LOGIN_MAX,
    RATE_LIMIT_LOGIN_MINUTOS,
    RATE_LIMIT_CADASTRO_MAX,
    RATE_LIMIT_CADASTRO_MINUTOS,
    RATE_LIMIT_ESQUECI_SENHA_MAX,
    RATE_LIMIT_ESQUECI_SENHA_MINUTOS
)

# Imports de dados
from data.usuario import usuario_repo
from dtos.login_dto import LoginDTO

router = APIRouter(prefix="/auth", tags=["Autenticação"])
templates = criar_templates("templates")

# Rate limiters
login_limiter = SimpleRateLimiter(RATE_LIMIT_LOGIN_MAX, RATE_LIMIT_LOGIN_MINUTOS)
cadastro_limiter = SimpleRateLimiter(RATE_LIMIT_CADASTRO_MAX, RATE_LIMIT_CADASTRO_MINUTOS)
esqueci_senha_limiter = SimpleRateLimiter(RATE_LIMIT_ESQUECI_SENHA_MAX, RATE_LIMIT_ESQUECI_SENHA_MINUTOS)


def obter_ip(request: Request) -> str:
    """Obtém IP do cliente"""
    if request.client:
        return request.client.host
    return "unknown"


@router.get("/login", response_class=HTMLResponse)
async def get_login(request: Request, redirect: Optional[str] = None):
    """
    Exibe formulário de login

    Args:
        request: Request do FastAPI
        redirect: URL para redirecionar após login (opcional)
    """
    # Se já está logado, redireciona
    if esta_logado(request):
        usuario = obter_usuario_logado(request)
        if usuario.perfil == "cuidador":
            return RedirectResponse("/cuidador/home_cuidador", status_code=status.HTTP_303_SEE_OTHER)
        elif usuario.perfil == "contratante":
            return RedirectResponse("/contratante/home_contratante", status_code=status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "redirect": redirect}
    )


@router.post("/login")
async def post_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    redirect: Optional[str] = None
):
    """
    Processa login do usuário

    Melhorias:
    - Rate limiting por IP
    - Validação com DTO
    - Flash messages
    - Logging de eventos
    - Reset de rate limiter em sucesso
    """
    ip = obter_ip(request)

    # Rate limiting
    if not login_limiter.verificar(ip):
        tempo_restante = login_limiter.tempo_ate_liberar(ip)
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60
        informar_erro(
            request,
            f"Muitas tentativas de login. Aguarde {minutos}min {segundos}s e tente novamente."
        )
        return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)

    try:
        # Validar com DTO
        dto = LoginDTO(email=email, senha=senha)

        # Buscar usuário
        usuario = usuario_repo.obter_por_email(dto.email)

        # Verificar credenciais
        if not usuario or not verificar_senha(dto.senha, usuario.senha):
            informar_erro(request, "Email ou senha incorretos")
            print(f"❌ Login falhou: {dto.email} (IP: {ip})")
            return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)

        # Login bem-sucedido - resetar rate limiter
        login_limiter.resetar(ip)

        # Criar sessão
        usuario_dict = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "perfil": usuario.perfil
        }
        criar_sessao(request, usuario_dict)

        print(f"✅ Login bem-sucedido: {usuario.email}")
        informar_sucesso(request, f"Bem-vindo(a), {usuario.nome}!")

        # Redirecionar conforme perfil
        if usuario.perfil == "contratante":
            return RedirectResponse("/contratante/home_contratante", status_code=status.HTTP_303_SEE_OTHER)
        elif usuario.perfil == "cuidador":
            return RedirectResponse("/cuidador/home_cuidador", status_code=status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

    except ValidationError as e:
        erros = [erro['msg'] for erro in e.errors()]
        informar_erro(request, " | ".join(erros))
        return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        print(f"❌ Erro no login: {str(e)}")
        informar_erro(request, "Erro ao processar login. Tente novamente.")
        return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/logout")
async def logout(request: Request):
    """
    Faz logout do usuário

    Melhorias:
    - Flash message
    - Logging
    """
    usuario = obter_usuario_logado(request)
    email = usuario.email if usuario else "Usuário"

    destruir_sessao(request)
    print(f"🚪 Logout: {email}")
    informar_sucesso(request, "Logout realizado com sucesso!")

    return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/redefinicao_senha", response_class=HTMLResponse)
async def get_redefinicao_senha(request: Request):
    """
    Exibe formulário para solicitar recuperação de senha
    """
    return templates.TemplateResponse("redefinicao_senha.html", {"request": request})


@router.post("/redefinicao_senha")
async def post_redefinicao_senha(request: Request, email: str = Form(...)):
    """
    Processa solicitação de recuperação de senha

    Melhorias:
    - Rate limiting
    - Envio de email funcional
    - Resposta genérica (segurança)
    - Flash messages
    """
    ip = obter_ip(request)

    # Rate limiting
    if not esqueci_senha_limiter.verificar(ip):
        tempo_restante = esqueci_senha_limiter.tempo_ate_liberar(ip)
        minutos = tempo_restante // 60
        informar_erro(
            request,
            f"Muitas solicitações. Aguarde {minutos} minuto(s) e tente novamente."
        )
        return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)

    try:
        # Buscar usuário
        usuario = usuario_repo.obter_por_email(email.strip().lower())

        if usuario:
            # Gerar token
            token = gerar_token_redefinicao()
            data_expiracao = obter_data_expiracao_token(horas=1)

            # Salvar token no banco
            usuario_repo.atualizar_token(usuario.email, token, data_expiracao)

            # Enviar email
            sucesso, mensagem = email_service.enviar_recuperacao_senha(
                para_email=usuario.email,
                para_nome=usuario.nome,
                token=token
            )

            if sucesso:
                print(f"📧 Email de recuperação enviado para: {usuario.email}")
            else:
                print(f"❌ Falha ao enviar email: {mensagem}")
        else:
            print(f"⚠️  Recuperação solicitada para email não cadastrado: {email}")

        # Sempre a mesma mensagem (segurança - não revelar se email existe)
        informar_sucesso(
            request,
            "Se o email existir em nossa base, você receberá instruções para redefinir sua senha."
        )
        return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)

    except Exception as e:
        print(f"❌ Erro na recuperação de senha: {str(e)}")
        informar_erro(request, "Erro ao processar solicitação. Tente novamente.")
        return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/confirmar_redefinir_senha", response_class=HTMLResponse)
async def get_confirmar_redefinir_senha(request: Request, token: str):
    """
    Exibe formulário para redefinir senha com token válido

    Args:
        request: Request do FastAPI
        token: Token de redefinição recebido por email
    """
    # Buscar usuário pelo token
    usuario = usuario_repo.obter_por_token(token)

    if not usuario or not usuario.data_token:
        informar_erro(request, "Token inválido ou expirado. Solicite uma nova recuperação.")
        return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)

    # Verificar se token expirou
    try:
        data_token = datetime.fromisoformat(usuario.data_token)
        if datetime.now() > data_token:
            informar_erro(request, "Token expirado. Solicite uma nova recuperação.")
            return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)
    except:
        informar_erro(request, "Token inválido. Solicite uma nova recuperação.")
        return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse(
        "confirmar_redefinir_senha.html",
        {"request": request, "token": token}
    )


@router.post("/confirmar_redefinir_senha")
async def post_confirmar_redefinir_senha(
    request: Request,
    token: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...)
):
    """
    Processa redefinição de senha

    Melhorias:
    - Validação de senha forte
    - Verificação de token
    - Flash messages
    """
    try:
        # Verificar se senhas coincidem
        if senha != confirmar_senha:
            informar_erro(request, "As senhas não coincidem")
            return RedirectResponse(
                f"/auth/confirmar_redefinir_senha?token={token}",
                status_code=status.HTTP_303_SEE_OTHER
            )

        # Validar força da senha
        valida, mensagem = validar_forca_senha(senha)
        if not valida:
            informar_erro(request, mensagem)
            return RedirectResponse(
                f"/auth/confirmar_redefinir_senha?token={token}",
                status_code=status.HTTP_303_SEE_OTHER
            )

        # Buscar usuário pelo token
        usuario = usuario_repo.obter_por_token(token)

        if not usuario or not usuario.data_token:
            informar_erro(request, "Token inválido ou expirado")
            return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)

        # Verificar se token expirou
        try:
            data_token = datetime.fromisoformat(usuario.data_token)
            if datetime.now() > data_token:
                informar_erro(request, "Token expirado. Solicite uma nova recuperação.")
                return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)
        except:
            informar_erro(request, "Token inválido")
            return RedirectResponse("/auth/redefinicao_senha", status_code=status.HTTP_303_SEE_OTHER)

        # Atualizar senha
        senha_hash = criar_hash_senha(senha)
        usuario_repo.atualizar_senha(usuario.id, senha_hash)

        # Limpar token
        usuario_repo.limpar_token(usuario.id)

        print(f"🔑 Senha redefinida: {usuario.email}")
        informar_sucesso(request, "Senha redefinida com sucesso! Faça login com sua nova senha.")
        return RedirectResponse("/auth/login", status_code=status.HTTP_303_SEE_OTHER)

    except Exception as e:
        print(f"❌ Erro ao redefinir senha: {str(e)}")
        informar_erro(request, "Erro ao redefinir senha. Tente novamente.")
        return RedirectResponse(
            f"/auth/confirmar_redefinir_senha?token={token}",
            status_code=status.HTTP_303_SEE_OTHER
        )
