CRIAR_TABELA_ESPECIALIDADE = """
CREATE TABLE IF NOT EXISTS especialidade (
id_especialidade INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR NOT NULL
)
"""

INSERIR_ESPECIALIDADE = """
INSERT INTO especialidade (nome) 
VALUES (?)
"""

OBTER_TODOS_ESPECIALIDADE = """
SELECT 
id_especialidade, nome
FROM especialidade
ORDER BY nome ASC
""" 

OBTER_ESPECIALIDADE_POR_ID = """
SELECT 
id_especialidade, nome
FROM especialidade
WHERE id_especialidade = ?
"""

ATUALIZAR_ESPECIALIDADE = """
UPDATE especialidade
SET nome = ?
WHERE id_especialidade = ?
"""

EXCLUIR_ESPECIALIDADE = """
DELETE FROM especialidade
WHERE id_especialidade = ?
"""
