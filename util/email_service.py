"""
Serviço de envio de emails usando Resend.com
"""
import resend
from typing import Optional
from util.config import (
    RESEND_API_KEY,
    RESEND_FROM_EMAIL,
    RESEND_FROM_NAME,
    BASE_URL
)


class EmailService:
    """
    Serviço centralizado para envio de emails via Resend.com
    """

    def __init__(self):
        self.api_key = RESEND_API_KEY
        self.from_email = RESEND_FROM_EMAIL
        self.from_name = RESEND_FROM_NAME
        self.base_url = BASE_URL

        if self.api_key:
            resend.api_key = self.api_key
        else:
            print("⚠️  AVISO: RESEND_API_KEY não configurada. Emails não serão enviados.")

    def _pode_enviar(self) -> bool:
        """Verifica se o serviço está configurado"""
        return bool(self.api_key)

    def enviar_email(
        self,
        para_email: str,
        para_nome: str,
        assunto: str,
        html: str,
        texto: Optional[str] = None
    ) -> tuple[bool, str]:
        """
        Envia um email genérico

        Args:
            para_email: Email do destinatário
            para_nome: Nome do destinatário
            assunto: Assunto do email
            html: Conteúdo HTML do email
            texto: Versão texto do email (opcional)

        Returns:
            Tupla (sucesso, mensagem)
        """
        if not self._pode_enviar():
            return False, "Serviço de email não configurado (RESEND_API_KEY ausente)"

        params = {
            "from": f"{self.from_name} <{self.from_email}>",
            "to": [para_email],
            "subject": assunto,
            "html": html
        }

        if texto:
            params["text"] = texto

        try:
            email = resend.Emails.send(params)
            email_id = email.get('id', 'N/A')
            return True, f"Email enviado com sucesso (ID: {email_id})"
        except Exception as e:
            return False, f"Erro ao enviar email: {str(e)}"

    def enviar_recuperacao_senha(
        self,
        para_email: str,
        para_nome: str,
        token: str
    ) -> tuple[bool, str]:
        """
        Envia email de recuperação de senha

        Args:
            para_email: Email do destinatário
            para_nome: Nome do destinatário
            token: Token de redefinição

        Returns:
            Tupla (sucesso, mensagem)
        """
        url_recuperacao = f"{self.base_url}/confirmar_redefinir_senha?token={token}"

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    background-color: #f9f9f9;
                    padding: 30px;
                    border-radius: 5px;
                    margin-top: 20px;
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 30px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    font-size: 12px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Recuperação de Senha</h1>
                </div>
                <div class="content">
                    <p>Olá <strong>{para_nome}</strong>,</p>

                    <p>Você solicitou a recuperação de senha para sua conta no Hestia.</p>

                    <p>Clique no botão abaixo para redefinir sua senha:</p>

                    <center>
                        <a href="{url_recuperacao}" class="button">Redefinir Senha</a>
                    </center>

                    <p><small>Ou copie e cole este link no navegador:</small><br>
                    <a href="{url_recuperacao}">{url_recuperacao}</a></p>

                    <p><strong>⚠️ Este link expira em 1 hora.</strong></p>

                    <p>Se você não solicitou esta recuperação, ignore este email. Sua senha permanecerá inalterada.</p>
                </div>
                <div class="footer">
                    <p>Este é um email automático. Não responda.</p>
                    <p>&copy; {para_nome.split()[0]} Hestia - Sistema de Cuidadores</p>
                </div>
            </div>
        </body>
        </html>
        """

        texto = f"""
        Recuperação de Senha - Hestia

        Olá {para_nome},

        Você solicitou a recuperação de senha para sua conta.

        Acesse o link abaixo para redefinir sua senha:
        {url_recuperacao}

        ⚠️ Este link expira em 1 hora.

        Se você não solicitou esta recuperação, ignore este email.

        ---
        Hestia - Sistema de Cuidadores
        """

        return self.enviar_email(
            para_email=para_email,
            para_nome=para_nome,
            assunto="Recuperação de Senha - Hestia",
            html=html,
            texto=texto
        )

    def enviar_boas_vindas(
        self,
        para_email: str,
        para_nome: str,
        perfil: str
    ) -> tuple[bool, str]:
        """
        Envia email de boas-vindas após cadastro

        Args:
            para_email: Email do destinatário
            para_nome: Nome do destinatário
            perfil: Perfil do usuário (admin/cuidador/contratante)

        Returns:
            Tupla (sucesso, mensagem)
        """
        perfil_texto = {
            "admin": "Administrador",
            "cuidador": "Cuidador",
            "contratante": "Contratante"
        }.get(perfil, "Usuário")

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    background-color: #f9f9f9;
                    padding: 30px;
                    border-radius: 5px;
                    margin-top: 20px;
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 30px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    font-size: 12px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Bem-vindo ao Hestia!</h1>
                </div>
                <div class="content">
                    <p>Olá <strong>{para_nome}</strong>,</p>

                    <p>Seu cadastro como <strong>{perfil_texto}</strong> foi realizado com sucesso!</p>

                    <p>Agora você pode acessar o sistema com seu email e senha.</p>

                    <center>
                        <a href="{self.base_url}/login" class="button">Fazer Login</a>
                    </center>

                    <p>Se você tiver alguma dúvida, entre em contato com nosso suporte.</p>

                    <p>Seja bem-vindo(a)!</p>
                </div>
                <div class="footer">
                    <p>Este é um email automático. Não responda.</p>
                    <p>&copy; 2025 Hestia - Sistema de Cuidadores</p>
                </div>
            </div>
        </body>
        </html>
        """

        texto = f"""
        Bem-vindo ao Hestia!

        Olá {para_nome},

        Seu cadastro como {perfil_texto} foi realizado com sucesso!

        Agora você pode acessar o sistema em: {self.base_url}/login

        Seja bem-vindo(a)!

        ---
        Hestia - Sistema de Cuidadores
        """

        return self.enviar_email(
            para_email=para_email,
            para_nome=para_nome,
            assunto="Bem-vindo ao Hestia!",
            html=html,
            texto=texto
        )


# Instância global do serviço
email_service = EmailService()
