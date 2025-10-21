from pydantic import Field, field_validator, model_validator
from dtos.base_dto import BaseDTO
from datetime import date
from dtos.validators import (
    validar_string_obrigatoria,
    validar_email,
    validar_cpf,
    validar_nome_pessoa,
    validar_telefone_br
)

class CadastroCuidadorDTO(BaseDTO):
    nome: str 
    data_nascimento: date 
    email: str 
    telefone: str 
    cpf: str 
    foto_perfil: str 
    cep: str 
    logradouro: str 
    numero: str 
    bairro: str 
    cidade: str 
    estado: str 
    experiencia: str 
    escolaridade: str 
    apresentacao: str
    cursos: str 
    senha: str
    confirmar_senha: str 
    termos: bool 
    verificacao: bool 
    comunicacoes: bool 
    _validar_nome = field_validator("nome")(validar_nome_pessoa())

    _validar_email = field_validator("email")(validar_email())

    _validar_senha = field_validator("senha")(
        validar_string_obrigatoria("Senha", tamanho_minimo=8)
    )

    _validar_confirmar_senha = field_validator("confirmar_senha")(
        validar_string_obrigatoria("Confirmar Senha", tamanho_minimo=8)
    )

    _validar_cpf = field_validator("cpf")(validar_cpf())

    _validar_telefone = field_validator("telefone")(validar_telefone_br())

    @model_validator(mode="after")
    def validar_senhas(self) -> "CadastroCuidadorDTO":
        """Valida que senha e confirmar_senha são iguais"""
        if self.senha != self.confirmar_senha:
            raise ValueError("As senhas não coincidem")
        return self  
