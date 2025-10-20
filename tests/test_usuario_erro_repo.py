import pytest
from data.usuario.usuario_repo import inserir, obter_por_cpf
from data.usuario.usuario_model import Usuario
from datetime import datetime
import sqlite3
import os


class TestUsuarioRepoErros:
    """Testes que cobrem cenários de erro nos repositórios"""

    def test_obter_por_cpf_inexistente(self, test_db):
        # Testa busca por CPF que não existe
        from data.usuario import usuario_repo
        usuario_repo.criar_tabela()

        resultado = obter_por_cpf("00000000000")
        assert resultado is None

    def test_inserir_com_cpf_duplicado(self, test_db):
        """Testa inserir usuário com CPF duplicado - deve retornar None"""
        from data.usuario import usuario_repo
        usuario_repo.criar_tabela()

        usuario1 = Usuario(
            nome="Usuario 1",
            dataNascimento="2000-01-01",
            email="user1@test.com",
            telefone="123456789",
            cpf="12345678901",
            senha="senha123",
            perfil="contratante",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="00000000",
            logradouro="Rua Teste",
            numero="123",
            complemento="",
            bairro="Centro",
            cidade="Cidade",
            estado="Estado",
            ativo=True,
        )

        id1 = inserir(usuario1)
        assert id1 is not None

        # Tenta inserir com mesmo CPF
        usuario2 = Usuario(
            nome="Usuario 2",
            dataNascimento="2000-01-01",
            email="user2@test.com",
            telefone="987654321",
            cpf="12345678901",  # CPF duplicado
            senha="senha456",
            perfil="contratante",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="11111111",
            logradouro="Rua Outra",
            numero="456",
            complemento="",
            bairro="Bairro",
            cidade="Cidade",
            estado="Estado",
            ativo=True,
        )

        # Deve retornar None por violação de constraint UNIQUE
        id2 = inserir(usuario2)
        assert id2 is None
