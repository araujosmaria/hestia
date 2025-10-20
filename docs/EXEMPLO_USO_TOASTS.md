# Exemplo de Uso do Sistema de Toasts

Este documento mostra como integrar o sistema de toasts nas rotas existentes do projeto Hestia.

## Exemplo 1: Rota de Login (ANTES e DEPOIS)

### ❌ ANTES (sem toasts)

```python
@router.post("/login")
async def post_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    usuario = usuario_repo.obter_por_email(email)

    if not usuario or not verificar_senha(senha, usuario.senha):
        # Renderiza template com erro diretamente
        return templates.TemplateResponse("login.html", {
            "request": request,
            "erro": "Usuário ou senha incorretos"
        })

    # ... resto do código
    return RedirectResponse("/home", status_code=303)
```

**Problemas:**
- Erro exibido apenas como texto no template
- Pouco visível para o usuário
- Sem feedback visual consistente

### ✅ DEPOIS (com toasts)

```python
from util.flash_messages import informar_sucesso, informar_erro

@router.post("/login")
async def post_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    usuario = usuario_repo.obter_por_email(email)

    if not usuario or not verificar_senha(senha, usuario.senha):
        # Adiciona mensagem de erro via toast
        informar_erro(request, "E-mail ou senha incorretos. Tente novamente.")
        return RedirectResponse("/login", status_code=303)

    # Sucesso - criar sessão
    criar_sessao(request, usuario)
    informar_sucesso(request, f"Bem-vindo(a), {usuario.nome}!")

    # Redirecionar conforme perfil
    if usuario.perfil == "cuidador":
        return RedirectResponse("/cuidador/home_cuidador", status_code=303)
    elif usuario.perfil == "contratante":
        return RedirectResponse("/contratante/home_contratante", status_code=303)
    else:
        return RedirectResponse("/", status_code=303)
```

**Vantagens:**
- ✅ Feedback visual bonito e profissional
- ✅ Toast aparece no canto da tela (não intrusivo)
- ✅ Desaparece automaticamente após 5 segundos
- ✅ Consistente com resto do sistema

## Exemplo 2: Cadastro de Contratante

### ✅ Implementação com Toasts

```python
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso

@router.post("/cadastro/contratante")
async def post_cadastro_contratante(
    request: Request,
    nome: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    foto: UploadFile = File(None)
):
    try:
        # Validar CPF duplicado
        if cliente_repo.obter_por_cpf(cpf):
            informar_erro(request, "CPF já cadastrado no sistema")
            return RedirectResponse("/cadastro/contratante", status_code=303)

        # Validar e-mail duplicado
        if usuario_repo.obter_por_email(email):
            informar_erro(request, "E-mail já cadastrado. Use outro e-mail.")
            return RedirectResponse("/cadastro/contratante", status_code=303)

        # Validar senha (mínimo 8 caracteres)
        if len(senha) < 8:
            informar_aviso(request, "A senha deve ter no mínimo 8 caracteres")
            return RedirectResponse("/cadastro/contratante", status_code=303)

        # Processar foto se enviada
        nome_foto = None
        if foto and foto.filename:
            nome_foto = salvar_foto(foto)

        # Criar usuário
        senha_hash = criar_hash_senha(senha)
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha_hash,
            perfil="contratante"
        )
        usuario_id = inserir_usuario(usuario)

        # Criar cliente
        cliente = Cliente(
            cpf=cpf,
            telefone=telefone,
            foto=nome_foto,
            usuario_id=usuario_id
        )
        inserir_cliente(cliente)

        # Sucesso!
        informar_sucesso(request, f"Cadastro realizado com sucesso! Bem-vindo, {nome}!")
        return RedirectResponse("/login", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao realizar cadastro. Tente novamente.")
        return RedirectResponse("/cadastro/contratante", status_code=303)
```

## Exemplo 3: Upload de Foto de Perfil

