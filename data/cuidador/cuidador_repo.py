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
        id_usuario = usuario_repo.inserir(cuidador)
        if id_usuario is None:
            print("Erro: inserção do usuário retornou None")
            return None

        # Inserir cuidador
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_CUIDADOR,
                (id_usuario, 
                 cuidador.experiencia, 
                 cuidador.valorHora, 
                 cuidador.escolaridade, 
                 cuidador.apresentacao, 
                 cuidador.cursos, 
                 cuidador.confirmarSenha, 
                 cuidador.termos, 
                 cuidador.verificacao, 
                 cuidador.comunicacoes)
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
                inicio_profissional=row["inicio_profissional"]
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
        cursor.execute(ATUALIZAR_CUIDADOR,
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

# Adicione este método no arquivo data/cuidador/cuidador_repo.py

def atualizar(cuidador: Cuidador) -> bool:
    """
    Atualiza os dados de um cuidador no banco de dados
    """
    try:
        with open_connection() as conexao:
            cursor = conexao.cursor()
            
            sql = """
            UPDATE tb_usuario SET 
                nome = %s,
                dataNascimento = %s,
                email = %s,
                telefone = %s,
                foto = %s,
                cep = %s,
                logradouro = %s,
                numero = %s,
                complemento = %s,
                bairro = %s,
                cidade = %s,
                estado = %s,
                experiencia = %s,
                valorHora = %s,
                escolaridade = %s,
                apresentacao = %s,
                cursos = %s
            WHERE id = %s AND perfil = 'cuidador'
            """
            
            cursor.execute(sql, (
                cuidador.nome,
                cuidador.dataNascimento,
                cuidador.email,
                cuidador.telefone,
                cuidador.foto,
                cuidador.cep,
                cuidador.logradouro,
                cuidador.numero,
                cuidador.complemento,
                cuidador.bairro,
                cuidador.cidade,
                cuidador.estado,
                cuidador.experiencia,
                cuidador.valorHora,
                cuidador.escolaridade,
                cuidador.apresentacao,
                cuidador.cursos,
                cuidador.id
            ))
            
            conexao.commit()
            
            # Verificar se alguma linha foi afetada
            return cursor.rowcount > 0
            
    except Exception as e:
        print(f"Erro ao atualizar cuidador: {e}")
        return False