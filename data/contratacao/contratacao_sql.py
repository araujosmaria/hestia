CRIAR_TABELA_CONTRATACAO = """
CREATE TABLE IF NOT EXISTS contratacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cuidador_id INTEGER NOT NULL,
    nome_contratante TEXT NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    observacoes TEXT NOT NULL,
    status TEXT NOT NULL
)
"""

INSERIR_CONTRATACAO = """
INSERT INTO contratacoes (cuidador_id, nome_contratante, data_inicio, data_fim, observacoes, status)
VALUES (?, ?, ?, ?, ?, ?)
"""

ATUALIZAR_CONTRATACAO = """
UPDATE contratacoes
SET cuidador_id = ?, nome_contratante = ?, data_inicio = ?, data_fim = ?, observacoes = ?, status = ?
WHERE id = ?
"""

EXCLUIR_CONTRATACAO = """
DELETE FROM contratacoes
WHERE id = ?
"""

OBTER_CONTRATACAO_POR_ID = """
SELECT id, cuidador_id, nome_contratante, data_inicio, data_fim, observacoes, status
FROM contratacoes
WHERE id = ?
"""

OBTER_CONTRATACOES_POR_CUIDADOR = """
SELECT id, cuidador_id, nome_contratante, data_inicio, data_fim, observacoes, status
FROM contratacoes
WHERE cuidador_id = ?
"""
