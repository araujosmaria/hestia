from data.especialidade_cuidador import especialidade_cuidador_repo as ec_repo
from data.especialidade_cuidador.especialidade_cuidador_model import EspecialidadeCuidador
from data.cuidador.cuidador_model import Cuidador
from data.especialidade.especialidade_model import Especialidade
from data.cuidador import cuidador_repo
from data.especialidade import especialidade_repo
from data.usuario import usuario_repo


class TestEspecialidadeCuidadorRepo:

    def test_criar_tabela(self, test_db):
        resultado1 = especialidade_repo.criar_tabela()
        resultado2 = cuidador_repo.criar_tabela()
        resultado3 = ec_repo.criar_tabela()
        assert (resultado1 and resultado2 and resultado3) is True, "A criação da tabela especialidade_cuidador deveria retornar True"

    def test_inserir_especialidade_cuidador(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()
        cuidador = Cuidador(
            id=0,
            nome="João",
            endereco="Rua A, 123",
            email="joao@mail.com",
            telefone="123456789",
            senha="123",
            experiencia_anos=5
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        especialidade = Especialidade(id=0, nome="Fisioterapia")
        id_especialidade = especialidade_repo.inserir(especialidade)        
        ec = EspecialidadeCuidador(
            id_cuidador=id_cuidador,
            id_especialidade=id_especialidade,
            anos_experiencia=5
        )

        # Act
        resultado = ec_repo.inserir(ec)

        # Assert
        assert resultado is True, "A inserção da especialidade_cuidador deveria retornar True"


    def test_atualizar_especialidade_cuidador(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        cuidador = Cuidador(
            id=0,
            nome="Maria",
            endereco="Rua B, 456",
            email="maria@mail.com",
            telefone="987654321",
            senha="456",
            experiencia_anos=3
        )
        id_cuidador = cuidador_repo.inserir(cuidador)

        especialidade = Especialidade(0, "Enfermagem")
        id_especialidade = especialidade_repo.inserir(especialidade)

        ec = EspecialidadeCuidador(id_cuidador, id_especialidade, 3, None, None)
        ec_repo.inserir(ec)

        # Atualizar experiência
        ec.anos_experiencia = 8
        resultado = ec_repo.atualizar(ec)

        # Assert
        assert resultado is True, "A atualização da especialidade_cuidador deveria retornar True"

    def test_excluir_especialidade_cuidador(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        cuidador = Cuidador(
            id=0,
            nome="Carlos",
            endereco="Rua C, 789",
            email="carlos@mail.com",
            telefone="000111222",
            senha="789",
            experiencia_anos=2
        )
        id_cuidador = cuidador_repo.inserir(cuidador)

        especialidade = Especialidade(0, "Psicologia")
        id_especialidade = especialidade_repo.inserir(especialidade)

        ec = EspecialidadeCuidador(id_cuidador, id_especialidade, 2, None, None)
        ec_repo.inserir(ec)

        # Act
        resultado = ec_repo.excluir(id_cuidador, id_especialidade)

        # Assert
        assert resultado is True, "A exclusão da especialidade_cuidador deveria retornar True"

    def test_obter_especialidades_por_cuidador(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        cuidador = Cuidador(
            id=0,
            nome="Ana",
            endereco="Rua D, 101",
            email="ana@mail.com",
            telefone="444555666",
            senha="321",
            experiencia_anos=4
        )
        id_cuidador = cuidador_repo.inserir(cuidador)

        especialidade = Especialidade(0, "Terapia Ocupacional")
        id_especialidade = especialidade_repo.inserir(especialidade)

        ec = EspecialidadeCuidador(id_cuidador, id_especialidade, 4, None, None)
        ec_repo.inserir(ec)

        # Act
        lista = ec_repo.obter_especialidades_por_cuidador(id_cuidador)

        # Assert
        assert len(lista) >= 1, "Deveria retornar ao menos uma especialidade_cuidador"
        encontrou = any(e.id_cuidador == id_cuidador and e.id_especialidade == id_especialidade for e in lista)
        assert encontrou, "A relação inserida deveria estar na lista de especialidades por cuidador"
