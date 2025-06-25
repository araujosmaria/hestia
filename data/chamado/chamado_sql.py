CRIAR_TABELA_CHAMADO = """
CREATE TABLE IF NOT EXISTS chamado (
    id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL,
    dataCriacao DATETIME NOT NULL,
    id_administrador INTEGER NOT NULL,
    FOREIGN KEY (id_administrador) REFERENCES administrador(id)
)
"""

INSERIR_CHAMADO = """
INSERT INTO chamado (titulo, descricao, status, dataCriacao, id_administrador) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_CHAMADOS = """
SELECT 
    id_chamado, titulo, descricao, status, dataCriacao, id_administrador
FROM chamado
ORDER BY dataCriacao DESC
"""
