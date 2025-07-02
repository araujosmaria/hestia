# from typing import Optional
from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_repo import (
    criar_tabela as criar_tabela_cuidador,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)
from data.usuario import usuario_repo
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario


class TestCuidadorRepo:
    def test_criar_tabela(self, test_db):
        criar_tabela_usuario()
        resultado = criar_tabela_cuidador()
        assert resultado == True, "A criação da tabela de cuidadores deveria retornar True"

    def test_inserir_cuidador(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(
            id=0,
            nome="Cuidador Teste",
            email="cuidador@test.com",
            senha="senha123",
            telefone="123456789",
            endereco="Rua Teste",
            experiencia_anos=5
        )

        id_inserido = inserir(cuidador)
        assert id_inserido is not None, "Deveria retornar id ao inserir"

        cuidador_db = obter_por_id(id_inserido)
        assert cuidador_db is not None, "O cuidador inserido não deveria ser None"
        assert cuidador_db.nome == cuidador.nome
        assert cuidador_db.email == cuidador.email
        assert cuidador_db.experiencia_anos == cuidador.experiencia_anos

    def test_obter_todos_cuidador(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        inserir(Cuidador(0, "Cuidador A", "a@cuidador.com", "senhaA", "1111", "Rua A", 3))
        inserir(Cuidador(0, "Cuidador B", "b@cuidador.com", "senhaB", "2222", "Rua B", 5))

        lista = obter_todos()
        nomes = [c.nome for c in lista]

        assert "Cuidador A" in nomes
        assert "Cuidador B" in nomes
        assert len(lista) >= 2

    def test_obter_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(0, "Cuidador Teste", "teste@cuidador.com", "123", "123456", "Rua A", 5)
        id_cuidador = inserir(cuidador)

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is not None
        assert cuidador_db.id == id_cuidador
        assert cuidador_db.nome == cuidador.nome

    def test_atualizar_cuidador(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(0, "Cuidador Antigo", "antigo@cuidador.com", "senha", "123", "Rua Antiga", 1)
        id_cuidador = inserir(cuidador)

        cuidador_atualizado = Cuidador(
            id=id_cuidador,
            nome="Cuidador Atualizado",
            email="novo@cuidador.com",
            senha="nova",
            telefone="999",
            endereco="Rua Nova",
            experiencia_anos=10
        )

        resultado = atualizar(cuidador_atualizado)
        assert resultado == True

        atualizado = obter_por_id(id_cuidador)
        assert atualizado.nome == "Cuidador Atualizado"
        assert atualizado.experiencia_anos == 10

    def test_excluir_cuidador(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cuidador()

        cuidador = Cuidador(0, "Excluir Cuidador", "del@cuidador.com", "senha", "000", "Rua Delete", 2)
        id_cuidador = inserir(cuidador)

        resultado = excluir(id_cuidador)
        assert resultado == True

        cuidador_db = obter_por_id(id_cuidador)
        assert cuidador_db is None
