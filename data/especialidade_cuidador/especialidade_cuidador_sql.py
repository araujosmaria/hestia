CRIAR_TABELA_ESPECIALIDADE_CUIDADOR = """
CREATE TABLE IF NOT EXISTS especialidade_cuidador (
    id_cuidador INTEGER NOT NULL,
    id_especialidade INTEGER NOT NULL,
    anos_experiencia INTEGER NOT NULL,
    PRIMARY KEY (id_cuidador, id_especialidade),
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador) ON DELETE CASCADE,
    FOREIGN KEY (id_especialidade) REFERENCES especialidade(id_especialidade) ON DELETE CASCADE
)
"""

INSERIR_ESPECIALIDADE_CUIDADOR = """
INSERT INTO especialidade_cuidador (id_cuidador, id_especialidade, anos_experiencia)
VALUES (?, ?, ?)
"""   

ATUALIZAR_ESPECIALIDADE_CUIDADOR = """
UPDATE especialidade_cuidador
SET anos_experiencia = ?
WHERE id_cuidador = ? AND id_especialidade = ?
"""

OBTER_TODOS = """
SELECT
    id_cuidador,
    id_especialidade,
    anos_experiencia
FROM
    especialidade_cuidador
ORDER BY id_cuidador, id_especialidade;
"""

OBTER_POR_ID = """
SELECT
    id_cuidador,
    id_especialidade,
    anos_experiencia
FROM
    especialidade_cuidador
WHERE
    id_cuidador = ? AND id_especialidade = ?;
"""

OBTER_ESPECIALIDADES_POR_CUIDADOR = """
SELECT
    id_cuidador,
    id_especialidade,
    anos_experiencia
FROM
    especialidade_cuidador
WHERE
    id_cuidador = ?;
"""

EXCLUIR_ESPECIALIDADE_CUIDADOR = """
DELETE FROM especialidade_cuidador
WHERE id_cuidador = ? AND id_especialidade = ?
"""