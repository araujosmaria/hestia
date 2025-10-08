
from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    id: int =''
    nome: str = ''   
    dataNascimento: str = ''
    email: str = ''
    telefone: str = ''
    cpf: str = ''
    senha: str = ''
    perfil: str = ''
    cep: str = ''
    logradouro: str = ''
    numero: str = ''
    bairro: str = ''
    cidade: str = ''
    estado: str = ''
    ativo: bool = False
    token_redefinicao: Optional[str] = None
    data_token: Optional[str] = None
    data_cadastro: Optional[str] = None
    foto: Optional[str] = None
    complemento: Optional[str] = None
