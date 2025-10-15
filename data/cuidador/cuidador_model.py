from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Cuidador(Usuario):
   experiencia: str = ''
   confirmarSenha: str = ''
   valorHora: float = 0.0
   escolaridade: str = ''
   apresentacao: str = ''
   cursos: str = ''
   inicio_profissional: str = ''
   termos: bool = False
   verificacao: bool = False
   comunicacoes: bool = False
   # perfil: str = 'cuidador'  

