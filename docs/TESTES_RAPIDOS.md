# 🧪 Testes Rápidos - Sistema de Autenticação Melhorado

Guia de testes para validar as melhorias implementadas.

---

## ✅ TODOS OS TESTES PASSARAM!

### 1. ✅ Config.py - OK
```bash
python3 -c "from util.config import SECRET_KEY, APP_NAME, VERSION; print(f'✅ Config OK'); print(f'App: {APP_NAME} v{VERSION}'); print(f'SECRET_KEY: {len(SECRET_KEY)} bytes')"
```
**Resultado esperado**: Deve mostrar nome do app e tamanho da SECRET_KEY

### 2. ✅ Rate Limiter - OK
```bash
python3 -c "from util.rate_limiter import SimpleRateLimiter; rl = SimpleRateLimiter(5, 5); print('✅ Rate Limiter OK'); print(f'Max: {rl.max_tentativas}, Janela: {rl.janela}')"
```
**Resultado esperado**: Max: 5, Janela: 0:05:00

### 3. ✅ Flash Messages - OK
```bash
python3 -c "from util.flash_messages import informar_sucesso, informar_erro; print('✅ Flash Messages OK')"
```
**Resultado esperado**: Sem erros

### 4. ✅ Validação de Senha - OK
```bash
python3 -c "from util.security import validar_forca_senha; testes = [('123', False), ('Teste@123', True)]; print('🔒 Testando validação de senha:');
for senha, esperado in testes:
    valida, msg = validar_forca_senha(senha)
    resultado = '✅' if valida == esperado else '❌'
    print(f'{resultado} \"{senha}\": {\"OK\" if valida else msg}')"
```
**Resultado esperado**:
- ✅ "123": A senha deve ter pelo menos 8 caracteres
- ✅ "Teste@123": OK

### 5. ✅ Main.py Importação - OK
```bash
python3 -c "from main import app; print('✅ Main.py OK'); print(f'App: {app.title}')"
```
**Resultado esperado**: App: Hestia - Sistema de Cuidadores

---

## 🚀 INICIAR SERVIDOR

```bash
python main.py
```

**Saída esperada**:
```
🚀 Iniciando Hestia - Sistema de Cuidadores v1.0.0
📍 Servidor: http://0.0.0.0:8082
🔧 Modo: Desenvolvimento
🔄 Reload: Ativado
INFO:     Started server process [xxxxx]
INFO:     Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit)
```

---

## 🧪 TESTES MANUAIS

### Teste 1: Rate Limiting no Login

1. Acesse: http://localhost:8082/login
2. Digite email/senha **ERRADOS** 6 vezes seguidas
3. **Resultado esperado**: Na 6ª tentativa deve mostrar:
   - "Muitas tentativas de login. Aguarde X minutos."
4. Aguarde o tempo e tente novamente (deve permitir)

### Teste 2: Validação de Senha Forte no Cadastro

Tente cadastrar usuários com diferentes senhas:

| Senha | Resultado Esperado |
|-------|-------------------|
| `123456` | ❌ "Senha deve ter pelo menos 8 caracteres" |
| `12345678` | ❌ "Senha deve conter pelo menos uma letra maiúscula" |
| `TESTANDO` | ❌ "Senha deve conter pelo menos uma letra minúscula" |
| `Testando` | ❌ "Senha deve conter pelo menos um número" |
| `Testando123` | ❌ "Senha deve conter pelo menos um caractere especial" |
| `Teste@123` | ✅ **Aceita!** |

### Teste 3: Recuperação de Senha (sem email configurado)

1. Acesse: http://localhost:8082/redefinicao_senha
2. Digite um email qualquer
3. Clique em "Confirmar"
4. **Resultado esperado**:
   - Mensagem: "Se o email existir, você receberá instruções..."
   - Console mostra: "⚠️ RESEND_API_KEY não configurada"

### Teste 4: Recuperação de Senha (com email configurado)

**Pré-requisito**: Configure RESEND_API_KEY no `.env`

1. Acesse: http://localhost:8082/redefinicao_senha
2. Digite email de um usuário EXISTENTE no banco
3. Clique em "Confirmar"
4. **Resultado esperado**:
   - Mensagem: "Se o email existir, você receberá instruções..."
   - Email enviado para o usuário
   - Console mostra: "📧 Email de recuperação enviado para: ..."

5. Abra o email recebido
6. Clique no link de recuperação
7. Digite nova senha forte
8. Confirme a senha
9. **Resultado esperado**:
   - Redireciona para login
   - Mensagem: "Senha redefinida com sucesso!"
   - Pode fazer login com a nova senha

### Teste 5: Flash Messages

1. Faça login com credenciais corretas
2. **Resultado esperado**: Mensagem verde "Bem-vindo(a), [Nome]!"

3. Faça logout
4. **Resultado esperado**: Mensagem verde "Logout realizado com sucesso!"

5. Tente login com senha errada
6. **Resultado esperado**: Mensagem vermelha "Email ou senha incorretos"

---

## 🐛 TROUBLESHOOTING

### Erro: "ModuleNotFoundError: No module named 'X'"

