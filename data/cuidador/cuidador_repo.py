from asyncio import open_connection
from typing import Optional

from data.cuidador_model import Cuidador
from data.cuidador_sql import CRIAR_TABELA_CUIDADOR, INSERIR_CUIDADOR, OBTER_TODOS_CUIDADOR


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CUIDADOR)
        return cursor.rowcount > 0

def inserir(cuidador: Cuidador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CUIDADOR, (
            cuidador.nome,  
            cuidador.email, 
            cuidador.senha,
            cuidador.telefone, 
            cuidador.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        cuidadores = [
            Cuidador(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return cuidadores
    
def adicionar_especialidade():