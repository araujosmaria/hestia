CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
)
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (id_cuidador, experiencia)
VALUES (?, ?)
"""

OBTER_TODOS_CUIDADOR = """
SELECT 
cu.id_cuidador, u.nome, cu.experiencia
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome
"""
