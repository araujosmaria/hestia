from asyncio import open_connection
from typing import Optional

from data.atendimento_model import Atendimento
from data.atendimento_sql import CRIAR_TABELA_ATENDIMENTO, INSERIR_ATENDIMENTO, OBTER_TODOS_ATENDIMENTO


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ATENDIMENTO)
        return cursor.rowcount > 0

def inserir(atendimento: Atendimento) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ATENDIMENTO, (
            atendimento.dataInicio,  
            atendimento.dataFim))
        return cursor.lastrowid

def obter_todos() -> list[Atendimento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ATENDIMENTO)
        rows = cursor.fetchall()
        atendimentos = [
            Atendimento(
                id=row["id"], 
                dataInicio=row["dataInicio"], 
                dataFim=row["dataFim"]) 
                for row in rows]
        return atendimentos