# Correção dos Testes de Integração

## Problema Encontrado

Os 12 testes estavam falhando devido a **incompatibilidade de versões** entre:
- `bcrypt 5.0.0` (instalado no .venv)
- `passlib 1.7.4` (biblioteca de hash de senhas)

**Erro**: `ValueError: password cannot be longer than 72 bytes`

## Causa Raiz

O `passlib 1.7.4` foi lançado em 2020 e não é compatível com `bcrypt >= 4.0.0`. Quando tentava fazer hash das senhas, o bcrypt falhava devido a mudanças na API interna.

## Soluções Aplicadas

### 1. Proteção no Código (util/security.py)
Adicionada proteção para truncar senhas maiores que 72 bytes (limite do bcrypt):

```python
def criar_hash_senha(senha: str) -> str:
    # Bcrypt tem limite de 72 bytes - trunca se necessário
    if len(senha.encode('utf-8')) > 72:
        senha = senha.encode('utf-8')[:72].decode('utf-8', errors='ignore')

    return pwd_context.hash(senha)
```

### 2. Downgrade do bcrypt
Instalada versão compatível: `bcrypt 3.2.2`

```bash
.venv/bin/pip install 'bcrypt<4.0.0' --force-reinstall
```

### 3. Fixação no requirements.txt
Adicionada restrição de versão:

```
bcrypt<4.0.0  # Compatibilidade com passlib 1.7.4
```

## Resultado Final

✅ **26 testes passando** (100% de sucesso)

```
======================== 26 passed, 19 warnings in 6.74s =========================
```

### Testes Inclusos

- **6 testes de Login**
  - Login de cuidador e contratante com sucesso
  - Validação de credenciais inválidas
  - Teste de logout

- **9 testes de Cadastro de Cuidador**
  - Cadastro com sucesso
  - Validação de hash de senha
  - Detecção de emails e CPFs duplicados
  - Validação de dados inválidos

- **9 testes de Cadastro de Contratante**
  - Mesmas validações do cuidador

- **2 testes de Fluxo Completo**
  - Cadastro → Login → Verificação de sessão

## Como Rodar os Testes

### No Terminal
```bash
python -m pytest tests/test_auth_integration.py -v
```

### No VSCode
1. Recarregue a janela: `Cmd+Shift+P` → "Reload Window"
2. No painel de testes, clique em "Refresh Tests" (🔄)
3. Execute os testes

## Importante

Se reinstalar as dependências, sempre use:
```bash
pip install -r requirements.txt
```

Isso garantirá que o `bcrypt` seja instalado na versão correta (< 4.0.0).
