from typing import Optional

from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CLIENTE)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de clientes: {e}")
        return False  

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