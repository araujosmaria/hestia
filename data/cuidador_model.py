from dataclasses import dataclass


@dataclass
class Cuidador:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str
    experiencia: int
    