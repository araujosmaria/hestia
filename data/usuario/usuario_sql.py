CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT,
    cpf TEXT UNIQUE,
    perfil TEXT NOT NULL DEFAULT 'cliente',
    foto TEXT,
    token_redefinicao TEXT,
    data_token TIMESTAMP,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo INTEGER DEFAULT 0
);
"""

INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, endereco, cpf, perfil)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS_USUARIOS = """ 
SELECT 
id_usuario, nome, email, senha, telefone, endereco, cpf, perfil, foto, data_cadastro
FROM usuario
ORDER BY nome;
"""
OBTER_USUARIO_POR_ID = """
SELECT 
id_usuario, nome, email, senha, telefone, endereco, cpf, perfil, foto, data_cadastro
FROM usuario
WHERE id_usuario = ?
"""

OBTER_USUARIO_POR_EMAIL = """
SELECT 
id_usuario, nome, email, senha, telefone, endereco, cpf, perfil, foto, data_cadastro
FROM usuario
WHERE email = ?
"""

EXCLUIR_USUARIO = """
DELETE FROM usuario
WHERE id_usuario = ?
"""

ATUALIZAR_USUARIO = """
UPDATE usuario
SET nome = ?, email = ?, senha = ?, telefone = ?, endereco = ?, cpf = ?
WHERE id_usuario = ?
""" 

VALIDAR_TOKEN = """
SELECT
id_usuario, nome, email, token_redefinicao, data_token
FROM usuario
WHERE token_redefinicao = ?
"""

ATIVAR_USUARIO = """
UPDATE usuario
SET ativo = 1
WHERE id_usuario = ?
"""