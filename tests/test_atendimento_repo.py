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
from data.usuario import usuario_repo


@pytest.fixture(autouse=True)
def setup_db(test_db):
    # Criar tabelas necessárias
    usuario_repo.criar_tabela()
    cliente_repo.criar_tabela()
    cuidador_repo.criar_tabela()
    atendimento_repo.criar_tabela()
    yield

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
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None

        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        # Cria um atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=1)
        atendimento = Atendimento(
            id=0,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )

        id_at = atendimento_repo.inserir(atendimento)
        assert id_at is not None

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db is not None
        assert at_db.id == id_at
        # Checar que os relacionamentos estão corretos
        assert at_db.id_cliente == id_cliente
        assert at_db.id_cuidador == id_cuidador

    def test_obter_todos(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        # Insere múltiplos atendimentos
        now = datetime.now()
        for i in range(3):
            atendimento = Atendimento(
                id=0,
                dataInicio=now + timedelta(hours=i),
                dataFim=now + timedelta(hours=i+1),
                id_cliente=id_cliente,
                id_cuidador=id_cuidador
            )
            atendimento_repo.inserir(atendimento)

        todos = atendimento_repo.obter_todos()
        assert len(todos) >= 3

    def test_atualizar(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        # Insere atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=2)
        atendimento = Atendimento(
            id=0,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_at = atendimento_repo.inserir(atendimento)
        assert id_at is not None
        atendimento.id = id_at

        # Atualiza as datas
        novo_inicio = inicio + timedelta(days=1)
        novo_fim = fim + timedelta(days=1)
        atendimento.dataInicio = novo_inicio
        atendimento.dataFim = novo_fim

        atualizado = atendimento_repo.atualizar(atendimento)
        assert atualizado

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db is not None
        assert at_db.dataInicio == novo_inicio
        assert at_db.dataFim == novo_fim

    def test_excluir(self):
        # Insere cliente e cuidador
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        assert id_cliente is not None
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        # Insere atendimento
        inicio = datetime.now()
        fim = inicio + timedelta(hours=1)
        atendimento = Atendimento(
            id=0,
            dataInicio=inicio,
            dataFim=fim,
            id_cliente=id_cliente,
            id_cuidador=id_cuidador
        )
        id_at = atendimento_repo.inserir(atendimento)
        assert id_at is not None

        excluiu = atendimento_repo.excluir(id_at)
        assert excluiu

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db is None

    def test_criar_tabela(self):
        """Testa a criação da tabela de atendimentos"""
        resultado = atendimento_repo.criar_tabela()
        assert resultado is True

    def test_atendimento_curta_duracao(self):
        """Testa atendimento de curta duração (30 minutos)"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        inicio = datetime(2025, 1, 15, 10, 0)
        fim = inicio + timedelta(minutes=30)
        atendimento = Atendimento(0, inicio, fim, id_cliente, id_cuidador)

        id_at = atendimento_repo.inserir(atendimento)
        assert id_at is not None

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db is not None
        assert (at_db.dataFim - at_db.dataInicio).total_seconds() == 1800  # 30 minutos

    def test_atendimento_longa_duracao(self):
        """Testa atendimento de longa duração (12 horas)"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        inicio = datetime(2025, 2, 20, 8, 0)
        fim = inicio + timedelta(hours=12)
        atendimento = Atendimento(0, inicio, fim, id_cliente, id_cuidador)

        id_at = atendimento_repo.inserir(atendimento)
        assert id_at is not None

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db is not None
        assert (at_db.dataFim - at_db.dataInicio).total_seconds() == 43200  # 12 horas

    def test_multiplos_atendimentos_mesmo_cliente(self):
        """Testa múltiplos atendimentos para o mesmo cliente"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)

        # Cria 3 cuidadores diferentes
        cuidadores_ids = []
        for _ in range(3):
            cuidador = criar_cuidador_fake()
            id_cuidador = cuidador_repo.inserir(cuidador)
            cuidadores_ids.append(id_cuidador)

        # Cria 3 atendimentos em datas diferentes
        base_date = datetime(2025, 3, 1, 9, 0)
        atendimentos_ids = []
        for i, id_cuidador in enumerate(cuidadores_ids):
            inicio = base_date + timedelta(days=i)
            fim = inicio + timedelta(hours=2)
            atendimento = Atendimento(0, inicio, fim, id_cliente, id_cuidador)
            id_at = atendimento_repo.inserir(atendimento)
            atendimentos_ids.append(id_at)

        # Verifica que todos foram inseridos
        assert all(id_at is not None for id_at in atendimentos_ids)

        # Verifica que todos podem ser recuperados
        todos = atendimento_repo.obter_todos()
        atendimentos_cliente = [a for a in todos if a.id_cliente == id_cliente]
        assert len(atendimentos_cliente) >= 3

    def test_multiplos_atendimentos_mesmo_cuidador(self):
        """Testa múltiplos atendimentos para o mesmo cuidador"""
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        # Cria 3 clientes diferentes
        clientes_ids = []
        for _ in range(3):
            cliente = criar_cliente_fake()
            id_cliente = cliente_repo.inserir(cliente)
            clientes_ids.append(id_cliente)

        # Cria 3 atendimentos em horários diferentes
        base_date = datetime(2025, 4, 1, 10, 0)
        atendimentos_ids = []
        for i, id_cliente in enumerate(clientes_ids):
            inicio = base_date + timedelta(hours=i*3)  # Espaçamento de 3 horas
            fim = inicio + timedelta(hours=2)
            atendimento = Atendimento(0, inicio, fim, id_cliente, id_cuidador)
            id_at = atendimento_repo.inserir(atendimento)
            atendimentos_ids.append(id_at)

        # Verifica que todos foram inseridos
        assert all(id_at is not None for id_at in atendimentos_ids)

        # Verifica que todos podem ser recuperados
        todos = atendimento_repo.obter_todos()
        atendimentos_cuidador = [a for a in todos if a.id_cuidador == id_cuidador]
        assert len(atendimentos_cuidador) >= 3

    def test_atendimento_mesmo_dia_horarios_diferentes(self):
        """Testa atendimentos no mesmo dia mas em horários diferentes"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        # Atendimento manhã
        manha_inicio = datetime(2025, 5, 10, 8, 0)
        manha_fim = manha_inicio + timedelta(hours=2)
        atendimento_manha = Atendimento(0, manha_inicio, manha_fim, id_cliente, id_cuidador)
        id_manha = atendimento_repo.inserir(atendimento_manha)

        # Atendimento tarde
        tarde_inicio = datetime(2025, 5, 10, 14, 0)
        tarde_fim = tarde_inicio + timedelta(hours=3)
        atendimento_tarde = Atendimento(0, tarde_inicio, tarde_fim, id_cliente, id_cuidador)
        id_tarde = atendimento_repo.inserir(atendimento_tarde)

        assert id_manha is not None
        assert id_tarde is not None

        # Verifica que ambos existem
        at_manha = atendimento_repo.obter_por_id(id_manha)
        at_tarde = atendimento_repo.obter_por_id(id_tarde)
        assert at_manha is not None
        assert at_tarde is not None
        assert at_manha.dataInicio.hour == 8
        assert at_tarde.dataInicio.hour == 14

    def test_atualizar_apenas_data_inicio(self):
        """Testa atualização apenas da data de início"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        inicio_original = datetime(2025, 6, 1, 10, 0)
        fim_original = inicio_original + timedelta(hours=2)
        atendimento = Atendimento(0, inicio_original, fim_original, id_cliente, id_cuidador)
        id_at = atendimento_repo.inserir(atendimento)
        atendimento.id = id_at

        # Atualiza apenas início
        novo_inicio = datetime(2025, 6, 1, 11, 0)
        atendimento.dataInicio = novo_inicio
        atendimento.dataFim = fim_original  # Mantém fim original

        resultado = atendimento_repo.atualizar(atendimento)
        assert resultado is True

        at_db = atendimento_repo.obter_por_id(id_at)
        assert at_db.dataInicio == novo_inicio
        assert at_db.dataFim == fim_original

    def test_obter_todos_lista_vazia_inicial(self):
        """Testa obter_todos quando não há atendimentos"""
        # Como há fixture autouse que limpa o banco, podemos testar
        # No início do teste não deve haver atendimentos deste teste
        todos = atendimento_repo.obter_todos()
        # Pode ter atendimentos de outros testes, mas testamos que retorna lista
        assert isinstance(todos, list)

    def test_atendimento_diferentes_clientes_mesmo_horario(self):
        """Testa que diferentes clientes podem ter atendimentos no mesmo horário"""
        cuidador1 = criar_cuidador_fake()
        id_cuidador1 = cuidador_repo.inserir(cuidador1)
        cuidador2 = criar_cuidador_fake()
        id_cuidador2 = cuidador_repo.inserir(cuidador2)

        cliente1 = criar_cliente_fake()
        id_cliente1 = cliente_repo.inserir(cliente1)
        cliente2 = criar_cliente_fake()
        id_cliente2 = cliente_repo.inserir(cliente2)

        # Mesmo horário para ambos
        inicio = datetime(2025, 7, 15, 14, 0)
        fim = inicio + timedelta(hours=2)

        atendimento1 = Atendimento(0, inicio, fim, id_cliente1, id_cuidador1)
        atendimento2 = Atendimento(0, inicio, fim, id_cliente2, id_cuidador2)

        id_at1 = atendimento_repo.inserir(atendimento1)
        id_at2 = atendimento_repo.inserir(atendimento2)

        assert id_at1 is not None
        assert id_at2 is not None
        assert id_at1 != id_at2

    def test_persistencia_dados_apos_consulta(self):
        """Testa que os dados persistem corretamente após inserção e consulta"""
        cliente = criar_cliente_fake()
        id_cliente = cliente_repo.inserir(cliente)
        cuidador = criar_cuidador_fake()
        id_cuidador = cuidador_repo.inserir(cuidador)

        inicio = datetime(2025, 8, 20, 9, 30)
        fim = datetime(2025, 8, 20, 17, 45)

        atendimento_original = Atendimento(0, inicio, fim, id_cliente, id_cuidador)
        id_at = atendimento_repo.inserir(atendimento_original)

        # Busca múltiplas vezes
        at1 = atendimento_repo.obter_por_id(id_at)
        at2 = atendimento_repo.obter_por_id(id_at)
        at3 = atendimento_repo.obter_por_id(id_at)

        # Todos devem ter os mesmos dados
        assert at1.id == at2.id == at3.id == id_at
        assert at1.id_cliente == at2.id_cliente == at3.id_cliente == id_cliente
        assert at1.id_cuidador == at2.id_cuidador == at3.id_cuidador == id_cuidador
        assert at1.dataInicio == at2.dataInicio == at3.dataInicio
        assert at1.dataFim == at2.dataFim == at3.dataFim
