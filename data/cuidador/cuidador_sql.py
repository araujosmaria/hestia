CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id INTEGER PRIMARY KEY,  -- recebe o id do usuário
    experiencia TEXT NOT NULL,
    valorHora REAL NOT NULL,
    escolaridade TEXT NOT NULL,
    apresentacao TEXT NOT NULL,
    cursos TEXT,
    inicio_profissional TEXT,
    confirmarSenha TEXT NOT NULL,
    termos BOOLEAN NOT NULL,
    verificacao BOOLEAN NOT NULL,
    comunicacoes BOOLEAN NOT NULL,
    FOREIGN KEY(id) REFERENCES usuario(id_usuario)
);
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (
    id,
    experiencia,
    valorHora,
    escolaridade,
    apresentacao,
    cursos,
    inicio_profissional,
    confirmarSenha,
    termos,
    verificacao,
    comunicacoes
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

OBTER_CUIDADOR_POR_ID = """
SELECT
    cu.id AS id,
    u.nome,
    u.dataNascimento,
    u.email,
    u.telefone,
    u.cpf,
    u.senha,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    u.cep,
    u.logradouro,
    u.numero,
    u.complemento,
    u.bairro,
    u.cidade,
    u.estado,
    u.ativo,
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
JOIN usuario u ON cu.id = u.id_usuario
WHERE cu.id = ?;
"""

OBTER_TODOS_CUIDADORES = """
SELECT  
    cu.id AS id,
    u.nome,
    u.dataNascimento,
    u.email,
    u.telefone,
    u.cpf,
    u.senha,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    u.cep,
    u.logradouro,
    u.numero,
    u.complemento,
    u.bairro,
    u.cidade,
    u.estado,
    u.ativo,
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
JOIN usuario u ON cu.id = u.id_usuario
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
WHERE id = ?;
"""

EXCLUIR_CUIDADOR = """
DELETE FROM cuidador
WHERE id = ?;
"""

