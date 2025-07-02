from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Cliente(Usuario):
    id: int
    