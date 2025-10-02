CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY,  -- recebe o id do usuario
    parentesco_paciente TEXT,
    confirmarSenha TEXT,
    termos BOOLEAN,
    verificacao BOOLEAN,
    comunicacoes BOOLEAN,
    FOREIGN KEY(id) REFERENCES usuario(id_usuario)
);
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (
    id, 
    parentesco_paciente,
    confirmarSenha,
    termos,
    verificacao,
    comunicacoes
) VALUES (?, ?, ?, ?, ?, ?);
"""

OBTER_TODOS_CLIENTE = """
SELECT 
    c.id AS id,
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
    u.ativo,
    c.parentesco_paciente,
    c.confirmarSenha,
    c.termos,
    c.verificacao,
    c.comunicacoes
FROM cliente c
JOIN usuario u ON c.id = u.id_usuario
ORDER BY u.nome
"""



OBTER_CLIENTE_POR_ID = """
SELECT 
    c.id AS id,
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
    c.parentesco_paciente,
    c.confirmarSenha,
    c.termos,
    c.verificacao,
    c.comunicacoes
FROM cliente c
JOIN usuario u ON c.id = u.id_usuario
WHERE c.id = ?
"""
                    
ATUALIZAR_CLIENTE = """
UPDATE cliente
SET parentesco_paciente = ?, termos = ?, comunicacoes = ?
WHERE id = ?
"""

EXCLUIR_CLIENTE = """
DELETE FROM cliente
WHERE id = ?
"""
