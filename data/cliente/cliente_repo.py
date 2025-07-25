from typing import Optional

from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.util import open_connection
from data.usuario import usuario_repo


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
    id_cliente = usuario_repo.inserir(cliente)
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CLIENTE, (id_cliente,))
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
    
def obter_por_id(id_cliente: int) -> Optional[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE_POR_ID,(id_cliente,))
        row = cursor.fetchone()
        if row:
            return Cliente(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"])     
        return None
    
def excluir(cliente_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
            
        # Exclui da tabela cliente primeiro (para não violar a FK)
        cursor.execute("DELETE FROM cliente WHERE id_cliente = ?", (cliente_id,))
            
        # Agora exclui da tabela usuario
        cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (cliente_id,))
            
        return cursor.rowcount > 0