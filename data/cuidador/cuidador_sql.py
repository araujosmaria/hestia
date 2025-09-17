
CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    experiencia TEXT NOT NULL,
    valorHora REAL NOT NULL,
    escolaridade TEXT NOT NULL,
    apresentacao TEXT NOT NULL,
    cursos TEXT,
    confirmarSenha TEXT NOT NULL,
    termos BOOLEAN NOT NULL,
    verificacao BOOLEAN NOT NULL,
    comunicacoes BOOLEAN NOT NULL,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
);
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (
    id_cuidador,
    experiencia,
    valorHora,
    escolaridade,
    apresentacao,
    cursos,
    confirmarSenha,
    termos,
    verificacao,
    comunicacoes)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

OBTER_TODOS_CUIDADOR = """
SELECT  
    cu.id_cuidador, 
    u.nome, 
    u.email, 
    u.senha, 
    u.telefone, 
    u.cpf,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    cu.inicio_profissional
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome
"""

OBTER_CUIDADOR_POR_ID = """
SELECT
    cu.id_cuidador,
    u.nome,
    u.email,
    u.senha,
    u.telefone,
    u.cpf,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    cu.inicio_profissional
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
WHERE cu.id_cuidador = ?;
"""

ATUALIZAR_CUIDADOR = """
UPDATE cuidador
SET inicio_profissional = ?
WHERE id_cuidador = ?
"""

EXCLUIR_CUIDADOR = """
DELETE FROM cuidador
WHERE id_cuidador = ?
"""
