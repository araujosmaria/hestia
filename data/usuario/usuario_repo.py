import sqlite3
from typing import Optional, List
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import (CRIAR_TABELA_USUARIO, INSERIR_USUARIO, OBTER_USUARIO_POR_ID, OBTER_USUARIO_POR_CPF, OBTER_TODOS_USUARIOS, ATUALIZAR_USUARIO, EXCLUIR_USUARIO)

DB_PATH = "hestia.db"  # caminho fixo do banco, pode ajustar se quiser parametrizar

def criar_conexao() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela(db_path: str = "default.db") -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executescript(CRIAR_TABELA_USUARIO)
            conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de usuários: {e}")
        return False

def inserir(usuario: Usuario, db_path: str = "default.db") -> Optional[int]:
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_USUARIO, (
                usuario.nome, usuario.dataNascimento, usuario.email, usuario.telefone,
                usuario.cpf, usuario.senha, usuario.perfil,
                usuario.token_redefinicao, usuario.data_token, usuario.data_cadastro,
                usuario.cep, usuario.logradouro, usuario.numero, usuario.complemento,
                usuario.bairro, usuario.cidade, usuario.estado, int(usuario.ativo),
                usuario.foto
            ))
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        return None

def obter_por_id(id_usuario: int, db_path: str = "default.db") -> Optional[Usuario]:
    try:
        with criar_conexao() as conn:
            cursor = conn.execute(OBTER_USUARIO_POR_ID, (id_usuario,))
            row = cursor.fetchone()
            if row:
                # mapear explicitamente as colunas
                return Usuario(
                    id=row["id_usuario"],
                    nome=row["nome"],
                    dataNascimento=row["dataNascimento"],
                    email=row["email"],
                    telefone=row["telefone"],
                    cpf=row["cpf"],
                    senha=row["senha"],
                    perfil=row["perfil"],
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
                    ativo=bool(row["ativo"]),
                    foto=row["foto"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter usuário por ID: {e}")
        return None

def obter_por_cpf(cpf: str, db_path: str = "default.db") -> Optional[Usuario]:
    try:
        with criar_conexao() as conn:
            cursor = conn.execute(OBTER_USUARIO_POR_CPF, (cpf,))
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
                    ativo=bool(row["ativo"]),
                    foto=row["foto"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter usuário por CPF: {e}")
        return None


def obter_todos(db_path: str = "default.db") -> list[Usuario]:
    try:
        with criar_conexao() as conn:
            cursor = conn.execute(OBTER_TODOS_USUARIOS)
            return [
                Usuario(
                    id=row["id_usuario"],
                    nome=row["nome"],
                    dataNascimento=row["dataNascimento"],
                    email=row["email"],
                    telefone=row["telefone"],
                    cpf=row["cpf"],
                    senha=row["senha"],
                    perfil=row["perfil"],
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
                    ativo=bool(row["ativo"]),
                    foto=row["foto"]
                )
                for row in cursor.fetchall()
            ]
    except Exception as e:
        print(f"Erro ao obter todos os usuários: {e}")
        return []


def atualizar(usuario: Usuario, db_path: str = "default.db") -> bool:
    try:
        with criar_conexao() as conn:
            cursor = conn.execute(ATUALIZAR_USUARIO, (
                usuario.nome, usuario.dataNascimento, usuario.email, usuario.telefone,
                usuario.cpf, usuario.senha, usuario.perfil,
                usuario.token_redefinicao, usuario.data_token, usuario.data_cadastro,
                usuario.cep, usuario.logradouro, usuario.numero, usuario.complemento,
                usuario.bairro, usuario.cidade, usuario.estado, int(usuario.ativo),
                usuario.foto, usuario.id
            ))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        return False

def excluir(id_usuario: int, db_path: str = "default.db") -> bool:
    try:
        with criar_conexao() as conn:
            cursor = conn.execute(EXCLUIR_USUARIO, (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
        return False
