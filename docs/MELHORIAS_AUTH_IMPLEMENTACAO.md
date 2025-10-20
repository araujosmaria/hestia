# Guia de Implementação das Melhorias de Autenticação

Este guia explica como aplicar as melhorias implementadas no sistema de autenticação do Hestia.

## 📋 O que foi implementado

✅ **Configuração segura**
- `util/config.py` - Configurações centralizadas
- `.env` - Variáveis de ambiente (com SECRET_KEY forte)
- `.env.example` - Template de configuração

✅ **Rate Limiting**
- `util/rate_limiter.py` - Proteção contra força bruta
- Limita tentativas de login, cadastro e recuperação de senha por IP

✅ **Validação de Senha Forte**
- `util/security.py` - Melhorado com validações configuráveis
- `util/validacoes_dto.py` - Nova função `validar_senha_forte()`

✅ **Serviço de Email**
- `util/email_service.py` - Integração com Resend.com
- Templates HTML profissionais para emails
- Recuperação de senha e boas-vindas

✅ **Flash Messages**
- `util/flash_messages.py` - Sistema de mensagens para feedback

✅ **Rotas Melhoradas**
- `routes/auth_routes_melhorado.py` - Versão completa com todas as melhorias

---

## 🚀 Opções de Implementação

### Opção 1: Integração Manual (Recomendado)

Integre as melhorias gradualmente no `public_routes.py` existente:

#### 1. Adicionar imports no início do arquivo

```python
# No início de public_routes.py, adicione:
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso
from util.rate_limiter import SimpleRateLimiter
from util.email_service import email_service
from util.config import (
    RATE_LIMIT_LOGIN_MAX,
    RATE_LIMIT_LOGIN_MINUTOS,
    RATE_LIMIT_CADASTRO_MAX,
    RATE_LIMIT_CADASTRO_MINUTOS,
    RATE_LIMIT_ESQUECI_SENHA_MAX,
    RATE_LIMIT_ESQUECI_SENHA_MINUTOS
)

# Criar rate limiters (após os imports)
login_limiter = SimpleRateLimiter(RATE_LIMIT_LOGIN_MAX, RATE_LIMIT_LOGIN_MINUTOS)
cadastro_limiter = SimpleRateLimiter(RATE_LIMIT_CADASTRO_MAX, RATE_LIMIT_CADASTRO_MINUTOS)
esqueci_senha_limiter = SimpleRateLimiter(RATE_LIMIT_ESQUECI_SENHA_MAX, RATE_LIMIT_ESQUECI_SENHA_MINUTOS)

# Função helper
def obter_ip(request: Request) -> str:
    """Obtém IP do cliente"""
    return request.client.host if request.client else "unknown"
```

#### 2. Melhorar a rota de login

Substitua a função `post_login` existente por esta versão:

```python
@router.post("/login")
async def post_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    redirect: Optional[str] = None
):
    ip = obter_ip(request)

    # Rate limiting
    if not login_limiter.verificar(ip):
        tempo_restante = login_limiter.tempo_ate_liberar(ip)
        minutos = tempo_restante // 60
        informar_erro(request, f"Muitas tentativas. Aguarde {minutos} minuto(s).")
        return RedirectResponse("/login", status_code=303)

    try:
        # Validar com DTO
        dto = LoginDTO(email=email, senha=senha)

        # Buscar usuário
        usuario = usuario_repo.obter_por_email(dto.email)

        # Verificar credenciais
        if not usuario or not verificar_senha(dto.senha, usuario.senha):
            informar_erro(request, "Email ou senha incorretos")
            return RedirectResponse("/login", status_code=303)

        # Login bem-sucedido - resetar rate limiter
        login_limiter.resetar(ip)

        # Criar sessão
        usuario_dict = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "perfil": usuario.perfil
        }
        criar_sessao(request, usuario_dict)

        informar_sucesso(request, f"Bem-vindo(a), {usuario.nome}!")

        # Redirecionar conforme perfil
        if usuario.perfil == "contratante":
            return RedirectResponse("/contratante/home_contratante", status_code=303)
        elif usuario.perfil == "cuidador":
            return RedirectResponse("/cuidador/home_cuidador", status_code=303)
        else:
            return RedirectResponse("/", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao processar login")
        return RedirectResponse("/login", status_code=303)
```

