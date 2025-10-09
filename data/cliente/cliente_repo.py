# import sqlite3
# from typing import Optional, List
# from data.cliente.cliente_model import Cliente
# from data.cliente.cliente_sql import (
#     CRIAR_TABELA_CLIENTE,
#     INSERIR_CLIENTE,
#     OBTER_CLIENTE_POR_ID,
#     OBTER_TODOS_CLIENTE,
#     ATUALIZAR_CLIENTE,
#     EXCLUIR_CLIENTE,
# )
# from data.usuario import usuario_repo
# from data.usuario.usuario_model import Usuario

# # Banco fixo da aplicação
# DB_PATH = "dados.db"

# def criar_tabela(db_path: str = DB_PATH) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         usuario_repo.criar_tabela(db_path=db_path)
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.executescript(CRIAR_TABELA_CLIENTE)
#             conn.commit()
#         return True
#     except Exception as e:
#         print(f"Erro ao criar tabela de clientes: {e}")
#         return False

# def inserir(cliente: Cliente, db_path: str = DB_PATH) -> Optional[int]:
#     try:
#         # Converte Cliente em Usuario
#         usuario = Usuario(
#             id=None,  # precisa ser None para AUTOINCREMENT do usuário
#             nome=cliente.nome,
#             dataNascimento=cliente.dataNascimento,
#             email=cliente.email,
#             telefone=cliente.telefone,
#             cpf=cliente.cpf,
#             senha=cliente.senha,
#             perfil=cliente.perfil,
#             token_redefinicao=cliente.token_redefinicao,
#             data_token=cliente.data_token,
#             data_cadastro=cliente.data_cadastro,
#             cep=cliente.cep,
#             logradouro=cliente.logradouro,
#             numero=cliente.numero,
#             complemento=cliente.complemento,
#             bairro=cliente.bairro,
#             cidade=cliente.cidade,
#             estado=cliente.estado,
#             ativo=True,
#             foto=cliente.foto
#         )

#         # Insere usuário
#         id_usuario = usuario_repo.inserir(usuario, db_path=db_path)
#         if id_usuario is None:
#             print("Erro: inserção do usuário retornou None")
#             return None

