import pytest
import datetime
from data.atendimento.atendimento_repo import *
from data.atendimento.atendimento_model import Atendimento
from data.cliente.cliente_repo import criar_tabela as criar_tabela_cliente, inserir as inserir_cliente
from data.cliente.cliente_model import Cliente
from data.cuidador.cuidador_repo import criar_tabela as criar_tabela_cuidador, inserir as inserir_cuidador
from data.cuidador.cuidador_model import Cuidador
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario


class TestAtendimentoRepo:
    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_cuidador()
        criar_tabela()    

    def criar_cliente_e_cuidador(self):
        cliente = Cliente(
            id=0,
            nome="Cliente Teste",
            email="cliente@test.com",
            senha="senha",
            telefone="123456",
            endereco="Rua Cliente"
        )
        id_cliente = inserir_cliente(cliente)

        cuidador = Cuidador(
            id=0,
            nome="Cuidador Teste",
            email="cuidador@test.com",
            senha="senha",
            telefone="987654",
            endereco="Rua Cuidador",
            experiencia_anos=2
        )
        id_cuidador = inserir_cuidador(cuidador)

        return id_cliente, id_cuidador

    def test_criar_tabela(self, test_db):
        resultado = criar_tabela()
        assert resultado == True, "A criação da tabela de atendimento deveria retornar True"

    def test_inserir_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime.datetime(2025, 7, 1, 14, 0),
            dataFim=datetime.datetime(2025, 7, 1, 18, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None, "Deveria retornar um ID ao inserir"

    def test_obter_todos(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento1 = Atendimento(0, datetime.datetime.now(), datetime.datetime.now(), id_cliente, id_cuidador)
        atendimento2 = Atendimento(0, datetime.datetime.now(), datetime.datetime.now(), id_cliente, id_cuidador)
        inserir(atendimento1)
        inserir(atendimento2)

        lista = obter_todos()
        assert len(lista) >= 2, "Deveria retornar ao menos 2 atendimentos"

    def test_atualizar_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(0, datetime.datetime(2025, 7, 1, 8, 0), datetime.datetime(2025, 7, 1, 12, 0), id_cliente, id_cuidador)
        id_atendimento = inserir(atendimento)

        atendimento_atualizado = Atendimento(
            id=id_atendimento,
            dataInicio=datetime.datetime(2025, 7, 1, 10, 0),
            dataFim=datetime.datetime(2025, 7, 1, 14, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        resultado = atualizar(atendimento_atualizado)
        assert resultado == True, "A atualização deveria retornar True"

    def test_excluir_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(0, datetime.datetime.now(), datetime.datetime.now(), id_cliente, id_cuidador)
        id_atendimento = inserir(atendimento)

        resultado = excluir(id_atendimento)
        assert resultado == True, "A exclusão deveria retornar True"
