from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_repo import (
    criar_tabela as criar_tabela_cuidador,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario

class TestCuidadorRepo:
    def test_criar_tabela(self):
        criar_tabela_usuario()  # cria tabela usuário se necessário
        resultado = criar_tabela_cuidador()
        assert resultado is True

    def test_inserir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(
            id=None,
            nome="Teste Cuidador",
            dataNascimento="1990-01-01",
            email="teste@cuidador.com",
            telefone="123456789",
            cpf="",
            senha="senha123",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-01-01",
            cep="12345-000",
            logradouro="Rua Teste",
            numero="123",
            complemento="",
            bairro="Centro",
            cidade="Cidade",
            estado="Estado",
            ativo=True,
            experiencia="5 anos",
            valorHora=50.0,
            escolaridade="Ensino Médio",
            apresentacao="Apresentação teste",
            cursos="Curso teste",
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True,
            inicio_profissional="2015-01-01"
        )

        id_inserido = inserir(cuidador)
        assert id_inserido is not None

        cuidador_db = obter_por_id(id_inserido)
        assert cuidador_db is not None
        assert cuidador_db.nome == cuidador.nome

    def test_obter_todos(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        c1 = Cuidador(
            id=None,
            nome="Cuidador A",
            dataNascimento="1980-01-01",
            email="cuidadorA@teste.com",
            telefone="111111111",
            cpf="11111111111",
            senha="senhaA",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-01-01",
            cep="00000-000",
            logradouro="Rua A",
            numero="1",
            complemento="",
            bairro="Bairro A",
            cidade="Cidade A",
            estado="Estado A",
            ativo=True,
            experiencia="3 anos",
            valorHora=40.0,
            escolaridade="Ensino Médio",
            apresentacao="Apresentação A",
            cursos="Curso A",
            confirmarSenha="senhaA",
            termos=True,
            verificacao=True,
            comunicacoes=True,
            inicio_profissional="2012-01-01"
        )
        inserir(c1)

        c2 = Cuidador(
            id=None,
            nome="Cuidador B",
            dataNascimento="1985-02-02",
            email="cuidadorB@teste.com",
            telefone="222222222",
            cpf="22222222222",
            senha="senhaB",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-01-01",
            cep="11111-111",
            logradouro="Rua B",
            numero="2",
            complemento="",
            bairro="Bairro B",
            cidade="Cidade B",
            estado="Estado B",
            ativo=True,
            experiencia="4 anos",
            valorHora=45.0,
            escolaridade="Ensino Superior",
            apresentacao="Apresentação B",
            cursos="Curso B",
            confirmarSenha="senhaB",
            termos=True,
            verificacao=True,
            comunicacoes=True,
            inicio_profissional="2013-01-01"
        )
        inserir(c2)

        lista = obter_todos()
        nomes = [c.nome for c in lista]

        assert "Cuidador A" in nomes
        assert "Cuidador B" in nomes
        assert len(lista) >= 2

    def test_atualizar_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(
            id=None,
            nome="Atualizar Teste",
            dataNascimento="1990-01-01",
            email="atualizar@teste.com",
            telefone="333333333",
            cpf="33333333333",
            senha="senha",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-01-01",
            cep="22222-222",
            logradouro="Rua Atualizar",
            numero="3",
            complemento="",
            bairro="Bairro Atualizar",
            cidade="Cidade Atualizar",
            estado="Estado Atualizar",
            ativo=True,
            experiencia="2 anos",
            valorHora=30.0,
            escolaridade="Ensino Médio",
            apresentacao="Apresentação inicial",
            cursos="Curso inicial",
            confirmarSenha="senha",
            termos=True,
            verificacao=True,
            comunicacoes=True,
            inicio_profissional="2014-01-01"
        )
        id_cuidador = inserir(cuidador)

        # atualiza
        cuidador_atualizado = obter_por_id(id_cuidador)
        cuidador_atualizado.experiencia = "10 anos"
        resultado = atualizar(cuidador_atualizado)
        assert resultado is True

        atualizado = obter_por_id(id_cuidador)
        assert atualizado.experiencia == "10 anos"

    def test_excluir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(
            id=None,
            nome="Excluir Teste",
            dataNascimento="1990-01-01",
            email="excluir@teste.com",
            telefone="444444444",
            cpf="44444444444",
            senha="senha",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-01-01",
            cep="33333-333",
            logradouro="Rua Excluir",
            numero="4",
            complemento="",
            bairro="Bairro Excluir",
            cidade="Cidade Excluir",
            estado="Estado Excluir",
            ativo=True,
            experiencia="1 ano",
            valorHora=25.0,
            escolaridade="Ensino Fundamental",
            apresentacao="Apresentação excluir",
            cursos="Curso excluir",
            confirmarSenha="senha",
            termos=True,
            verificacao=True,
            comunicacoes=True,
            inicio_profissional="2016-01-01"
        )
        id_cuidador = inserir(cuidador)

        resultado = excluir(id_cuidador)
        assert resultado is True

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is None
