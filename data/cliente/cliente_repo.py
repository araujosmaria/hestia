from typing import Optional
from data.util import open_connection
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.usuario import usuario_repo


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CLIENTE)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de clientes: {e}")
        return False  


def inserir(cliente: Cliente) -> Optional[int]:
    try:
        # Garantir que o perfil está definido como 'contratante'
        if not cliente.perfil:
            cliente.perfil = "contratante"
        elif cliente.perfil != "contratante":
            print(f"Warning: perfil diferente de 'contratante' detectado: {cliente.perfil}. Corrigindo.")
            cliente.perfil = "contratante"

        # Inserir usuário na tabela principal (usuario)
        id_cliente = usuario_repo.inserir(cliente)
        if id_cliente is None:
            print("Erro: inserção do usuário (cliente) retornou None")
            return None

        # Inserir dados específicos do cliente na tabela cliente
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(INSERIR_CLIENTE, (id_cliente, cliente.parentesco_paciente))
            conn.commit()
            print(f"Cliente inserido com sucesso com ID {id_cliente}")
            return id_cliente

    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")
        return None


def obter_todos() -> list[Cliente]:
    with open_connection() as conn:
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
                ativo=row["ativo"],
                parentesco_paciente=row["parentesco_paciente"]
            )
            for row in rows
        ]
        return clientes


def obter_por_id(id_cliente: int) -> Optional[Cliente]:
    try:
        with open_connection() as conn:
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
                    ativo=row["ativo"],
                    parentesco_paciente=row["parentesco_paciente"]
                )
            return None
    except Exception as e:
        print(f"Erro ao obter cliente por ID: {e}")
        return None


def excluir(id_cliente: int) -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
            cliente_excluido = cursor.rowcount > 0

        usuario_excluido = usuario_repo.excluir(id_cliente)
        return cliente_excluido and usuario_excluido
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")
        return False
