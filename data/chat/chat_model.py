from dataclasses import dataclass
from typing import Optional


@dataclass
class Chat:
    id: int
    conteudo: str
    dataHora: str
    id_remetente: int
    id_destinatario: int
    
     
     