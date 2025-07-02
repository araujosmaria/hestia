from dataclasses import dataclass
import datetime


@dataclass
class Agenda:
    id_agenda: int
    dataHora: datetime
    disponibilidade: bool
    id_cuidador: int
    