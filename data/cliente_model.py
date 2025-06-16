from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str
    
    