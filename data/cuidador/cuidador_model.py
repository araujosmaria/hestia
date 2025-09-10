from dataclasses import dataclass
from datetime import date
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Cuidador(Usuario):
   inicio_profissional: Optional[date] = None

