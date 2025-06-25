CREATE TABLE IF NOT EXISTS especialidade_cuidador (
    id_cuidador INTEGER,
    id_especialidade INTEGER,
    PRIMARY KEY (id_cuidador, id_especialidade),
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador) ON DELETE CASCADE,
    FOREIGN KEY (id_especialidade) REFERENCES especialidade(id_especialidade) ON DELETE CASCADE
);

INSERT INTO especialidade_cuidador (id_cuidador, id_especialidade)
VALUES (?, ?);
        

SELECT 
    ec.id_cuidador,
    c.experiencia,
    ec.id_especialidade,
    e.nome AS nome_especialidade
FROM 
    especialidade_cuidador ec
JOIN 
    cuidador c ON ec.id_cuidador = c.id_cuidador
JOIN 
    especialidade e ON ec.id_especialidade = e.id_especialidade
ORDER BY 
    c.id_cuidador;