from dataclasses import dataclass
from datetime import date
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Cuidador(Usuario):   
   experiencia: str
   confirmarSenha: str
   valorHora: float
   escolaridade: str
   apresentacao: str
   cursos: str
   inicio_profissional: Optional[str] = None
   termos: bool
   verificacao: bool
   comunicacoes: bool

