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
VALUES (?, ?, ?, ?, ?);
"""

OBTER_TODOS_USUARIO = """ 
SELECT 
id_usuario, nome, email, telefone, endereco
FROM usuario
ORDER BY nome;
"""