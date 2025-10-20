# Sistema de Notificações Toast - Hestia

Sistema completo de notificações toast usando Bootstrap 5, integrado com flash messages do FastAPI para feedback visual ao usuário.

## 📋 Índice

- [Características](#características)
- [Arquivos do Sistema](#arquivos-do-sistema)
- [Como Usar](#como-usar)
  - [No Backend (Python)](#no-backend-python)
  - [No Frontend (JavaScript)](#no-frontend-javascript)
- [Tipos de Mensagens](#tipos-de-mensagens)
- [Customização](#customização)
- [Exemplos Práticos](#exemplos-práticos)
- [Rota de Teste](#rota-de-teste)
- [Troubleshooting](#troubleshooting)

## ✨ Características

- ✅ **Zero dependências extras** - Usa apenas Bootstrap 5 (já presente no projeto)
- ✅ **Integração nativa** - Funciona com FastAPI sessions
- ✅ **4 tipos de mensagens** - Sucesso, Erro, Aviso, Info
- ✅ **Auto-dismiss configurável** - Padrão: 5 segundos
- ✅ **Ícones Bootstrap** - Ícones visuais para cada tipo
- ✅ **Posicionamento flexível** - Padrão: inferior direito
- ✅ **Remoção automática** - Limpa o DOM após esconder
- ✅ **API JavaScript** - Uso programático disponível
- ✅ **Responsivo** - Funciona em mobile e desktop
- ✅ **Acessível** - Suporte ARIA completo
- ✅ **Animações suaves** - Entrada e saída animadas

## 📁 Arquivos do Sistema

```
hestia/
├── util/
│   └── flash_messages.py          # Funções backend para mensagens
├── static/
│   ├── js/
│   │   └── toasts.js              # JavaScript do sistema de toasts
│   └── css/
│       └── toasts.css             # Estilos customizados
├── templates/
│   ├── base.html                  # Template base atualizado
│   ├── base_simples.html          # Template simples atualizado
│   ├── base_hcontratante.html     # Template home contratante
│   ├── base_login.html            # Template login atualizado
│   ├── base_cadastro.html         # Template cadastro atualizado
│   └── base_senha.html            # Template senha atualizado
└── routes/
    └── teste_toast_routes.py      # Rota de teste (remover em produção)
```

## 🚀 Como Usar

### No Backend (Python)

Em qualquer rota FastAPI, importe as funções de flash messages:

```python
from fastapi import Request
from fastapi.responses import RedirectResponse
from util.flash_messages import (
    informar_sucesso,
    informar_erro,
    informar_aviso,
    informar_info
)

@app.post("/exemplo")
async def exemplo(request: Request):
    # Mensagem de sucesso (verde)
    informar_sucesso(request, "Operação realizada com sucesso!")

    # Mensagem de erro (vermelho)
    informar_erro(request, "Erro ao processar dados. Tente novamente.")

    # Mensagem de aviso (amarelo)
    informar_aviso(request, "Atenção: Esta ação não pode ser desfeita!")

    # Mensagem informativa (azul)
    informar_info(request, "Dados carregados: 150 registros encontrados.")

    # IMPORTANTE: Use redirect após mensagens flash (padrão PRG)
    return RedirectResponse("/destino", status_code=303)
```

#### Padrão POST-REDIRECT-GET (PRG)

**Sempre use redirect após adicionar mensagens flash:**

```python
@app.post("/criar")
async def criar(request: Request, nome: str = Form(...)):
    try:
        # Lógica de criação
        criar_item(nome)

        # Mensagem de sucesso
        informar_sucesso(request, f"Item '{nome}' criado com sucesso!")

        # Redirecionar (PRG pattern)
        return RedirectResponse("/lista", status_code=303)

    except Exception as e:
        # Mensagem de erro
        informar_erro(request, f"Erro ao criar item: {str(e)}")

        # Redirecionar de volta
        return RedirectResponse("/criar", status_code=303)
```

### No Frontend (JavaScript)

Para exibir toasts programaticamente via JavaScript:

```javascript
// Sucesso
window.exibirToast('Upload concluído!', 'success');

// Erro
window.exibirToast('Conexão perdida', 'danger');

// Aviso
window.exibirToast('Sessão expira em 5 minutos', 'warning');

// Info
window.exibirToast('Nova versão disponível', 'info');

// Com tempo customizado (10 segundos)
window.exibirToast('Mensagem importante', 'warning', 10000);
```

**Exemplo em evento:**

```html
<button onclick="salvar()">Salvar</button>

<script>
function salvar() {
    // Simular salvamento
    setTimeout(() => {
        window.exibirToast('Dados salvos com sucesso!', 'success');
    }, 1000);
}
</script>
```

## 🎨 Tipos de Mensagens

| Tipo Backend | Tipo Frontend | Cor | Ícone | Uso |
|-------------|---------------|-----|-------|-----|
| `sucesso` | `success` | Verde | ✓ | Operações bem-sucedidas |
| `erro` | `danger` | Vermelho | ✗ | Erros e falhas |
| `aviso` | `warning` | Amarelo | ⚠ | Avisos importantes |
| `info` | `info` | Azul | ℹ | Informações gerais |

## 🎨 Customização

### Alterar Posicionamento

No template base, altere as classes do container:

```html
<!-- Inferior Direito (padrão) -->
<div id="toast-container" class="toast-container position-fixed bottom-0 end-0 p-4"></div>

<!-- Superior Direito -->
<div id="toast-container" class="toast-container position-fixed top-0 end-0 p-4"></div>

<!-- Inferior Esquerdo -->
<div id="toast-container" class="toast-container position-fixed bottom-0 start-0 p-4"></div>

<!-- Superior Esquerdo -->
<div id="toast-container" class="toast-container position-fixed top-0 start-0 p-4"></div>

<!-- Centro Superior -->
<div id="toast-container" class="toast-container position-fixed top-0 start-50 translate-middle-x p-4"></div>
```

### Alterar Tempo de Auto-Dismiss

**Globalmente** (em `static/js/toasts.js`):

```javascript
// Encontre a linha (aproximadamente linha 82)
const bsToast = new bootstrap.Toast(toastElement, {
    autohide: true,
    delay: 10000  // 10 segundos (padrão: 5000)
});
```

**Por toast individual** (JavaScript):

```javascript
window.exibirToast('Mensagem longa', 'info', 15000); // 15 segundos
```

### Desabilitar Auto-Dismiss

```javascript
const bsToast = new bootstrap.Toast(toastElement, {
    autohide: false  // Usuário precisa fechar manualmente
});
```

### Estilização Customizada

Edite `static/css/toasts.css`:

```css
/* Toast com sombra maior */
.toast {
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.25) !important;
}

/* Toast maior */
.toast {
    min-width: 300px;
    max-width: 400px;
}

/* Fonte maior */
.toast-body {
    font-size: 1rem;
}
```

## 💡 Exemplos Práticos

### Exemplo 1: CRUD Completo

```python
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso

@app.post("/produtos/criar")
async def criar_produto(request: Request, nome: str = Form(...), preco: float = Form(...)):
    try:
        produto = criar(nome, preco)
        informar_sucesso(request, f"Produto '{nome}' criado com sucesso!")
        return RedirectResponse("/produtos", status_code=303)
    except ValueError as e:
        informar_erro(request, str(e))
        return RedirectResponse("/produtos/criar", status_code=303)

@app.post("/produtos/{id}/atualizar")
async def atualizar_produto(request: Request, id: int, nome: str = Form(...)):
    try:
        atualizar(id, nome)
        informar_sucesso(request, "Produto atualizado!")
        return RedirectResponse("/produtos", status_code=303)
    except Exception as e:
        informar_erro(request, "Erro ao atualizar produto")
        return RedirectResponse(f"/produtos/{id}/editar", status_code=303)

@app.post("/produtos/{id}/excluir")
async def excluir_produto(request: Request, id: int):
    try:
        excluir(id)
        informar_aviso(request, "Produto excluído permanentemente")
        return RedirectResponse("/produtos", status_code=303)
    except Exception:
        informar_erro(request, "Não foi possível excluir o produto")
        return RedirectResponse("/produtos", status_code=303)
```

### Exemplo 2: Upload de Arquivo

```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload(request: Request, arquivo: UploadFile = File(...)):
    try:
        # Validar arquivo
        if arquivo.size > 5_000_000:
            informar_erro(request, "Arquivo muito grande (máx: 5MB)")
            return RedirectResponse("/upload", status_code=303)

        # Processar
        salvar_arquivo(arquivo)
        informar_sucesso(request, f"Arquivo '{arquivo.filename}' enviado com sucesso!")
        return RedirectResponse("/arquivos", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao fazer upload do arquivo")
        return RedirectResponse("/upload", status_code=303)
```

### Exemplo 3: Validação Múltipla

```python
@app.post("/configurar")
async def configurar(request: Request, email: str = Form(...), telefone: str = Form(...)):
    erros = []

    if not validar_email(email):
        erros.append("E-mail inválido")

    if not validar_telefone(telefone):
        erros.append("Telefone inválido")

    if erros:
        for erro in erros:
            informar_erro(request, erro)
        return RedirectResponse("/configurar", status_code=303)

    # Salvar
    salvar_config(email, telefone)
    informar_sucesso(request, "Configurações salvas!")
    return RedirectResponse("/configurar", status_code=303)
```

### Exemplo 4: Autenticação

```python
@app.post("/login")
async def login(request: Request, email: str = Form(...), senha: str = Form(...)):
    if autenticar(email, senha):
        informar_sucesso(request, f"Bem-vindo, {email}!")
        return RedirectResponse("/dashboard", status_code=303)
    else:
        informar_erro(request, "E-mail ou senha inválidos")
        return RedirectResponse("/login", status_code=303)
```

## 🧪 Rota de Teste

**Acesse:** `http://localhost:8000/teste/toast`

Esta rota demonstra:
- Mensagens do backend (4 tipos)
- Botões para testar JavaScript
- Console do navegador para testes
- Informações técnicas do sistema

**Para remover em produção:**

1. Delete o arquivo: `routes/teste_toast_routes.py`
2. Remova do `main.py`:
   ```python
   # Remover estas linhas:
   from routes import teste_toast_routes
   app.include_router(teste_toast_routes.router)
   ```

## 🔧 Troubleshooting

### Problema: Toasts não aparecem

**Checklist:**
- [ ] Bootstrap 5 JS carregado? (verifique console)
- [ ] Container `#toast-container` existe no HTML?
- [ ] Script `toasts.js` carregado?
- [ ] Mensagens no JSON? (inspecionar `#mensagens-data`)
- [ ] SessionMiddleware configurado no `main.py`?

**Debug no console do navegador:**
```javascript
console.log(document.getElementById('toast-container')); // Deve retornar elemento
console.log(typeof window.exibirToast); // Deve ser 'function'
console.log(typeof bootstrap); // Deve ser 'object'
```

### Problema: Toasts aparecem mas sem estilo

**Causa:** Bootstrap CSS não carregado

**Solução:** Adicione no `<head>` do template:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

### Problema: Ícones não aparecem

**Causa:** Bootstrap Icons não carregado

**Solução:** Adicione no `<head>` do template:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
```

### Problema: `bootstrap is not defined`

**Causa:** Bootstrap JS não carregado ou carregado depois de `toasts.js`

**Solução:** Garanta ordem correta no final do `<body>`:
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="/static/js/toasts.js"></script>
```

### Problema: Toasts aparecem sobrepostos ao footer

**Solução:** Ajustar `.toast-offset` no `static/css/toasts.css`:
```css
.toast-offset {
    margin-bottom: 80px; /* Aumentar valor */
}
```

## 📚 Referências

- [Bootstrap 5 Toasts](https://getbootstrap.com/docs/5.3/components/toasts/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [FastAPI Sessions](https://fastapi.tiangolo.com/tutorial/middleware/)
- [Padrão PRG](https://en.wikipedia.org/wiki/Post/Redirect/Get)

## 📝 Notas Importantes

1. **Sempre use redirect** após adicionar mensagens flash (padrão PRG)
2. **SessionMiddleware é obrigatório** para flash messages funcionarem
3. **Mensagens são consumidas** na primeira leitura (aparecem uma vez)
4. **Bootstrap 5 é obrigatório** - este sistema não funciona com Bootstrap 4
5. **Ordem dos scripts importa** - Bootstrap JS antes de `toasts.js`

## 🎯 Boas Práticas

- Use `informar_sucesso()` para operações bem-sucedidas
- Use `informar_erro()` para erros que o usuário precisa saber
- Use `informar_aviso()` para ações irreversíveis ou importantes
- Use `informar_info()` para feedback informativo geral
- Sempre redirecione após adicionar mensagens (padrão PRG)
- Evite mensagens muito longas (máximo 2-3 linhas)
- Seja específico nas mensagens de erro
- Use emojis com moderação (ou evite)

---

**Sistema implementado em:** 20/10/2025
**Versão Bootstrap:** 5.3.0
**Versão Bootstrap Icons:** 1.10.5
