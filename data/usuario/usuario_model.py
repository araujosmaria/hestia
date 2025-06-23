from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str