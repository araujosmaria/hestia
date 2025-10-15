from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Cuidador(Usuario):
   experiencia: str = ''
   confirmarSenha: str = ''
   inicio_profissional: str = ''
   termos: bool = False
   verificacao: bool = False
   comunicacoes: bool = False
   perfil: str = 'cuidador'  # sobrescreve o valor herdado para garantir o perfil correto

