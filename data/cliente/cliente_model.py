from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Cliente(Usuario):
    parentesco_paciente: str
    confirmarSenha: str
    termos: bool
    verificacao: bool
    comunicacoes: bool