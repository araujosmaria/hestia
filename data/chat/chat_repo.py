from asyncio import open_connection
from typing import Optional

from data.chat_model import Chat
from data.chat_sql import CRIAR_TABELA_CHAT, INSERIR_CHAT, OBTER_TODOS_CHAT


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CHAT)
        return cursor.rowcount > 0

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
        cursor.execute(OBTER_TODOS_CHAT)
        rows = cursor.fetchall()
        chamados = [
            Chat(
                id=row["id"], 
                conteudo=row["conteudo"], 
                dataHor=row["dataHora"]) 
                for row in rows]
        return chamados