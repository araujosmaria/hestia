CRIAR_TABELA_ATENDIMENTO = """
CREATE TABLE IF NOT EXISTS atendimento (
    id_atendimento INTEGER PRIMARY KEY AUTOINCREMENT,
    dataInicio DATETIME NOT NULL,
    dataFim DATETIME NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_cuidador INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador)
)
"""

INSERIR_ATENDIMENTO = """
INSERT INTO atendimento (dataInicio, dataFim, id_cliente, id_cuidador) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_ATENDIMENTO = """
SELECT 
    id_atendimento, dataInicio, dataFim, id_cliente, id_cuidador
FROM atendimento
ORDER BY dataInicio
"""
ATUALIZAR_ATENDIMENTO = """
UPDATE atendimento
SET dataInicio = ?, dataFim = ?
WHERE id_atendimento = ?
"""

EXCLUIR_ATENDIMENTO = """
DELETE FROM atendimento
WHERE id_atendimento = ?
"""
