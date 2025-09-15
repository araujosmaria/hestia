from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: int
    nome: str    
    dataNascimento: str
    email: str
    telefone: str
    cpf: str
    senha: str
    perfil: str
    foto: Optional[str]
    token_redefinicao: Optional[str]
    data_token: Optional[str]
    data_cadastro: Optional[str]
    cep: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    ativo: bool