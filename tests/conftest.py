import pytest
import os
import sys
import tempfile
from fastapi.testclient import TestClient
from starlette.middleware.sessions import SessionMiddleware

# Adiciona o diretório raiz do projeto ao PYTHONPATH
# Isso permite importar módulos do projeto nos testes
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Fixture para criar um banco de dados temporário para testes
@pytest.fixture(scope="function")
def test_db():
    # Cria um arquivo temporário para o banco de dados
    db_fd, db_path = tempfile.mkstemp(suffix='.db')

    # IMPORTANTE: Configura a variável de ambiente ANTES de qualquer importação
    os.environ['TEST_DATABASE_PATH'] = db_path

    # Retorna o caminho do banco de dados temporário
    yield db_path

    # Remove o arquivo temporário ao concluir o teste
    os.close(db_fd)
    if os.path.exists(db_path):
        os.unlink(db_path)

# Fixture para a aplicação FastAPI
@pytest.fixture(scope="function")
def app():
    """Retorna uma instância da aplicação FastAPI para testes"""
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles
    from util.config import SECRET_KEY
    from routes.public_routes import router as public_routes

    # Cria uma instância limpa do app para testes
    test_app = FastAPI(title="Hestia Test App", version="1.0.0")

    # Adiciona middleware de sessão
    test_app.add_middleware(
        SessionMiddleware,
        secret_key=SECRET_KEY,
        max_age=3600,
        same_site="lax",
        https_only=False  # False para testes
    )

    # Monta arquivos estáticos se necessário
    try:
        test_app.mount("/static", StaticFiles(directory="static"), name="static")
    except:
        pass  # Ignora se o diretório não existir em testes

    # Inclui rotas
    test_app.include_router(public_routes)

    return test_app

# Fixture para o cliente de testes
@pytest.fixture(scope="function")
def client(test_db, app):
    """
    Retorna um TestClient configurado com a aplicação e banco de dados de teste

    Esta fixture depende das fixtures 'test_db' e 'app' para garantir que:
    1. O banco de dados temporário esteja configurado PRIMEIRO
    2. A aplicação esteja configurada corretamente

    IMPORTANTE: test_db deve vir ANTES de app para garantir que a variável
    de ambiente TEST_DATABASE_PATH esteja configurada antes da importação das rotas
    """
    # Verifica que a variável de ambiente está configurada
    assert os.environ.get('TEST_DATABASE_PATH') == test_db, \
        f"TEST_DATABASE_PATH deve estar configurado para {test_db}"

    # Cria as tabelas necessárias no banco de teste
    from data.usuario import usuario_repo
    from data.cliente import cliente_repo
    from data.cuidador import cuidador_repo
    import sqlite3

    # IMPORTANTE: Remove as tabelas existentes para garantir que as novas
    # definições (com UNIQUE constraints) sejam aplicadas
    with sqlite3.connect(test_db) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS cuidador")
        cursor.execute("DROP TABLE IF EXISTS cliente")
        cursor.execute("DROP TABLE IF EXISTS usuario")
        conn.commit()

    # Cria as tabelas com as definições atualizadas
    usuario_repo.criar_tabela()
    cliente_repo.criar_tabela()
    cuidador_repo.criar_tabela()

    # Retorna o cliente de testes
    # raise_server_exceptions=True faz com que exceções do servidor sejam lançadas
    # em vez de retornarem respostas HTTP 500
    with TestClient(app, raise_server_exceptions=True) as test_client:
        yield test_client 