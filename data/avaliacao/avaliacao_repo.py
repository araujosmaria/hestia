from asyncio import open_connection
from typing import Optional

from data.avaliacao_model import Avaliacao
from data.avaliacao_sql import CRIAR_TABELA_AVALIACAO, INSERIR_AVALIACAO, OBTER_TODOS_AVALIACAO


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_AVALIACAO)
        return cursor.rowcount > 0

def inserir(avaliacao: Avaliacao) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_AVALIACAO, (
            avaliacao.nota,  
            avaliacao.comentario, 
            avaliacao.dataAvaliacao))
        return cursor.lastrowid

def obter_todos() -> list[Avaliacao]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_AVALIACAO)
        rows = cursor.fetchall()
        avaliacoes = [
            Avaliacao(
                id=row["id"], 
                nota=row["nota"], 
                comentario=row["comentario"],
                dataAvaliacao=row["dataAvaliacao"]) 
                for row in rows]
        return avaliacoes