CRIAR_TABELA_ADMINISTRADOR = """
CREATE TABLE IF NOT EXISTS administrador  (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    senha TEXT,
    telefone TEXT
);
"""

INSERIR_ADMINISTRADOR = """
INSERT INTO administrador (nome, email, senha, telefone ) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_ADMINISTRADOR = """
SELECT 
id, nome, email, senha, telefone
FROM administrador
ORDER BY nome
""" 

OBTER_ADMINISTRADOR_POR_ID = """
SELECT id, nome, email, senha, telefone
FROM administrador
WHERE id = ?
"""

ATUALIZAR_ADMINISTRADOR = """
UPDATE administrador
SET nome = ?, email = ?, senha = ?, telefone = ?
WHERE id = ?
"""

EXCLUIR_ADMINISTRADOR = """
DELETE FROM administrador
WHERE id = ?
"""
