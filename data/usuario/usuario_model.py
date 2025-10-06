
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
    token_redefinicao: Optional[str] = None
    data_token: Optional[str] = None
    data_cadastro: Optional[str] = None
    cep: str = ''
    logradouro: str = ''
    numero: str = ''
    complemento: Optional[str] = None
    bairro: str = ''
    cidade: str = ''
    estado: str = ''
    ativo: bool = False
    foto: Optional[str] = None
