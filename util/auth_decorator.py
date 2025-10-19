
"""
Decorator para proteger rotas com autenticação e autorização
"""
from functools import wraps
from typing import List, Optional
from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
import asyncio
from pytest import Session
from data.usuario.usuario_model import Usuario
from data.util import open_connection



# ======================
# SESSÃO
# ======================

def criar_sessao(request: Request, usuario: dict) -> None:
    """
    Cria uma sessão para o usuário após login
    
    Args:
        request: Objeto Request do FastAPI
        usuario: Dicionário com dados do usuário
    """
    if hasattr(request, 'session'):
        # Remove senha da sessão por segurança
        usuario_sessao = usuario.copy()
        usuario_sessao.pop('senha', None)
        request.session['usuario'] = usuario_sessao

def get_usuario_por_id(user_id: int, db: Session) -> Usuario | None:
    """
    Busca um usuário no banco pelo ID.
    
    Args:
        user_id (int): ID do usuário.
        db (Session): Sessão do SQLAlchemy.
    
    Returns:
        Usuario | None: Retorna o objeto Usuario se encontrado, senão None.
    """
    return db.query(Usuario).filter(Usuario.id == user_id).first()


# def obter_usuario_logado(request: Request):
#     user_id = request.session.get('user_id')  # tenta pegar o ID do usuário da sessão
#     if not user_id:                           # se não houver usuário logado
#         return None                           # retorna None
#     # busca usuário no banco pelo ID
#     return get_usuario_por_id(user_id) 

def obter_usuario_logado(request: Request):
    usuario_dict = request.session.get("usuario")
    if not usuario_dict:
        return None

    # Se quiser transformar de volta em objeto Usuario:
    from data.usuario.usuario_model import Usuario
    usuario = Usuario(**usuario_dict)
    return usuario


def esta_logado(request: Request) -> bool:
    """
    Verifica se há um usuário logado
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        True se há usuário logado, False caso contrário
    """
    return obter_usuario_logado(request) is not None


def destruir_sessao(request: Request) -> None:
    """
    Destrói a sessão do usuário (logout)
    
    Args:
        request: Objeto Request do FastAPI
    """
    if hasattr(request, 'session'):
        request.session.clear()


# ======================
# DECORATOR DE AUTENTICAÇÃO
# ======================

def requer_autenticacao(perfis_autorizados: List[str] = None):
    """
    Decorator para proteger rotas que requerem autenticação
    
    Args:
        perfis_autorizados: Lista de perfis autorizados a acessar a rota.
                           Se None, qualquer usuário logado pode acessar.
    
    Exemplo de uso:
        @router.get("/admin")
        @requer_autenticacao(['admin'])
        async def admin_page(request: Request):
            ...
        
        @router.get("/perfil")
        @requer_autenticacao()  # Qualquer usuário logado
        async def perfil(request: Request):
            ...
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Encontra o objeto Request nos argumentos
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            if not request:
                for value in kwargs.values():
                    if isinstance(value, Request):
                        request = value
                        break
            
            if not request:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Request object not found"
                )
            
            # Verifica se o usuário está logado
            usuario = obter_usuario_logado(request)
            if not usuario:
                # Redireciona para login se não estiver autenticado
                return RedirectResponse(
                    url="/login?redirect=" + str(request.url.path),
                    status_code=status.HTTP_303_SEE_OTHER
                )
            
            # Verifica autorização se perfis foram especificados
            if perfis_autorizados:
                perfil_usuario = usuario.get('perfil', 'cliente')
                if perfil_usuario not in perfis_autorizados:
                    # Retorna erro 403 se não autorizado
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Você não tem permissão para acessar este recurso"
                    )
            
            # Adiciona o usuário aos kwargs para fácil acesso na rota
            kwargs['usuario_logado'] = usuario
            
            # Chama a função original
            if asyncio.iscoroutinefunction(func):
                return await func(*args, **kwargs)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator