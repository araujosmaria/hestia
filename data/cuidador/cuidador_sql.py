
CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    experiencia_anos INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
);
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (nome, email, senha, telefone, endereco, cpf, perfil, foto, token_redefinicao, data_token, data_cadastro, experiencia_anos)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS_CUIDADOR = """
SELECT  
    cu.id_cuidador, 
    u.nome, 
    u.email, 
    u.senha, 
    u.telefone, 
    u.endereco,
    u.cpf,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    cu.experiencia_anos
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
    u.endereco,
    u.cpf,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    cu.experiencia_anos
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
WHERE cu.id_cuidador = ?;
"""

ATUALIZAR_CUIDADOR = """
UPDATE cuidador
SET nome = ?, email = ?, senha = ?, telefone = ?, endereco = ?, cpf = ?, perfil = ?, foto = ?, token_redefinicao = ?, data_token = ?, data_cadastro = ?, experiencia_anos = ?
WHERE id_cuidador = ?
"""

EXCLUIR_CUIDADOR = """
DELETE FROM cuidador
WHERE id_cuidador = ?
"""
