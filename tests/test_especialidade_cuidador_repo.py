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
            dataNascimento="1985-05-15",
            email="joao@mail.com",
            telefone="123456789",
            cpf="11111111111",
            senha="123",
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
            confirmarSenha="123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None
        especialidade = Especialidade(id=0, nome="Fisioterapia")
        id_especialidade = especialidade_repo.inserir(especialidade)
        assert id_especialidade is not None
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
            dataNascimento="1990-03-20",
            email="maria@mail.com",
            telefone="987654321",
            cpf="22222222222",
            senha="456",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="12345678",
            logradouro="Rua Maria",
            numero="200",
            complemento="Apto 2",
            bairro="Bairro",
            cidade="São Paulo",
            estado="SP",
            ativo=True,
            experiencia="3 anos",
            valorHora=35.0,
            escolaridade="Ensino Superior",
            apresentacao="Cuidadora experiente",
            cursos="Enfermagem",
            inicio_profissional="2020-01-01",
            confirmarSenha="456",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        especialidade = Especialidade(0, "Enfermagem")
        id_especialidade = especialidade_repo.inserir(especialidade)
        assert id_especialidade is not None

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
            dataNascimento="1988-07-10",
            email="carlos@mail.com",
            telefone="000111222",
            cpf="33333333333",
            senha="789",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="12345678",
            logradouro="Rua Carlos",
            numero="300",
            complemento="Casa",
            bairro="Centro",
            cidade="Rio de Janeiro",
            estado="RJ",
            ativo=True,
            experiencia="2 anos",
            valorHora=28.0,
            escolaridade="Ensino Médio",
            apresentacao="Cuidador atencioso",
            cursos="Geriatria",
            inicio_profissional="2021-01-01",
            confirmarSenha="789",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        especialidade = Especialidade(0, "Psicologia")
        id_especialidade = especialidade_repo.inserir(especialidade)
        assert id_especialidade is not None

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
            dataNascimento="1992-11-25",
            email="ana@mail.com",
            telefone="444555666",
            cpf="44444444444",
            senha="321",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="12345678",
            logradouro="Rua Ana",
            numero="400",
            complemento="Apto 10",
            bairro="Vila",
            cidade="Belo Horizonte",
            estado="MG",
            ativo=True,
            experiencia="4 anos",
            valorHora=40.0,
            escolaridade="Ensino Superior",
            apresentacao="Cuidadora qualificada",
            cursos="Terapia Ocupacional",
            inicio_profissional="2019-01-01",
            confirmarSenha="321",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        especialidade = Especialidade(0, "Terapia Ocupacional")
        id_especialidade = especialidade_repo.inserir(especialidade)
        assert id_especialidade is not None

        ec = EspecialidadeCuidador(id_cuidador, id_especialidade, 4, None, None)
        ec_repo.inserir(ec)

        # Act
        lista = ec_repo.obter_especialidades_por_cuidador(id_cuidador)

        # Assert
        assert len(lista) >= 1, "Deveria retornar ao menos uma especialidade_cuidador"
        encontrou = any(e.id_cuidador == id_cuidador and e.id_especialidade == id_especialidade for e in lista)
        assert encontrou, "A relação inserida deveria estar na lista de especialidades por cuidador"

    def test_obter_especialidades_por_cuidador_inexistente(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        # Act - busca por cuidador que não existe
        lista = ec_repo.obter_especialidades_por_cuidador(99999)

        # Assert
        assert len(lista) == 0, "Deveria retornar lista vazia para cuidador inexistente"

    def test_inserir_com_dados_duplicados(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        cuidador = Cuidador(
            id=0,
            nome="Pedro",
            dataNascimento="1987-09-15",
            email="pedro@mail.com",
            telefone="555666777",
            cpf="55555555555",
            senha="senha123",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="12345678",
            logradouro="Rua Pedro",
            numero="500",
            complemento="Casa",
            bairro="Centro",
            cidade="Curitiba",
            estado="PR",
            ativo=True,
            experiencia="6 anos",
            valorHora=50.0,
            escolaridade="Ensino Superior",
            apresentacao="Cuidador profissional",
            cursos="Diversos",
            inicio_profissional="2017-01-01",
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = cuidador_repo.inserir(cuidador)
        assert id_cuidador is not None

        especialidade = Especialidade(0, "Nutrição")
        id_especialidade = especialidade_repo.inserir(especialidade)
        assert id_especialidade is not None

        ec = EspecialidadeCuidador(id_cuidador, id_especialidade, 6, None, None)
        resultado1 = ec_repo.inserir(ec)
        assert resultado1 is True

        # Act - tenta inserir duplicado (deve falhar devido à primary key)
        resultado2 = ec_repo.inserir(ec)

        # Assert - inserção duplicada deve retornar False
        assert resultado2 is False

    def test_atualizar_registro_inexistente(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        ec = EspecialidadeCuidador(99999, 99999, 10, None, None)

        # Act
        resultado = ec_repo.atualizar(ec)

        # Assert - atualização de registro inexistente deve retornar False
        assert resultado is False

    def test_excluir_registro_inexistente(self, test_db):
        # Arrange
        especialidade_repo.criar_tabela()
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()
        ec_repo.criar_tabela()

        # Act
        resultado = ec_repo.excluir(99999, 99999)

        # Assert - exclusão de registro inexistente deve retornar False
        assert resultado is False
