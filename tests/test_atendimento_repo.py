import pytest
from datetime import datetime
from data.atendimento.atendimento_repo import criar_tabela, inserir, obter_todos, obter_por_id, atualizar, excluir
from data.atendimento.atendimento_model import Atendimento
from data.cliente.cliente_repo import criar_tabela as criar_tabela_cliente, inserir as inserir_cliente, obter_por_id as obter_cliente_por_id
from data.cliente.cliente_model import Cliente
from data.cuidador.cuidador_repo import criar_tabela as criar_tabela_cuidador, inserir as inserir_cuidador, obter_por_id as obter_cuidador_por_id
from data.cuidador.cuidador_model import Cuidador
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario
from data.util import open_connection

class TestAtendimentoRepo:
    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_cuidador()
        criar_tabela()

    def criar_cliente_e_cuidador(self):
        # Verifica se cliente já existe (exemplo pelo CPF ou email)
        cliente_existente = obter_cliente_por_id(1)  
        if cliente_existente:
            id_cliente = cliente_existente.id
        else:
            cliente = Cliente(
                id_cliente=None,  # None para autoincrement
                nome="Teste Cliente",
                dataNascimento="2000-01-01",
                email="teste@email.com",
                telefone="999999999",
                cpf="12345678900",
                senha="senha",
                perfil="paciente",
                foto=None,
                token_redefinicao=None,
                data_token=None,
                data_cadastro=str(datetime.now().date()),
                cep="00000000",
                logradouro="Rua Teste",
                numero="123",
                complemento="",
                bairro="Centro",
                cidade="Cidade",
                estado="Estado",
                ativo=True,
                parentesco_paciente="pai",
                confirmarSenha="senha",
                termos=True,
                verificacao=True,
                comunicacoes=True,
            )
            id_cliente = inserir_cliente(cliente)

        # Verifica se cuidador já existe
        cuidador_existente = obter_cuidador_por_id(1)  # ajuste conforme chave única
        if cuidador_existente:
            id_cuidador = cuidador_existente.id
        else:
            cuidador = Cuidador(
                id_cuidador=None,  # None para autoincrement
                experiencia="5 anos",
                valorHora=50.0,
                escolaridade="Ensino Superior",
                apresentacao="Sou cuidador dedicado.",
                cursos="Primeiros Socorros",
                confirmarSenha="senha",
                termos=True,
                verificacao=True,
                comunicacoes=True
            )
            id_cuidador = inserir_cuidador(cuidador)

        return id_cliente, id_cuidador

    def test_criar_tabela(self) -> bool:
        try:
            with open_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='atendimento'")
                tabela = cursor.fetchone()
                assert tabela is not None
            return True
        except Exception as e:
            print(f"Erro ao criar tabela de atendimentos: {e}")
            return False

    def test_inserir_atendimento(self):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(
            id=None,
            dataInicio=datetime(2025, 7, 1, 14, 0),
            dataFim=datetime(2025, 7, 1, 18, 0),
            id_cliente=id_cliente,
            id_cuidador=id_cuidador,
        )
        id_atendimento = inserir(atendimento)
        assert id_atendimento is not None

    def test_obter_todos(self):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        inserir(Atendimento(None, datetime.now(), datetime.now(), id_cliente, id_cuidador))
        atendimentos = obter_todos()
        assert len(atendimentos) > 0

    def test_obter_por_id(self):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        atendimento = Atendimento(None, datetime.now(), datetime.now(), id_cliente, id_cuidador)
        id_atendimento = inserir(atendimento)
        atendimento_db = obter_por_id(id_atendimento)
        assert atendimento_db is not None
        assert atendimento_db.id == id_atendimento

    def test_atualizar_atendimento(self):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        id_atendimento = inserir(
            Atendimento(None, datetime(2025, 7, 1, 8, 0), datetime(2025, 7, 1, 12, 0), id_cliente, id_cuidador)
        )
        atendimento_atualizado = Atendimento(
            id_atendimento,
            datetime(2025, 7, 1, 9, 0),
            datetime(2025, 7, 1, 13, 0),
            id_cliente,
            id_cuidador,
        )
        sucesso = atualizar(atendimento_atualizado)
        assert sucesso

    def test_excluir_atendimento(self):
        id_cliente, id_cuidador = self.criar_cliente_e_cuidador()
        id_atendimento = inserir(Atendimento(None, datetime.now(), datetime.now(), id_cliente, id_cuidador))
        sucesso = excluir(id_atendimento)
        assert sucesso
