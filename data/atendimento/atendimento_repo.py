from typing import Optional

from data.atendimento.atendimento_model import Atendimento
from data.atendimento.atendimento_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ATENDIMENTO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de atendimentos: {e}")
        return False  

def inserir(atendimento: Atendimento) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ATENDIMENTO, (
            atendimento.dataInicio,
            atendimento.dataFim,
            atendimento.id_cliente,
            atendimento.id_cuidador
        ))
        return cursor.lastrowid

def obter_todos() -> list[Atendimento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ATENDIMENTO)
        rows = cursor.fetchall()
        atendimentos = [
            Atendimento(
                id=row["id_atendimento"],
                dataInicio=row["dataInicio"],
                dataFim=row["dataFim"],
                id_cliente=row["id_cliente"],
                id_cuidador=row["id_cuidador"]
            )
            for row in rows
        ]
        return atendimentos
 
def atualizar(atendimento: Atendimento) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ATENDIMENTO, (
            atendimento.dataInicio,
            atendimento.dataFim,
            atendimento.id
        ))
        return cursor.rowcount > 0


def excluir(atendimento_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_ATENDIMENTO, (atendimento_id,))
        return cursor.rowcount > 0
