INSERIR_CUIDADOR = """
INSERT INTO cuidador (id_cuidador, experiencia)
VALUES (?, ?);
"""

OBTER_TODOS_CUIDADOR = """
SELECT 
cu.id_cuidador, u.nome, cu.experiencia
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome;
"""
