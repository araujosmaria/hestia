import sys
import os
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario
from data.cliente.cliente_repo import (criar_tabela as criar_tabela_cliente, inserir, obter_todos, obter_por_id, excluir)


class TestClienteRepo:
    def test_criar_tabela(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela_cliente()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_teste = Cliente(
            id=0,
            nome="Cliente Teste",
            email="email@test.com",
            senha="Senha",
            telefone="Telefone",
            endereco="Endereco"
        )
        # Act
        id_cliente_inserido = inserir(cliente_teste)
        # Assert
        cliente_db = obter_por_id(id_cliente_inserido)
        assert cliente_db is not None, "O cliente inserido não deveria ser None"
        assert cliente_db.id == id_cliente_inserido, "O ID do cliente não confere"
        assert cliente_db.nome == cliente_teste.nome, "O nome inserido não confere"
        assert cliente_db.email == cliente_teste.email, "O email inserido não confere"
        assert cliente_db.senha == cliente_teste.senha, "A senha inserida não confere"
        assert cliente_db.telefone == cliente_teste.telefone, "O telefone inserido não confere"
        assert cliente_db.endereco == cliente_teste.endereco, "O endereço inserido não confere"

    def test_obter_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_teste = Cliente(0, "Cliente Teste", "teste@cliente.com", "123", "9999-0000", "Rua Teste")
        id_cliente = inserir(cliente_teste)
        # Act
        cliente_db = obter_por_id(id_cliente)
        # Assert
        assert cliente_db is not None, "O cliente retornado não deveria ser None"
        assert cliente_db.id == id_cliente, "O ID do cliente buscado deveria ser igual ao ID inserido"
        assert cliente_db.nome == cliente_teste.nome, "O nome do cliente buscado deveria ser igual ao inserido"

    def test_obter_todos_clientes(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        inserir(Cliente(0, "Cliente A", "a@cliente.com", "abc", "111", "Rua A"))
        inserir(Cliente(0, "Cliente B", "b@cliente.com", "def", "222", "Rua B"))
        # Act
        lista_clientes = obter_todos()
        # Assert
        assert len(lista_clientes) >= 2, "Deveria retornar pelo menos 2 clientes"
        nomes = [c.nome for c in lista_clientes]
        assert "Cliente A" in nomes, "Cliente A deveria estar na lista"
        assert "Cliente B" in nomes, "Cliente B deveria estar na lista"

    def test_excluir_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente = Cliente(0, "Cliente Excluir", "excluir@cliente.com", "000", "999", "Rua X")
        id_cliente = inserir(cliente)

        # Act
        resultado = excluir(id_cliente)
        cliente_db = obter_por_id(id_cliente)

        # Assert
        assert resultado == True, "A exclusão do cliente deveria retornar True"
        assert cliente_db is None, "O cliente excluído deveria ser None"
