import pytest
from unittest.mock import patch
from datetime import datetime, timedelta
from data.atendimento.atendimento_model import Atendimento
from data.atendimento import atendimento_repo


class TestAtendimentoExceptions:
    """Testes para cobrir blocos except do atendimento_repo"""

    def test_criar_tabela_com_erro(self, test_db):
        """Testa o bloco except de criar_tabela quando ocorre erro"""
        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de conexão")
            resultado = atendimento_repo.criar_tabela()
            assert resultado is False

    def test_inserir_com_erro_db(self, test_db):
        """Testa o bloco except de inserir quando ocorre erro"""
        atendimento = Atendimento(
            id=0,
            dataInicio=datetime.now(),
            dataFim=datetime.now() + timedelta(hours=1),
            id_cliente=1,
            id_cuidador=1
        )

        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de inserção")
            resultado = atendimento_repo.inserir(atendimento)
            assert resultado is None

    def test_obter_todos_com_erro_db(self, test_db):
        """Testa o bloco except de obter_todos quando ocorre erro"""
        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de consulta")
            resultado = atendimento_repo.obter_todos()
            assert resultado == []

    def test_obter_por_id_com_erro_db(self, test_db):
        """Testa o bloco except de obter_por_id quando ocorre erro"""
        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de consulta")
            resultado = atendimento_repo.obter_por_id(1)
            assert resultado is None

    def test_atualizar_com_erro_db(self, test_db):
        """Testa o bloco except de atualizar quando ocorre erro"""
        atendimento = Atendimento(
            id=1,
            dataInicio=datetime.now(),
            dataFim=datetime.now() + timedelta(hours=1),
            id_cliente=1,
            id_cuidador=1
        )

        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de atualização")
            resultado = atendimento_repo.atualizar(atendimento)
            assert resultado is False

    def test_excluir_com_erro_db(self, test_db):
        """Testa o bloco except de excluir quando ocorre erro"""
        with patch('sqlite3.connect') as mock_connect:
            mock_connect.side_effect = Exception("Erro simulado de exclusão")
            resultado = atendimento_repo.excluir(1)
            assert resultado is False
