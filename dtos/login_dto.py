from pydantic import Field, field_validator
from dtos.base_dto import BaseDTO
from util.validacoes_dto import validar_texto_obrigatorio, validar_email

class LoginDTO(BaseDTO):
    email: str = Field(..., description="Email do usuário")
    senha: str = Field(..., description="Senha do usuário")

    @field_validator("email")
    def validar_email_usuario(cls, valor):
        validar_email(valor, "Email")  # Deve levantar ValueError se inválido
        return valor

    @field_validator("senha")
    def validar_senha_usuario(cls, valor):
        validar_texto_obrigatorio(valor, "Senha", min_chars=6)
        return valor
