from asyncio import open_connection
from typing import Optional

from data.agenda_model import Agenda
from data.agenda_sql import CRIAR_TABELA_AGENDA, INSERIR_AGENDA, OBTER_TODOS_AGENDA


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_AGENDA)
        return cursor.rowcount > 0

def inserir(agenda: Agenda) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_AGENDA, (
            agenda.dataHrora,  
            agenda.disponibilidade))
        return cursor.lastrowid

def obter_todos() -> list[Agenda]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_AGENDA)
        rows = cursor.fetchall()
        agendas = [
            Agenda(
                id=row["id"], 
                dataHrora=row["dataHrora"], 
                disponibilidade=row["disponibilidade"]) 
                for row in rows]
        return agendas