```python
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso

@router.post("/perfil/atualizar-foto")
async def atualizar_foto_perfil(request: Request, foto: UploadFile = File(...)):
    try:
        # Validar tamanho (máx 5MB)
        if foto.size > 5_000_000:
            informar_erro(request, "Foto muito grande. Máximo permitido: 5MB")
            return RedirectResponse("/perfil/dados", status_code=303)

        # Validar tipo de arquivo
        tipos_permitidos = ['image/jpeg', 'image/png', 'image/jpg']
        if foto.content_type not in tipos_permitidos:
            informar_aviso(request, "Formato não permitido. Use JPG ou PNG")
            return RedirectResponse("/perfil/dados", status_code=303)

        # Salvar foto
        usuario = obter_usuario_logado(request)
        nome_arquivo = salvar_foto(foto)

        # Atualizar no banco
        atualizar_foto_usuario(usuario.id, nome_arquivo)

        informar_sucesso(request, "Foto de perfil atualizada com sucesso!")
        return RedirectResponse("/perfil/dados", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao atualizar foto. Tente novamente.")
        return RedirectResponse("/perfil/dados", status_code=303)
```

## Exemplo 4: Contratação de Cuidador

```python
from util.flash_messages import informar_sucesso, informar_erro, informar_aviso, informar_info

@router.post("/contratante/contratar/{cuidador_id}")
async def solicitar_contratacao(
    request: Request,
    cuidador_id: int,
    data_inicio: str = Form(...),
    data_fim: str = Form(...),
    observacoes: str = Form(None)
):
    try:
        contratante = obter_usuario_logado(request)

        # Validar datas
        if data_inicio > data_fim:
            informar_aviso(request, "Data de início não pode ser posterior à data de fim")
            return RedirectResponse(f"/contratante/cuidadores/{cuidador_id}", status_code=303)

        # Verificar disponibilidade do cuidador
        if not verificar_disponibilidade(cuidador_id, data_inicio, data_fim):
            informar_erro(request, "Cuidador não disponível neste período")
            return RedirectResponse(f"/contratante/cuidadores/{cuidador_id}", status_code=303)

        # Criar solicitação
        solicitacao = criar_solicitacao_contratacao(
            contratante_id=contratante.id,
            cuidador_id=cuidador_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            observacoes=observacoes
        )

        # Notificar cuidador (em desenvolvimento)
        # notificar_cuidador(cuidador_id, solicitacao)

        informar_sucesso(request, "Solicitação enviada! O cuidador será notificado.")
        informar_info(request, "Você pode acompanhar o status em 'Minhas Contratações'")
        return RedirectResponse("/contratante/contratacoes_realizadas", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao solicitar contratação. Tente novamente.")
        return RedirectResponse(f"/contratante/cuidadores/{cuidador_id}", status_code=303)
```

## Exemplo 5: Exclusão de Item (com confirmação)

```python
from util.flash_messages import informar_sucesso, informar_aviso

@router.post("/admin/excluir-usuario/{usuario_id}")
async def excluir_usuario(request: Request, usuario_id: int):
    try:
        usuario = obter_usuario_por_id(usuario_id)

        if not usuario:
            informar_erro(request, "Usuário não encontrado")
            return RedirectResponse("/admin/usuarios", status_code=303)

        # Verificar se pode excluir (ex: tem contratações ativas)
        if tem_contratacoes_ativas(usuario_id):
            informar_aviso(request, f"Não é possível excluir {usuario.nome}. Existem contratações ativas.")
            return RedirectResponse("/admin/usuarios", status_code=303)

        # Excluir
        excluir_usuario_por_id(usuario_id)

        informar_aviso(request, f"Usuário {usuario.nome} excluído permanentemente")
        return RedirectResponse("/admin/usuarios", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao excluir usuário")
        return RedirectResponse("/admin/usuarios", status_code=303)
```

## Exemplo 6: Múltiplas Mensagens

