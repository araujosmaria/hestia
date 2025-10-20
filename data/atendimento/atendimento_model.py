from dataclasses import dataclass
from datetime import datetime


@dataclass
class Atendimento:
    id: int
    dataInicio: datetime
    dataFim: datetime
    id_cliente: int
    id_cuidador: int
    
    