"""
Sistema de Flash Messages para feedback ao usuário
"""
from fastapi import Request
from typing import Literal

TipoMensagem = Literal["sucesso", "erro", "aviso", "info"]


def adicionar_mensagem(
    request: Request,
    mensagem: str,
    tipo: TipoMensagem = "info"
) -> None:
    """
    Adiciona uma mensagem flash à sessão do usuário

    Args:
        request: Request do FastAPI
        mensagem: Texto da mensagem
        tipo: Tipo da mensagem (sucesso, erro, aviso, info)
    """
    if not hasattr(request, 'session'):
        return

    if "mensagens" not in request.session:
        request.session["mensagens"] = []

    request.session["mensagens"].append({
        "texto": mensagem,
        "tipo": tipo
    })


def informar_sucesso(request: Request, mensagem: str) -> None:
    """Adiciona mensagem de sucesso"""
    adicionar_mensagem(request, mensagem, "sucesso")


def informar_erro(request: Request, mensagem: str) -> None:
    """Adiciona mensagem de erro"""
    adicionar_mensagem(request, mensagem, "erro")


def informar_aviso(request: Request, mensagem: str) -> None:
    """Adiciona mensagem de aviso"""
    adicionar_mensagem(request, mensagem, "aviso")


def informar_info(request: Request, mensagem: str) -> None:
    """Adiciona mensagem informativa"""
    adicionar_mensagem(request, mensagem, "info")


def obter_mensagens(request: Request) -> list:
    """
    Obtém e limpa mensagens da sessão

    Args:
        request: Request do FastAPI

    Returns:
        Lista de dicionários com mensagens
    """
    if not hasattr(request, 'session'):
        return []

    mensagens = request.session.pop("mensagens", [])
    return mensagens
