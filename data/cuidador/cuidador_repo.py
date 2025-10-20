
# from typing import Optional, List
# from data.cuidador.cuidador_model import Cuidador
# from data.cuidador.cuidador_sql import *
# from data.usuario import usuario_repo
# from data.usuario.usuario_model import Usuario
# from data.util import open_connection
# import sqlite3
# import uuid
# from util.db_util import get_connection

# DB_PATH = "dados.db"

# def get_dados_cuidador(id_usuario: int) -> Optional[Cuidador]:
#     query = """
#     SELECT especialidade, experiencia, valorHora, escolaridade, apresentacao
#     FROM cuidador
#     WHERE id_usuario = ?
#     """
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(query, (id_usuario,))
#         row = cursor.fetchone()
#         if row:
#             return Cuidador(
#                 id_usuario=id_usuario,
#                 especialidade=row["especialidade"],
#                 experiencia=row["experiencia"],
#                 valorHora=row["valorHora"],
#                 escolaridade=row["escolaridade"],
#                 apresentacao=row["apresentacao"]
#             )
#     return None

# def criar_tabela(db_path: str = None) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         usuario_repo.criar_tabela(db_path=db_path)
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.executescript(CRIAR_TABELA_CUIDADOR)
#             conn.commit()
#         return True
#     except Exception as e:
#         print(f"Erro ao criar tabela de cuidadores: {e}")
#         return False

# def inserir(cuidador: Cuidador, db_path: str = None) -> Optional[int]:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         usuario = Usuario(
#             id=None,
#             nome=cuidador.nome,
#             dataNascimento=cuidador.dataNascimento,
#             email=cuidador.email,
#             telefone=cuidador.telefone,
#             cpf=cuidador.cpf,
#             senha=cuidador.senha,
#             perfil=cuidador.perfil,
#             token_redefinicao=cuidador.token_redefinicao,
#             data_token=cuidador.data_token,
#             data_cadastro=cuidador.data_cadastro,
#             cep=cuidador.cep,
#             logradouro=cuidador.logradouro,
#             numero=cuidador.numero,
#             complemento=cuidador.complemento,
#             bairro=cuidador.bairro,
#             cidade=cuidador.cidade,
#             estado=cuidador.estado,
#             ativo=True,
#             foto=cuidador.foto
#         )
#         id_usuario = usuario_repo.inserir(usuario, db_path=db_path)
#         if id_usuario is None:
#             return None

#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(INSERIR_CUIDADOR, (
#                 id_usuario,
#                 cuidador.experiencia,
#                 cuidador.valorHora,
#                 cuidador.escolaridade,
#                 cuidador.apresentacao,
#                 cuidador.cursos,
#                 cuidador.inicio_profissional,
#                 cuidador.confirmarSenha,
#                 int(cuidador.termos),
#                 int(cuidador.verificacao),
#                 int(cuidador.comunicacoes),
#             ))
#             conn.commit()
#         return id_usuario
#     except Exception as e:
#         print(f"Erro ao inserir cuidador: {e}")
#         return None



# def obter_por_id(id_cuidador: int, db_path: str = None) -> Optional[Cuidador]:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()
#             cursor.execute(OBTER_CUIDADOR_POR_ID, (id_cuidador,))
#             row = cursor.fetchone()
#             if row:
#                 return Cuidador(
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
#                     ativo=bool(row["ativo"]),
#                     experiencia=row["experiencia"],
#                     valorHora=row["valorHora"],
#                     escolaridade=row["escolaridade"],
#                     apresentacao=row["apresentacao"],
#                     cursos=row["cursos"],
#                     confirmarSenha=row["confirmarSenha"],
#                     termos=bool(row["termos"]),
#                     verificacao=bool(row["verificacao"]),
#                     comunicacoes=bool(row["comunicacoes"]),
#                     inicio_profissional=row["inicio_profissional"],
#                 )
#             return None
#     except Exception as e:
#         print(f"Erro ao obter cuidador por id: {e}")
#         return None


# def obter_todos(db_path: str = None) -> List[Cuidador]:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()
#             cursor.execute(OBTER_TODOS_CUIDADORES)
#             rows = cursor.fetchall()
#             return [
#                 Cuidador(
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
#                     ativo=bool(row["ativo"]),
#                     experiencia=row["experiencia"],
#                     valorHora=row["valorHora"],
#                     escolaridade=row["escolaridade"],
#                     apresentacao=row["apresentacao"],
#                     cursos=row["cursos"],
#                     confirmarSenha=row["confirmarSenha"],
#                     termos=bool(row["termos"]),
#                     verificacao=bool(row["verificacao"]),
#                     comunicacoes=bool(row["comunicacoes"]),
#                     inicio_profissional=row["inicio_profissional"],
#                 )
#                 for row in rows
#             ]
#     except Exception as e:
#         print(f"Erro ao obter todos os cuidadores: {e}")
#         return []



# def atualizar(cuidador: Cuidador, db_path: str = None) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(ATUALIZAR_CUIDADOR, (
#                 cuidador.experiencia,
#                 cuidador.valorHora,
#                 cuidador.escolaridade,
#                 cuidador.apresentacao,
#                 cuidador.cursos,
#                 cuidador.confirmarSenha,
#                 int(cuidador.termos),
#                 int(cuidador.verificacao),
#                 int(cuidador.comunicacoes),
#                 cuidador.inicio_profissional,
#                 cuidador.id
#             ))
#             conn.commit()
#             return cursor.rowcount > 0
#     except Exception as e:
#         print(f"Erro ao atualizar cuidador: {e}")
#         return False


