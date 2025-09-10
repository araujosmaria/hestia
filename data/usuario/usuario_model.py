from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str
    cpf: str
    perfil: str
    foto: Optional[str]
    token_redefinicao: Optional[str]
    data_token: Optional[str]
    data_cadastro: Optional[str]