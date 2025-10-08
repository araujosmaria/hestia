from pydantic import Field, field_validator
from dtos.base_dto import BaseDTO
from datetime import date
from util.validacoes_dto import validar_texto_obrigatorio, validar_email, validar_cpf, validar_nome_pessoa, validar_telefone, validar_estado_brasileiro

class CadastroContratanteDTO(BaseDTO):
    nome: str = Field(..., description="Nome completo")
    data_nascimento: date = Field(..., alias="dataNascimento")
    email: str = Field(..., description="Email do usuário")
    telefone: str = Field(..., description="Telefone ou WhatsApp")
    cpf: str = Field(..., description="CPF do usuário")
    relacao: str = Field(..., description="Relação com a pessoa a ser cuidada")
    outro_relacao: str | None = Field(None, alias="outroRelacao", description="Descrição se 'outro' foi selecionado")
    foto_perfil: str | None = Field(None, alias="fotoPerfil", description="Foto de perfil (opcional)")
    cep: str = Field(..., description="CEP")
    endereco: str = Field(..., description="Endereço")
    numero: str | None = Field(None, description="Número do endereço")
    bairro: str = Field(..., description="Bairro")
    cidade: str = Field(..., description="Cidade")
    estado: str = Field(..., description="Estado")
    local_atendimento: bool = Field(default=False, alias="localAtendimento")
    senha: str = Field(..., min_length=8)
    confirmar_senha: str = Field(..., alias="confirmarSenha")
    termos: bool = Field(..., description="Aceitou os termos de uso?")
    comunicacoes: bool = Field(default=False)
    compartilhar_dados: bool = Field(default=False, alias="compartilharDados")

    @field_validator("nome")
    def validar_nome(cls, valor):
        return validar_nome_pessoa(valor)

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
    
    @field_validator("telefone")
    def validar_telefone_valido(cls, valor):
        return validar_telefone(valor)  # Validação do telefone

    @field_validator("estado")
    def validar_estado_valido(cls, valor):
        return validar_estado_brasileiro(valor)  #
