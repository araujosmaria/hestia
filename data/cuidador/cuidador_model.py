from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Cuidador(Usuario):
   experiencia_anos: Optional[int] = None