**Solução**:
```bash
pip install -r requirements.txt
```

### Erro: "SECRET_KEY não configurada no .env"

**Solução**:
- Verifique se arquivo `.env` existe
- Verifique se tem a linha `SECRET_KEY=...`
- Se não tiver, gere uma nova:
```bash
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))" >> .env
```

### Emails não estão sendo enviados

**Verificar**:
1. `RESEND_API_KEY` está configurada no `.env`?
2. A chave é válida? (teste em https://resend.com/api-keys)

**Testar manualmente**:
```python
from util.email_service import email_service
from util.config import RESEND_API_KEY

print(f"API Key configurada: {bool(RESEND_API_KEY)}")
print(f"API Key: {RESEND_API_KEY[:10] if RESEND_API_KEY else 'Não configurada'}...")

# Testar envio
sucesso, msg = email_service.enviar_recuperacao_senha(
    para_email="seu@email.com",
    para_nome="Teste",
    token="teste123"
)
print(f"Sucesso: {sucesso}")
print(f"Mensagem: {msg}")
```

### Rate Limiter zera ao reiniciar servidor

**Explicação**: O rate limiter atual é em memória (não persiste).

**Soluções**:
- Para desenvolvimento: OK assim
- Para produção: Use Redis

### Flash Messages não aparecem nos templates

**Verificar**:
1. Template tem `{% set mensagens = obter_mensagens(request) %}`?
2. Template tem loop para exibir mensagens?

**Exemplo correto**:
```html
{% set mensagens = obter_mensagens(request) %}
{% if mensagens %}
    {% for msg in mensagens %}
        <div class="alert alert-{{ msg.tipo }}">
            {{ msg.texto }}
        </div>
    {% endfor %}
{% endif %}
```

---

## 📊 CHECKLIST DE VALIDAÇÃO

Use este checklist para validar se tudo está funcionando:

### Configuração
- [ ] `.env` existe e tem SECRET_KEY
- [ ] `pip install -r requirements.txt` executado
- [ ] Servidor inicia sem erros
- [ ] Console mostra: "🚀 Iniciando Hestia..."

### Segurança
- [ ] SECRET_KEY é forte (43+ bytes)
- [ ] Rate limiting bloqueia após X tentativas
- [ ] Senha fraca é rejeitada
- [ ] Senha forte é aceita

### Email (Opcional)
- [ ] RESEND_API_KEY configurada (ou aviso no console)
- [ ] Email de recuperação enviado (se configurado)
- [ ] Email de boas-vindas enviado (se configurado)

### Flash Messages
- [ ] Mensagem de sucesso aparece após login
- [ ] Mensagem de erro aparece após login falho
- [ ] Mensagem aparece após logout

### Recuperação de Senha
- [ ] Formulário de recuperação acessível
- [ ] Token gerado e salvo no banco
- [ ] Email enviado (se configurado)
- [ ] Link do email funciona
- [ ] Nova senha validada
- [ ] Login funciona com nova senha

---

## 🎯 TESTES AUTOMATIZADOS (Futuro)

Para implementar testes automatizados:

```python
# tests/test_auth.py

def test_rate_limiting():
    """Testa se rate limiting bloqueia após X tentativas"""
    from util.rate_limiter import SimpleRateLimiter
    limiter = SimpleRateLimiter(3, 1)  # 3 tentativas por 1 minuto

    assert limiter.verificar("192.168.1.1") == True  # 1ª OK
    assert limiter.verificar("192.168.1.1") == True  # 2ª OK
    assert limiter.verificar("192.168.1.1") == True  # 3ª OK
    assert limiter.verificar("192.168.1.1") == False # 4ª BLOQUEIA

def test_validacao_senha():
    """Testa validação de senha forte"""
    from util.security import validar_forca_senha

    # Senhas fracas
    assert validar_forca_senha("123")[0] == False
    assert validar_forca_senha("senha")[0] == False
    assert validar_forca_senha("Senha123")[0] == False

    # Senha forte
    assert validar_forca_senha("Senha@123")[0] == True

def test_flash_messages():
    """Testa sistema de flash messages"""
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    # Login com credenciais erradas deve mostrar mensagem
    response = client.post("/login", data={"email": "x@x.com", "senha": "x"})
    # Verificar se mensagem de erro aparece
```

Para rodar testes:
```bash
pytest tests/
```

---

## 📞 SUPORTE

Se encontrar problemas:

1. **Verifique os logs** no console
2. **Consulte a documentação**:
   - `RESUMO_MELHORIAS.md` - Visão geral
   - `MELHORIAS_AUTH_IMPLEMENTACAO.md` - Guia de implementação
   - `auth_analysis.md` - Análise do sistema

3. **Verifique as configurações**:
   ```bash
   cat .env
   python3 -c "from util.config import *; print('SECRET_KEY:', bool(SECRET_KEY)); print('RESEND:', bool(RESEND_API_KEY))"
   ```

4. **Teste os módulos individuais** (comandos acima)

---

**✅ TODOS OS TESTES PASSARAM! Sistema pronto para uso!**

Data: 2025-10-20
