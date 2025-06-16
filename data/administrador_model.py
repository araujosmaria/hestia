from dataclasses import dataclass


@dataclass
class Administrador:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str
    