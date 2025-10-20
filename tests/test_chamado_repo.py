import datetime
import pytest
from data.chamado.chamado_repo import (
    criar_tabela,
    inserir,
    obter_todos,
    atualizar,
    excluir
)
from data.chamado.chamado_model import Chamado

class TestChamadoRepo:
    def test_criar_tabela(test_db):
        resultado = criar_tabela()
        assert resultado is True, "A criação da tabela de chamados deve retornar True"


    def test_inserir_chamado(self, test_db):
        criar_tabela()
        chamado_teste = Chamado(
            id=0,
            titulo="Erro no sistema",
            descricao="Não consigo acessar a plataforma",
            status="Aberto",
            data_criacao=datetime.datetime.now(),
            id_administrador=1
        )

        id_inserido = inserir(chamado_teste)
        assert id_inserido is not None, "O ID retornado após inserção não pode ser None"


    def test_obter_todos_chamados(test_db):
        criar_tabela()
        chamado_teste = Chamado(
            id=0,
            titulo="Erro teste",
            descricao="Descrição teste",
            status="Aberto",
            data_criacao=datetime.datetime.now(),
            id_administrador=1
        )

        id_inserido = inserir(chamado_teste)
        chamados = obter_todos()

        assert isinstance(chamados, list), "obter_todos deve retornar uma lista"
        assert any(c.id == id_inserido for c in chamados), "Chamado inserido não encontrado na lista"


    def test_atualizar_chamado(test_db):
        criar_tabela()
        chamado = Chamado(
            id=0,
            titulo="Erro X",
            descricao="Descrição X",
            status="Aberto",
            data_criacao=datetime.datetime.now(),
            id_administrador=1
        )
        id_chamado = inserir(chamado)
        assert id_chamado is not None

        chamado.id = id_chamado
        chamado.titulo = "Erro Corrigido"
        chamado.descricao = "Erro resolvido"
        chamado.status = "Fechado"

        atualizado = atualizar(chamado)
        assert atualizado is True, "A atualização do chamado deveria retornar True"

        chamados = obter_todos()
        chamado_db = next((c for c in chamados if c.id == id_chamado), None)
        assert chamado_db is not None
        assert chamado_db.status == "Fechado", "O status atualizado não foi salvo corretamente"
        assert chamado_db.titulo == "Erro Corrigido", "O título atualizado não foi salvo corretamente"


    def test_excluir_chamado(test_db):
        criar_tabela()
        chamado = Chamado(
            id=0,
            titulo="Chamado para deletar",
            descricao="Teste",
            status="Aberto",
            data_criacao=datetime.datetime.now(),
            id_administrador=1
        )
        id_chamado = inserir(chamado)
        assert id_chamado is not None

        resultado = excluir(id_chamado)
        assert resultado is True, "A exclusão do chamado deveria retornar True"

        chamados = obter_todos()
        assert all(c.id != id_chamado for c in chamados), "Chamado excluído ainda está na lista"

    def test_criar_tabela_error_handling(self, test_db):
        # Test que a função criar_tabela retorna True mesmo quando já existe
        criar_tabela()
        resultado1 = criar_tabela()
        resultado2 = criar_tabela()
        assert resultado1 is True
        assert resultado2 is True