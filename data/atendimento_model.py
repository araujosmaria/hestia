from dataclasses import dataclass


@dataclass
class Atendimento:
    id: int
    dataInicio: datetime
    dataFim: datetime
    id_cliente: int
    id_cuidador: int
    
    