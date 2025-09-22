import pytest
from datetime import date, datetime
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
            dataNascimento=date(1990, 1, 1),
            email="cliente@test.com",
            telefone="123456",
            cpf="123.456.789-00",
            perfil="cliente",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="12345-678",
            logradouro="Rua Cliente",
            numero="100",
            complemento="Apto 101",
            bairro="Bairro Teste",
            cidade="Cidade Teste",
            estado="Estado Teste",
            ativo=True,
            parentesco_paciente=None,
            confirmarSenha="senha",
            termos=True,
            verificacao=False,
            comunicacoes=True,
        )
        id_cliente = inserir_cliente(cliente)

        cuidador = Cuidador(
            id=0,
            nome="Cuidador Teste",
            dataNascimento=date(1985, 5, 20),
            email="cuidador@test.com",
            telefone="987654",
            cpf="987.654.321-00",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="87654-321",
            logradouro="Rua Cuidador",
            numero="200",
            complemento="Casa",
            bairro="Bairro Cuidador",
            cidade="Cidade Cuidador",
            estado="Estado Cuidador",
            ativo=True,
            experiencia="2 anos",
            valorHora=25.0,
            escolaridade="Ensino Médio",
            apresentacao="Cuidador dedicado e experiente.",
            cursos="Primeiros Socorros",
            confirmarSenha="senha",
            termos=True,
            verificacao=False,
            comunicacoes=True,
        )
        id_cuidador = inserir_cuidador(cuidador)

        return id_cliente, id_cuidador

    def test_criar_tabela(self, test_db):
        resultado = criar_tabela()
        assert resultado is True, "A criação da tabela de atendimento deveria retornar True"

    def test_inserir_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime(2025, 7, 1, 14, 0),
            dataFim=datetime(2025, 7, 1, 18, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None, "Deveria retornar um ID ao inserir"

    def test_obter_todos(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento1 = Atendimento(0, datetime.now(), datetime.now(), id_cliente, id_cuidador)
        atendimento2 = Atendimento(0, datetime.now(), datetime.now(), id_cliente, id_cuidador)
        inserir(atendimento1)
        inserir(atendimento2)

        lista = obter_todos()
        assert len(lista) >= 2, "Deveria retornar ao menos 2 atendimentos"

    def test_obter_por_id(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime(2025, 7, 1, 14, 0),
            dataFim=datetime(2025, 7, 1, 18, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None, "Inserção deve retornar um ID válido"

        atendimento_obtido = obter_por_id(id_atendimento)

        assert atendimento_obtido is not None, "Deveria retornar um objeto Atendimento"
        assert atendimento_obtido.id == id_atendimento
        assert atendimento_obtido.dataInicio == atendimento.dataInicio
        assert atendimento_obtido.dataFim == atendimento.dataFim
        assert atendimento_obtido.id_cliente == atendimento.id_cliente
        assert atendimento_obtido.id_cuidador == atendimento.id_cuidador

    def test_atualizar_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime(2025, 7, 1, 8, 0),
            dataFim=datetime(2025, 7, 1, 12, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None, "Inserção deve retornar um ID válido"

        atendimento_atualizado = Atendimento(
            id=id_atendimento,
            dataInicio=datetime(2025, 7, 1, 10, 0),
            dataFim=datetime(2025, 7, 1, 14, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        resultado = atualizar(atendimento_atualizado)
        assert resultado is True, "A atualização deveria retornar True"

    def test_excluir_atendimento(self, test_db):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime.now(),
            dataFim=datetime.now(),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None, "Inserção deve retornar um ID válido"

        resultado = excluir(id_atendimento)
        assert resultado is True, "A exclusão deveria retornar True"
