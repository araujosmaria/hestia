from dataclasses import dataclass


@dataclass
class Agenda:
    id: int
    dataHora: datetime
    disponibilidade: boolean
    id_cuidador: int
    