from dataclasses import dataclass
from typing import Optional

@dataclass
class Administrador:
    id: Optional[int] = None
    nome: str    
    email: str
    senha: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None