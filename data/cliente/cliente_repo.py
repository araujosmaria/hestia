import sqlite3
from typing import Optional, List
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.usuario import usuario_repo

# Função para criar a tabela de clientes
def criar_tabela(db_path: str = "default.db") -> bool:
    try:
        # Cria tabela de usuário primeiro
        usuario_repo.criar_tabela(db_path=db_path)
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executescript(CRIAR_TABELA_CLIENTE)
            conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de clientes: {e}")
        return False

# Função para inserir um cliente
def inserir(cliente: Cliente, db_path: str = "default.db") -> Optional[int]:
    try:
        # Inserir primeiro no usuário
        id_usuario = usuario_repo.inserir(cliente, db_path=db_path)
        if id_usuario is None:
            print("Erro: inserção do usuário retornou None")
            return None

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                INSERIR_CLIENTE,
                (
                    id_usuario,
                    cliente.parentesco_paciente,
                    cliente.confirmarSenha,
                    cliente.termos,
                    cliente.verificacao,
                    cliente.comunicacoes
                )
            )
            conn.commit()
        return id_usuario
    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")
        return None

# Função para obter cliente por ID
def obter_por_id(id_cliente: int, db_path: str = "default.db") -> Optional[Cliente]:
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(OBTER_CLIENTE_POR_ID, (id_cliente,))
            row = cursor.fetchone()
            if row:
                return Cliente(
                    id=row["id_cliente"],
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
                    ativo=bool(row["ativo"]),
                    parentesco_paciente=row["parentesco_paciente"],
                    confirmarSenha=row.get("confirmarSenha", ""),
                    termos=row.get("termos", True),
                    verificacao=row.get("verificacao", True),
                    comunicacoes=row.get("comunicacoes", True)
                )
            return None
    except Exception as e:
        print(f"Erro ao obter cliente por ID: {e}")
        return None

# Função para obter todos os clientes
def obter_todos(db_path: str = "default.db") -> List[Cliente]:
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(OBTER_TODOS_CLIENTE)
            rows = cursor.fetchall()
            clientes = [
                Cliente(
                    id=row["id_cliente"],
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
                    ativo=bool(row["ativo"]),
                    parentesco_paciente=row["parentesco_paciente"],
                    confirmarSenha=row.get("confirmarSenha", ""),
                    termos=row.get("termos", True),
                    verificacao=row.get("verificacao", True),
                    comunicacoes=row.get("comunicacoes", True)
                )
                for row in rows
            ]
            return clientes
    except Exception as e:
        print(f"Erro ao obter todos os clientes: {e}")
        return []

# Função para atualizar um cliente
def atualizar(cliente: Cliente, db_path: str = "default.db") -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                ATUALIZAR_CLIENTE,
                (cliente.parentesco_paciente, bool(cliente.termos), bool(cliente.comunicacoes), cliente.id)
            )
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        return False


# Função para excluir um cliente
def excluir(id_cliente: int, db_path: str = "default.db") -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(EXCLUIR_CLIENTE, (id_cliente,))
            cliente_excluido = cursor.rowcount > 0

        usuario_excluido = usuario_repo.excluir(id_cliente, db_path=db_path)
        return cliente_excluido and usuario_excluido
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")
        return False
