from typing import Optional
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *
from data.usuario import usuario_repo
from data.usuario.usuario_sql import *  # para atualizar/excluir usuario
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CUIDADOR)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de cuidadores: {e}")
        return False  


def inserir(cuidador: Cuidador) -> Optional[int]:
    cuidador.id = usuario_repo.inserir(cuidador)
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CUIDADOR, (
            cuidador.id,
            cuidador.experiencia_anos
        ))
        return cursor.lastrowid


def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        cuidadores = [
            Cuidador(
                id_cuidador=row["id_cuidador"], 
                nome=row.get("nome"),
                experiencia_anos=row.get("experiencia_anos")
            )
            for row in rows
        ]
        return cuidadores


def atualizar(cuidador: Cuidador) -> bool:
    usuario_repo.atualizar(cuidador)
    with open_connection() as conn:
        cursor = conn.cursor()        
        cursor.execute(ATUALIZAR_CUIDADOR, (
            cuidador.experiencia_anos,
            cuidador.id_cuidador
        ))
        cuidador_ok = cursor.rowcount > 0
        return cuidador_ok


def excluir(id_cuidador: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CUIDADOR, (id_cuidador,))
        cuidador_excluido = cursor.rowcount > 0
        usuario_excluido = usuario_repo.excluir(id_cuidador)
        return cuidador_excluido and usuario_excluido
