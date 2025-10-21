from pydantic import Field, field_validator, model_validator
from dtos.base_dto import BaseDTO
from datetime import date
from dtos.validators import (
    validar_string_obrigatoria,
    validar_email,
    validar_cpf,
    validar_nome_pessoa,
    validar_telefone_br,
    validar_estado_brasileiro
)

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

    _validar_estado = field_validator("estado")(validar_estado_brasileiro())

    @model_validator(mode="after")
    def validar_senhas(self) -> "CadastroContratanteDTO":
        """Valida que senha e confirmar_senha são iguais"""
        if self.senha != self.confirmar_senha:
            raise ValueError("As senhas não coincidem")
        return self
