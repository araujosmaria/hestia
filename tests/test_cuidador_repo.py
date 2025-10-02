import os
import random
import string
import pytest
from datetime import datetime
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo
from data.usuario.usuario_model import Usuario
from data.usuario import usuario_repo

TEST_DB = "test_dados_cuidador.db"

# ===============================
# FIXTURE DO BANCO DE TESTES
# ===============================
@pytest.fixture(autouse=True)
def reset_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    usuario_repo.criar_tabela()  # garante que tabela de usuário exista
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
        dataNascimento="1990-01-01",
        email=f"cuidador{sufixo}@teste.com",
        telefone=f"1199999{sufixo}",
        cpf=f"{random.randint(10000000000, 99999999999)}",
        senha="senha123",
        perfil="cuidador",
        foto=None,
        token_redefinicao=None,
        data_token=None,
        data_cadastro=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        cep="12345678",
        logradouro="Rua Teste",
        numero="100",
        complemento="Apto 1",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        ativo=True,
        experiencia="5 anos",
        valorHora=50.0,
        escolaridade="Ensino Médio",
        apresentacao="Apresentação teste",
        cursos="Curso teste",
        inicio_profissional="2015-01-01",
        confirmarSenha="senha123",
        termos=True,
        verificacao=True,
        comunicacoes=True
    )

# ===============================
# TESTES
# ===============================
class TestCuidadorRepo:

    def test_inserir(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

    def test_obter_por_id(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        cuidador.id = id_cuidador

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.id == id_cuidador

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
        cuidador.id = id_cuidador
        cuidador.experiencia = "10 anos"

        atualizado = cuidador_repo.atualizar(cuidador)
        assert atualizado

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db.experiencia == "10 anos"

    def test_excluir(self):
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        excluido = cuidador_repo.excluir(id_cuidador)
        assert excluido

        cuidador_db = cuidador_repo.obter_por_id(id_cuidador)
        assert cuidador_db is None