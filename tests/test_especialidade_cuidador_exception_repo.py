import pytest
from unittest.mock import patch, MagicMock
from data.especialidade_cuidador import especialidade_cuidador_repo as ec_repo
from data.especialidade_cuidador.especialidade_cuidador_model import EspecialidadeCuidador


class TestEspecialidadeCuidadorExceptions:
    """Testes para cobrir blocos except do especialidade_cuidador_repo"""

    def test_criar_tabela_com_erro(self, test_db):
        """Testa o bloco except de criar_tabela quando ocorre erro"""
        with patch('data.especialidade_cuidador.especialidade_cuidador_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de conexão")
            resultado = ec_repo.criar_tabela()
            assert resultado is False

    def test_inserir_com_erro_db(self, test_db):
        """Testa o bloco except de inserir quando ocorre erro"""
        ec_repo.criar_tabela()

        ec = EspecialidadeCuidador(1, 1, 5)

        with patch('data.especialidade_cuidador.especialidade_cuidador_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de inserção")
            resultado = ec_repo.inserir(ec)
            assert resultado is False

    def test_atualizar_com_erro_db(self, test_db):
        """Testa o bloco except de atualizar quando ocorre erro"""
        ec_repo.criar_tabela()

        ec = EspecialidadeCuidador(1, 1, 10)

        with patch('data.especialidade_cuidador.especialidade_cuidador_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de atualização")
            resultado = ec_repo.atualizar(ec)
            assert resultado is False

    def test_excluir_com_erro_db(self, test_db):
        """Testa o bloco except de excluir quando ocorre erro"""
        ec_repo.criar_tabela()

        with patch('data.especialidade_cuidador.especialidade_cuidador_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de exclusão")
            resultado = ec_repo.excluir(1, 1)
            assert resultado is False

    def test_obter_especialidades_com_erro_db(self, test_db):
        """Testa o bloco except de obter_especialidades_por_cuidador quando ocorre erro"""
        ec_repo.criar_tabela()

        with patch('data.especialidade_cuidador.especialidade_cuidador_repo.open_connection') as mock_conn:
            mock_conn.side_effect = Exception("Erro simulado de consulta")
            resultado = ec_repo.obter_especialidades_por_cuidador(1)
            assert resultado == []
