from dataclasses import dataclass


@dataclass
class Avaliação:
    id: int
    nota: float
    comentario: str
    dataAvaliacao: date
    id_atendimento: int
   
    
    