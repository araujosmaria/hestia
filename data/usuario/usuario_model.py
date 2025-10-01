from dataclasses import dataclass
from typing import Optional

# @dataclass
# class Usuario:
#     id: int
#     nome: str    
#     dataNascimento: str
#     email: str
#     telefone: str
#     cpf: str
#     senha: str
#     perfil: str
#     token_redefinicao: str
#     data_token: str
#     data_cadastro: str
#     cep: str
#     logradouro: str
#     numero: str
#     complemento: str
#     bairro: str
#     cidade: str
#     estado: str
#     ativo: bool 
#     foto: Optional[str] = None
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
