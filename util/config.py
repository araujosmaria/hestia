"""
Módulo de configurações centralizadas da aplicação Hestia.
Carrega variáveis de ambiente e fornece valores padrão seguros.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# === Configurações da Aplicação ===
APP_NAME = os.getenv("APP_NAME", "Hestia - Sistema de Cuidadores")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8082")
SECRET_KEY = os.getenv("SECRET_KEY")

# Validar SECRET_KEY
if not SECRET_KEY:
    import secrets
    SECRET_KEY = secrets.token_urlsafe(32)
    print("⚠️  AVISO: SECRET_KEY não configurada no .env!")
    print(f"⚠️  Usando chave temporária: {SECRET_KEY}")
    print("⚠️  Adicione esta linha ao seu .env:")
    print(f'SECRET_KEY={SECRET_KEY}')
    print()

# === Configurações do Banco de Dados ===
DATABASE_PATH = os.getenv("DATABASE_PATH", "database.db")

# === Configurações de Logging ===
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# === Configurações de Email (Resend.com) ===
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
RESEND_FROM_EMAIL = os.getenv("RESEND_FROM_EMAIL", "noreply@hestia.com")
RESEND_FROM_NAME = os.getenv("RESEND_FROM_NAME", APP_NAME)

# === Configurações do Servidor ===
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8082"))
RELOAD = os.getenv("RELOAD", "True").lower() == "true"

# === Modo de Execução ===
RUNNING_MODE = os.getenv("RUNNING_MODE", "Production")
IS_DEVELOPMENT = RUNNING_MODE.lower() == "development"

# === Configurações de Rate Limiting ===
RATE_LIMIT_LOGIN_MAX = int(os.getenv("RATE_LIMIT_LOGIN_MAX", "5"))
RATE_LIMIT_LOGIN_MINUTOS = int(os.getenv("RATE_LIMIT_LOGIN_MINUTOS", "5"))
RATE_LIMIT_CADASTRO_MAX = int(os.getenv("RATE_LIMIT_CADASTRO_MAX", "3"))
RATE_LIMIT_CADASTRO_MINUTOS = int(os.getenv("RATE_LIMIT_CADASTRO_MINUTOS", "10"))
RATE_LIMIT_ESQUECI_SENHA_MAX = int(os.getenv("RATE_LIMIT_ESQUECI_SENHA_MAX", "2"))
RATE_LIMIT_ESQUECI_SENHA_MINUTOS = int(os.getenv("RATE_LIMIT_ESQUECI_SENHA_MINUTOS", "5"))

# === Configurações de Senha ===
SENHA_MIN_CHARS = int(os.getenv("SENHA_MIN_CHARS", "8"))
SENHA_REQUER_MAIUSCULA = os.getenv("SENHA_REQUER_MAIUSCULA", "True").lower() == "true"
SENHA_REQUER_MINUSCULA = os.getenv("SENHA_REQUER_MINUSCULA", "True").lower() == "true"
SENHA_REQUER_NUMERO = os.getenv("SENHA_REQUER_NUMERO", "True").lower() == "true"
SENHA_REQUER_ESPECIAL = os.getenv("SENHA_REQUER_ESPECIAL", "True").lower() == "true"

# === Versão da Aplicação ===
VERSION = "1.0.0"

# === Diretórios ===
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
LOGS_DIR = BASE_DIR / "logs"

# Criar diretórios se não existirem
LOGS_DIR.mkdir(exist_ok=True)
