from dataclasses import dataclass
from datetime import date
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Cuidador(Usuario):   
   experiencia: str
   valorHora: float
   escolaridade: str
   apresentacao: str
   cursos: str
   confirmarSenha: str
   termos: bool
   verificacao: bool
   comunicacoes: bool