```python
from util.flash_messages import informar_sucesso, informar_aviso

@router.post("/configuracoes/salvar")
async def salvar_configuracoes(request: Request, ...):
    try:
        # Salvar múltiplas configurações
        configs_salvas = []
        configs_falharam = []

        if salvar_config_email():
            configs_salvas.append("E-mail")
        else:
            configs_falharam.append("E-mail")

        if salvar_config_notificacoes():
            configs_salvas.append("Notificações")
        else:
            configs_falharam.append("Notificações")

        # Feedback para o usuário
        if configs_salvas:
            informar_sucesso(request, f"Configurações salvas: {', '.join(configs_salvas)}")

        if configs_falharam:
            informar_aviso(request, f"Não foi possível salvar: {', '.join(configs_falharam)}")

        return RedirectResponse("/configuracoes", status_code=303)

    except Exception as e:
        informar_erro(request, "Erro ao salvar configurações")
        return RedirectResponse("/configuracoes", status_code=303)
```

## Exemplo 7: Integração com JavaScript (AJAX)

### Backend (Python)

```python
from fastapi.responses import JSONResponse

@router.post("/api/favoritar/{cuidador_id}")
async def favoritar_cuidador(request: Request, cuidador_id: int):
    try:
        usuario = obter_usuario_logado(request)
        adicionar_favorito(usuario.id, cuidador_id)

        return JSONResponse({
            "success": True,
            "message": "Cuidador adicionado aos favoritos!"
        })
    except Exception as e:
        return JSONResponse({
            "success": False,
            "message": "Erro ao adicionar favorito"
        }, status_code=400)
```

### Frontend (JavaScript)

```javascript
async function favoritarCuidador(cuidadorId) {
    try {
        const response = await fetch(`/api/favoritar/${cuidadorId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        if (data.success) {
            // Exibir toast de sucesso
            window.exibirToast(data.message, 'success');
        } else {
            // Exibir toast de erro
            window.exibirToast(data.message, 'danger');
        }
    } catch (error) {
        window.exibirToast('Erro de conexão. Tente novamente.', 'danger');
    }
}
```

## Padrões e Boas Práticas

### ✅ FAÇA

```python
# Seja específico nas mensagens
informar_erro(request, "CPF já cadastrado no sistema")

# Use o tipo correto para cada situação
informar_sucesso(request, "Cadastro realizado!")  # Operação bem-sucedida
informar_erro(request, "Erro ao salvar dados")    # Erro/falha
informar_aviso(request, "Esta ação não pode ser desfeita")  # Aviso importante
informar_info(request, "Você tem 3 novas mensagens")  # Informação geral

# Sempre redirecione após adicionar mensagens
informar_sucesso(request, "Salvo!")
return RedirectResponse("/lista", status_code=303)

# Use try/except para capturar erros
try:
    salvar_dados()
    informar_sucesso(request, "Dados salvos!")
except Exception as e:
    informar_erro(request, "Erro ao salvar dados")
```

### ❌ NÃO FAÇA

```python
# Não use mensagens genéricas
informar_erro(request, "Erro")  # ❌ Muito genérico

# Não misture tipos
informar_sucesso(request, "Erro ao processar")  # ❌ Tipo errado

# Não esqueça de redirecionar
informar_sucesso(request, "Salvo!")
# ❌ Faltou o RedirectResponse!

# Não adicione mensagens sem try/except
salvar_dados()  # ❌ Pode dar erro e não avisar o usuário
informar_sucesso(request, "Salvo!")

# Não use mensagens muito longas
informar_erro(request, "Erro ao processar dados porque o servidor está ocupado e não conseguiu completar a operação neste momento devido a problemas de conexão")  # ❌ Muito longo
```

## Resumo

- Use `informar_sucesso()` para operações bem-sucedidas
- Use `informar_erro()` para erros que o usuário precisa saber
- Use `informar_aviso()` para ações irreversíveis ou importantes
- Use `informar_info()` para feedback informativo geral
- **SEMPRE redirecione** após adicionar mensagens (padrão PRG)
- Seja específico e claro nas mensagens
- Use try/except para capturar erros
- Valide dados antes de processar
- Forneça feedback para TODAS as ações do usuário

---

**Sistema implementado em:** 20/10/2025
