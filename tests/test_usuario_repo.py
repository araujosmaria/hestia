import pytest
import random
import string
from datetime import datetime
from data.usuario.usuario_repo import (
    criar_tabela,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)
from data.usuario.usuario_model import Usuario


class TestUsuarioRepo:
    def test_criar_tabela(self, test_db):
        resultado = criar_tabela()
        assert resultado is True, "A criação da tabela deveria retornar True"

    def criar_usuario_fake(self) -> Usuario:
        """Cria um usuário válido para testes com email e cpf únicos"""
        sufixo = ''.join(random.choices(string.digits, k=6))  # garante unicidade
        return Usuario(
            id=None,
            nome="Usuario Teste",
            dataNascimento="2000-01-01",
            email=f"email{sufixo}@test.com",  # email único
            telefone="123456789",
            cpf=f"123456{sufixo}",  # cpf único
            senha="Senha123",
            perfil="contratante",
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
        )

    def test_inserir(self, test_db):
        criar_tabela()
        usuario_teste = self.criar_usuario_fake()

        id_usuario_inserido = inserir(usuario_teste)
        usuario_db = obter_por_id(id_usuario_inserido)

        assert usuario_db is not None, "O usuário inserido não deveria ser None"
        assert usuario_db.id == id_usuario_inserido, "O ID não confere"
        assert usuario_db.nome == usuario_teste.nome, "O nome não confere"
        assert usuario_db.email == usuario_teste.email, "O email não confere"
        assert usuario_db.telefone == usuario_teste.telefone, "O telefone não confere"
        assert usuario_db.cpf == usuario_teste.cpf, "O CPF não confere"

    def test_obter_todos(self, test_db):
        criar_tabela()
        inserir(self.criar_usuario_fake())
        inserir(self.criar_usuario_fake())

        lista_usuarios = obter_todos()
        assert len(lista_usuarios) >= 2, "Deveria retornar pelo menos 2 usuários"
        nomes = [u.nome for u in lista_usuarios]
        assert "Usuario Teste" in nomes, "Usuario Teste deveria estar na lista"

    def test_obter_por_id(self, test_db):
        criar_tabela()
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is not None, "O usuário retornado não deveria ser None"
        assert usuario_db.id == id_usuario_inserido, "O ID buscado não confere"
        assert usuario_db.nome == usuario_teste.nome, "O nome buscado não confere"

    def test_atualizar_usuario(self, test_db):
        criar_tabela()
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)
        usuario_inserido = obter_por_id(id_usuario_inserido)

        usuario_inserido.nome = "Usuario Atualizado"
        usuario_inserido.email = "atualizado@test.com"
        usuario_inserido.senha = "NovaSenha"
        usuario_inserido.telefone = "987654321"
        usuario_inserido.cidade = "Cidade Nova"

        resultado = atualizar(usuario_inserido)
        assert resultado is True, "A atualização deveria retornar True"

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db.nome == "Usuario Atualizado", "Nome atualizado não confere"
        assert usuario_db.email == "atualizado@test.com", "Email atualizado não confere"
        assert usuario_db.senha == "NovaSenha", "Senha atualizada não confere"
        assert usuario_db.telefone == "987654321", "Telefone atualizado não confere"
        assert usuario_db.cidade == "Cidade Nova", "Cidade atualizada não confere"

    def test_excluir_usuario(self, test_db):
        criar_tabela()
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)

        resultado = excluir(id_usuario_inserido)
        assert resultado is True, "A exclusão deveria retornar True"

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is None, "Usuário excluído não deveria ser encontrado"