#### 3. Melhorar logout

```python
@router.get("/logout")
async def logout(request: Request):
    usuario = obter_usuario_logado(request)
    email = usuario.email if usuario else "Usuário"

    destruir_sessao(request)
    informar_sucesso(request, "Logout realizado com sucesso!")

    return RedirectResponse("/login", status_code=303)
```

#### 4. Implementar recuperação de senha funcional

**Substituir as rotas existentes:**

```python
@router.post("/redefinicao_senha")
async def post_redefinicao_senha(request: Request, email: str = Form(...)):
    ip = obter_ip(request)

    # Rate limiting
    if not esqueci_senha_limiter.verificar(ip):
        tempo_restante = esqueci_senha_limiter.tempo_ate_liberar(ip)
        minutos = tempo_restante // 60
        informar_erro(request, f"Muitas solicitações. Aguarde {minutos} minuto(s).")
        return RedirectResponse("/redefinicao_senha", status_code=303)

    try:
        # Buscar usuário
        usuario = usuario_repo.obter_por_email(email.strip().lower())

        if usuario:
            from util.security import gerar_token_redefinicao, obter_data_expiracao_token

            # Gerar token
            token = gerar_token_redefinicao()
            data_expiracao = obter_data_expiracao_token(horas=1)

            # Salvar token no banco
            usuario_repo.atualizar_token(usuario.email, token, data_expiracao)

            # Enviar email
            sucesso, mensagem = email_service.enviar_recuperacao_senha(
                para_email=usuario.email,
                para_nome=usuario.nome,
                token=token
            )

        # Sempre a mesma mensagem (segurança)
        informar_sucesso(
            request,
            "Se o email existir, você receberá instruções para redefinir sua senha."
        )
        return RedirectResponse("/login", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao processar solicitação")
        return RedirectResponse("/redefinicao_senha", status_code=303)


@router.get("/confirmar_redefinir_senha", response_class=HTMLResponse)
async def get_confirmar_redefinir_senha(request: Request, token: str):
    # Buscar usuário pelo token
    usuario = usuario_repo.obter_por_token(token)

    if not usuario or not usuario.data_token:
        informar_erro(request, "Token inválido ou expirado")
        return RedirectResponse("/redefinicao_senha", status_code=303)

    # Verificar se token expirou
    try:
        from datetime import datetime
        data_token = datetime.fromisoformat(usuario.data_token)
        if datetime.now() > data_token:
            informar_erro(request, "Token expirado. Solicite uma nova recuperação.")
            return RedirectResponse("/redefinicao_senha", status_code=303)
    except:
        informar_erro(request, "Token inválido")
        return RedirectResponse("/redefinicao_senha", status_code=303)

    return templates.TemplateResponse(
        "confirmar_redefinir_senha.html",
        {"request": request, "token": token}
    )


@router.post("/confirmar_redefinir_senha")
async def post_confirmar_redefinir_senha(
    request: Request,
    token: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...)
):
    try:
        from util.security import validar_forca_senha, criar_hash_senha
        from datetime import datetime

        # Verificar se senhas coincidem
        if senha != confirmar_senha:
            informar_erro(request, "As senhas não coincidem")
            return RedirectResponse(
                f"/confirmar_redefinir_senha?token={token}",
                status_code=303
            )

        # Validar força da senha
        valida, mensagem = validar_forca_senha(senha)
        if not valida:
            informar_erro(request, mensagem)
            return RedirectResponse(
                f"/confirmar_redefinir_senha?token={token}",
                status_code=303
            )

        # Buscar usuário pelo token
        usuario = usuario_repo.obter_por_token(token)

        if not usuario or not usuario.data_token:
            informar_erro(request, "Token inválido ou expirado")
            return RedirectResponse("/redefinicao_senha", status_code=303)

        # Verificar se token expirou
        data_token = datetime.fromisoformat(usuario.data_token)
        if datetime.now() > data_token:
            informar_erro(request, "Token expirado")
            return RedirectResponse("/redefinicao_senha", status_code=303)

        # Atualizar senha
        senha_hash = criar_hash_senha(senha)
        usuario_repo.atualizar_senha(usuario.id, senha_hash)
        usuario_repo.limpar_token(usuario.id)

        informar_sucesso(request, "Senha redefinida com sucesso!")
        return RedirectResponse("/login", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao redefinir senha")
        return RedirectResponse(f"/confirmar_redefinir_senha?token={token}", status_code=303)
```

