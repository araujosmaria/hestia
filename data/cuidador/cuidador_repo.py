from typing import Optional

from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *
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
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CUIDADOR, (
            cuidador.nome,  
            cuidador.email, 
            cuidador.senha,
            cuidador.telefone, 
            cuidador.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        cuidadores = [
            Cuidador(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return cuidadores
    
def adicionar_especialidade(cuidador_id: int, especialidade: str) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cuidador_especialidades (cuidador_id, especialidade)
            VALUES (?, ?)
        """, (cuidador_id, especialidade))
        return cursor.rowcount > 0

def obter_especialidades(cuidador_id: int) -> list[str]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT especialidade FROM cuidador_especialidades
            WHERE cuidador_id = ?
        """, (cuidador_id,))
        rows = cursor.fetchall()
        return [row["especialidade"] for row in rows]
