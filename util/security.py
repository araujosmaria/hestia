"""
Módulo de segurança para gerenciar senhas e tokens
"""
import os
import secrets
import string
from datetime import datetime, timedelta
from passlib.context import CryptContext

# Contexto para hash de senhas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def criar_hash_senha(senha: str) -> str:
    """
    Cria um hash seguro da senha usando bcrypt

    Args:
        senha: Senha em texto plano

    Returns:
        Hash da senha

    Note:
        Bcrypt tem limite de 72 bytes. Senhas maiores são truncadas automaticamente.
    """
    # Bcrypt tem limite de 72 bytes - trunca se necessário
    if len(senha.encode('utf-8')) > 72:
        senha = senha.encode('utf-8')[:72].decode('utf-8', errors='ignore')

    return pwd_context.hash(senha)


def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """
    Verifica se a senha em texto plano corresponde ao hash
    
    Args:
        senha_plana: Senha em texto plano
        senha_hash: Hash da senha armazenado no banco
    
    Returns:
        True se a senha está correta, False caso contrário
    """
    try:
        return pwd_context.verify(senha_plana, senha_hash)
    except:
        return False


def gerar_token_redefinicao(tamanho: int = 32) -> str:
    """
    Gera um token aleatório seguro para redefinição de senha
    
    Args:
        tamanho: Tamanho do token em caracteres
    
    Returns:
        Token aleatório
    """
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))


def obter_data_expiracao_token(horas: int = 24) -> str:
    """
    Calcula a data de expiração do token
    
    Args:
        horas: Número de horas de validade do token
    
    Returns:
        Data de expiração no formato ISO
    """
    expiracao = datetime.now() + timedelta(hours=horas)
    return expiracao.isoformat()


def validar_forca_senha(senha: str) -> tuple[bool, str]:
    """
    Valida se a senha atende aos requisitos mínimos de segurança.
    Requisitos configuráveis via util/config.py

    Args:
        senha: Senha a ser validada

    Returns:
        Tupla (válida, mensagem de erro se inválida)
    """
    import re
    from util.config import (
        SENHA_MIN_CHARS,
        SENHA_REQUER_MAIUSCULA,
        SENHA_REQUER_MINUSCULA,
        SENHA_REQUER_NUMERO,
        SENHA_REQUER_ESPECIAL
    )

    if len(senha) < SENHA_MIN_CHARS:
        return False, f"A senha deve ter pelo menos {SENHA_MIN_CHARS} caracteres"

    if SENHA_REQUER_MAIUSCULA and not re.search(r"[A-Z]", senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula"

    if SENHA_REQUER_MINUSCULA and not re.search(r"[a-z]", senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"

    if SENHA_REQUER_NUMERO and not re.search(r"\d", senha):
        return False, "A senha deve conter pelo menos um número"

    if SENHA_REQUER_ESPECIAL and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "A senha deve conter pelo menos um caractere especial (!@#$%^&*...)"

    return True, ""


def calcular_nivel_senha(senha: str) -> str:
    """
    Calcula o nível de força da senha: fraca, média ou forte

    Args:
        senha: Senha a avaliar

    Returns:
        "fraca", "média" ou "forte"
    """
    import re

    pontos = 0

    # Comprimento
    if len(senha) >= 8: pontos += 1
    if len(senha) >= 12: pontos += 1
    if len(senha) >= 16: pontos += 1

    # Complexidade
    if re.search(r"[A-Z]", senha): pontos += 1
    if re.search(r"[a-z]", senha): pontos += 1
    if re.search(r"\d", senha): pontos += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha): pontos += 1

    if pontos <= 3: return "fraca"
    if pontos <= 5: return "média"
    return "forte"


def gerar_senha_aleatoria(tamanho: int = 8) -> str:
    """
    Gera uma senha aleatória segura
    
    Args:
        tamanho: Tamanho da senha
    
    Returns:
        Senha aleatória
    """
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def salvar_foto(conteudo_foto, nome_arquivo):
    diretorio = "static/uploads"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    caminho = os.path.join(diretorio, nome_arquivo)
    with open(caminho, "wb") as f:
        f.write(conteudo_foto)

    return caminho