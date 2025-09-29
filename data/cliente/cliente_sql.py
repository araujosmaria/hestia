# CRIAR_TABELA_CLIENTE = """
# CREATE TABLE IF NOT EXISTS cliente (
#     id_cliente INTEGER PRIMARY KEY,
#     parentesco_paciente TEXT NOT NULL,
#     confirmarSenha TEXT NOT NULL,
#     termos BOOLEAN NOT NULL,
#     verificacao BOOLEAN NOT NULL,
#     comunicacoes BOOLEAN NOT NULL,
#     FOREIGN KEY (id_cliente) REFERENCES usuario(id_usuario)
# );
# """

# INSERIR_CLIENTE = """
# INSERT INTO cliente (
#     id_cliente, 
#     parentesco_paciente,
#     confirmarSenha,
#     termos,
#     verificacao,
#     comunicacoes)
# VALUES (?,?,?,?,?,?);
# """

# OBTER_TODOS_CLIENTE = """
# SELECT 
#     c.id_cliente AS id,
#     u.nome,
#     u.dataNascimento,
#     u.email,
#     u.telefone,
#     u.cpf,
#     u.senha,
#     u.perfil,
#     u.foto,
#     u.token_redefinicao,
#     u.data_token,
#     u.data_cadastro,
#     u.cep,
#     u.logradouro,
#     u.numero,
#     u.complemento,
#     u.bairro,
#     u.cidade,
#     u.estado,
#     c.parentesco_paciente
# FROM cliente c
# JOIN usuario u ON c.id_cliente = u.id_usuario
# ORDER BY u.nome
# """

# OBTER_CLIENTE_POR_ID = """
# SELECT 
#     c.id_cliente AS id,
#     u.nome,
#     u.dataNascimento,
#     u.email,
#     u.telefone,
#     u.cpf,
#     u.senha,
#     u.perfil,
#     u.foto,
#     u.token_redefinicao,
#     u.data_token,
#     u.data_cadastro,
#     u.cep,
#     u.logradouro,
#     u.numero,
#     u.complemento,
#     u.bairro,
#     u.cidade,
#     u.estado,
#     c.parentesco_paciente

# FROM cliente c
# JOIN usuario u ON c.id_cliente = u.id_usuario
# WHERE c.id_cliente = ?
# """ 

# ATUALIZAR_CLIENTE = """
# UPDATE cliente
# SET parentesco_paciente = ?
# WHERE id_cliente = ?
# """

# EXCLUIR_CLIENTE = """
# DELETE FROM cliente
# WHERE id_cliente = ?
# """


CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY,
    parentesco_paciente TEXT NOT NULL,
    confirmarSenha TEXT NOT NULL,
    termos BOOLEAN NOT NULL,
    verificacao BOOLEAN NOT NULL,
    comunicacoes BOOLEAN NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES usuario(id_usuario)
);
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (
    id_cliente, 
    parentesco_paciente,
    confirmarSenha,
    termos,
    verificacao,
    comunicacoes
) VALUES (?,?,?,?,?,?);
"""

OBTER_TODOS_CLIENTE = """
SELECT 
    c.id_cliente AS id_cliente,
    u.nome,
    u.dataNascimento,
    u.email,
    u.telefone,
    u.cpf,
    u.senha,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    u.cep,
    u.logradouro,
    u.numero,
    u.complemento,
    u.bairro,
    u.cidade,
    u.estado,
    c.parentesco_paciente
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
ORDER BY u.nome
"""

OBTER_CLIENTE_POR_ID = """
SELECT 
    c.id_cliente AS id_cliente,
    u.nome,
    u.dataNascimento,
    u.email,
    u.telefone,
    u.cpf,
    u.senha,
    u.perfil,
    u.foto,
    u.token_redefinicao,
    u.data_token,
    u.data_cadastro,
    u.cep,
    u.logradouro,
    u.numero,
    u.complemento,
    u.bairro,
    u.cidade,
    u.estado,
    c.parentesco_paciente
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
WHERE c.id_cliente = ?
"""

ATUALIZAR_CLIENTE = """
UPDATE cliente
SET parentesco_paciente = ?
WHERE id_cliente = ?
"""

EXCLUIR_CLIENTE = """
DELETE FROM cliente
WHERE id_cliente = ?
"""
