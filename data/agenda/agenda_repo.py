from typing import Optional

from data.agenda.agenda_model import Agenda
from data.agenda.agenda_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_AGENDA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de agendas: {e}")
        return False  

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
    
def atualizar(agenda: Agenda) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_AGENDA, (
            agenda.dataHrora,
            agenda.disponibilidade,
            agenda.id
        ))
        return cursor.rowcount > 0


def excluir(agenda_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_AGENDA, (agenda_id,))
        return cursor.rowcount > 0
