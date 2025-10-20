CRIAR_TABELA_CHAT = """
CREATE TABLE IF NOT EXISTS chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    dataHora TEXT NOT NULL,
    id_remetente INTEGER NOT NULL,
    id_destinatario INTEGER NOT NULL
)
"""

INSERIR_CHAT = """
INSERT INTO chat (conteudo, dataHora, id_remetente, id_destinatario) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_CHATS = """
SELECT
    id, conteudo, dataHora, id_remetente, id_destinatario
FROM chat
ORDER BY dataHora
"""

OBTER_POR_ID = """
SELECT
    id, conteudo, dataHora, id_remetente, id_destinatario
FROM chat
WHERE id = ?
"""

ATUALIZAR_CHAT = """
UPDATE chat
SET conteudo = ?, dataHora = ?
WHERE id = ?
"""

EXCLUIR_CHAT = """
DELETE FROM chat
WHERE id = ?
"""
