CRIAR_TABELA_ESPECIALIDADE = """
CREATE TABLE IF NOT EXISTS especialidade (
id_especialidade INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR NOT NULL
);
"""

INSERIR_ESPECIALIDADE = """
INSERT INTO especialidade (nome) 
VALUES (?);
"""

OBTER_TODOS_ESPECIALIDADE = """
SELECT 
id_especialidade, nome
FROM especialidade
ORDER BY nome ASC;
""" 