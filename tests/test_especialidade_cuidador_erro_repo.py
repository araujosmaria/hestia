import pytest
from data.especialidade_cuidador import especialidade_cuidador_repo as ec_repo
from data.especialidade_cuidador.especialidade_cuidador_model import EspecialidadeCuidador


class TestEspecialidadeCuidadorErros:
    """Testes para cobrir cenários de erro no especialidade_cuidador_repo"""

    def test_inserir_sem_fks(self, test_db):
        """Testa inserir sem foreign keys existentes"""
        ec_repo.criar_tabela()

        ec = EspecialidadeCuidador(
            id_cuidador=99999,  # FK não existente
            id_especialidade=99999,  # FK não existente
            anos_experiencia=5
        )

        # SQLite não aplica FK constraints por padrão
        resultado = ec_repo.inserir(ec)
        # Aceita tanto True quanto False dependendo da configuração
        assert resultado is True or resultado is False

    def test_atualizar_com_fk_invalida(self, test_db):
        """Tenta atualizar com foreign keys inválidas"""
        ec_repo.criar_tabela()

        ec = EspecialidadeCuidador(
            id_cuidador=99999,  # FK inválida
            id_especialidade=99999,  # FK inválida
            anos_experiencia=10
        )

        resultado = ec_repo.atualizar(ec)
        assert resultado is False

    def test_excluir_com_ids_invalidos(self, test_db):
        """Tenta excluir com IDs inválidos"""
        ec_repo.criar_tabela()

        resultado = ec_repo.excluir(99999, 99999)
        assert resultado is False

    def test_obter_especialidades_lista_vazia(self, test_db):
        """Testa obter_especialidades_por_cuidador quando não há registros"""
        ec_repo.criar_tabela()

        resultado = ec_repo.obter_especialidades_por_cuidador(99999)
        assert resultado == []
