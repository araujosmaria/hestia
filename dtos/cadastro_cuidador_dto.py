from pydantic import Field, field_validator
from dtos.base_dto import BaseDTO
from datetime import date
from util.validacoes_dto import validar_texto_obrigatorio, validar_email, validar_cpf

class CadastroCuidadorDTO(BaseDTO):
    nome: str = Field(..., description="Nome completo")
    data_nascimento: date = Field(..., alias="dataNascimento")
    email: str = Field(..., description="Email do usuário")
    telefone: str = Field(..., description="Telefone ou WhatsApp")
    cpf: str = Field(..., description="CPF do usuário")

    foto_perfil: str | None = Field(None, alias="fotoPerfil", description="Foto de perfil (opcional)")

    cep: str = Field(..., description="CEP")
    logradouro: str = Field(..., description="Logradouro")
    numero: str = Field(..., description="Número")
    bairro: str = Field(..., description="Bairro")
    cidade: str = Field(..., description="Cidade")
    estado: str = Field(..., description="Estado")

    experiencia: str = Field(..., description="Tempo de experiência")
    valor_hora: float = Field(..., alias="valorHora", description="Valor por hora")
    escolaridade: str = Field(..., description="Nível de escolaridade")
    apresentacao: str = Field(..., max_length=500, description="Apresentação pessoal")
    cursos: str | None = Field(None, description="Cursos e certificações")

    senha: str = Field(..., min_length=8)
    confirmar_senha: str = Field(..., alias="confirmarSenha")

    termos: bool = Field(..., description="Aceitou os termos de uso?")
    verificacao: bool = Field(..., description="Autorizou verificação de antecedentes?")
    comunicacoes: bool = Field(default=False)

    @field_validator("email")
    def validar_email_valido(cls, valor):
        return validar_email(valor, "Email")

    @field_validator("senha")
    def validar_senha(cls, valor):
        return validar_texto_obrigatorio(valor, "Senha", min_length=8)

    @field_validator("confirmar_senha")
    def validar_confirmar_senha(cls, valor):
        return validar_texto_obrigatorio(valor, "Confirmar Senha", min_length=8)

    @field_validator("cpf")
    def validar_cpf_valido(cls, valor):
        return validar_cpf(valor, "CPF")
