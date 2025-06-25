from typing import Optional

from data.avaliacao.avaliacao_model import Avaliacao
from data.avaliacao.avaliacao_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_AVALIACAO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de avaliações: {e}")
        return False  

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
    
def atualizar(avaliacao: Avaliacao) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_AVALIACAO, (
            avaliacao.nota,
            avaliacao.comentario,
            avaliacao.dataAvaliacao,
            avaliacao.id
        ))
        return cursor.rowcount > 0


def excluir(avaliacao_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_AVALIACAO, (avaliacao_id,))
        return cursor.rowcount > 0
