CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dataNascimento TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    cpf TEXT UNIQUE,
    senha TEXT NOT NULL,
    perfil TEXT NOT NULL DEFAULT 'contratante',
    foto TEXT,
    token_redefinicao TEXT,
    data_token TIMESTAMP,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cep TEXT NOT NULL,
    logradouro TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    ativo INTEGER NOT NULL DEFAULT 0
);
"""

INSERIR_USUARIO = """
INSERT INTO usuario (
    nome,
    dataNascimento,
    email,
    telefone,
    cpf,
    senha,
    perfil,
    foto,
    token_redefinicao,
    data_token,
    data_cadastro,
    cep,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    estado,
    ativo
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS_USUARIOS = """ 
SELECT 
    id_usuario, 
    nome,
    dataNascimento,
    email,
    telefone,
    cpf,
    senha,
    perfil,
    foto
FROM usuario
ORDER BY nome;
"""
OBTER_USUARIO_POR_ID = """
SELECT 
    id_usuario, 
    nome,
    dataNascimento,
    email,
    telefone,
    cpf,
    senha,
    perfil,
    foto
FROM usuario
WHERE id_usuario = ?
"""

OBTER_USUARIO_POR_EMAIL = """
SELECT 
    id_usuario, 
    nome,
    dataNascimento,
    email,
    telefone,
    cpf,
    senha,
    perfil,
    foto,
    token_redefinicao,
    data_token,
    data_cadastro,
    cep,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    estado,
    ativo
FROM usuario
WHERE email = ?
"""


EXCLUIR_USUARIO = """
DELETE FROM usuario
WHERE id_usuario = ?
"""

ATUALIZAR_USUARIO = """
UPDATE usuario
SET 
    nome = ?, 
    dataNascimento = ?, 
    email = ?, 
    telefone = ?, 
    cpf = ?, 
    perfil = ?, 
    foto = ?, 
    token_redefinicao = ?, 
    data_token = ?, 
    data_cadastro = ?, 
    cep = ?, 
    logradouro = ?, 
    numero = ?, 
    complemento = ?, 
    bairro = ?, 
    cidade = ?, 
    estado = ?, 
    ativo = ?
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