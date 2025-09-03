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
    perfil: str = 'cliente'
    foto: Optional[str] = None
    token_redefinicao: Optional[str] = None
    data_token: Optional[str] = None
    data_cadastro: Optional[str] = None