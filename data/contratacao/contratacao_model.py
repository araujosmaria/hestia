from dataclasses import dataclass

@dataclass
class Contratacao:
    id: int
    cuidador_id: int
    nome_contratante: str
    data_inicio: str
    data_fim: str
    observacoes: str
    status: str
