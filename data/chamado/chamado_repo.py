from typing import Optional

from data.chamado.chamado_model import Chamado
from data.chamado.chamado_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CHAMADO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de chamados: {e}")
        return False  

def inserir(chamado: Chamado) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CHAMADO, (
            chamado.titulo,
            chamado.descricao,
            chamado.status,
            chamado.data_criacao,
            chamado.id_administrador  # <- campo faltando
        ))
        return cursor.lastrowid

def obter_todos() -> list[Chamado]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CHAMADOS)
        rows = cursor.fetchall()
        chamados = [
            Chamado(
                id=row["id_chamado"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                status=row["status"],
                data_criacao=row["dataCriacao"],
                id_administrador=row["id_administrador"]
            )
            for row in rows
        ]
        return chamados


def atualizar(chamado: Chamado) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_CHAMADO, (
            chamado.titulo,
            chamado.descricao,
            chamado.status,
            chamado.data_criacao,
            chamado.id_administrador,  # faltava este campo aqui
            chamado.id  # id do chamado para WHERE
        ))
        return cursor.rowcount > 0


def excluir(chamado_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CHAMADO, (chamado_id,))
        return cursor.rowcount > 0
