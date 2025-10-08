from typing import Any, Optional, List
from data.usuario.usuario_sql import *
from data.usuario.usuario_model import Usuario
from util.db_util import get_connection

def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executescript(CRIAR_TABELA_USUARIO)
        return True  # executscript não retorna rowcount, assumimos sucesso se não levantar erro

def inserir(usuario: Usuario, cursor: Any = None, db_path: str = None) -> Optional[int]:
    from util.db_util import get_connection
    from data.config import DB_PATH  # se tiver constante padrão

    params = (
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
        int(usuario.ativo),
        usuario.foto
    )

    if cursor:
        cursor.execute(INSERIR_USUARIO, params)
        return cursor.lastrowid
    else:
        if db_path:
            import sqlite3
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(INSERIR_USUARIO, params)
                return cursor.lastrowid
        else:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(INSERIR_USUARIO, params)
                return cursor.lastrowid


def alterar(usuario: Usuario, cursor: Any = None) -> bool:
    # Aqui "alterar" seria atualizar, sem senha e token, vamos considerar que alterar atualiza campos básicos
    params = (
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
        int(usuario.ativo),
        usuario.foto,
        usuario.id
    )
    if cursor:
        cursor.execute(ATUALIZAR_USUARIO, params)
        return cursor.rowcount > 0
    else:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_USUARIO, params)
            return cursor.rowcount > 0

def atualizar_senha(id_usuario: int, senha: str, cursor: Any = None) -> bool:
    query = "UPDATE usuario SET senha = ? WHERE id_usuario = ?"
    if cursor:
        cursor.execute(query, (senha, id_usuario))
        return cursor.rowcount > 0
    else:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (senha, id_usuario))
            return cursor.rowcount > 0

def excluir(id_usuario: int, cursor: Any = None) -> bool:
    if cursor:
        cursor.execute(EXCLUIR_USUARIO, (id_usuario,))
        return cursor.rowcount > 0
    else:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_USUARIO, (id_usuario,))
            return cursor.rowcount > 0

def obter_por_id(id_usuario: int) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_ID, (id_usuario,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],
                perfil=row["perfil"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=bool(row["ativo"]),
                foto=row["foto"]
            )
        return None

def obter_todos() -> List[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIOS)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],
                perfil=row["perfil"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=bool(row["ativo"]),
                foto=row["foto"]
            )
            for row in rows
        ]
        return usuarios

def obter_por_email(email: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_EMAIL, (email,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],
                perfil=row["perfil"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=bool(row["ativo"]),
                foto=row["foto"]
            )
        return None

def atualizar_token(email: str, token: str, data_expiracao: str) -> bool:
    query = """
    UPDATE usuario 
    SET token_redefinicao = ?, data_token = ? 
    WHERE email = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (token, data_expiracao, email))
        return cursor.rowcount > 0

def atualizar_foto(id_usuario: int, caminho_foto: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_FOTO, (caminho_foto, id_usuario))
        return cursor.rowcount > 0

def obter_por_token(token: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(VALIDAR_TOKEN, (token,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                email=row["email"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"]
            )
        return None

def limpar_token(id_usuario: int) -> bool:
    query = """
    UPDATE usuario 
    SET token_redefinicao = NULL, data_token = NULL 
    WHERE id_usuario = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (id_usuario,))
        return cursor.rowcount > 0

def obter_todos_por_perfil(perfil: str) -> List[Usuario]:
    query = """
    SELECT * FROM usuario 
    WHERE perfil = ? 
    ORDER BY nome
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (perfil,))
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],
                perfil=row["perfil"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=bool(row["ativo"]),
                foto=row["foto"]
            )
            for row in rows
        ]
        return usuarios

def obter_por_cpf(cpf: str) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_CPF, (cpf,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],
                perfil=row["perfil"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=bool(row["ativo"]),
                foto=row["foto"]
            )
        return None
