from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Cuidador(Usuario):
   experiencia: str
   confirmarSenha: str
   valorHora: float
   escolaridade: str
   apresentacao: str
   cursos: str
   inicio_profissional: str
   termos: bool
   verificacao: bool
   comunicacoes: bool
   perfil: str = 'cuidador'  # sobrescreve o valor herdado para garantir o perfil correto

