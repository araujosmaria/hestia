"""
Rota de teste para o sistema de toasts Bootstrap 5
Esta rota é temporária e serve apenas para demonstração

Para testar:
1. Acesse http://localhost:8000/teste-toast
2. Você verá 4 toasts automaticamente (um de cada tipo)
3. Clique no botão para testar toasts via JavaScript

Para remover esta rota de teste:
1. Remova este arquivo (routes/teste_toast_routes.py)
2. Remova a importação e inclusão no main.py
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso, informar_info

router = APIRouter(prefix="/teste", tags=["Testes"])


@router.get("/toast", response_class=HTMLResponse)
async def teste_toast(request: Request):
    """
    Rota de teste do sistema de toasts
    Adiciona mensagens de cada tipo e exibe uma página de demonstração
    """
    # Adicionar mensagens de cada tipo
    informar_sucesso(request, "✓ Mensagem de sucesso testada!")
    informar_erro(request, "✗ Mensagem de erro testada!")
    informar_aviso(request, "⚠ Mensagem de aviso testada!")
    informar_info(request, "ℹ Mensagem de info testada!")

    # Renderizar página de teste
    from util.flash_messages import obter_mensagens
    import json

    mensagens_json = json.dumps(obter_mensagens(request))

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Teste de Toasts - Hestia</title>

        <!-- Bootstrap 5 -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

        <!-- CSS customizado de toasts -->
        <link rel="stylesheet" href="/static/css/toasts.css">

        <style>
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .test-card {{
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                padding: 3rem;
                max-width: 600px;
                width: 100%;
            }}
            .test-card h1 {{
                color: #2b8c6a;
                margin-bottom: 1.5rem;
            }}
            .btn-test {{
                margin: 0.5rem;
            }}
        </style>
    </head>
    <body>
        <div class="test-card">
            <h1>
                <i class="bi bi-broadcast"></i>
                Teste de Toasts
            </h1>

            <p class="lead">
                Você deve ver 4 toasts no canto inferior direito da tela.
            </p>

            <hr>

            <h5>Testes Programáticos (JavaScript)</h5>
            <p class="text-muted">Clique nos botões abaixo para testar toasts via JavaScript:</p>

            <div class="d-flex flex-wrap">
                <button class="btn btn-success btn-test" onclick="window.exibirToast('Toast de sucesso via JavaScript!', 'success')">
                    <i class="bi bi-check-circle"></i> Sucesso
                </button>

                <button class="btn btn-danger btn-test" onclick="window.exibirToast('Toast de erro via JavaScript!', 'danger')">
                    <i class="bi bi-exclamation-circle"></i> Erro
                </button>

                <button class="btn btn-warning btn-test" onclick="window.exibirToast('Toast de aviso via JavaScript!', 'warning')">
                    <i class="bi bi-exclamation-triangle"></i> Aviso
                </button>

                <button class="btn btn-info btn-test" onclick="window.exibirToast('Toast de info via JavaScript!', 'info')">
                    <i class="bi bi-info-circle"></i> Info
                </button>

                <button class="btn btn-secondary btn-test" onclick="window.exibirToast('Toast com 10 segundos de duração', 'info', 10000)">
                    <i class="bi bi-clock"></i> 10 segundos
                </button>
            </div>

            <hr>

            <h5>Console do Navegador</h5>
            <p class="text-muted">Abra o console (F12) e teste:</p>
            <pre class="bg-light p-3 rounded"><code>window.exibirToast('Minha mensagem', 'success')
window.exibirToast('Erro!', 'danger')
window.exibirToast('Atenção', 'warning', 8000)</code></pre>

            <div class="mt-4">
                <a href="/" class="btn btn-outline-secondary">
                    <i class="bi bi-arrow-left"></i> Voltar para Home
                </a>

                <a href="/teste/toast" class="btn btn-primary">
                    <i class="bi bi-arrow-clockwise"></i> Recarregar Teste
                </a>
            </div>

            <hr>

            <div class="alert alert-info mt-3">
                <h6><i class="bi bi-info-circle"></i> Informações Técnicas</h6>
                <ul class="mb-0">
                    <li>Sistema: Bootstrap 5 Toasts</li>
                    <li>Backend: FastAPI Flash Messages</li>
                    <li>Auto-dismiss: 5 segundos (padrão)</li>
                    <li>Posição: Inferior direito</li>
                    <li>Framework CSS: Bootstrap 5.3.0</li>
                    <li>Ícones: Bootstrap Icons 1.10.5</li>
                </ul>
            </div>
        </div>

        <!-- Container para Toasts (inferior direito) -->
        <div id="toast-container" class="toast-container position-fixed bottom-0 end-0 p-4"></div>

        <!-- Dados de mensagens (hidden) -->
        <script id="mensagens-data" type="application/json">
            {mensagens_json}
        </script>

        <!-- Scripts -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script src="/static/js/toasts.js"></script>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)
