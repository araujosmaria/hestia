from datetime import datetime
import pytest
from data.agenda.agenda_model import Agenda
from data.agenda.agenda_repo import criar_tabela, inserir, obter_todos, excluir, obter_por_id, atualizar
from data.usuario import usuario_repo
from data.cuidador import cuidador_repo
from data.cuidador.cuidador_model import Cuidador


class TestAgendaRepo:
    @pytest.fixture(autouse=True)
    def setup_db(self, test_db):
        # Cria as tabelas necessárias
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        criar_tabela()
        yield

    def criar_cuidador_teste(self):
        """Cria um cuidador para usar nos testes de agenda"""
        cuidador = Cuidador(
            id=0,
            nome="Cuidador Teste",
            dataNascimento="1985-05-15",
            email="cuidador@teste.com",
            telefone="11988888888",
            cpf="12345678901",
            senha="senha123",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="12345678",
            logradouro="Rua Teste",
            numero="100",
            complemento="Casa",
            bairro="Centro",
            cidade="São Paulo",
            estado="SP",
            ativo=True,
            experiencia="5 anos",
            valorHora=30.0,
            escolaridade="Ensino Médio",
            apresentacao="Cuidador dedicado",
            cursos="Primeiros Socorros",
            inicio_profissional="2018-01-01",
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        return cuidador_repo.inserir(cuidador)

    def test_criar_tabela(self, test_db):
        # A tabela já é criada no setup_db
        resultado = criar_tabela()
        assert resultado is True

    def test_inserir_agenda(self, test_db):
        id_cuidador = self.criar_cuidador_teste()
        assert id_cuidador is not None

        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=id_cuidador
        )
        id_agenda = inserir(agenda_teste)
        assert isinstance(id_agenda, int) and id_agenda > 0
        agendas = obter_todos()

        agenda_inserida = next((a for a in agendas if a.id_agenda == id_agenda), None)
        assert agenda_inserida is not None
        assert agenda_inserida.disponibilidade == agenda_teste.disponibilidade
        assert agenda_inserida.id_cuidador == agenda_teste.id_cuidador

    def test_obter_todos(self, test_db):
        id_cuidador = self.criar_cuidador_teste()
        assert id_cuidador is not None

        # Insere algumas agendas
        agenda1 = Agenda(0, datetime(2025, 7, 1, 11, 0, 0), True, id_cuidador)
        agenda2 = Agenda(0, datetime(2025, 7, 2, 14, 0, 0), False, id_cuidador)
        inserir(agenda1)
        inserir(agenda2)

        agendas = obter_todos()
        assert len(agendas) >= 2

    def test_obter_por_id(self, test_db):
        id_cuidador = self.criar_cuidador_teste()
        assert id_cuidador is not None

        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=id_cuidador
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None

        agenda = obter_por_id(id_agenda)

        assert agenda is not None
        assert agenda.id_agenda == id_agenda
        assert isinstance(agenda.dataHora, (str, datetime))
        assert agenda.disponibilidade in [True, False, 0, 1]
        assert isinstance(agenda.id_cuidador, int)

    def test_atualizar(self, test_db):
        id_cuidador = self.criar_cuidador_teste()
        assert id_cuidador is not None

        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=id_cuidador
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None
        agenda_inserida = obter_por_id(id_agenda)
        assert agenda_inserida is not None

        # Atualize um campo válido
        agenda_inserida.disponibilidade = False
        resultado = atualizar(agenda_inserida)

        assert resultado == True, "A atualização da agenda deveria retornar True"

        # Verifique se atualizou no banco
        agenda_atualizada = obter_por_id(id_agenda)
        assert agenda_atualizada is not None
        assert agenda_atualizada.disponibilidade == False

    def test_excluir(self, test_db):
        id_cuidador = self.criar_cuidador_teste()
        assert id_cuidador is not None

        # Arrange
        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=id_cuidador
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None
        # Act
        resultado = excluir(id_agenda)
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"

    def test_criar_tabela_error_handling(self, test_db):
        # Test que a função criar_tabela retorna True mesmo quando já existe
        resultado1 = criar_tabela()
        resultado2 = criar_tabela()
        assert resultado1 is True
        assert resultado2 is True