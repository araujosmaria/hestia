import pytest
from unittest.mock import patch, MagicMock
from data.cuidador import cuidador_repo
from data.cuidador.cuidador_model import Cuidador
from data.usuario import usuario_repo
from datetime import datetime
import sqlite3


class TestCuidadorExceptions:
    """Testes para cobrir blocos except do cuidador_repo"""

    def test_inserir_com_usuario_erro(self, test_db):
        """Testa quando inserir usuario retorna None - cobre linha 291"""
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()

        cuidador = Cuidador(
            id=0,
            nome="Cuidador Teste",
            dataNascimento="1985-05-15",
            email="cuidador@test.com",
            telefone="11988888888",
            cpf="11111111111",
            senha="senha123",
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
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

        # Mock usuario_repo.inserir para retornar None
        with patch('data.cuidador.cuidador_repo.usuario_repo.inserir') as mock_inserir:
            mock_inserir.return_value = None

            # Isso deve ativar a linha 291 (return None quando id_usuario é None)
            resultado = cuidador_repo.inserir(cuidador)
            assert resultado is None

    def test_inserir_cpf_duplicado(self, test_db):
        """Testa inserção com CPF duplicado - cobre linha 264-265"""
        from data.usuario import usuario_repo
        usuario_repo.criar_tabela()
        cuidador_repo.criar_tabela()

        cuidador1 = Cuidador(
            id=0,
            nome="Cuidador 1",
            dataNascimento="1985-05-15",
            email="cuidador1@test.com",
            telefone="11988888888",
            cpf="12345678901",
            senha="senha123",
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
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

        id1 = cuidador_repo.inserir(cuidador1)
        assert id1 is not None

        # Tenta inserir com mesmo CPF
        cuidador2 = Cuidador(
            id=0,
            nome="Cuidador 2",
            dataNascimento="1990-03-20",
            email="cuidador2@test.com",
            telefone="11977777777",
            cpf="12345678901",  # CPF duplicado
            senha="senha456",
            perfil="cuidador",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            cep="87654321",
            logradouro="Rua Outra",
            numero="200",
            complemento="Apto",
            bairro="Bairro",
            cidade="Rio de Janeiro",
            estado="RJ",
            ativo=True,
            experiencia="3 anos",
            valorHora=25.0,
            escolaridade="Ensino Superior",
            apresentacao="Cuidadora experiente",
            cursos="Enfermagem",
            inicio_profissional="2020-01-01",
            confirmarSenha="senha456",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

        id2 = cuidador_repo.inserir(cuidador2)
        # Deve retornar None por CPF duplicado
        assert id2 is None