#### 5. Melhorar rotas de cadastro (opcional)

Adicione rate limiting e flash messages nas rotas de cadastro:

```python
@router.post("/cadastro_cuidador")
async def post_cadastro_cuidador(request: Request, ...):
    ip = obter_ip(request)

    # Rate limiting
    if not cadastro_limiter.verificar(ip):
        tempo_restante = cadastro_limiter.tempo_ate_liberar(ip)
        minutos = tempo_restante // 60
        informar_erro(request, f"Muitas tentativas. Aguarde {minutos} minuto(s).")
        return RedirectResponse("/cadastro_cuidador", status_code=303)

    try:
        # ... código de cadastro existente ...

        # Após cadastro bem-sucedido:
        email_service.enviar_boas_vindas(
            para_email=usuario.email,
            para_nome=usuario.nome,
            perfil="cuidador"
        )

        informar_sucesso(request, "Cadastro realizado com sucesso!")
        return RedirectResponse("/login", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao cadastrar. Tente novamente.")
        return RedirectResponse("/cadastro_cuidador", status_code=303)
```

#### 6. Atualizar DTOs com validação forte

Em `dtos/cadastro_cuidador_dto.py` e `dtos/cadastro_contratante_dto.py`:

```python
from util.validacoes_dto import validar_senha_forte

# Na classe do DTO:
@field_validator("senha")
def validar_senha_usuario(cls, valor):
    validar_senha_forte(valor)  # Agora usa validação completa!
    return valor
```

---

### Opção 2: Usar auth_routes_melhorado.py (Mais Rápido)

Se você quiser usar as rotas melhoradas diretamente:

#### 1. No `main.py`, adicione:

```python
from routes.auth_routes_melhorado import router as auth_router

app.include_router(auth_router)
```

#### 2. Ajuste os templates

Os templates precisam chamar `/auth/login` ao invés de `/login`:

```html
<!-- Em login.html -->
<form action="/auth/login" method="POST">
```

#### 3. Atualize redirecionamentos

Em todo o código, ajuste:
- `/login` → `/auth/login`
- `/logout` → `/auth/logout`
- `/redefinicao_senha` → `/auth/redefinicao_senha`

---

## 🎨 Atualizar Templates HTML

### 1. Adicionar suporte a flash messages

Em todos os templates (login.html, cadastro.html, etc.), adicione no topo:

```html
{% from "macros/flash_messages.html" import render_flash_messages %}

{{ render_flash_messages(request) }}
```

### 2. Criar macro de flash messages

Crie `templates/macros/flash_messages.html`:

```html
{% macro render_flash_messages(request) %}
    {% set mensagens = obter_mensagens(request) %}
    {% if mensagens %}
        <div class="flash-messages">
            {% for msg in mensagens %}
                <div class="alert alert-{{ msg.tipo }}">
                    {{ msg.texto }}
                </div>
            {% endfor %}
        </div>
    {% endif %}
{% endmacro %}
```

### 3. CSS para flash messages

Em `static/css/style.css`:

```css
.flash-messages {
    margin: 20px 0;
}

.alert {
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid transparent;
}

.alert-sucesso {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
}

.alert-erro {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
}

.alert-aviso {
    background-color: #fff3cd;
    border-color: #ffeeba;
    color: #856404;
}

.alert-info {
    background-color: #d1ecf1;
    border-color: #bee5eb;
    color: #0c5460;
}
```

