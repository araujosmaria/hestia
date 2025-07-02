import sys
import os
from data.chat.chat_repo import *
from data.chat.chat_model import Chat


class TestChatRepo:
    def test_criar_tabela(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir(self, test_db): 
        # Arrange
        criar_tabela()
        chat_teste = Chat(
            id=0,
            conteudo="Mensagem de teste",
            dataHora="2025-07-01 10:00:00",
            id_remetente=1,      # Corrigi para int, assumindo que seja ID
            id_destinatario=2    # Corrigi nome e tipo também
        )

        # Act
        id_chat_inserido = inserir(chat_teste)
        chat_db = obter_por_id(id_chat_inserido)  # Função para buscar Chat por ID, deve existir no repo

        # Assert
        assert chat_db is not None, "O chat inserido não deveria ser None"
        assert chat_db.id == id_chat_inserido, "O ID do chat não confere"
        assert chat_db.conteudo == chat_teste.conteudo, "O conteúdo inserido não confere"
        assert chat_db.dataHora == chat_teste.dataHora, "A dataHora inserida não confere"
        assert chat_db.id_remetente == chat_teste.id_remetente, "O id_remetente inserido não confere"
        assert chat_db.id_destinatario == chat_teste.id_destinatario, "O id_destinatario inserido não confere"



    def test_obter_todos(self, test_db):
        criar_tabela()
        inserir(Usuario(0, "Usuario A", "a@test.com", "123", "000", "Rua A"))
        inserir(Usuario(0, "Usuario B", "b@test.com", "456", "111", "Rua B"))

        lista_usuarios = obter_todos()                                                                                            
        assert len(lista_usuarios) >= 2, "Deveria retornar pelo menos 2 usuários"
        nomes = [u.nome for u in lista_usuarios]
        assert "Usuario A" in nomes, "Usuario A deveria estar na lista"
        assert "Usuario B" in nomes, "Usuario B deveria estar na lista"  

    def test_obter_por_id(self, test_db):
        criar_tabela()
        usuario_teste = Usuario(0, "Usuario Teste", "email@test.com", "senha", "tel", "end")
        id_usuario_inserido = inserir(usuario_teste)

        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is not None, "O usuário retornado não deveria ser None"
        assert usuario_db.id == id_usuario_inserido, "O ID do usuário buscado não confere"
        assert usuario_db.nome == usuario_teste.nome, "O nome do usuário buscado não confere"

    def test_atualizar_usuario(self, test_db):
        # Arrange
        criar_tabela()
        usuario_teste = Usuario(
            id=0,
            nome="Usuario Teste",
            email="email@test.com",
            senha="Senha123",
            telefone="123456789",
            endereco="Endereco Teste"
        )
        id_usuario_inserido = inserir(usuario_teste)
        usuario_inserido = obter_por_id(id_usuario_inserido)

        # Act
        usuario_inserido.nome = "Usuario Atualizada"
        usuario_inserido.email = "email_atualizado@test.com"
        usuario_inserido.senha = "NovaSenha"
        usuario_inserido.telefone = "987654321"
        usuario_inserido.endereco = "Endereco Atualizado"
        resultado = atualizar(usuario_inserido)

        # Assert
        assert resultado == True, "A atualização do usuário deveria retornar True"
        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db.nome == "Usuario Atualizada", "O nome do usuário atualizado não confere"
        assert usuario_db.email == "email_atualizado@test.com", "O email atualizado não confere"
        assert usuario_db.senha == "NovaSenha", "A senha atualizada não confere"
        assert usuario_db.telefone == "987654321", "O telefone atualizado não confere"
        assert usuario_db.endereco == "Endereco Atualizado", "O endereço atualizado não confere"


    def test_excluir_usuario(self, test_db):
        # Arrange
        criar_tabela()
        usuario_teste = Usuario(
            id=0,
            nome="Usuario Teste",
            email="email@test.com",
            senha="Senha123",
            telefone="123456789",
            endereco="Endereco Teste"
        )
        id_usuario_inserido = inserir(usuario_teste)
        
        # Act
        resultado = excluir(id_usuario_inserido)
        
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"
        usuario_db = obter_por_id(id_usuario_inserido)
        assert usuario_db is None, "O usuário excluído deveria ser None"
