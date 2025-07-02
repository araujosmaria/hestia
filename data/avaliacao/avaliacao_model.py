from dataclasses import dataclass
import datetime


@dataclass
class Avaliação:
    id: int
    nota: float
    comentario: str
    dataAvaliacao: datetime
    id_atendimento: int
   
    
    