from dataclasses import dataclass


@dataclass
class Chat:
    id: int
    conteudo: txt
    dataHora: datetime
    id_remetente: int
    id_destinatario: int
    
    