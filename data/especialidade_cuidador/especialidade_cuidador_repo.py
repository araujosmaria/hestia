from typing import Optional
from data.especialidade_cuidador.especialidade_cuidador_model import EspecialidadeCuidador
from data.especialidade_cuidador.especialidade_cuidador_sql import *
from data.util import open_connection
from data.cuidador import cuidador_repo
from data.especialidade import especialidade_repo


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ESPECIALIDADE_CUIDADOR)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela especialidade_cuidador: {e}")
        return False


def inserir(ec: EspecialidadeCuidador) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_ESPECIALIDADE_CUIDADOR, (ec.id_cuidador, ec.id_especialidade, ec.anos_experiencia))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao inserir especialidade do cuidador: {e}")
        return False
    
def atualizar(ec: EspecialidadeCuidador) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_ESPECIALIDADE_CUIDADOR, (ec.anos_experiencia, ec.id_cuidador, ec.id_especialidade))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar especialidade do cuidador: {e}")
        return False
    
def excluir(id_cuidador: int, id_especialidade: int) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_ESPECIALIDADE_CUIDADOR, (id_cuidador, id_especialidade))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir especialidade do cuidador: {e}")
        return False


def obter_especialidades_por_cuidador(id_cuidador: int) -> list[EspecialidadeCuidador]:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_ESPECIALIDADES_POR_CUIDADOR, (id_cuidador,))
            rows = cursor.fetchall()
            resultado = [EspecialidadeCuidador(
                id_cuidador=row["id_cuidador"],
                id_especialidade=row["id_especialidade"],
                anos_experiencia=row["anos_experiencia"],
                cuidador=cuidador_repo.obter_por_id(row["id_cuidador"]),
                especialidade=especialidade_repo.obter_por_id(row["id_especialidade"]))
                for row in rows]
            return resultado
    except Exception as e:
        print(f"Erro ao obter especialidades dos cuidadores: {e}")
        return []