---

## 📧 Configurar Resend.com (Obrigatório para recuperação de senha)

### 1. Criar conta no Resend.com

1. Acesse: https://resend.com/signup
2. Crie conta gratuita (100 emails/dia grátis)
3. Verifique seu email

### 2. Obter API Key

1. Acesse: https://resend.com/api-keys
2. Clique em "Create API Key"
3. Nome: "Hestia Production"
4. Copie a chave gerada

### 3. Configurar domínio (opcional, para produção)

1. Acesse: https://resend.com/domains
2. Adicione seu domínio
3. Configure registros DNS
4. Aguarde verificação

Para desenvolvimento, você pode usar o domínio padrão do Resend.

### 4. Atualizar .env

```env
RESEND_API_KEY=re_sua_chave_aqui
RESEND_FROM_EMAIL=noreply@seudominio.com
RESEND_FROM_NAME=Hestia
```

---

## 🧪 Testes

### 1. Testar SECRET_KEY

```bash
python3 -c "from util.config import SECRET_KEY; print('✅ SECRET_KEY:', SECRET_KEY[:10] + '...')"
```

### 2. Testar rate limiting

Tente fazer login 6 vezes seguidas com senha errada. Na 6ª tentativa deve bloquear.

### 3. Testar validação de senha forte

Tente cadastrar com senhas fracas:
- "123456" → deve rejeitar (menos de 8 chars)
- "12345678" → deve rejeitar (sem maiúscula)
- "Teste123" → deve rejeitar (sem caractere especial)
- "Teste@123" → deve aceitar ✅

### 4. Testar recuperação de senha

1. Acesse `/redefinicao_senha`
2. Digite um email cadastrado
3. Verifique se recebeu o email
4. Clique no link do email
5. Defina nova senha
6. Faça login com a nova senha

---

## 📝 Checklist de Implementação

- [ ] Instalar dependências: `pip install -r requirements.txt`
- [ ] Verificar `.env` criado com SECRET_KEY forte
- [ ] Testar se servidor inicia sem erros
- [ ] Integrar flash messages nos templates
- [ ] Atualizar rotas de login/logout
- [ ] Implementar recuperação de senha
- [ ] Configurar Resend.com (se quiser emails)
- [ ] Atualizar DTOs com validação forte
- [ ] Adicionar rate limiting no cadastro
- [ ] Testar todo o fluxo de autenticação

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'resend'"

```bash
pip install resend
```

### Erro: "ModuleNotFoundError: No module named 'dotenv'"

```bash
pip install python-dotenv
```

### Secret key aparece como temporária no console

Edite o `.env` e adicione:
```env
SECRET_KEY=sua_chave_secreta_forte_aqui
```

### Emails não estão sendo enviados

1. Verifique se `RESEND_API_KEY` está no `.env`
2. Teste a chave: `python3 -c "from util.email_service import email_service; print(email_service.api_key)"`
3. Verifique logs do console

### Rate limiter não funciona

Se você reiniciar o servidor, o rate limiter zera (memória). Para produção, use Redis.

---

## 📚 Próximos Passos

Após implementar as melhorias básicas, considere:

1. **Confirmação de email no cadastro**
2. **2FA (autenticação de dois fatores)**
3. **OAuth com Google/Facebook**
4. **Auditoria de login** (registrar todas as tentativas no banco)
5. **Bloqueio permanente de conta** (após N tentativas falhas)
6. **Rate limiting com Redis** (para produção em escala)
7. **Testes automatizados**

---

## 🆘 Suporte

Se tiver dúvidas ou problemas:

1. Verifique os logs no console
2. Consulte este guia novamente
3. Leia os comentários nos arquivos criados
4. Revise o `auth_analysis.md` para entender o sistema atual

---

**Data de criação**: 2025-10-20
**Versão**: 1.0.0
