from asyncio import open_connection
from typing import Optional

from data.chamado_model import Chamado
from data.chamado_sql import CRIAR_TABELA_CHAMADO, INSERIR_CHAMADO, OBTER_TODOS_CHAMADO


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CHAMADO)
        return cursor.rowcount > 0

def inserir(chamado: Chamado) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CHAMADO, (
            chamado.titulo,  
            chamado.descricao, 
            chamado.status,
            chamado.dataCriacao))
        return cursor.lastrowid

def obter_todos() -> list[Chamado]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CHAMADO)
        rows = cursor.fetchall()
        chamados = [
            Chamado(
                id=row["id"], 
                titulo=row["titulo"], 
                descricao=row["descricao"],
                status=row["status"],
                dataCriacao=row["dataCriacao"]) 
                for row in rows]
        return chamados