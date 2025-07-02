CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);
"""

INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, endereco)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_USUARIO = """ 
SELECT 
id_usuario, nome, email, senha, telefone, endereco
FROM usuario
ORDER BY nome;
"""
OBTER_USUARIO_POR_ID = """
SELECT 
id_usuario, nome, email, senha, telefone, endereco
FROM usuario
WHERE id_usuario = ?
"""

EXCLUIR_USUARIO = """
DELETE FROM usuario
WHERE id_usuario = ?
"""

ATUALIZAR_USUARIO = """
UPDATE usuario
SET nome = ?, email = ?, senha = ?, telefone = ?, endereco = ?
WHERE id_usuario = ?
""" 