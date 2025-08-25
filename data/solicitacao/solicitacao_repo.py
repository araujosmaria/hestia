from typing import Optional
from data.solicitacao.solicitacao_model import Solicitacao
from data.solicitacao.solicitacao_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_SOLICITACAO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela solicitacao: {e}")
        return False


def inserir(s: Solicitacao) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_SOLICITACAO, (s.cuidador_id, s.nome_contratante, s.descricao, s.status))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao inserir solicitacao: {e}")
        return False


def atualizar(s: Solicitacao) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_SOLICITACAO, (s.cuidador_id, s.nome_contratante, s.descricao, s.status, s.id))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar solicitacao: {e}")
        return False


def excluir(id: int) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_SOLICITACAO, (id,))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir solicitacao: {e}")
        return False


def obter_por_id(id: int) -> Optional[Solicitacao]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_SOLICITACAO_POR_ID, (id,))
            row = cursor.fetchone()
            if row:
                return Solicitacao(
                    id=row["id"],
                    cuidador_id=row["cuidador_id"],
                    nome_contratante=row["nome_contratante"],
                    descricao=row["descricao"],
                    status=row["status"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter solicitacao por ID: {e}")
        return None


def obter_por_cuidador(id_cuidador: int) -> list[Solicitacao]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_SOLICITACOES_POR_CUIDADOR, (id_cuidador,))
            rows = cursor.fetchall()
            resultado = [
                Solicitacao(
                    id=row["id"],
                    cuidador_id=row["cuidador_id"],
                    nome_contratante=row["nome_contratante"],
                    descricao=row["descricao"],
                    status=row["status"]
                )
                for row in rows
            ]
            return resultado
    except Exception as e:
        print(f"Erro ao obter solicitacoes por cuidador: {e}")
        return []
