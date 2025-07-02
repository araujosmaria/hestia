from dataclasses import dataclass
import datetime


@dataclass
class Atendimento:
    id: int
    dataInicio: datetime
    dataFim: datetime
    id_cliente: int
    id_cuidador: int
    
    