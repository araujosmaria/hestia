from typing import Optional
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *
from data.usuario import usuario_repo
from data.util import open_connection
import sqlite3
import uuid

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
        # Gera CPF único caso não exista
        if not cuidador.cpf:
            cuidador.cpf = str(uuid.uuid4().int)[:11]
        if not cuidador.email:
            cuidador.email = f"cuidador_{cuidador.cpf}@example.com"

        # Inserir o usuário primeiro
        id_usuario = usuario_repo.inserir(cuidador)
        if id_usuario is None:
            print("Erro: inserção do usuário retornou None")
            return None

        cuidador.id = id_usuario

        with open_connection() as conn:
            cursor = conn.cursor()
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
                cuidador.comunicacoes,
            ))
            conn.commit()
            return id_usuario

    except Exception as e:
        print(f"Erro ao inserir cuidador: {e}")
        return None

def obter_por_id(id_cuidador: int) -> Optional[Cuidador]:
    with open_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(OBTER_CUIDADOR_POR_ID, (id_cuidador,))
        row = cursor.fetchone()
        if row:
            return Cuidador(
                id=row["id_cuidador"],
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
                confirmarSenha=row["confirmarSenha"],
                termos=row["termos"],
                verificacao=row["verificacao"],
                comunicacoes=row["comunicacoes"],
                inicio_profissional=row["inicio_profissional"]
            )
        return None

def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        return [
            Cuidador(
                id=row["id_cuidador"],
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
                confirmarSenha=row["confirmarSenha"],
                termos=row["termos"],
                verificacao=row["verificacao"],
                comunicacoes=row["comunicacoes"],
                inicio_profissional=row["inicio_profissional"]
            )
            for row in rows
        ]

def atualizar(cuidador: Cuidador) -> bool:
    try:
        # Atualiza dados do usuário
        usuario_atualizado = usuario_repo.atualizar(cuidador)
        if not usuario_atualizado:
            return False

        # Atualiza dados específicos do cuidador
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE cuidador
                SET experiencia = ?, valorHora = ?, escolaridade = ?, apresentacao = ?, cursos = ?, inicio_profissional = ?
                WHERE id_cuidador = ?
            """, (
                cuidador.experiencia,
                cuidador.valorHora,
                cuidador.escolaridade,
                cuidador.apresentacao,
                cuidador.cursos,
                cuidador.inicio_profissional,
                cuidador.id
            ))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar cuidador: {e}")
        return False

def excluir(id_cuidador: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cuidador WHERE id_cuidador = ?", (id_cuidador,))
        cuidador_excluido = cursor.rowcount > 0
    usuario_excluido = usuario_repo.excluir(id_cuidador)
    return cuidador_excluido and usuario_excluido
