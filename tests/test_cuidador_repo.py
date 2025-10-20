import os
import random
import string
import pytest
from datetime import datetime
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo

TEST_DB = "test_dados.db"

# ===============================
# FIXTURE DO BANCO DE TESTES
# ===============================
@pytest.fixture(autouse=True)
def reset_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    cuidador_repo.criar_tabela()
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

# ===============================
# FUNÇÃO AUXILIAR PARA CRIAR CUIDADOR FAKE
# ===============================
def criar_cuidador_fake() -> Cuidador:
    sufixo = ''.join(random.choices(string.digits, k=6))
    return Cuidador(
        id=None,
        nome=f"Cuidador {sufixo}",
        dataNascimento="1985-05-15",
        email=f"cuidador{sufixo}@teste.com",
        telefone=f"1199999{sufixo}",
        cpf=f"123456{sufixo}",
        senha="senha123",
        perfil="cuidador",
        token_redefinicao=None,
        data_token=None,
        data_cadastro=datetime.now(),
        cep="12345678",
        logradouro="Rua dos Testes",
        numero="123",
        complemento="Casa B",
        bairro="Bairro Legal",
        cidade="São Paulo",
        estado="SP",
        ativo=True,
        foto=None,
        experiencia="3 anos em cuidados com idosos",
        valorHora=30.0,
        escolaridade="Ensino Médio Completo",
        apresentacao="Sou cuidador dedicado e experiente.",
        cursos="Primeiros Socorros, Cuidados Geriátricos",
        inicio_profissional="2018-01-01",
        confirmarSenha="senha123",
        termos=True,
        verificacao=True,
        comunicacoes=True
    )

# ===============================
# TESTES
# ===============================
class TestCuidadorRepo:

    def test_criar_tabela(self):
        assert cuidador_repo.criar_tabela()

    def test_inserir(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

    def test_obter_por_id(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None
        cuidador.id = id_cuidador

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.id == id_cuidador
        assert cuidador_db.nome == cuidador.nome

    def test_obter_todos(self):
        cuidador1 = criar_cuidador_fake()
        cuidador2 = criar_cuidador_fake()
        cuidador_repo.inserir(cuidador1)
        cuidador_repo.inserir(cuidador2)

        cuidadores = cuidador_repo.obter_todos()
        assert len(cuidadores) >= 2

    def test_atualizar(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None
        cuidador.id = id_cuidador
        cuidador.experiencia = "Atualizado: 5 anos de experiência"
        cuidador.valorHora = 50.0

        atualizado = cuidador_repo.atualizar(cuidador)
        assert atualizado

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.experiencia == "Atualizado: 5 anos de experiência"
        assert cuidador_db.valorHora == 50.0

    def test_excluir(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        excluido = cuidador_repo.excluir(id_cuidador)
        assert excluido

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db is None
