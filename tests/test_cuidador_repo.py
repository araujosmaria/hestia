from data.cuidador import cuidador_repo
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import inserir as inserir_usuario, criar_tabela as criar_tabela_usuario
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_repo import (
    criar_tabela as criar_tabela_cuidador,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)

def criar_usuario_teste():
    usuario = Usuario(
        id=None,
        nome="Usuário Teste",
        dataNascimento="1990-01-01",
        email="usuario@teste.com",
        telefone="999999999",
        cpf="12345678901",
        senha="senha123",
        perfil="cuidador",
        foto=None,
        token_redefinicao=None,
        data_token=None,
        data_cadastro=None,
        cep="00000-000",
        logradouro="Rua Teste",
        numero="100",
        complemento="",
        bairro="Bairro Teste",
        cidade="Cidade Teste",
        estado="Estado Teste",
        ativo=True
    )
    return inserir_usuario(usuario)

class TestCuidadorRepo:

    def test_criar_tabela(self):
        criar_tabela_usuario()
        resultado = criar_tabela_cuidador()
        assert resultado is True

    def test_inserir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        id_usuario = criar_usuario_teste()

        cuidador = Cuidador(
            id=id_usuario,
            experiencia="5 anos",
            valorHora=50.0,
            escolaridade="Ensino Médio",
            apresentacao="Apresentação teste",
            cursos="Curso teste",
            inicio_profissional="2015-01-01",
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )
        id_cuidador = inserir(cuidador)
        assert id_cuidador == id_usuario

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.id == id_usuario
        assert cuidador_db.experiencia == cuidador.experiencia

    def test_obter_todos(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        id_usuario1 = criar_usuario_teste()
        cuidador1 = Cuidador(
            id=id_usuario1,
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
        inserir(cuidador1)

        usuario2 = Usuario(
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
            data_cadastro=None,
            cep="11111-111",
            logradouro="Rua B",
            numero="2",
            complemento="",
            bairro="Bairro B",
            cidade="Cidade B",
            estado="Estado B",
            ativo=True
        )
        id_usuario2 = inserir_usuario(usuario2)
        cuidador2 = Cuidador(
            id=id_usuario2,
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
        inserir(cuidador2)

        lista = obter_todos()
        ids = [c.id for c in lista]

        assert id_usuario1 in ids
        assert id_usuario2 in ids
        assert len(lista) >= 2

    def test_atualizar_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        id_usuario = criar_usuario_teste()
        cuidador = Cuidador(
            id=id_usuario,
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
        inserir(cuidador)

        cuidador_atualizado = obter_por_id(id_usuario)
        cuidador_atualizado.experiencia = "10 anos"
        resultado = atualizar(cuidador_atualizado)
        assert resultado is True

        atualizado = obter_por_id(id_usuario)
        assert atualizado.experiencia == "10 anos"

    def test_excluir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        id_usuario = criar_usuario_teste()
        cuidador = Cuidador(
            id=id_usuario,
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
        inserir(cuidador)

        resultado = excluir(id_usuario)
        assert resultado is True

        cuidador_db = obter_por_id(id_usuario)
        assert cuidador_db is None


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
