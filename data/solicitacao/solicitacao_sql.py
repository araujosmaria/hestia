CRIAR_TABELA_SOLICITACAO = """
CREATE TABLE IF NOT EXISTS solicitacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cuidador_id INTEGER NOT NULL,
    nome_contratante TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL
)
"""

INSERIR_SOLICITACAO = """
INSERT INTO solicitacoes (cuidador_id, nome_contratante, descricao, status)
VALUES (?, ?, ?, ?)
"""

ATUALIZAR_SOLICITACAO = """
UPDATE solicitacoes
SET cuidador_id = ?, nome_contratante = ?, descricao = ?, status = ?
WHERE id = ?
"""

EXCLUIR_SOLICITACAO = """
DELETE FROM solicitacoes
WHERE id = ?
"""

OBTER_TODOS = """
SELECT id, cuidador_id, nome_contratante, descricao, status
FROM solicitacoes
ORDER BY id DESC
"""

OBTER_SOLICITACAO_POR_ID = """
SELECT id, cuidador_id, nome_contratante, descricao, status
FROM solicitacoes
WHERE id = ?
"""

OBTER_SOLICITACOES_POR_CUIDADOR = """
SELECT id, cuidador_id, nome_contratante, descricao, status
FROM solicitacoes
WHERE cuidador_id = ?
"""
