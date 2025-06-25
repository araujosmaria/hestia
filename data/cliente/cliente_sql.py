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
c.id_cliente, u.nome, u.email
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
ORDER BY u.nome
"""