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
            agenda.dataHora,  
            agenda.disponibilidade,
            agenda.id_cuidador))
        return cursor.lastrowid

def obter_todos() -> list[Agenda]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_AGENDA)
        rows = cursor.fetchall()
        agendas = [
            Agenda(
                id_agenda=row["id_agenda"], 
                dataHora=row["dataHora"],
                disponibilidade=row["disponibilidade"],
                id_cuidador=row["id_cuidador"]) 
                for row in rows]
        return agendas

def obter_por_id(id_agenda) -> Agenda:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_agenda,))
        row = cursor.fetchone()
        agenda = Agenda(
            id_agenda=row["id_agenda"], 
            dataHora=row["dataHora"],
            disponibilidade=row["disponibilidade"],
            id_cuidador=row["id_cuidador"]
        ) 
        return agenda

def atualizar(agenda: Agenda) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_AGENDA, (
            agenda.dataHora,
            agenda.disponibilidade,
            agenda.id_cuidador,
            agenda.id_agenda
        ))
        return cursor.rowcount > 0


def excluir(id_agenda: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_AGENDA, (id_agenda,))
        return cursor.rowcount > 0
