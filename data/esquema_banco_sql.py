CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);
"""

INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, endereco)
VALUES (?, ?, ?, ?, ?);
"""

OBTER_TODOS_USUARIO = """ 
SELECT 
id_usuario, nome, email, telefone, endereco
FROM usuario
ORDER BY nome;


CREATE TABLE IF NOT EXISTS administrador (
    id_administrador INTEGER PRIMARY KEY,
    FOREIGN KEY (id_administrador) REFERENCES usuario(id_usuario)
);

INSERIR_ADMINISTRADOR = """
INSERT INTO administrador (id_administrador)
VALUES (?);

OBTER_TODOS_ADMINISTRADOR = """
SELECT 
a.id_administrador, u.nome, u.email
FROM administrador a
JOIN usuario u ON a.id_administrador = u.id_usuario
ORDER BY u.nome;


CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY,
    FOREIGN KEY (id_cliente) REFERENCES usuario(id_usuario)
);

INSERIR_CLIENTE = """
INSERT INTO cliente (id_cliente)
VALUES (?);

OBTER_TODOS_CLIENTE = """
SELECT 
c.id_cliente, u.nome, u.email
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
ORDER BY u.nome;

CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    experiencia TEXT NOT NULL,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
);

INSERIR_CUIDADOR = """
INSERT INTO cuidador (id_cuidador, experiencia)
VALUES (?, ?);

OBTER_TODOS_CUIDADOR = """
SELECT 
cu.id_cuidador, u.nome, cu.experiencia
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome;



