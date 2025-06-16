CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL,
telefone TEXT NOT NULL,
endereco TEXT NOT NULL,
)
"""

INSERIR = """
INSERT INTO administrador (nome, email, senha, telefone, endereco ) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
id, nome, email, senha, telefone, endereco
FROM administrador
ORDER BY nome
""" 