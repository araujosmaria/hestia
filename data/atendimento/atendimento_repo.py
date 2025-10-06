import sqlite3
from typing import Optional, List
from data.atendimento.atendimento_model import Atendimento
from data.atendimento.atendimento_sql import *
from datetime import datetime

# Caminho padrão do banco de dados
DB_PATH = "dados.db"

def criar_tabela(db_path: str = None) -> bool:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ATENDIMENTO)
            conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de atendimentos: {e}")
        return False

def inserir(atendimento: Atendimento, db_path: str = None) -> Optional[int]:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_ATENDIMENTO, (
                atendimento.dataInicio,
                atendimento.dataFim,
                atendimento.id_cliente,
                atendimento.id_cuidador
            ))
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir atendimento: {e}")
        return None

def obter_todos(db_path: str = None) -> List[Atendimento]:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(OBTER_TODOS_ATENDIMENTO)
            rows = cursor.fetchall()
            return [
                Atendimento(
                    id=row["id_atendimento"],
                    dataInicio=datetime.fromisoformat(row["dataInicio"]),
                    dataFim=datetime.fromisoformat(row["dataFim"]),
                    id_cliente=row["id_cliente"],
                    id_cuidador=row["id_cuidador"]
                )
                for row in rows
            ]
    except Exception as e:
        print(f"Erro ao obter atendimentos: {e}")
        return []

def obter_por_id(id_atendimento: int, db_path: str = None) -> Optional[Atendimento]:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(OBTER_POR_ID_ATENDIMENTO, (id_atendimento,))
            row = cursor.fetchone()
            if row:
                return Atendimento(
                    id=row["id_atendimento"],
                    dataInicio=datetime.fromisoformat(row["dataInicio"]),
                    dataFim=datetime.fromisoformat(row["dataFim"]),
                    id_cliente=row["id_cliente"],
                    id_cuidador=row["id_cuidador"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter atendimento por ID: {e}")
        return None

def atualizar(atendimento: Atendimento, db_path: str = None) -> bool:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_ATENDIMENTO, (
                atendimento.dataInicio,
                atendimento.dataFim,
                atendimento.id
            ))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar atendimento: {e}")
        return False

def excluir(atendimento_id: int, db_path: str = None) -> bool:
    if db_path is None:
        db_path = DB_PATH
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_ATENDIMENTO, (atendimento_id,))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir atendimento: {e}")
        return False
