from dataclasses import dataclass
from typing import Optional

from data.cuidador.cuidador_model import Cuidador
from data.especialidade.especialidade_model import Especialidade


@dataclass
class EspecialidadeCuidador:
    id_cuidador: int
    id_especialidade: int
    anos_experiencia: int
    cuidador: Optional[Cuidador] = None
    especialidade: Optional[Especialidade] = None