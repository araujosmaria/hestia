import pytest
from unittest.mock import patch
from data.avaliacao import avaliacao_repo


class TestAvaliacaoExceptions:
    """Testes para cobrir blocos except do avaliacao_repo"""

    def test_criar_tabela_com_erro(self, test_db):
        """Testa o bloco except de criar_tabela quando ocorre erro"""
        with patch('data.avaliacao.avaliacao_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de conexão")
            resultado = avaliacao_repo.criar_tabela()
            assert resultado is False
