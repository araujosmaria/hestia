"""
Sistema de Logging Centralizado para Hestia
Configura logging com arquivos rotativos e console
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from util.config import LOG_LEVEL, LOGS_DIR, IS_DEVELOPMENT

# Garantir que diretório de logs existe
LOGS_DIR.mkdir(exist_ok=True)

# Configurar logger principal
logger = logging.getLogger("hestia")

# Definir nível de log baseado em configuração
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logger.setLevel(log_level)

# Evitar duplicação de handlers
if not logger.handlers:
    # === Handler para arquivo (com rotação) ===
    file_handler = RotatingFileHandler(
        LOGS_DIR / "app.log",
        maxBytes=10485760,  # 10MB
        backupCount=10,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # === Handler para arquivo de erros ===
    error_handler = RotatingFileHandler(
        LOGS_DIR / "errors.log",
        maxBytes=10485760,  # 10MB
        backupCount=10,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    error_handler.setFormatter(error_formatter)
    logger.addHandler(error_handler)

    # === Handler para console (apenas em desenvolvimento) ===
    if IS_DEVELOPMENT:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(
            '%(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

# Evitar propagação para o logger raiz
logger.propagate = False

# Log inicial
logger.info(f"Sistema de logging iniciado - Nível: {LOG_LEVEL}")
