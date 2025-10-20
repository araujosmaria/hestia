# Sistema de Tratamento de Exceções Global - Hestia

Sistema completo e robusto de tratamento centralizado de exceções para a aplicação FastAPI, seguindo as melhores práticas de desenvolvimento web.

## 📋 Índice

- [Características](#características)
- [Arquivos do Sistema](#arquivos-do-sistema)
- [Como Funciona](#como-funciona)
- [Tipos de Exceções Tratadas](#tipos-de-exceções-tratadas)
- [Modo Development vs Production](#modo-development-vs-production)
- [Como Testar](#como-testar)
- [Logging](#logging)
- [Customização](#customização)
- [Troubleshooting](#troubleshooting)

## ✨ Características

- ✅ **Tratamento centralizado** - Todas as exceções capturadas em um único lugar
- ✅ **Diferencia Dev/Prod** - Mostra detalhes técnicos apenas em desenvolvimento
- ✅ **Logging apropriado** - Registra erros com níveis corretos (debug, warning, error)
- ✅ **Mensagens amigáveis** - Interface clara para o usuário
- ✅ **Integração com toasts** - Flash messages para feedback visual
- ✅ **Páginas de erro customizadas** - 404 e 500 profissionais
- ✅ **Traceback completo** - Em desenvolvimento, mostra stack trace
- ✅ **Redirecionamento inteligente** - 401/403 redirecionam para login
- ✅ **Validação Pydantic** - Trata erros de validação de forma amigável
- ✅ **Responsivo** - Páginas de erro funcionam em mobile e desktop

## 📁 Arquivos do Sistema

```
hestia/
├── util/
│   ├── exception_handlers.py    # Handlers de exceções
│   ├── logger_config.py          # Configuração de logging
│   ├── config.py                 # Configurações (IS_DEVELOPMENT)
│   └── flash_messages.py         # Sistema de mensagens flash
├── templates/
│   └── errors/
│       ├── 404.html              # Página de erro 404
│       └── 500.html              # Página de erro 500
├── static/
│   └── css/
│       └── errors.css            # Estilos das páginas de erro
├── logs/
│   ├── app.log                   # Log geral da aplicação
│   └── errors.log                # Log apenas de erros
└── routes/
    └── teste_errors_routes.py    # Rotas de teste (remover em produção)
```

## 🔧 Como Funciona

### 1. Captura de Exceções

O sistema registra 3 exception handlers no `main.py`:

```python
# Ordem importa: do mais específico para o mais genérico
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
```

### 2. Fluxo de Tratamento

```
Exceção Lançada
      ↓
Handler Apropriado
      ↓
┌─────┴─────────────────┐
│   Logar Exceção       │ → logs/app.log
│   (nível apropriado)  │   logs/errors.log
└─────┬─────────────────┘
      ↓
┌─────┴──────────────────┐
│  Adicionar Flash Msg?  │ → Mensagem para usuário
│  (se aplicável)        │   (via toast)
└─────┬──────────────────┘
      ↓
┌─────┴──────────────────┐
│  Retornar Resposta     │
│  - Redirect (401/403)  │
│  - Template (404/500)  │
└────────────────────────┘
```

## 🎯 Tipos de Exceções Tratadas

### 1. HTTPException (StarletteHTTPException)

**Handler:** `http_exception_handler()`

Trata exceções HTTP do FastAPI/Starlette.

#### Status 401 - Unauthorized
- **Comportamento:** Redireciona para `/login?redirect={path_atual}`
- **Flash Message:** "Você precisa estar autenticado para acessar esta página."
- **Log:** Warning

```python
# Exemplo de uso no código
from fastapi import HTTPException, status

@app.get("/admin/usuarios")
async def listar_usuarios(usuario_logado: Usuario = Depends(get_usuario_logado)):
    if not usuario_logado:
        raise HTTPException(status_code=401, detail="Não autenticado")
    # ...
```

#### Status 403 - Forbidden
- **Comportamento:** Redireciona para `/login`
- **Flash Message:** "Você não tem permissão para acessar esta página."
- **Log:** Warning

```python
# Exemplo de uso no código
@app.get("/admin/usuarios")
async def listar_usuarios(usuario_logado: Usuario = Depends(get_usuario_logado)):
    if usuario_logado.perfil != "admin":
        raise HTTPException(status_code=403, detail="Sem permissão")
    # ...
```

#### Status 404 - Not Found
- **Comportamento:** Renderiza `errors/404.html`
- **Log:** Warning (ou Debug para arquivos estáticos opcionais)

**Otimização:** Arquivos estáticos opcionais (`.map`, `.ico`, `.woff`, etc.) não geram warnings, apenas debug.

#### Outros Status HTTP
- **Comportamento:** Renderiza `errors/500.html` com status apropriado
- **Mensagem:** Técnica em Dev, genérica em Prod
- **Log:** Warning

### 2. RequestValidationError (Pydantic)

**Handler:** `validation_exception_handler()`

Trata erros de validação do Pydantic.

- **Comportamento:** Renderiza `errors/500.html` com status 422
- **Flash Message:** Lista de erros (Dev) ou mensagem genérica (Prod)
- **Log:** Warning com detalhes completos

**Exemplo de erro capturado:**

```python
from pydantic import BaseModel, Field

class DadosCadastro(BaseModel):
    nome: str = Field(..., min_length=3)
    idade: int = Field(..., ge=18)
    email: str

@app.post("/cadastro")
async def cadastrar(dados: DadosCadastro):
    # Se dados inválidos, RequestValidationError é lançado automaticamente
    pass
```

### 3. Exceções Genéricas (Exception)

**Handler:** `generic_exception_handler()`

Captura TODAS as exceções Python não tratadas.

- **Comportamento:** Renderiza `errors/500.html` com status 500
- **Mensagem:** Tipo e mensagem em Dev, genérica em Prod
- **Log:** Error com `exc_info=True` (traceback completo)
- **Traceback:** Exibido apenas em Development

**Exemplos capturados:**

```python
# ValueError
raise ValueError("CPF inválido")

# KeyError
dados = {"nome": "João"}
sobrenome = dados["sobrenome"]  # KeyError

# AttributeError
objeto_none = None
objeto_none.metodo()  # AttributeError

# Qualquer exceção Python
```

## 🔄 Modo Development vs Production

Controlado pela variável `IS_DEVELOPMENT` no `util/config.py`.

### Development Mode

```env
RUNNING_MODE=Development
```

**Características:**
- ✅ Mensagens de erro técnicas e detalhadas
- ✅ Traceback completo exibido nas páginas
- ✅ Detalhes da requisição (path, method, IP)
- ✅ Erros de validação com campos específicos
- ✅ Logs no console (além de arquivo)

**Exemplo de mensagem:**
```
ValueError: CPF inválido: 123.456.789-00 não passou na validação de dígitos verificadores
```

### Production Mode

```env
RUNNING_MODE=Production
```

**Características:**
- ✅ Mensagens genéricas e amigáveis
- ❌ Sem traceback ou detalhes técnicos
- ❌ Sem exposição de caminhos de arquivos
- ✅ Logs apenas em arquivos
- ✅ Foco na experiência do usuário

**Exemplo de mensagem:**
```
Erro interno do servidor. Nossa equipe foi notificada.
```

## 🧪 Como Testar

### 1. Rota de Teste (Development)

Acesse: **http://localhost:8000/teste/errors**

Esta rota interativa permite testar todos os tipos de exceções:

- ✅ Erro 404 (página não encontrada)
- ✅ Erro 500 (erro interno)
- ✅ Erro 401 (não autorizado)
- ✅ Exceção genérica (ValueError, etc.)
- ✅ Erro de validação (Pydantic)

### 2. Testes Manuais

**Forçar erro 404:**
```
http://localhost:8000/pagina-que-nao-existe
```

**Forçar erro genérico (adicionar rota temporária):**
```python
@app.get("/test-error")
async def test_error():
    raise ValueError("Teste de erro")
```

**Forçar erro de validação:**
```python
# Enviar dados inválidos para uma rota com validação Pydantic
```

### 3. Remover Rotas de Teste em Produção

**Arquivos a remover:**
1. `routes/teste_errors_routes.py`
2. `routes/teste_toast_routes.py`

**No `main.py`, remover:**
```python
# Rotas de teste (remover em produção)
from routes import teste_toast_routes
from routes import teste_errors_routes
app.include_router(teste_toast_routes.router)
app.include_router(teste_errors_routes.router)
```

## 📊 Logging

### Estrutura de Logs

#### app.log
- **Nível:** INFO e acima
- **Conteúdo:** Todos os logs da aplicação
- **Formato:** `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
- **Rotação:** 10MB por arquivo, mantém 10 backups

#### errors.log
- **Nível:** ERROR e acima
- **Conteúdo:** Apenas erros críticos
- **Formato:** Inclui pathname e linha do erro
- **Rotação:** 10MB por arquivo, mantém 10 backups

### Níveis de Log Usados

| Exceção | Nível | Justificativa |
|---------|-------|---------------|
| 404 (arquivos estáticos opcionais) | DEBUG | Não é um erro real |
| 404 (páginas) | WARNING | Pode indicar link quebrado |
| 401/403 | WARNING | Tentativa de acesso não autorizado |
| Validação | WARNING | Dados inválidos enviados |
| 500+ | ERROR | Erro real que precisa atenção |
| Exceções não tratadas | ERROR | Bug no código |

### Exemplos de Log

**Warning (404):**
```
2025-10-20 14:30:15 - hestia - WARNING - HTTPException 404: Not Found - Path: /admin/usuarios - IP: 192.168.1.100
```

**Error (exceção genérica):**
```
2025-10-20 14:35:22 - hestia - ERROR - Exceção não tratada: ValueError: CPF inválido - Path: /cadastro - IP: 192.168.1.100
Traceback (most recent call last):
  File "/app/routes/auth_routes.py", line 45, in cadastrar
    validar_cpf(cpf)
  File "/app/util/validacoes.py", line 12, in validar_cpf
    raise ValueError("CPF inválido")
ValueError: CPF inválido
```

## 🎨 Customização

### Alterar Mensagens de Erro

**Arquivo:** `util/exception_handlers.py`

```python
# 401
informar_erro(request, "Você precisa estar autenticado para acessar esta página.")

# 403
informar_erro(request, "Você não tem permissão para acessar esta página.")

# Validação (production)
mensagem_flash = "Os dados fornecidos são inválidos. Por favor, verifique e tente novamente."

# Genérico (production)
error_message = "Erro interno do servidor. Nossa equipe foi notificada."
```

### Alterar Redirecionamento

**401 - Redirecionar para página diferente:**

```python
# ANTES
return RedirectResponse(
    f"/login?redirect={request.url.path}",
    status_code=status.HTTP_303_SEE_OTHER
)

# DEPOIS (redirecionar para /auth)
return RedirectResponse(
    f"/auth?redirect={request.url.path}",
    status_code=status.HTTP_303_SEE_OTHER
)
```

### Personalizar Páginas de Erro

**Templates:** `templates/errors/404.html` e `templates/errors/500.html`

**CSS:** `static/css/errors.css`

Você pode:
- Alterar cores e layout
- Adicionar logo da empresa
- Modificar textos e ícones
- Adicionar links úteis
- Personalizar botões de ação

### Adicionar Novo Handler

```python
from fastapi import Request, status

async def custom_exception_handler(request: Request, exc: CustomException):
    """Handler para exceção customizada"""
    logger.warning(f"CustomException: {str(exc)}")

    return templates.TemplateResponse(
        "errors/custom.html",
        {"request": request, "error": str(exc)},
        status_code=status.HTTP_400_BAD_REQUEST
    )

# Registrar no main.py
app.add_exception_handler(CustomException, custom_exception_handler)
```

## 🔧 Troubleshooting

### Problema: Exceções não estão sendo capturadas

**Checklist:**
- [ ] Handlers registrados no `main.py`?
- [ ] Ordem de registro correta? (específico → genérico)
- [ ] Import correto dos handlers?
- [ ] Templates de erro existem?

**Verificar no console:**
```python
# No main.py, após registrar handlers
logger.info("Exception handlers registrados")
```

### Problema: Traceback não aparece em Development

**Verificar configuração:**

```python
# Em util/config.py
RUNNING_MODE = os.getenv("RUNNING_MODE", "Production")
IS_DEVELOPMENT = RUNNING_MODE.lower() == "development"

print(f"IS_DEVELOPMENT: {IS_DEVELOPMENT}")  # Deve ser True
```

**Verificar .env:**
```env
RUNNING_MODE=Development
```

### Problema: Logs não estão sendo criados

**Verificar diretório:**
```bash
ls -la logs/
# Deve mostrar app.log e errors.log
```

**Verificar permissões:**
```bash
chmod 755 logs/
```

**Verificar criação do diretório:**
```python
# Em util/config.py
LOGS_DIR.mkdir(exist_ok=True)
```

### Problema: Página de erro sem estilo

**Verificar carregamento do CSS:**

No template, deve ter:
```html
<link rel="stylesheet" href="/static/css/errors.css">
```

**Verificar arquivos estáticos montados:**
```python
# No main.py
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### Problema: Flash messages não aparecem

**Verificar:**
1. SessionMiddleware configurado?
2. Template base tem sistema de toasts?
3. `informar_erro()` sendo chamado?

```python
# Debug
informar_erro(request, "Teste de mensagem")
mensagens = request.session.get("mensagens", [])
print(f"Mensagens na sessão: {mensagens}")
```

## 📚 Boas Práticas

### ✅ FAÇA

```python
# Use HTTPException para erros HTTP conhecidos
raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Use exceções específicas para erros de negócio
raise ValueError("CPF inválido")

# Logue contexto útil
logger.error(f"Erro ao processar pagamento #{pagamento_id}", exc_info=True)

# Sempre use try/except em operações críticas
try:
    processar_pagamento()
except Exception as e:
    logger.error("Erro ao processar pagamento", exc_info=True)
    raise
```

### ❌ NÃO FAÇA

```python
# Não use print() para logs
print("Erro aconteceu")  # ❌ Use logger.error()

# Não exponha informações sensíveis em production
raise HTTPException(status_code=500, detail=f"Senha incorreta: {senha}")  # ❌ Vazamento

# Não capture exceções silenciosamente
try:
    processar()
except:
    pass  # ❌ Erro perdido!

# Não use Exception genérico para tudo
raise Exception("erro")  # ❌ Seja específico: ValueError, etc.
```

## 🎯 Checklist de Produção

Antes de colocar em produção:

- [ ] `RUNNING_MODE=Production` no `.env`
- [ ] Remover rotas de teste (`teste_errors_routes.py`, `teste_toast_routes.py`)
- [ ] Remover imports de rotas de teste no `main.py`
- [ ] Verificar se logs estão sendo criados
- [ ] Testar todas as páginas de erro em production mode
- [ ] Configurar monitoramento externo (Sentry, Rollbar, etc.)
- [ ] Revisar mensagens de erro para não expor informações sensíveis
- [ ] Configurar backup de logs
- [ ] Testar redirecionamentos 401/403

---

**Sistema implementado em:** 20/10/2025
**Modo padrão:** Production
**Logs:** `/logs/app.log` e `/logs/errors.log`
