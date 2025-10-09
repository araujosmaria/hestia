from dataclasses import dataclass
from typing import Optional

@dataclass
class Administrador:
    nome: str = ''  
    email: str = ''
    senha: str = ''
    telefone: Optional[str] = None
    id: Optional[int] = None