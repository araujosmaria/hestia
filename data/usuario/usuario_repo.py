from asyncio import open_connection
from typing import Optional

from data.usuario_model import Usuario
from data.usuario_sql import CRIAR_TABELA_USUARIO, INSERIR_USUARIO, OBTER_TODOS_USUARIO


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_USUARIO)
        return cursor.rowcount > 0

def inserir(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO, (
            usuario.nome,  
            usuario.email, 
            usuario.senha,
            usuario.telefone, 
            usuario.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIO)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return usuarios