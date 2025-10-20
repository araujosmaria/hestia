CRIAR_TABELA_AGENDA = """
CREATE TABLE IF NOT EXISTS agenda (
    id_agenda INTEGER PRIMARY KEY AUTOINCREMENT,
    dataHora DATETIME NOT NULL,
    disponibilidade BOOLEAN NOT NULL,
    id_cuidador INTEGER NOT NULL,
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id)
)
"""

INSERIR_AGENDA = """
INSERT INTO agenda (dataHora, disponibilidade, id_cuidador) 
VALUES (?, ?, ?)
"""

OBTER_TODOS_AGENDA = """
SELECT 
    id_agenda, dataHora, disponibilidade, id_cuidador
FROM agenda
ORDER BY dataHora
"""

OBTER_POR_ID = """
SELECT 
    id_agenda, dataHora, disponibilidade, id_cuidador
FROM agenda
WHERE id_agenda = ?
ORDER BY dataHora
"""

ATUALIZAR_AGENDA = """
UPDATE agenda
SET dataHora = ?, disponibilidade = ?, id_cuidador = ?
WHERE id_agenda = ?
"""

EXCLUIR_AGENDA = """
DELETE FROM agenda
WHERE id_agenda = ?
"""
