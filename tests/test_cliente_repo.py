import sys
import os
from data.cliente import cliente_repo
from data.usuario import usuario_repo
from data.cliente.cliente_model import Cliente


class TestClienteRepo:
    def test_criar_tabela(self, test_db):
        # Arrange
        # Act
        resultado = cliente_repo.criar_tabela()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir(self, test_db):
        # Arrange
        usuario_repo.criar_tabela()
        cliente_repo.criar_tabela()
        cliente_teste = Cliente(
            id=0,
            nome="Cliente Teste",
            email="email@test.com",
            senha="Senha",
            telefone="Telefone",
            endereco="Endereco"
        )
        # Act
        id_cliente_inserido = cliente_repo.inserir(cliente_teste)
        # Assert
        cliente_db = cliente_repo.obter_por_id(id_cliente_inserido)
        assert cliente_db is not None, "O cliente inserido não deveria ser None"
        assert cliente_db.id == id_cliente_inserido, "O ID do cliente não confere"
        assert cliente_db.nome == cliente_teste.nome, "O nome inserido não confere"
        assert cliente_db.email == cliente_teste.email, "O email inserido não confere"
        assert cliente_db.senha == cliente_teste.senha, "A senha inserida não confere"
        assert cliente_db.telefone == cliente_teste.telefone, "O telefone inserido não confere"
        assert cliente_db.endereco == cliente_teste.endereco, "O endereço inserido não confere"



    def test_obter_todos(self, test_db):
        criar_tabela()
        inserir(Cliente(0, "Cliente 1", "a@test.com", "123", "000", "Rua A"))
        inserir(Cliente(0, "Cliente 2", "b@test.com", "456", "111", "Rua B"))

        lista_clientes = obter_todos()                                                                                            
        assert len(lista_clientes) >= 2, "Deveria retornar pelo menos 2 clientes"
        nomes = [u.nome for u in lista_clientes]
        assert "Cliente 1" in nomes, "Cliente 1 deveria estar na lista"
        assert "Cliente 2" in nomes, "Cliente 2 deveria estar na lista"  

    def test_obter_por_id(self, test_db):
        criar_tabela()
        cliente_teste = Cliente(0, "Cliente Teste", "email@test.com", "senha", "tel", "end")
        id_cliente_inserido = inserir(cliente_teste)

        cliente_db = obter_por_id(id_cliente_inserido)
        assert cliente_db is not None, "O cliente retornado não deveria ser None"
        assert cliente_db.id == id_cliente_inserido, "O ID do cliente buscado não confere"
        assert cliente_db.nome == cliente_teste.nome, "O nome do cliente buscado não confere"

    def test_atualizar_clientes(self, test_db):
        # Arrange
        criar_tabela()
        cliente_teste = Cliente(
            id=0,
            nome="Usuario Teste",
            email="email@test.com",
            senha="Senha123",
            telefone="123456789",
            endereco="Endereco Teste"
        )
        id_cliente_inserido = inserir(cliente_teste)
        cliente_inserido = obter_por_id(id_cliente_inserido)

        # Act
        cliente_inserido.nome = "Cliente Atualizado"
        cliente_inserido.email = "email_atualizado@test.com"
        cliente_inserido.senha = "NovaSenha"
        cliente_inserido.telefone = "987654321"
        cliente_inserido.endereco = "Endereco Atualizado"
        resultado = atualizar(cliente_inserido)

        # Assert
        assert resultado == True, "A atualização do cliente deveria retornar True"
        cliente_db = obter_por_id(id_cliente_inserido)
        assert cliente_db.nome == "Cliente Atualizado", "O nome do cliente atualizado não confere"
        assert cliente_db.email == "email_atualizado@test.com", "O email atualizado não confere"
        assert cliente_db.senha == "NovaSenha", "A senha atualizada não confere"
        assert cliente_db.telefone == "987654321", "O telefone atualizado não confere"
        assert cliente_db.endereco == "Endereco Atualizado", "O endereço atualizado não confere"


    def test_excluir_cliente(self, test_db):
        # Arrange
        criar_tabela()
        cliente_teste = Cliente(
            id=0,
            nome="Usuario Teste",
            email="email@test.com",
            senha="Senha123",
            telefone="123456789",
            endereco="Endereco Teste"
        )
        id_cliente_inserido = inserir(cliente_teste)
        
        # Act
        resultado = excluir(id_cliente_inserido)
        
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"
        cliente_db = obter_por_id(id_cliente_inserido)
        assert cliente_db is None, "O usuário excluído deveria ser None"
