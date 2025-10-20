from pydantic import Field, field_validator
from dtos.base_dto import BaseDTO
from datetime import date
from util.validacoes_dto import (
    validar_texto_obrigatorio,
    validar_email,
    validar_cpf,
    validar_nome_pessoa,
    validar_telefone
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
    @field_validator("nome")
    def validar_nome(cls, valor):
        return validar_nome_pessoa(valor)

    @field_validator("email")
    def validar_email_valido(cls, valor):
        return validar_email(valor, "Email")

    @field_validator("senha")
    def validar_senha(cls, valor):
        return validar_texto_obrigatorio(valor, "Senha", min_chars=8)

    @field_validator("confirmar_senha")
    def validar_confirmar_senha(cls, valor):
        return validar_texto_obrigatorio(valor, "Confirmar Senha", min_chars=8)

    @field_validator("cpf")
    def validar_cpf_valido(cls, valor):
        return validar_cpf(valor)
    
    @field_validator("telefone")
    def validar_telefone_valido(cls, valor):
        return validar_telefone(valor)  
