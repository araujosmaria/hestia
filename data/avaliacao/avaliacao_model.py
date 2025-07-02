from dataclasses import dataclass
import datetime


@dataclass
class Avaliacao:
    id: int
    nota: float
    comentario: str
    dataAvaliacao: datetime.datetime
    id_atendimento: int
   
    
    