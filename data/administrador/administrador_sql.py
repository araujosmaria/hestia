CRIAR_TABELA_ADMINISTRADOR = """
CREATE TABLE IF NOT EXISTS administrador (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL,
telefone TEXT NOT NULL,
endereco TEXT NOT NULL,
)
"""

INSERIR_ADMINISTRADOR = """
INSERT INTO administrador (nome, email, senha, telefone, endereco ) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_ADMINISTRADOR = """
SELECT 
id, nome, email, senha, telefone, endereco
FROM administrador
ORDER BY nome
""" 

OBTER_ADMINISTRADOR_POR_ID = """
SELECT id, nome, email, senha, telefone, endereco
FROM administrador
WHERE id = ?
"""

ATUALIZAR_ADMINISTRADOR = """
UPDATE administrador
SET nome = ?, email = ?, senha = ?, telefone = ?, endereco = ?
WHERE id = ?
"""

EXCLUIR_ADMINISTRADOR = """
DELETE FROM administrador
WHERE id = ?
"""
