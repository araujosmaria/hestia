import os
import random
import string
import pytest
from datetime import datetime
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo


DB_PATH = "dados.db"

# ===============================
# FIXTURE DO BANCO DE TESTES
# ===============================
@pytest.fixture(autouse=True)
def reset_test_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    cliente_repo.criar_tabela()
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

# ===============================
# FUNÇÃO AUXILIAR PARA CRIAR CLIENTE FAKE
# ===============================
def criar_cliente_fake() -> Cliente:
    sufixo = ''.join(random.choices(string.digits, k=6))
    return Cliente(
        id=None,
        nome=f"Cliente {sufixo}",
        dataNascimento="1990-01-01",
        email=f"cliente{sufixo}@teste.com",
        telefone=f"1199999{sufixo}",
        cpf=f"123456{sufixo}",
        senha="senha123",
        perfil="cliente",
        foto=None,
        token_redefinicao=None,
        data_token=None,
        data_cadastro=datetime.now(),
        cep="12345678",
        logradouro="Rua Teste",
        numero="100",
        complemento="Apto 1",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        ativo=True,
        parentesco_paciente="Filho",
        confirmarSenha="senha123",
        termos=True,
        verificacao=True,
        comunicacoes=True
    )

# ===============================
# TESTES
# ===============================
class TestClienteRepo:

    def test_criar_tabela(self):
        assert cliente_repo.criar_tabela()

    def test_inserir(self):
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None

    def test_obter_por_id(self):
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cliente.id = id_cliente

        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cliente_db = cliente_repo.obter_por_id(id_cliente)
        assert cliente_db is not None
        assert cliente_db.id == id_cliente

    def test_obter_todos(self):
        cliente1 = criar_cliente_fake()
        cliente2 = criar_cliente_fake()
        cliente_repo.inserir(cliente1)
        cliente_repo.inserir(cliente2)

        clientes = cliente_repo.obter_todos()
        assert len(clientes) >= 2

    def test_atualizar(self):
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cliente.id = id_cliente
        cliente.parentesco_paciente = "Pai"

        atualizado = cliente_repo.atualizar(cliente)
        assert atualizado

        cliente_db = cliente_repo.obter_por_id(id_cliente)
        assert cliente_db is not None
        assert cliente_db.parentesco_paciente == "Pai"

    def test_excluir(self):
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None

        excluido = cliente_repo.excluir(id_cliente)
        assert excluido

        cliente_db = cliente_repo.obter_por_id(id_cliente)
        assert cliente_db is None
