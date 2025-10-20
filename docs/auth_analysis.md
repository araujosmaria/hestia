# Análise do Sistema de Autenticação Atual - Projeto Hestia

## 1. RESUMO EXECUTIVO

**Tipo de Autenticação**: Baseado em Sessões (SessionMiddleware)
**Bibliotecas**: passlib[bcrypt], FastAPI, Jinja2
**Banco de Dados**: SQLite
**Status**: Parcialmente implementado

## 2. PERFIS EXISTENTES

```python
1. "admin"         - Administrador do sistema
2. "cuidador"      - Profissional cuidador
3. "contratante"   - Cliente que contrata serviços
```

## 3. CAMPOS DO MODELO USUARIO

```python
- id_usuario: INTEGER (PK)
- nome: TEXT
- dataNascimento: TEXT
- email: TEXT (login)
- telefone: TEXT
- cpf: TEXT (UNIQUE)
- senha: TEXT (bcrypt hash)
- perfil: TEXT (admin/cuidador/contratante)
- cep, logradouro, numero, complemento, bairro, cidade, estado
- ativo: INTEGER (0/1)
- foto: TEXT (caminho)
- token_redefinicao: TEXT
- data_token: TIMESTAMP
- data_cadastro: TIMESTAMP
```

### Extensões por Perfil:

**Cuidador**:
- experiencia, escolaridade, apresentacao, cursos, inicio_profissional, valorHora

**Contratante**:
- parentesco_paciente

## 4. COMPONENTES EXISTENTES

### ✅ Implementados e Funcionais
- [x] Login/Logout
- [x] Cadastro (cuidador/contratante)
- [x] Hash de senhas (bcrypt)
- [x] Sessões (SessionMiddleware)
- [x] Decorator de proteção (@requer_autenticacao)
- [x] Validação de email/CPF/telefone
- [x] Templates HTML (login, cadastro)
- [x] Admin padrão (admin@admin.com / admin123)

### ⚠️ Parcialmente Implementados
- [~] Recuperação de senha (rotas existem, mas sem envio de email)
- [~] Validação de senha forte (apenas min 6 chars)
- [~] Flash messages (código preparado, não ativado)
- [~] Logger (código preparado, não ativado)

### ❌ Não Implementados
- [ ] Rate limiting
- [ ] Envio de email
- [ ] Confirmação de email no cadastro
- [ ] 2FA
- [ ] OAuth/Social login
- [ ] Bloqueio de conta
- [ ] Auditoria de tentativas de login

## 5. PROBLEMAS CRÍTICOS IDENTIFICADOS

### 🔴 CRÍTICO
1. **Secret key fraca**: `"uma_chave_secreta_aleatoria"` hardcoded
2. **Sem rate limiting**: vulnerável a ataques de força bruta

### 🟠 ALTO
3. **Recuperação de senha não funcional**: sem envio de email
4. **Senha fraca permitida**: apenas 6 caracteres mínimo
5. **Sem confirmação de email**: qualquer email pode ser usado

### 🟡 MÉDIO
6. **Sem bloqueio de conta**: tentativas ilimitadas
7. **Sem auditoria de login**: não registra tentativas falhas

## 6. ARQUIVOS ENVOLVIDOS

```
util/
  ├── auth_decorator.py      # Decorator + gerenciamento de sessão
  ├── security.py            # Hash + tokens
  ├── validacoes_dto.py      # Validadores
  └── criar_admin.py         # Admin padrão

routes/
  ├── public_routes.py       # Login, logout, cadastro
  └── perfil_routes.py       # Upload de foto

dtos/
  ├── login_dto.py
  ├── cadastro_cuidador_dto.py
  └── cadastro_contratante_dto.py

data/
  ├── usuario/               # Model, Repo, SQL base
  ├── cliente/               # Extensão para contratante
  ├── cuidador/              # Extensão para cuidador
  └── administrador/         # Model de admin

templates/
  ├── login.html
  ├── cadastro*.html
  └── redefinicao_senha.html
```

## 7. RECOMENDAÇÃO

### Opção 1: Melhorar Sistema Existente (RECOMENDADO)
- ✅ Manter estrutura atual (funciona bem)
- ✅ Corrigir problemas críticos
- ✅ Adicionar funcionalidades faltantes
- ✅ Menos invasivo
- ✅ Aproveita código existente

### Opção 2: Substituir Completamente
- ⚠️ Reescrever do zero
- ⚠️ Perder customizações (cuidador/contratante)
- ⚠️ Mais trabalhoso
- ⚠️ Risco de quebrar funcionalidades

## 8. PLANO DE AÇÃO PROPOSTO

### Fase 1: Correções Críticas
1. Corrigir SECRET_KEY (usar variável de ambiente)
2. Implementar rate limiting
3. Melhorar validação de senha (8 chars + maiúscula + número + especial)

### Fase 2: Funcionalidades Faltantes
4. Implementar envio de email (Resend.com)
5. Completar recuperação de senha
6. Ativar flash messages
7. Ativar logger

### Fase 3: Melhorias (Opcional)
8. Confirmação de email no cadastro
9. Bloqueio de conta após N tentativas
10. Auditoria de login
11. 2FA (opcional)

---

**Gerado em**: 2025-10-20
**Status**: Aguardando confirmação do usuário
