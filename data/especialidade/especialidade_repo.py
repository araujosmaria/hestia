import sqlite3
from typing import Optional
from data.especialidade.especialidade_model import Especialidade
from data.especialidade.especialidade_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ESPECIALIDADE) 
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de especialidades: {e}")
        return False  

def inserir(especialidade: Especialidade) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ESPECIALIDADE, (
            especialidade.nome,))
        return cursor.lastrowid
    
def obter_por_id(especialidade_id: int) -> Optional[Especialidade]:
    with open_connection() as conn:
        conn.row_factory = sqlite3.Row  
        cursor = conn.cursor()
        cursor.execute(OBTER_ESPECIALIDADE_POR_ID, (especialidade_id,))
        row = cursor.fetchone()
        if row:
            return Especialidade(
                id=row["id_especialidade"],
                nome=row["nome"]
            )
        return None


def obter_todos() -> list[Especialidade]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ESPECIALIDADE)
        rows = cursor.fetchall()
        especialidade = [
            Especialidade(
                id=row["id_especialidade"], 
                nome=row["nome"]) 
                for row in rows]
        return especialidade
    
def atualizar(especialidade: Especialidade) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ESPECIALIDADE, (
            especialidade.nome,
            especialidade.id
        ))
        return cursor.rowcount > 0


def excluir(especialidade_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_ESPECIALIDADE, (especialidade_id,))
        return cursor.rowcount > 0
