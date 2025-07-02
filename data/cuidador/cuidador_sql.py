CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    experiencia_anos INTEGER NOT NULLL,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
)
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (id_cuidador, experiencia_anos)
VALUES (?, ?)
"""

OBTER_TODOS_CUIDADOR = """
SELECT 
cu.id_cuidador, u.nome, cu.experiencia_anos
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome
"""

ATUALIZAR_CUIDADOR = """
UPDATE cuidador
SET experiencia_anos = ?
WHERE id_cuidador = ?
"""

EXCLUIR_CUIDADOR = """
DELETE FROM cuidador
WHERE id_cuidador = ?
"""