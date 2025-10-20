"""
Rotas de teste para o sistema de exception handlers
ESTAS ROTAS SÃO APENAS PARA DEMONSTRAÇÃO E DEVEM SER REMOVIDAS EM PRODUÇÃO

Para testar:
- http://localhost:8000/teste/errors - Página inicial com todos os testes
- http://localhost:8000/teste/errors/404 - Força erro 404
- http://localhost:8000/teste/errors/500 - Força erro 500
- http://localhost:8000/teste/errors/validation - Força erro de validação
- http://localhost:8000/teste/errors/generic - Força exceção genérica

Para remover:
1. Delete este arquivo (routes/teste_errors_routes.py)
2. Remova a importação e inclusão no main.py
"""

from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from util.config import IS_DEVELOPMENT

router = APIRouter(prefix="/teste/errors", tags=["Testes - Exception Handlers"])


@router.get("/", response_class=HTMLResponse)
async def teste_errors_index(request: Request):
    """
    Página principal de testes de exceções
    Lista todos os tipos de erros disponíveis para teste
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Teste de Exception Handlers - Hestia</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

        <style>
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem 0;
            }}
            .test-card {{
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                padding: 2.5rem;
                max-width: 800px;
                width: 100%;
            }}
            .test-card h1 {{
                color: #2b8c6a;
                margin-bottom: 1rem;
            }}
            .test-item {{
                background: #f8f9fa;
                border-radius: 8px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                border-left: 4px solid #667eea;
                transition: all 0.3s ease;
            }}
            .test-item:hover {{
                transform: translateX(5px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .test-item h5 {{
                margin-bottom: 0.5rem;
                color: #333;
            }}
            .test-item p {{
                margin-bottom: 1rem;
                color: #6c757d;
            }}
            .badge-mode {{
                font-size: 0.875rem;
                padding: 0.5rem 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="test-card">
            <div class="text-center mb-4">
                <h1>
                    <i class="bi bi-bug"></i>
                    Teste de Exception Handlers
                </h1>
                <p class="lead text-muted">Sistema de tratamento centralizado de exceções</p>
                <div>
                    <span class="badge bg-{'success' if IS_DEVELOPMENT else 'danger'} badge-mode">
                        Modo: {'Development' if IS_DEVELOPMENT else 'Production'}
                    </span>
                </div>
            </div>

            <div class="alert alert-info" role="alert">
                <i class="bi bi-info-circle"></i>
                <strong>Instruções:</strong> Clique nos botões abaixo para testar diferentes tipos de exceções.
                {'Em modo Development, você verá detalhes técnicos completos.' if IS_DEVELOPMENT else 'Em modo Production, mensagens técnicas são ocultadas.'}
            </div>

            <div class="test-item">
                <h5>
                    <i class="bi bi-file-earmark-x text-primary"></i>
                    Erro 404 - Not Found
                </h5>
                <p>Simula acesso a uma página que não existe</p>
                <a href="/teste/errors/404" class="btn btn-primary">
                    <i class="bi bi-arrow-right-circle"></i> Testar 404
                </a>
            </div>

            <div class="test-item">
                <h5>
                    <i class="bi bi-exclamation-triangle text-danger"></i>
                    Erro 500 - Internal Server Error
                </h5>
                <p>Força uma exceção HTTP 500 (erro interno do servidor)</p>
                <a href="/teste/errors/500" class="btn btn-danger">
                    <i class="bi bi-arrow-right-circle"></i> Testar 500
                </a>
            </div>

            <div class="test-item">
                <h5>
                    <i class="bi bi-exclamation-octagon text-warning"></i>
                    Exceção Genérica
                </h5>
                <p>Força uma exceção Python não tratada (será capturada pelo handler genérico)</p>
                <a href="/teste/errors/generic" class="btn btn-warning">
                    <i class="bi bi-arrow-right-circle"></i> Testar Exceção
                </a>
            </div>

            <div class="test-item">
                <h5>
                    <i class="bi bi-check2-square text-info"></i>
                    Erro de Validação (Pydantic)
                </h5>
                <p>Força um erro de validação de dados</p>
                <button type="button" class="btn btn-info" data-bs-toggle="collapse" data-bs-target="#formValidation">
                    <i class="bi bi-arrow-right-circle"></i> Testar Validação
                </button>
                <div class="collapse mt-3" id="formValidation">
                    <form method="POST" action="/teste/errors/validation">
                        <div class="alert alert-secondary">
                            <small>
                                Envie o formulário sem preencher para gerar erro de validação.
                                Ou preencha corretamente para ver sucesso.
                            </small>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Nome (obrigatório, mín. 3 caracteres)</label>
                            <input type="text" name="nome" class="form-control" placeholder="Digite seu nome">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Idade (obrigatório, entre 18 e 120)</label>
                            <input type="number" name="idade" class="form-control" placeholder="Digite sua idade">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Email (obrigatório, formato válido)</label>
                            <input type="text" name="email" class="form-control" placeholder="Digite seu e-mail">
                        </div>
                        <button type="submit" class="btn btn-info">
                            <i class="bi bi-send"></i> Enviar
                        </button>
                    </form>
                </div>
            </div>

            <div class="test-item">
                <h5>
                    <i class="bi bi-shield-lock text-secondary"></i>
                    Erro 401 - Unauthorized
                </h5>
                <p>Simula acesso não autorizado (redirecionamento para login)</p>
                <a href="/teste/errors/401" class="btn btn-secondary">
                    <i class="bi bi-arrow-right-circle"></i> Testar 401
                </a>
            </div>

            <div class="mt-4 text-center">
                <hr>
                <a href="/" class="btn btn-outline-secondary">
                    <i class="bi bi-arrow-left"></i> Voltar para Home
                </a>
            </div>

            <div class="alert alert-warning mt-4" role="alert">
                <h6><i class="bi bi-exclamation-triangle-fill"></i> Importante</h6>
                <small>
                    Esta é uma rota de teste e deve ser removida em produção.<br>
                    Arquivo: <code>routes/teste_errors_routes.py</code>
                </small>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@router.get("/404")
async def teste_error_404():
    """
    Força um erro 404 (HTTPException com status 404)
    """
    raise HTTPException(status_code=404, detail="Esta página de teste não existe (404 forçado)")


@router.get("/500")
async def teste_error_500():
    """
    Força um erro 500 (HTTPException com status 500)
    """
    raise HTTPException(status_code=500, detail="Erro interno forçado para teste")


@router.get("/401")
async def teste_error_401():
    """
    Força um erro 401 (Unauthorized)
    Deve redirecionar para login com mensagem de erro
    """
    raise HTTPException(status_code=401, detail="Acesso não autorizado (teste)")


@router.get("/generic")
async def teste_error_generic():
    """
    Força uma exceção genérica Python (não HTTPException)
    Será capturada pelo generic_exception_handler
    """
    # Forçar diferentes tipos de exceções para teste
    raise ValueError("Este é um erro genérico de teste para demonstração do exception handler!")


# Modelo Pydantic para validação
class DadosFormulario(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    idade: int = Field(..., ge=18, le=120)
    email: str = Field(..., regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


@router.post("/validation", response_class=HTMLResponse)
async def teste_error_validation(
    nome: str = Form(...),
    idade: int = Form(...),
    email: str = Form(...)
):
    """
    Teste de validação com Pydantic
    Se os dados forem inválidos, RequestValidationError será lançado
    """
    try:
        # Validar dados usando Pydantic
        dados = DadosFormulario(nome=nome, idade=idade, email=email)

        # Se passou pela validação, retornar sucesso
        return HTMLResponse(content=f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Validação Bem-sucedida</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header bg-success text-white">
                                <h5>✓ Validação Bem-sucedida!</h5>
                            </div>
                            <div class="card-body">
                                <p><strong>Nome:</strong> {dados.nome}</p>
                                <p><strong>Idade:</strong> {dados.idade}</p>
                                <p><strong>Email:</strong> {dados.email}</p>
                                <hr>
                                <p class="text-muted">
                                    Os dados passaram pela validação do Pydantic!
                                </p>
                            </div>
                            <div class="card-footer">
                                <a href="/teste/errors" class="btn btn-primary">Voltar para Testes</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """)
    except Exception as e:
        # Re-lançar exceção para ser capturada pelo handler
        raise
