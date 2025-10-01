import random
import sqlite3
import string
from datetime import datetime
import pytest
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import (
    criar_tabela, inserir, obter_por_id, obter_todos, atualizar, excluir
)
from data.cliente.cliente_sql import ATUALIZAR_CLIENTE

class TestClienteRepo:

    def criar_cliente_fake(self) -> Cliente:
        sufixo = ''.join(random.choices(string.digits, k=6))
        return Cliente(
            id=None,
            nome=f"Cliente Teste {sufixo}",
            dataNascimento="2000-01-01",
            email=f"cliente{sufixo}@teste.com",
            telefone="123456789",
            cpf=f"123456{sufixo}",
            senha="Senha123",
            perfil="cliente",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=str(datetime.now().date()),
            cep="12345-000",
            logradouro="Rua Teste",
            numero="123",
            complemento="",
            bairro="Centro",
            cidade="Cidade",
            estado="Estado",
            ativo=True,
            parentesco_paciente="Filho",
            confirmarSenha="Senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

    def test_criar_tabela(self, test_db):
        resultado = criar_tabela(db_path=str(test_db))
        assert resultado is True

    def test_inserir(self, test_db):
        criar_tabela(db_path=str(test_db))
        cliente = self.criar_cliente_fake()
        id_cliente = inserir(cliente, db_path=str(test_db))
        assert id_cliente is not None

        cliente_db = obter_por_id(id_cliente, db_path=str(test_db))
        assert cliente_db is not None
        assert cliente_db.parentesco_paciente == "Filho"

    def test_obter_por_id(self, test_db):
        criar_tabela(db_path=str(test_db))
        cliente = self.criar_cliente_fake()
        id_cliente = inserir(cliente, db_path=str(test_db))

        cliente_db = obter_por_id(id_cliente, db_path=str(test_db))
        assert cliente_db is not None
        assert cliente_db.id == id_cliente

    def test_obter_todos(self, test_db):
        criar_tabela(db_path=str(test_db))
        inserir(self.criar_cliente_fake(), db_path=str(test_db))
        inserir(self.criar_cliente_fake(), db_path=str(test_db))

        clientes = obter_todos(db_path=str(test_db))
        assert len(clientes) >= 2

    def atualizar(cliente: Cliente, db_path: str = "default.db") -> bool:
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    ATUALIZAR_CLIENTE,(
                        cliente.parentesco_paciente,
                        bool(cliente.termos),
                        bool(cliente.comunicacoes),
                        cliente.id
                    )
                )
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            return False

    def test_excluir(self, test_db):
        criar_tabela(db_path=str(test_db))
        cliente = self.criar_cliente_fake()
        id_cliente = inserir(cliente, db_path=str(test_db))

        resultado = excluir(id_cliente, db_path=str(test_db))
        assert resultado is True

        cliente_db = obter_por_id(id_cliente, db_path=str(test_db))
        assert cliente_db is None
