from dataclasses import dataclass

@dataclass
class Solicitacao:
    id: int
    cuidador_id: int
    nome_contratante: str
    descricao: str
    status: str
