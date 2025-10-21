from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Usuario:
    id: Optional[int] = None
    nome: str = ''
    dataNascimento: str = ''
    email: str = ''
    telefone: str = ''
    cpf: str = ''
    senha: str = ''
    perfil: str = ''
    cep: str = ''
    logradouro: str = ''
    numero: str = ''
    bairro: str = ''
    cidade: str = ''
    estado: str = ''
    ativo: bool = False
    token_redefinicao: Optional[str] = None
    data_token: Optional[str] = None
    data_cadastro: datetime = field(default_factory=datetime.now)
    foto: Optional[str] = None
    complemento: Optional[str] = None

    @classmethod
    def from_row(cls, row) -> 'Usuario':
        """
        Cria Usuario a partir de sqlite3.Row com verificação de chaves.

        Args:
            row: sqlite3.Row com dados do usuário

        Returns:
            Usuario: Instância de Usuario

        Raises:
            KeyError: Se chave obrigatória estiver faltando
        """
        # Campos obrigatórios
        required_fields = {
            'id_usuario', 'nome', 'dataNascimento', 'email',
            'telefone', 'cpf', 'senha', 'perfil'
        }

        # Verificar se todas as chaves obrigatórias existem
        row_keys = set(row.keys())
        missing = required_fields - row_keys
        if missing:
            raise KeyError(f"Chaves obrigatórias faltando: {missing}")

        # Função helper para obter valor com fallback e verificação
        def get_value(key: str, default=None):
            try:
                return row[key] if key in row.keys() else default
            except (KeyError, IndexError):
                return default

        return cls(
            id=row["id_usuario"],
            nome=row["nome"],
            dataNascimento=row["dataNascimento"],
            email=row["email"],
            telefone=row["telefone"],
            cpf=row["cpf"],
            senha=row["senha"],
            perfil=row["perfil"],
            cep=get_value("cep", ""),
            logradouro=get_value("logradouro", ""),
            numero=get_value("numero", ""),
            complemento=get_value("complemento"),
            bairro=get_value("bairro", ""),
            cidade=get_value("cidade", ""),
            estado=get_value("estado", ""),
            ativo=bool(get_value("ativo", False)),
            foto=get_value("foto"),
            token_redefinicao=get_value("token_redefinicao"),
            data_token=get_value("data_token"),
            data_cadastro=get_value("data_cadastro", datetime.now())
        )
