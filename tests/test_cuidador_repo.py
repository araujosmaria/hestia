from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_repo import (
    criar_tabela as criar_tabela_cuidador,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario
from datetime import date
import random
import string

class TestCuidadorRepo:

    def test_criar_cuidador_fake(self) -> Cuidador:
        sufixo = ''.join(random.choices(string.digits, k=6))
        return Cuidador(
            id=None,
            nome=f"Cuidador Teste {sufixo}",
            dataNascimento="1990-01-01",
            email=f"cuidador_{sufixo}@teste.com",
            telefone="123456789",
            cpf=f"123456{sufixo}",
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

    def test_criar_tabela(self):
        criar_tabela_usuario()
        resultado = criar_tabela_cuidador()
        assert resultado is True

    def test_inserir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = self.criar_cuidador_fake()
        id_inserido = inserir(cuidador)

        assert id_inserido is not None

        cuidador_db = obter_por_id(id_inserido)
        assert cuidador_db is not None
        assert cuidador_db.nome == cuidador.nome
        assert cuidador_db.experiencia == cuidador.experiencia

    def test_obter_todos_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        c1 = self.criar_cuidador_fake()
        c1.nome = "Cuidador A"
        inserir(c1)

        c2 = self.criar_cuidador_fake()
        c2.nome = "Cuidador B"
        inserir(c2)

        lista = obter_todos()
        nomes = [c.nome for c in lista]

        assert "Cuidador A" in nomes
        assert "Cuidador B" in nomes
        assert len(lista) >= 2

    def test_obter_por_id(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = self.criar_cuidador_fake()
        id_cuidador = inserir(cuidador)

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.id == id_cuidador
        assert cuidador_db.nome == cuidador.nome

    def test_atualizar_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = self.criar_cuidador_fake()
        id_cuidador = inserir(cuidador)

        cuidador_atualizado = cuidador
        cuidador_atualizado.experiencia = "10 anos"
        resultado = atualizar(cuidador_atualizado)

        assert resultado is True

        atualizado = obter_por_id(id_cuidador)
        assert atualizado.experiencia == "10 anos"

    def test_excluir_cuidador(self):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = self.criar_cuidador_fake()
        id_cuidador = inserir(cuidador)

        resultado = excluir(id_cuidador)
        assert resultado is True

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is None
