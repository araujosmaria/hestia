from dataclasses import dataclass


@dataclass
class Chamado:
    id: int
    titulo: str
    descricao: str
    status: str
    data_criacao: datetime
    id_administrador: int
    