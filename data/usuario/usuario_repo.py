from typing import Optional
import sqlite3
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_USUARIO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de usuarios: {e}")
        return False  

def inserir(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO, (
            usuario.nome,  
            usuario.email, 
            usuario.senha,
            usuario.telefone, 
            usuario.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIO)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id_usuario"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return usuarios
    
def obter_por_id(id_usuario: int) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_ID,(id_usuario,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"])
        
        return None
  
def atualizar(usuario: Usuario) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_USUARIO, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.telefone,
            usuario.endereco,
            usuario.id
        ))
        return cursor.rowcount > 0


def excluir(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_USUARIO, (usuario_id,))
        return cursor.rowcount > 0
