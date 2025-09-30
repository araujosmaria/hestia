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
    inicio_profissional TEXT,
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
    inicio_profissional,
    confirmarSenha,
    termos,
    verificacao,
    comunicacoes)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

OBTER_CUIDADOR_POR_ID = """
SELECT
    cu.id_cuidador,
    u.nome,
    u.email,
    u.telefone,
    u.foto,
    cu.experiencia,
    cu.valorHora,
    cu.escolaridade,
    cu.apresentacao,
    cu.cursos,
    cu.inicio_profissional,
    cu.confirmarSenha,
    cu.termos,
    cu.verificacao,
    cu.comunicacoes
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
WHERE cu.id_cuidador = ?;
"""

OBTER_TODOS_CUIDADORES = """
SELECT  
    cu.id_cuidador, 
    u.nome, 
    cu.valorHora,
    cu.escolaridade,
    u.foto
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome;
"""

ATUALIZAR_CUIDADOR = """
UPDATE cuidador
SET
    experiencia = ?,
    valorHora = ?,
    escolaridade = ?,
    apresentacao = ?,
    cursos = ?,
    confirmarSenha = ?,
    termos = ?,
    verificacao = ?,
    comunicacoes = ?,
    inicio_profissional = ?
WHERE id_cuidador = ?
"""


EXCLUIR_CUIDADOR = """
DELETE FROM cuidador
WHERE id_cuidador = ?
"""
