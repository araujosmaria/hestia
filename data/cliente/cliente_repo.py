from typing import Optional
from data.util import open_connection
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo
from data.cliente.cliente_sql import *
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
    try:
        # Inserir usuário (cliente)
        id_cliente = usuario_repo.inserir(cliente)
        if id_cliente is None:
            print("Erro: inserção do usuário (cliente) retornou None")
            return None

        # Inserir dados específicos do cliente
        parentesco_paciente = cliente_repo.inserir(cliente)
        if parentesco_paciente is None:
            print("Erro: inserção do parentesco do cliente retornou None")
            return None

        # Inserir cliente na tabela específica
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_CLIENTE, (id_cliente, parentesco_paciente))
            conn.commit()
            return cursor.lastrowid

    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")
        return None


def obter_todos() -> list[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CLIENTE)
        rows = cursor.fetchall()
        clientes = [
            Cliente(
                id=row["id_cliente"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"],
                parentesco_paciente=row["parentesco_paciente"]) 
                for row in rows]
        return clientes


def obter_por_id(id_cliente: int) -> Optional[Cliente]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_CLIENTE_POR_ID, (id_cliente,))
            row = cursor.fetchone()
            if row:
                return Cliente(
                    id=row["id_cliente"],
                    nome=row["nome"],
                    email=row["email"],
                    senha=row["senha"],
                    telefone=row["telefone"],
                    endereco=row["endereco"],
                    parentesco_paciente=row["parentesco_paciente"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter cliente por ID: {e}")
        return None



def excluir(id_cliente: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
            
        # Exclui da tabela cliente primeiro (para não violar a FK)
        cursor.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
            
        # Agora exclui da tabela usuario
        cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (id_cliente,))
            
        return cursor.rowcount > 0