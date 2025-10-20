import pytest
import random
import string
from datetime import datetime
import sqlite3

from data.usuario.usuario_repo import (
    criar_tabela, inserir, obter_por_cpf, obter_por_id,
    obter_todos, alterar, excluir, atualizar_foto, obter_por_email,
    ativar_usuario, obter_por_token
)
from data.usuario.usuario_model import Usuario

DB_PATH = "dados.db"

class TestUsuarioRepo:

    def setup_method(self):
        """Roda antes de cada teste: recria a tabela para garantir ambiente limpo"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS usuario;")  # corrigido: nome correto da tabela
        conn.commit()
        conn.close()
        criar_tabela()

    def criar_usuario_fake(self) -> Usuario:
        sufixo = ''.join(random.choices(string.digits, k=6))  # garante unicidade
        return Usuario(
            id=None,
            nome="Usuario Teste",
            dataNascimento="2000-01-01",
            email=f"email{sufixo}@test.com",
            telefone="123456789",
            cpf=f"123456{sufixo}",
            senha="Senha123",
            perfil="contratante",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),  # melhor usar datetime, não string
            cep="00000000",
            logradouro="Rua Teste",
            numero="123",
            complemento="",
            bairro="Centro",
            cidade="Cidade",
            estado="Estado",
            ativo=True,
        )

    def test_inserir(self):
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)
        assert id_usuario_inserido is not None

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is not None
        assert usuario_db.id == id_usuario_inserido
        assert usuario_db.nome == usuario_teste.nome
        assert usuario_db.email == usuario_teste.email
        assert usuario_db.telefone == usuario_teste.telefone
        assert usuario_db.cpf == usuario_teste.cpf

    def test_obter_por_cpf(self):
        usuario_teste = self.criar_usuario_fake()
        inserir(usuario_teste)

        usuario_db = obter_por_cpf(usuario_teste.cpf)
        assert usuario_db is not None
        assert usuario_db.cpf == usuario_teste.cpf
        assert usuario_db.nome == usuario_teste.nome
        assert usuario_db.email == usuario_teste.email

    def test_obter_todos(self):
        inserir(self.criar_usuario_fake())
        inserir(self.criar_usuario_fake())

        lista_usuarios = obter_todos()
        assert len(lista_usuarios) >= 2
        nomes = [u.nome for u in lista_usuarios]
        assert "Usuario Teste" in nomes

    def test_obter_por_id(self):
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)
        assert id_usuario_inserido is not None

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is not None
        assert usuario_db.id == id_usuario_inserido
        assert usuario_db.nome == usuario_teste.nome

    def test_atualizar(self):
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)
        assert id_usuario_inserido is not None
        usuario_inserido = obter_por_id(id_usuario_inserido)
        assert usuario_inserido is not None

        usuario_inserido.nome = "Usuario Atualizado"
        usuario_inserido.email = "atualizado@test.com"
        usuario_inserido.senha = "NovaSenha"
        usuario_inserido.telefone = "987654321"
        usuario_inserido.cidade = "Cidade Nova"
        usuario_inserido.foto = "nova_foto.png"

        resultado = alterar(usuario_inserido)
        assert resultado is True

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is not None
        assert usuario_db.nome == "Usuario Atualizado"
        assert usuario_db.email == "atualizado@test.com"
        assert usuario_db.senha == "NovaSenha"
        assert usuario_db.telefone == "987654321"
        assert usuario_db.cidade == "Cidade Nova"
        assert usuario_db.foto == "nova_foto.png"

    def test_atualizar_foto(self):
        usuario_teste = self.criar_usuario_fake()
        id_usuario = inserir(usuario_teste)
        assert id_usuario is not None

        nova_foto = "foto_atualizada.png"
        resultado = atualizar_foto(id_usuario, nova_foto)

        assert resultado is True
        usuario_db = obter_por_id(id_usuario)
        assert usuario_db is not None
        assert usuario_db.foto == nova_foto

    def test_excluir_usuario(self):
        usuario_teste = self.criar_usuario_fake()
        id_usuario_inserido = inserir(usuario_teste)
        assert id_usuario_inserido is not None

        resultado = excluir(id_usuario_inserido)
        assert resultado is True

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is None

    def test_obter_por_email(self):
        usuario_teste = self.criar_usuario_fake()
        inserir(usuario_teste)

        usuario_db = obter_por_email(usuario_teste.email)
        assert usuario_db is not None
        assert usuario_db.email == usuario_teste.email
        assert usuario_db.nome == usuario_teste.nome

        # Testa email inexistente
        usuario_inexistente = obter_por_email("naoexiste@test.com")
        assert usuario_inexistente is None

    def test_ativar_usuario(self):
        usuario_teste = self.criar_usuario_fake()
        usuario_teste.ativo = False
        id_usuario = inserir(usuario_teste)
        assert id_usuario is not None

        # Verifica que está inativo
        usuario_db = obter_por_id(id_usuario)
        assert usuario_db is not None
        assert usuario_db.ativo == False

        # Ativa o usuário
        resultado = ativar_usuario(id_usuario)
        assert resultado is True

        # Verifica que está ativo
        usuario_db = obter_por_id(id_usuario)
        assert usuario_db is not None
        assert usuario_db.ativo == True

    def test_obter_por_token(self):
        usuario_teste = self.criar_usuario_fake()
        token_teste = "token123abc"
        usuario_teste.token_redefinicao = token_teste
        usuario_teste.data_token = datetime.now()
        id_usuario = inserir(usuario_teste)
        assert id_usuario is not None

        # Obtém por token
        usuario_db = obter_por_token(token_teste)
        assert usuario_db is not None
        assert usuario_db.id == id_usuario
        assert usuario_db.token_redefinicao == token_teste

        # Testa token inexistente
        usuario_inexistente = obter_por_token("tokeninvalido")
        assert usuario_inexistente is None
