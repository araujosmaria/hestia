import pytest
from unittest.mock import patch
from data.chat import chat_repo


class TestChatExceptions:
    """Testes para cobrir blocos except do chat_repo"""

    def test_criar_tabela_com_erro(self, test_db):
        """Testa o bloco except de criar_tabela quando ocorre erro"""
        with patch('data.chat.chat_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de conexão")
            resultado = chat_repo.criar_tabela()
            assert resultado is False
