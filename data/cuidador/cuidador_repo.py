from typing import Optional
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
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
    try:
        # Inserir usuário primeiro
        usuario = Usuario(
            id=0,
            nome=cuidador.nome,
            email=cuidador.email,
            senha=cuidador.senha,
            telefone=cuidador.telefone,
            endereco=cuidador.endereco
        )
        id_usuario = usuario_repo.inserir(usuario)
        if id_usuario is None:
            print("Erro: inserção do usuário retornou None")
            return None

        # Inserir cuidador
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cuidador (id_cuidador, experiencia_anos) VALUES (?, ?)",
                (id_usuario, cuidador.experiencia_anos)
            )
            conn.commit()
            return id_usuario

    except Exception as e:
        print(f"Erro ao inserir cuidador: {e}")
        return None


def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        cuidadores = [
            Cuidador(
                id=row["id_cuidador"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"],
                experiencia_anos=row["experiencia_anos"]
            ) for row in rows
        ]
        return cuidadores

def obter_por_id(id_cuidador: int) -> Optional[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CUIDADOR_POR_ID, (id_cuidador,))
        row = cursor.fetchone()
        if row:
            return Cuidador(
                id=row["id_cuidador"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"],
                experiencia_anos=row["experiencia_anos"]
            )
        return None

def atualizar(cuidador: Cuidador) -> bool:
    # Atualiza primeiro a tabela usuário
    usuario_atualizado = usuario_repo.atualizar(cuidador)
    if not usuario_atualizado:
        return False

    # Depois atualiza a tabela cuidador (somente experiencia_anos)
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cuidador SET experiencia_anos = ? WHERE id_cuidador = ?",
            (cuidador.experiencia_anos, cuidador.id)
        )
        conn.commit()
        return cursor.rowcount > 0

def excluir(id_cuidador: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CUIDADOR, (id_cuidador,))
        cuidador_excluido = cursor.rowcount > 0
    usuario_excluido = usuario_repo.excluir(id_cuidador)
    return cuidador_excluido and usuario_excluido


# from typing import Optional
# from data.cuidador.cuidador_model import Cuidador
# from data.cuidador.cuidador_sql import *
# from data.usuario import usuario_repo
# from data.usuario.usuario_sql import * 
# from data.util import open_connection 

# def criar_tabela() -> bool:
#     try:
#         with open_connection() as conn:
#             cursor = conn.cursor()
#             cursor.execute(CRIAR_TABELA_CUIDADOR)
#             return True
#     except Exception as e:
#         print(f"Erro ao criar tabela de cuidadores: {e}")
#         return False


# def inserir(cuidador: Cuidador) -> Optional[int]:
#     try:
#         with open_connection() as conn:
#             cursor = conn.cursor()
#             cursor.execute(INSERIR_CUIDADOR, (
#                 cuidador.nome,
#                 cuidador.email,
#                 cuidador.senha,
#                 cuidador.telefone,
#                 cuidador.endereco,
#                 cuidador.experiencia_anos
#             ))
#             conn.commit()
#             return cursor.lastrowid
#     except Exception as e:
#         print(f"Erro ao inserir cuidador: {e}")
#         return None
 


# def obter_todos() -> list[Cuidador]:
#     with open_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(OBTER_TODOS_CUIDADOR)
#         rows = cursor.fetchall()
#         cuidadores = [
#             Cuidador(
#                 id=row["id_cuidador"],
#                 nome=row["nome"],
#                 email=row["email"],
#                 senha=row["senha"],
#                 telefone=row["telefone"],
#                 endereco=row["endereco"],
#                 experiencia_anos=row["experiencia_anos"]
#             )
#             for row in rows
#         ]
#         return cuidadores



# def obter_por_id(id_cuidador: int) -> Optional[Cuidador]:
#     with open_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(OBTER_CUIDADOR_POR_ID, (id_cuidador,))
#         row = cursor.fetchone()
#         if row:
#             # Mapeia a linha do banco de dados para um objeto Cuidador
#             return Cuidador(
#                 # CORRIGIDO: Passando 'id' como argumento, usando o valor de row["id_cuidador"]
#                 id=row["id_cuidador"],
#                 nome=row["nome"],
#                 email=row["email"],
#                 senha=row["senha"],
#                 telefone=row["telefone"],
#                 endereco=row["endereco"],
#                 experiencia_anos=row["experiencia_anos"]
#             )
#         return None


# def atualizar(cuidador: Cuidador) -> bool:
#     usuario_repo.atualizar(cuidador)
#     with open_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(ATUALIZAR_CUIDADOR, (
#             cuidador.experiencia_anos,
#             cuidador.id_cuidador
#         ))
#         cuidador_ok = cursor.rowcount > 0
#         return cuidador_ok


# def excluir(id_cuidador: int) -> bool:
#     with open_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(EXCLUIR_CUIDADOR, (id_cuidador,))
#         cuidador_excluido = cursor.rowcount > 0
#         usuario_excluido = usuario_repo.excluir(id_cuidador)
#         return cuidador_excluido and usuario_excluido
