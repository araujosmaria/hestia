from asyncio import open_connection
from typing import Optional

from data.especialidade_model import Especialidade
from data.especialidade_sql import CRIAR_TABELA_ESPECIALIDADE, INSERIR_ESPECIALIDADE, OBTER_TODOS_ESPECIALIDADE


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ESPECIALIDADE)
        return cursor.rowcount > 0

def inserir(especialidade: Especialidade) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ESPECIALIDADE, (
            especialidade.nome))
        return cursor.lastrowid

def obter_todos() -> list[Especialidade]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ESPECIALIDADE)
        rows = cursor.fetchall()
        especialidade = [
            Especialidade(
                id=row["id"], 
                nome=row["nome"]) 
                for row in rows]
        return especialidade