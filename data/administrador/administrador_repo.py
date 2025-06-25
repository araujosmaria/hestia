from asyncio import open_connection
from typing import Optional

from data.administrador_model import Administrador
from data.administrador_sql import CRIAR_TABELA_ADMINISTRADOR, INSERIR_ADMINISTRADOR, OBTER_TODOS_ADMINISTRADOR


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ADMINISTRADOR)
        return cursor.rowcount > 0

def inserir(administrador: Administrador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ADMINISTRADOR, (
            administrador.nome,  
            administrador.email, 
            administrador.senha,
            administrador.telefone, 
            administrador.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ADMINISTRADOR)
        rows = cursor.fetchall()
        administradores = [
            Administrador(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return administradores