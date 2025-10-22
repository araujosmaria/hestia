from typing import Any, Optional
from data.usuario.usuario_sql import ATIVAR_USUARIO, ATUALIZAR_FOTO, ATUALIZAR_USUARIO, CRIAR_TABELA_USUARIO, EXCLUIR_USUARIO, INSERIR_USUARIO, OBTER_TODOS_USUARIOS, OBTER_USUARIO_POR_CPF, OBTER_USUARIO_POR_EMAIL, OBTER_USUARIO_POR_ID, VALIDAR_TOKEN
from data.usuario.usuario_model import Usuario
from util.db_util import get_connection
from util.logger_config import logger


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_USUARIO)
        return (cursor.rowcount > 0)


def inserir(usuario: Usuario, cursor: Any = None) -> Optional[int]:
    import sqlite3
    parametros = (
        usuario.nome,
        usuario.dataNascimento,
        usuario.email,
        usuario.telefone,
        usuario.cpf,
        usuario.senha,
        usuario.perfil,
        usuario.token_redefinicao,
        usuario.data_token,
        usuario.data_cadastro,
        usuario.cep,
        usuario.logradouro,
        usuario.numero,
        usuario.complemento,
        usuario.bairro,
        usuario.cidade,
        usuario.estado,
        usuario.ativo,
        usuario.foto
    )
    if cursor:
        cursor.execute(INSERIR_USUARIO, parametros)
        return cursor.lastrowid

    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(INSERIR_USUARIO, parametros)
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            conn.rollback()
            logger.error(f"Erro ao inserir usuário: {e}", exc_info=True)
            return None
        except Exception as e:
            conn.rollback()
            logger.error(f"Erro ao inserir usuário: {e}", exc_info=True)
            raise

def alterar(usuario: Usuario, cursor: Any = None) -> bool:
    parametros = (
        usuario.nome,
        usuario.dataNascimento,
        usuario.email,
        usuario.telefone,
        usuario.cpf,
        usuario.senha,
        usuario.perfil,
        usuario.token_redefinicao,
        usuario.data_token,
        usuario.data_cadastro,
        usuario.cep,
        usuario.logradouro,
        usuario.numero,
        usuario.complemento,
        usuario.bairro,
        usuario.cidade,
        usuario.estado,
        usuario.ativo,
        usuario.foto,
        usuario.id
    )
    if cursor:
        cursor.execute(ATUALIZAR_USUARIO, parametros)
        return (cursor.rowcount > 0)
    else:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_USUARIO, parametros)
            return (cursor.rowcount > 0)


def excluir(id: int, cursor: Any = None) -> bool:
    if cursor:
        cursor.execute(EXCLUIR_USUARIO, (id,))
        return (cursor.rowcount > 0)
    else:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_USUARIO, (id,))
            return (cursor.rowcount > 0)


def obter_por_id(id: int) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return Usuario.from_row(row)
        return None


def obter_todos() -> list[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIOS)
        rows = cursor.fetchall()
        return [Usuario.from_row(row) for row in rows]


def obter_por_email(email: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_EMAIL, (email,))
        row = cursor.fetchone()
        if row:
            return Usuario.from_row(row)
        return None


def atualizar_foto(id: int, caminho_foto: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_FOTO, (caminho_foto, id))
        return (cursor.rowcount > 0)


def ativar_usuario(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATIVAR_USUARIO, (id,))
        return (cursor.rowcount > 0)


def obter_por_cpf(cpf: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_CPF, (cpf,))
        row = cursor.fetchone()
        if row:
            return Usuario.from_row(row)
        return None


def obter_por_token(token: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(VALIDAR_TOKEN, (token,))
        row = cursor.fetchone()
        if row:
            return Usuario.from_row(row)
        return None
