import pytest
import datetime
from data.avaliacao.avaliacao_repo import *
from data.avaliacao.avaliacao_model import Avaliacao
from data.atendimento.atendimento_repo import criar_tabela as criar_tabela_atendimento, inserir as inserir_atendimento
from data.atendimento.atendimento_model import Atendimento
from data.cliente.cliente_repo import criar_tabela as criar_tabela_cliente, inserir as inserir_cliente
from data.cliente.cliente_model import Cliente
from data.cuidador.cuidador_repo import criar_tabela as criar_tabela_cuidador, inserir as inserir_cuidador
from data.cuidador.cuidador_model import Cuidador
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario


class TestAvaliacaoRepo:
    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_cuidador()
        criar_tabela_atendimento()
        criar_tabela()

    def criar_cliente_cuidador_atendimento(self):
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

        atendimento = Atendimento(
            id=0,
            dataInicio=datetime.datetime(2025, 7, 1, 14, 0),
            dataFim=datetime.datetime(2025, 7, 1, 18, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir_atendimento(atendimento)

        return id_cliente, id_cuidador, id_atendimento

    def test_criar_tabela(self, test_db):
        resultado = criar_tabela()
        assert resultado == True, "A criação da tabela de avaliação deveria retornar True"

    def test_inserir_avaliacao(self, test_db):
        _, _, id_atendimento = self.criar_cliente_cuidador_atendimento()
        avaliacao = Avaliacao(
            id=0,
            nota=4.5,
            comentario="Muito bom",
            dataAvaliacao=datetime.datetime.now(),
            id_atendimento=id_atendimento
        )
        id_avaliacao = inserir(avaliacao)
        assert id_avaliacao is not None, "Deveria retornar um ID ao inserir avaliação"

    def test_obter_todos(self, test_db):
        _, _, id_atendimento = self.criar_cliente_cuidador_atendimento()
        avaliacao1 = Avaliacao(0, 5.0, "Ótimo", datetime.datetime.now(), id_atendimento)
        avaliacao2 = Avaliacao(0, 3.0, "Regular", datetime.datetime.now(), id_atendimento)
        inserir(avaliacao1)
        inserir(avaliacao2)

        lista = obter_todos()
        assert len(lista) >= 2, "Deveria retornar ao menos 2 avaliações"

    def test_atualizar_avaliacao(self, test_db):
        _, _, id_atendimento = self.criar_cliente_cuidador_atendimento()
        avaliacao = Avaliacao(0, 4.0, "Bom", datetime.datetime(2025, 7, 1), id_atendimento)
        id_avaliacao = inserir(avaliacao)

        avaliacao_atualizada = Avaliacao(
            id=id_avaliacao,
            nota=4.8,
            comentario="Muito bom, revisado",
            dataAvaliacao=datetime.datetime(2025, 7, 2),
            id_atendimento=id_atendimento
        )
        resultado = atualizar(avaliacao_atualizada)
        assert resultado == True, "A atualização deveria retornar True"

    def test_excluir_avaliacao(self, test_db):
        _, _, id_atendimento = self.criar_cliente_cuidador_atendimento()
        avaliacao = Avaliacao(0, 2.5, "Ruim", datetime.datetime.now(), id_atendimento)
        id_avaliacao = inserir(avaliacao)

        resultado = excluir(id_avaliacao)
        assert resultado == True, "A exclusão deveria retornar True"