#         # Insere dados específicos do cliente
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(
#                 INSERIR_CLIENTE,
#                 (
#                     id_usuario,
#                     cliente.parentesco_paciente,
#                     cliente.confirmarSenha,
#                     int(cliente.termos),
#                     int(cliente.verificacao),
#                     int(cliente.comunicacoes),
#                 ),
#             )
#             conn.commit()
#         return id_usuario
#     except Exception as e:
#         print(f"Erro ao inserir cliente: {e}")
#         return None


# def obter_por_id(id_cliente: int, db_path: str = DB_PATH) -> Optional[Cliente]:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()
#             cursor.execute(OBTER_CLIENTE_POR_ID, (id_cliente,))
#             row = cursor.fetchone()
#             if row:
#                 return Cliente(
#                     id=row["id"],
#                     nome=row["nome"],
#                     dataNascimento=row["dataNascimento"],
#                     email=row["email"],
#                     telefone=row["telefone"],
#                     cpf=row["cpf"],
#                     senha=row["senha"],
#                     perfil=row["perfil"],
#                     foto=row["foto"],
#                     token_redefinicao=row["token_redefinicao"],
#                     data_token=row["data_token"],
#                     data_cadastro=row["data_cadastro"],
#                     cep=row["cep"],
#                     logradouro=row["logradouro"],
#                     numero=row["numero"],
#                     complemento=row["complemento"],
#                     bairro=row["bairro"],
#                     cidade=row["cidade"],
#                     estado=row["estado"],
#                     ativo=True,  # sempre True para cliente inserido
#                     parentesco_paciente=row["parentesco_paciente"],
#                     confirmarSenha=row["confirmarSenha"] or "",
#                     termos=bool(row["termos"]),
#                     verificacao=bool(row["verificacao"]),
#                     comunicacoes=bool(row["comunicacoes"]),
#                 )
#             return None
#     except Exception as e:
#         print(f"Erro ao obter cliente por ID: {e}")
#         return None


# def obter_todos(db_path: str = DB_PATH) -> List[Cliente]:
#     try:
#         with sqlite3.connect(db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()
#             cursor.execute(OBTER_TODOS_CLIENTE)
#             rows = cursor.fetchall()
#             return [
#                 Cliente(
#                     id=row["id"],
#                     nome=row["nome"],
#                     dataNascimento=row["dataNascimento"],
#                     email=row["email"],
#                     telefone=row["telefone"],
#                     cpf=row["cpf"],
#                     senha=row["senha"],
#                     perfil=row["perfil"],
#                     foto=row["foto"],
#                     token_redefinicao=row["token_redefinicao"],
#                     data_token=row["data_token"],
#                     data_cadastro=row["data_cadastro"],
#                     cep=row["cep"],
#                     logradouro=row["logradouro"],
#                     numero=row["numero"],
#                     complemento=row["complemento"],
#                     bairro=row["bairro"],
#                     cidade=row["cidade"],
#                     estado=row["estado"],
#                     parentesco_paciente=row["parentesco_paciente"],
#                     confirmarSenha=row["confirmarSenha"],
#                     termos=bool(row["termos"]),
#                     verificacao=bool(row["verificacao"]),
#                     comunicacoes=bool(row["comunicacoes"]),
#                 )
#                 for row in rows
#             ]
#     except Exception as e:
#         print(f"Erro ao obter todos os clientes: {e}")
#         return []


# def atualizar(cliente: Cliente, db_path: str = DB_PATH) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(
#                 ATUALIZAR_CLIENTE,
#                 (
#                     cliente.parentesco_paciente,
#                     bool(cliente.termos),
#                     bool(cliente.comunicacoes),
#                     cliente.id,
#                 ),
#             )
#             conn.commit()
#             return cursor.rowcount > 0
#     except Exception as e:
#         print(f"Erro ao atualizar cliente: {e}")
#         return False


# def excluir(id_cliente: int, db_path: str = DB_PATH) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(EXCLUIR_CLIENTE, (id_cliente,))
#             cliente_excluido = cursor.rowcount > 0

#         usuario_excluido = usuario_repo.excluir(id_cliente, db_path=db_path)
#         return cliente_excluido and usuario_excluido
#     except Exception as e:
#         print(f"Erro ao excluir cliente: {e}")
#         return False

from typing import Optional
from data.usuario import usuario_repo
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.usuario.usuario_model import Usuario
from util.db_util import get_connection


def criar_tabela() -> bool:
    """Cria a tabela de cliente (se não existir)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CLIENTE)
        return True


def inserir(cliente: Cliente) -> Optional[int]:
    """Insere um novo cliente (e o respectivo usuário)."""
    with get_connection() as conn:
        cursor = conn.cursor()

        # Cria o usuário primeiro
        usuario = Usuario(
            nome=cliente.nome,
            dataNascimento=cliente.dataNascimento,
            email=cliente.email,
            telefone=cliente.telefone,
            cpf=cliente.cpf,
            senha=cliente.senha,
            perfil=cliente.perfil,
            foto=cliente.foto,
            token_redefinicao=cliente.token_redefinicao,
            data_token=cliente.data_token,
            data_cadastro=cliente.data_cadastro,
            cep=cliente.cep,
            logradouro=cliente.logradouro,
            numero=cliente.numero,
            complemento=cliente.complemento,
            bairro=cliente.bairro,
            cidade=cliente.cidade,
            estado=cliente.estado,
            ativo=cliente.ativo
        )
        id_usuario = usuario_repo.inserir(usuario, cursor)

        # Insere os dados específicos de cliente
        cursor.execute(INSERIR_CLIENTE, (
            id_usuario,
            cliente.parentesco_paciente,
            cliente.confirmarSenha,
            cliente.termos,
            cliente.verificacao,
            cliente.comunicacoes
        ))

        conn.commit()
        return id_usuario


def atualizar(cliente: Cliente) -> bool:
    """Atualiza informações do cliente e do usuário associado."""
    with get_connection() as conn:
        cursor = conn.cursor()

        usuario = Usuario(
            id_usuario=cliente.id,
            nome=cliente.nome,
            dataNascimento=cliente.dataNascimento,
            email=cliente.email,
            telefone=cliente.telefone,
            cpf=cliente.cpf,
            senha=cliente.senha,
            perfil=cliente.perfil,
            foto=cliente.foto,
            token_redefinicao=cliente.token_redefinicao,
            data_token=cliente.data_token,
            data_cadastro=cliente.data_cadastro,
            cep=cliente.cep,
            logradouro=cliente.logradouro,
            numero=cliente.numero,
            complemento=cliente.complemento,
            bairro=cliente.bairro,
            cidade=cliente.cidade,
            estado=cliente.estado,
            ativo=cliente.ativo
        )
        usuario_repo.atualizar(usuario, cursor)

        cursor.execute(ATUALIZAR_CLIENTE, (
            cliente.parentesco_paciente,
            cliente.termos,
            cliente.comunicacoes,
            cliente.id
        ))

        conn.commit()
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    """Exclui um cliente e seu usuário."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CLIENTE, (id,))
        usuario_repo.excluir(id, cursor)
        conn.commit()
        return cursor.rowcount > 0


def obter_por_id(id: int) -> Optional[Cliente]:
    """Obtém um cliente pelo ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE_POR_ID, (id,))
        row = cursor.fetchone()

        if not row:
            return None

        return Cliente(
            id=row["id"],
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
            ativo=row["ativo"],
            parentesco_paciente=row["parentesco_paciente"],
            confirmarSenha=row["confirmarSenha"],
            termos=row["termos"],
            verificacao=row["verificacao"],
            comunicacoes=row["comunicacoes"]
        )


def obter_todos() -> list[Cliente]:
    """Obtém todos os clientes cadastrados."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CLIENTE)
        rows = cursor.fetchall()

        return [
            Cliente(
                id=row["id"],
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
                ativo=row["ativo"],
                parentesco_paciente=row["parentesco_paciente"],
                confirmarSenha=row["confirmarSenha"],
                termos=row["termos"],
                verificacao=row["verificacao"],
                comunicacoes=row["comunicacoes"]
            )
            for row in rows
        ]
