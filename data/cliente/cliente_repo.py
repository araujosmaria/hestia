from asyncio import open_connection
from typing import Optional

from data.cliente_model import Cliente
from data.cliente_sql import CRIAR_TABELA_CLIENTE, INSERIR_CLIENTE, OBTER_TODOS_CLIENTE


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CLIENTE)
        return cursor.rowcount > 0

def inserir(cliente: Cliente) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CLIENTE, (
            cliente.nome,  
            cliente.email, 
            cliente.senha,
            cliente.telefone, 
            cliente.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CLIENTE)
        rows = cursor.fetchall()
        clientes = [
            Cliente(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return clientes