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

def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_USUARIO)
            cursor.execute(CORRIGIR_PERFIL_NULO)  # <- aqui faz o update após a criação da tabela
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de usuarios: {e}")
        return False


def inserir(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO, (
            usuario.nome,
            usuario.dataNascimento,
            usuario.email,
            usuario.telefone,
            usuario.cpf,
            usuario.senha,
            usuario.perfil,
            usuario.foto,
            usuario.token_redefinicao,
            usuario.data_token,
            usuario.data_cadastro,
            usuario.cep,
            usuario.logradouro,
            usuario.numero,
            usuario.complemento,
            usuario.bairro,
            usuario.cidade,
            usuario.estado,
            usuario.ativo))
        return cursor.lastrowid

def obter_todos() -> list[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIOS)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id_usuario"], 
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                perfil=row["perfil"],
                foto=row["foto"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=row["ativo"]) 
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
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                perfil=row["perfil"],
                foto=row["foto"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=row["ativo"])
        return None
    
def obter_por_email(email: str) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_EMAIL, (email,))
        row = cursor.fetchone()

        if row:
            return Usuario(
                id=row["id_usuario"],
                nome=row["nome"],
                dataNascimento=row["dataNascimento"],
                email=row["email"],
                telefone=row["telefone"],
                cpf=row["cpf"],
                senha=row["senha"],  
                perfil=row["perfil"],
                foto=row["foto"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"],
                data_cadastro=row["data_cadastro"],
                cep=row["cep"],
                logradouro=row["logradouro"],
                numero=row["numero"],
                complemento=row["complemento"],
                bairro=row["bairro"],
                cidade=row["cidade"],
                estado=row["estado"],
                ativo=row["ativo"]
            )
        return None
  
def atualizar(usuario: Usuario) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_USUARIO, (
            usuario.nome,
            usuario.dataNascimento,
            usuario.email,
            usuario.telefone,
            usuario.cpf,
            usuario.perfil,
            usuario.foto,
            usuario.token_redefinicao,
            usuario.data_token,
            usuario.data_cadastro,
            usuario.cep,
            usuario.logradouro,
            usuario.numero,
            usuario.complemento,
            usuario.bairro,
            usuario.cidade,
            usuario.estado,
            usuario.ativo,
            usuario.id

        ))
        return cursor.rowcount > 0


def excluir(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_USUARIO, (usuario_id,))
        return cursor.rowcount > 0

def validar_token(token: str) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(VALIDAR_TOKEN, (token,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id_usuario"], 
                nome=row["nome"], 
                email=row["email"],
                token_redefinicao=row["token_redefinicao"],
                data_token=row["data_token"])
        return None
    
def ativar_usuario(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATIVAR_USUARIO, (usuario_id,))
        return cursor.rowcount > 0

def atualizar_foto(id: int, caminho_foto: str) -> bool:
    """Atualiza apenas a foto do usuário"""
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_FOTO, (caminho_foto, id))
        return cursor.rowcount > 0


# def atualizar_senha(email: str, nova_senha: str) -> bool:
#     try:
#         with open_connection() as conn:
#             cursor = conn.cursor()
#             cursor.execute("""
#                 UPDATE usuario SET senha = %s WHERE email = %s
#             """, (nova_senha, email))
#             conn.commit()
#             return cursor.rowcount > 0  # retorna True se alguma linha foi alterada
#     except Exception as e:
#         print(f"Erro ao atualizar senha: {e}")
#         return False
