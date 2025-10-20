import pytest
from data.chat.chat_model import Chat
from data.chat.chat_repo import (
    criar_tabela as criar_tabela_chat,
    inserir,
    obter_todos,
    atualizar,
    excluir
)
from datetime import datetime


class TestChatRepo:
    def test_criar_tabela_chat(self, test_db):
        # Act
        resultado = criar_tabela_chat()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir_chat(self, test_db):
        # Arrange
        criar_tabela_chat()
        chat = Chat(id=0, conteudo="Olá!", dataHora="2025-07-01 10:00:00", id_remetente=1, id_destinatario=2)
        # Act
        id_chat = inserir(chat)
        # Assert
        chats = obter_todos()
        assert any(c.id == id_chat for c in chats), "O chat inserido deveria estar na lista"

    def test_obter_todos_chat(self, test_db):
        # Arrange
        criar_tabela_chat()
        inserir(Chat(0, "Oi A", "2025-07-01 11:00:00", 1, 2))
        inserir(Chat(0, "Oi B", "2025-07-01 12:00:00", 2, 1))
        # Act
        chats = obter_todos()
        # Assert
        assert len(chats) >= 2, "Deveria retornar pelo menos 2 chats"
        conteudos = [c.conteudo for c in chats]
        assert "Oi A" in conteudos
        assert "Oi B" in conteudos

    def test_atualizar_chat(self, test_db):
        # Arrange
        criar_tabela_chat()
        chat = Chat(0, "Mensagem Original", "2025-07-01 13:00:00", 1, 2)
        id_chat = inserir(chat)
        assert id_chat is not None
        chat_atualizado = Chat(id_chat, "Mensagem Atualizada", "2025-07-01 14:00:00", 1, 2)
        # Act
        resultado = atualizar(chat_atualizado)
        # Assert
        assert resultado == True, "A atualização do chat deveria retornar True"
        chats = obter_todos()
        atualizado = next((c for c in chats if c.id == id_chat), None)
        assert atualizado is not None
        assert atualizado.conteudo == "Mensagem Atualizada"

    def test_excluir_chat(self, test_db):
        # Arrange
        criar_tabela_chat()
        chat = Chat(0, "Mensagem a excluir", "2025-07-01 15:00:00", 1, 2)
        id_chat = inserir(chat)
        assert id_chat is not None
        # Act
        resultado = excluir(id_chat)
        chats = obter_todos()
        # Assert
        assert resultado == True, "A exclusão do chat deveria retornar True"
        assert not any(c.id == id_chat for c in chats), "O chat excluído não deveria estar na lista"
