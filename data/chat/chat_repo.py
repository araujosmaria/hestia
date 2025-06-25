from typing import Optional

from data.chat.chat_model import Chat
from data.chat.chat_sql import *
from data.util import open_connection


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CHAT)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de chat: {e}")
        return False  

def inserir(chat: Chat) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CHAT, (
            chat.conteudo,  
            chat.dataHora))
        return cursor.lastrowid

def obter_todos() -> list[Chat]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CHATS)
        rows = cursor.fetchall()
        chamados = [
            Chat(
                id=row["id"], 
                conteudo=row["conteudo"], 
                dataHor=row["dataHora"]) 
                for row in rows]
        return chamados
    
