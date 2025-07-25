import sqlite3
from data.util import open_connection
from typing import Optional

from data.administrador.administrador_model import Administrador
from data.administrador.administrador_sql import *



def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ADMINISTRADOR)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de administradores: {e}")
        return False  

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
    
def obter_por_id(administrador_id: int) -> Optional[Administrador]:
    with open_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(OBTER_ADMINISTRADOR_POR_ID, (administrador_id,))
        row = cursor.fetchone()
        if row:
            return Administrador(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]
            )
        return None


def atualizar(administrador: Administrador) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ADMINISTRADOR, (
            administrador.nome,
            administrador.email,
            administrador.senha,
            administrador.telefone,
            administrador.endereco,
            administrador.id
        ))
        return cursor.rowcount > 0


def excluir(administrador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_ADMINISTRADOR, (administrador_id,))
        return cursor.rowcount > 0
