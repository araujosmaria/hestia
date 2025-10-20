import pytest
from unittest.mock import patch
from datetime import datetime
from data.agenda.agenda_model import Agenda
from data.agenda import agenda_repo


class TestAgendaExceptions:
    """Testes para cobrir blocos except do agenda_repo"""

    def test_criar_tabela_com_erro(self, test_db):
        """Testa o bloco except de criar_tabela quando ocorre erro"""
        with patch('data.agenda.agenda_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de conexão")
            resultado = agenda_repo.criar_tabela()
            assert resultado is False
