CRIAR_TABELA_AVALIACAO = """
CREATE TABLE IF NOT EXISTS avaliacao (
id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
nota FLOAT,
comentario TEXT NOT NULL,
dataAvaliacao DATE,
id_atendimento INTEGER NOT NULL,
FOREIGN KEY (id_atendimento) REFERENCES atendimento(id_atendimento)
);
"""

INSERIR_AVALIACAO = """
INSERT INTO avaliacao (nota, comentario, dataAvaliacao, id_atendimento) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_AVALIACAO = """
SELECT 
    id_avaliacao, nota, comentario, dataAvaliacao, id_atendimento
FROM avaliacao
ORDER BY dataAvaliacao DESC
""" 
ATUALIZAR_AVALIACAO = """
UPDATE avaliacao
SET nota = ?, comentario = ?, dataAvaliacao = ?
WHERE id_avaliacao = ?
"""

EXCLUIR_AVALIACAO = """
DELETE FROM avaliacao
WHERE id_avaliacao = ?
"""