# def excluir(id_cuidador: int, db_path: str = None) -> bool:
#     if db_path is None:
#         db_path = DB_PATH
#     try:
#         with sqlite3.connect(db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(EXCLUIR_CUIDADOR, (id_cuidador,))
#             conn.commit()
#             return cursor.rowcount > 0
#     except Exception as e:
#         print(f"Erro ao excluir cuidador: {e}")
#         return False

from typing import Optional
from data.usuario import usuario_repo
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *
from data.usuario.usuario_model import Usuario
from util.db_util import get_connection


def criar_tabela() -> bool:
    """Cria a tabela de cuidador (se não existir)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CUIDADOR)
        return True



def inserir(cuidador: Cuidador) -> Optional[int]:
    """Insere um novo cuidador (e o respectivo usuário), evitando CPF duplicado."""
    with get_connection() as conn:
        cursor = conn.cursor()

        # Verifica se o CPF já existe
        cursor.execute("SELECT id_usuario FROM usuario WHERE cpf = ?", (cuidador.cpf,))
        if cursor.fetchone():
            print(f"Erro: CPF {cuidador.cpf} já cadastrado")
            return None

        # Cria o usuário primeiro
        usuario = Usuario(
            nome=cuidador.nome,
            dataNascimento=cuidador.dataNascimento,
            email=cuidador.email,
            telefone=cuidador.telefone,
            cpf=cuidador.cpf,
            senha=cuidador.senha,
            perfil=cuidador.perfil,
            foto=cuidador.foto,
            token_redefinicao=cuidador.token_redefinicao,
            data_token=cuidador.data_token,
            data_cadastro=cuidador.data_cadastro,
            cep=cuidador.cep,
            logradouro=cuidador.logradouro,
            numero=cuidador.numero,
            complemento=cuidador.complemento,
            bairro=cuidador.bairro,
            cidade=cuidador.cidade,
            estado=cuidador.estado,
            ativo=cuidador.ativo
        )
        id_usuario = usuario_repo.inserir(usuario, cursor)
        if id_usuario is None:
            return None

        # Insere os dados específicos do cuidador
        cursor.execute(INSERIR_CUIDADOR, (
            id_usuario,
            cuidador.experiencia,
            cuidador.valorHora,
            cuidador.escolaridade,
            cuidador.apresentacao,
            cuidador.cursos,
            cuidador.inicio_profissional,
            cuidador.confirmarSenha,
            cuidador.termos,
            cuidador.verificacao,
            cuidador.comunicacoes
        ))

        conn.commit()
        return id_usuario

def atualizar(cuidador: Cuidador) -> bool:
    """Atualiza informações do cuidador e do usuário associado."""
    with get_connection() as conn:
        cursor = conn.cursor()

        # Atualiza o usuário vinculado
        usuario = Usuario(
            id=cuidador.id,
            nome=cuidador.nome,
            dataNascimento=cuidador.dataNascimento,
            email=cuidador.email,
            telefone=cuidador.telefone,
            cpf=cuidador.cpf,
            senha=cuidador.senha,
            perfil=cuidador.perfil,
            foto=cuidador.foto,
            token_redefinicao=cuidador.token_redefinicao,
            data_token=cuidador.data_token,
            data_cadastro=cuidador.data_cadastro,
            cep=cuidador.cep,
            logradouro=cuidador.logradouro,
            numero=cuidador.numero,
            complemento=cuidador.complemento,
            bairro=cuidador.bairro,
            cidade=cuidador.cidade,
            estado=cuidador.estado,
            ativo=cuidador.ativo
        )
        usuario_repo.alterar(usuario, cursor)

        # Atualiza os dados específicos do cuidador
        cursor.execute(ATUALIZAR_CUIDADOR, (
            cuidador.experiencia,
            cuidador.valorHora,
            cuidador.escolaridade,
            cuidador.apresentacao,
            cuidador.cursos,
            cuidador.confirmarSenha,
            cuidador.termos,
            cuidador.verificacao,
            cuidador.comunicacoes,
            cuidador.inicio_profissional,
            cuidador.id
        ))

        conn.commit()
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    """Exclui um cuidador e seu usuário."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CUIDADOR, (id,))
        usuario_repo.excluir(id, cursor)
        conn.commit()
        return cursor.rowcount > 0


def obter_por_id(id: int) -> Optional[Cuidador]:
    """Obtém um cuidador pelo ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CUIDADOR_POR_ID, (id,))
        row = cursor.fetchone()

        if not row:
            return None

        return Cuidador(
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
            experiencia=row["experiencia"],
            valorHora=row["valorHora"],
            escolaridade=row["escolaridade"],
            apresentacao=row["apresentacao"],
            cursos=row["cursos"],
            inicio_profissional=row["inicio_profissional"],
            confirmarSenha=row["confirmarSenha"],
            termos=row["termos"],
            verificacao=row["verificacao"],
            comunicacoes=row["comunicacoes"]
        )


def obter_todos() -> list[Cuidador]:
    """Obtém todos os cuidadores cadastrados."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADORES)
        rows = cursor.fetchall()

        return [
            Cuidador(
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
                experiencia=row["experiencia"],
                valorHora=row["valorHora"],
                escolaridade=row["escolaridade"],
                apresentacao=row["apresentacao"],
                cursos=row["cursos"],
                inicio_profissional=row["inicio_profissional"],
                confirmarSenha=row["confirmarSenha"],
                termos=row["termos"],
                verificacao=row["verificacao"],
                comunicacoes=row["comunicacoes"]
            )
            for row in rows
        ]

