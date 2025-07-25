CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY,
    FOREIGN KEY (id_cliente) REFERENCES usuario(id_usuario)
)
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (id_cliente)
VALUES (?)
"""

OBTER_TODOS_CLIENTE = """
SELECT 
    c.id_cliente AS id,
    u.nome,
    u.email,
    u.senha,
    u.telefone,
    u.endereco
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
ORDER BY u.nome
"""

OBTER_CLIENTE_POR_ID = """
SELECT 
    c.id_cliente AS id,
    u.nome,
    u.email,
    u.senha,
    u.telefone,
    u.endereco
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
WHERE id_cliente = ?
"""

EXCLUIR_CLIENTE = """
DELETE FROM usuario
WHERE id_usuario = ?
"""
