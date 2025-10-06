import os
import random
import string
import pytest
from datetime import datetime, timedelta
from data.atendimento.atendimento_model import Atendimento
from data.atendimento import atendimento_repo
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo

TEST_DB = "test_dados_atendimento.db"

@pytest.fixture(autouse=True)
def reset_db():
    # Remove se já existir
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    # Criar tabelas necessárias
    cliente_repo.criar_tabela(db_path=TEST_DB)
    cuidador_repo.criar_tabela(db_path=TEST_DB)
    atendimento_repo.criar_tabela(db_path=TEST_DB)
    yield
    # Cleanup
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

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
        parentesco_paciente="Filho",
        confirmarSenha="senha123",
        termos=True,
        verificacao=True,
        comunicacoes=True
    )

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
        data_cadastro=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        cep="12345678",
        logradouro="Rua Cuidador",
        numero="200",
        complemento="Casa B",
        bairro="Bairro Legal",
        cidade="São Paulo",
        estado="SP",
        ativo=True,
        foto=None,
        experiencia="5 anos de experiência com idosos",
        valorHora=50.0,
        escolaridade="Ensino Médio Completo",
        apresentacao="Sou um cuidador dedicado e paciente.",
        cursos="Curso de primeiros socorros, Curso de cuidador de idosos",
        inicio_profissional="2018-01-01",
        confirmarSenha="senha123",
        termos=True,
        verificacao=True,
        comunicacoes=True
    )

class TestAtendimentoRepo:

    def test_inserir_e_obter_por_id(self):
        # Insere cliente e cuidador no banco de teste
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente, db_path=TEST_DB)
        assert id_cliente is not None

        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador, db_path=TEST_DB)
        assert id_cuidador is not None

        # Cria um atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=1)
        atendimento = Atendimento(
            id=None,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )

        id_at = atendimento_repo.inserir(atendimento, db_path=TEST_DB)
        assert id_at is not None

        at_db = atendimento_repo.obter_por_id(id_at, db_path=TEST_DB)
        assert at_db is not None
        assert at_db.id == id_at
        # Checar que os relacionamentos estão corretos
        assert at_db.id_cliente == id_cliente
        assert at_db.id_cuidador == id_cuidador

    def test_obter_todos(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente, db_path=TEST_DB)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador, db_path=TEST_DB)

        # Insere múltiplos atendimentos
        now = datetime.now()
        for i in range(3):
            atendimento = Atendimento(
                id=None,
                dataInicio=now + timedelta(hours=i),
                dataFim=now + timedelta(hours=i+1),
                id_cliente=id_cliente,
                id_cuidador=id_cuidador
            )
            atendimento_repo.inserir(atendimento, db_path=TEST_DB)

        todos = atendimento_repo.obter_todos(db_path=TEST_DB)
        assert len(todos) >= 3

    def test_atualizar(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente, db_path=TEST_DB)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador, db_path=TEST_DB)

        # Insere atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=2)
        atendimento = Atendimento(
            id=None,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_at = atendimento_repo.inserir(atendimento, db_path=TEST_DB)
        atendimento.id = id_at

        # Atualiza as datas
        novo_inicio = inicio + timedelta(days=1)
        novo_fim = fim + timedelta(days=1)
        atendimento.dataInicio = novo_inicio
        atendimento.dataFim = novo_fim

        atualizado = atendimento_repo.atualizar(atendimento, db_path=TEST_DB)
        assert atualizado

        at_db = atendimento_repo.obter_por_id(id_at, db_path=TEST_DB)
        assert at_db.dataInicio == novo_inicio
        assert at_db.dataFim == novo_fim

    def test_excluir(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente, db_path=TEST_DB)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador, db_path=TEST_DB)

        # Insere atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=1)
        atendimento = Atendimento(
            id=None,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_at = atendimento_repo.inserir(atendimento, db_path=TEST_DB)

        excluiu = atendimento_repo.excluir(id_at, db_path=TEST_DB)
        assert excluiu

        at_db = atendimento_repo.obter_por_id(id_at, db_path=TEST_DB)
        assert at_db is None
