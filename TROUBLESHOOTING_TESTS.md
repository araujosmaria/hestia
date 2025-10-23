# Troubleshooting - Testes no VSCode

## Problema
Testes passam no terminal mas falham no VSCode.

## Soluções

### 1. Limpar Cache do Python
```bash
# No terminal, execute:
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

### 2. Recarregar Janela do VSCode
1. Pressione `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux)
2. Digite "Reload Window"
3. Pressione Enter

### 3. Verificar Interpretador Python
1. Pressione `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux)
2. Digite "Python: Select Interpreter"
3. Selecione o mesmo interpretador usado no terminal
4. Execute no terminal: `which python3` e compare

### 4. Reconfigurar Python Testing no VSCode
1. Abra `.vscode/settings.json`
2. Verifique se tem:
```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

### 5. Limpar Discovery Cache do VSCode
1. Feche o VSCode
2. Delete a pasta: `rm -rf .vscode/.pytest_cache`
3. Reabra o VSCode
4. No painel de testes, clique em "Refresh Tests"

### 6. Rodar Testes pelo Terminal Integrado do VSCode
1. Abra o terminal integrado no VSCode (Ctrl+`)
2. Execute: `python -m pytest tests/test_auth_integration.py -v`
3. Compare com os resultados do painel de testes

### 7. Verificar PYTHONPATH
Execute no terminal integrado do VSCode:
```bash
python -c "import sys; print('\n'.join(sys.path))"
```

Compare com o terminal normal.

## Comando de Verificação Rápida

Execute este comando para verificar se os testes funcionam:
```bash
python -m pytest tests/test_auth_integration.py -v --tb=short
```

**Resultado esperado:** `26 passed`

## Se Ainda Não Funcionar

Tente rodar os testes diretamente pelo terminal integrado do VSCode em vez do painel de testes:

```bash
# Terminal integrado do VSCode
python -m pytest tests/test_auth_integration.py -v
```

## Verificação de Ambiente

Execute este script de diagnóstico:
```bash
python3 << 'EOF'
import sys
import os

print("=== DIAGNÓSTICO ===")
print(f"Python: {sys.executable}")
print(f"Versão: {sys.version}")
print(f"Diretório: {os.getcwd()}")
print(f"TEST_DATABASE_PATH: {os.environ.get('TEST_DATABASE_PATH', 'NÃO CONFIGURADO')}")

# Tenta importar pytest
try:
    import pytest
    print(f"Pytest: {pytest.__version__}")
except:
    print("Pytest: NÃO INSTALADO")

# Verifica se consegue importar o projeto
sys.path.insert(0, os.getcwd())
try:
    from data.usuario import usuario_repo
    print("Import do projeto: OK")
except Exception as e:
    print(f"Import do projeto: ERRO - {e}")
EOF
```

## Contato

Se o problema persistir, execute o script de diagnóstico acima e compartilhe a saída.
