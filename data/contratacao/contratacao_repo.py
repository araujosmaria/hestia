from typing import Optional, List
from data.contratacao.contratacao_model import Contratacao
from data.contratacao.contratacao_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CONTRATACAO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela contratacao: {e}")
        return False


def inserir(c: Contratacao) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_CONTRATACAO, (
                c.cuidador_id,
                c.nome_contratante,
                c.data_inicio,
                c.data_fim,
                c.observacoes,
                c.status
            ))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao inserir contratacao: {e}")
        return False


def atualizar(c: Contratacao) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_CONTRATACAO, (
                c.cuidador_id,
                c.nome_contratante,
                c.data_inicio,
                c.data_fim,
                c.observacoes,
                c.status,
                c.id
            ))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar contratacao: {e}")
        return False


def excluir(id: int) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_CONTRATACAO, (id,))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir contratacao: {e}")
        return False


def obter_por_id(id: int) -> Optional[Contratacao]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_CONTRATACAO_POR_ID, (id,))
            row = cursor.fetchone()
            if row:
                return Contratacao(
                    id=row["id"],
                    cuidador_id=row["cuidador_id"],
                    nome_contratante=row["nome_contratante"],
                    data_inicio=row["data_inicio"],
                    data_fim=row["data_fim"],
                    observacoes=row["observacoes"],
                    status=row["status"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter contratacao por ID: {e}")
        return None


def obter_por_cuidador(id_cuidador: int) -> List[Contratacao]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_CONTRATACOES_POR_CUIDADOR, (id_cuidador,))
            rows = cursor.fetchall()
            resultado = [
                Contratacao(
                    id=row["id"],
                    cuidador_id=row["cuidador_id"],
                    nome_contratante=row["nome_contratante"],
                    data_inicio=row["data_inicio"],
                    data_fim=row["data_fim"],
                    observacoes=row["observacoes"],
                    status=row["status"]
                )
                for row in rows
            ]
            return resultado
    except Exception as e:
        print(f"Erro ao obter contratacoes por cuidador: {e}")
        return []
