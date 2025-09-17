from fastapi import APIRouter, Request, Form, File, UploadFile, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import os
import secrets

# ADICIONAR ESTAS IMPORTAÇÕES:
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo
from data.usuario import usuario_repo
from util.auth_decorator import obter_usuario_logado, esta_logado, criar_sessao, requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# TELA INICIAL
# ======================
@router.get("/cuidador/home_cuidador")
@requer_autenticacao()
async def get_home_cuidador(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "cuidador/home_cuidador.html",
        {"request": request, "mensagem": "Bem-vindo ao painel do cuidador!"}
    )

# ======================
# ALTERAR SENHA (GET)
# ======================
@router.get("/cuidador/alterar_senha")
@requer_autenticacao()
async def get_alterar_senha(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "cuidador/alterar_senha.html",
        {"request": request}
    )

# ======================
# ALTERAR SENHA (POST)
# ======================
@router.post("/cuidador/alterar_senha")
@requer_autenticacao()
async def post_alterar_senha(
    request: Request,
    senha_atual: str = Form(...),
    nova_senha: str = Form(...),
    confirmar_senha: str = Form(...),
    usuario_logado: dict = None
):
    if nova_senha != confirmar_senha:
        mensagem = "As senhas não coincidem!"
        return templates.TemplateResponse(
            "cuidador/alterar_senha.html",
            {"request": request, "mensagem": mensagem}
        )
    response = RedirectResponse(url="/cuidador/home_cuidador", status_code=303)
    return response

# ======================
# ABERTURA DE CHAMADOS (GET)
# ======================
@router.get("/cuidador/chamados/abrir")
@requer_autenticacao()
async def get_abertura_chamados(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "abertura_chamados.html",
        {"request": request}
    )

# ======================
# ABERTURA DE CHAMADOS (POST)
# ======================
@router.post("/cuidador/chamados/abrir")
@requer_autenticacao()
async def post_abertura_chamados(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(...),
    usuario_logado: dict = None
):
    mensagem = f"Chamado '{titulo}' aberto com sucesso!"
    return templates.TemplateResponse(
        "abertura_chamados.html",
        {"request": request, "mensagem": mensagem}
    )

# ======================
# LISTAR CHAMADOS ABERTOS
# ======================
@router.get("/cuidador/chamados/abertos")
@requer_autenticacao()
async def get_chamados_abertos(request: Request, usuario_logado: dict = None):
    chamados_fake = [
        {"id": 1, "titulo": "Problema no acesso", "status": "Em análise"},
        {"id": 2, "titulo": "Erro ao atualizar perfil", "status": "Aberto"}
    ]
    return templates.TemplateResponse(
        "chamados_abertos.html",
        {"request": request, "chamados": chamados_fake}
    )

# ======================
# DADOS DO PERFIL
# ======================
@router.get("/cuidador/perfil")
@requer_autenticacao()
async def get_dados_perfil(request: Request, sucesso: str = None, erro: str = None, foto_sucesso: str = None, usuario_logado: dict = None):
    # Buscar dados reais do perfil do banco
    id_usuario = usuario_logado['id']
    cuidador = cuidador_repo.obter_por_id(id_usuario)
    
    if not cuidador:
        return RedirectResponse("/login", status_code=303)
    
    perfil_cuidador = {
        "nome": cuidador.nome,
        "email": cuidador.email,
        "telefone": cuidador.telefone, 
        "especialidades_principais": ["Cuidados com Idosos", "Alzheimer/Demência"],
        "avaliacao": "4.8",
        "total_atendimentos": 15,
        "anos_experiencia": "5",
        "valor_hora": str(cuidador.valorHora),
        "status_agenda": "disponivel",
        "apresentacao": cuidador.apresentacao,
        "foto_perfil": cuidador.foto or "/static/img/default-avatar.jpg"
    }
    
    mensagem_sucesso = None
    mensagem_erro = None
    
    if sucesso:
        mensagem_sucesso = "Perfil atualizado com sucesso!"
    if foto_sucesso:
        mensagem_sucesso = "Foto de perfil atualizada com sucesso!"
    if erro == "tipo_invalido":
        mensagem_erro = "Tipo de arquivo inválido. Use apenas JPG, PNG ou JPEG."
    elif erro == "upload_falhou":
        mensagem_erro = "Erro no upload da foto. Tente novamente."
    
    return templates.TemplateResponse(
        "cuidador/perfil.html",
        {
            "request": request, 
            "perfil": perfil_cuidador,
            "mensagem": mensagem_sucesso,
            "erro": mensagem_erro
        }
    )

# ======================
# EDITAR PERFIL (GET)
# ======================
@router.get("/cuidador/editar_perfil")
@requer_autenticacao()
async def get_editar_perfil(request: Request, usuario_logado: dict = None):
    id_usuario = usuario_logado['id']
    
    # Buscar dados reais do cuidador no banco
    cuidador = cuidador_repo.obter_por_id(id_usuario)
    
    if not cuidador:
        return RedirectResponse("/login", status_code=303)
    
    # Converter os dados do modelo para o formato esperado pelo template
    perfil_cuidador = {
        "nome": cuidador.nome,
        "email": cuidador.email,
        "telefone": cuidador.telefone,
        "cpf": cuidador.cpf,
        "data_nascimento": cuidador.dataNascimento,
        "cep": cuidador.cep,
        "endereco": cuidador.logradouro,
        "numero": cuidador.numero,
        "bairro": cuidador.bairro,
        "cidade": cuidador.cidade,
        "estado": cuidador.estado,
        "experiencia": cuidador.experiencia,
        "valor_hora": str(cuidador.valorHora),
        "escolaridade": cuidador.escolaridade,
        "apresentacao": cuidador.apresentacao,
        "cursos": cuidador.cursos or "",
        "foto_perfil": cuidador.foto or "/static/img/default-avatar.jpg",
        
        # Campos que podem não existir no modelo atual - valores padrão
        "disponibilidade": [],  # Você precisa adicionar este campo no modelo/banco
        "especialidades": [],   # Você precisa adicionar este campo no modelo/banco
        "status_agenda": "disponivel",
        "avaliacao": "0.0",
        "total_atendimentos": 0,
        "anos_experiencia_display": "0"
    }
    
    return templates.TemplateResponse(
        "cuidador/editar_perfil.html",
        {"request": request, "perfil": perfil_cuidador}
    )

# ======================
# EDITAR PERFIL (POST)
# ======================
@router.post("/cuidador/editar_perfil")
@requer_autenticacao()
async def post_editar_perfil(
    request: Request,
    
    # Dados pessoais
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    data_nascimento: str = Form(...),
    
    # Endereço
    cep: str = Form(...),
    endereco: str = Form(...),
    numero: str = Form(None),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    
    # Dados profissionais
    experiencia: str = Form(...),
    valor_hora: float = Form(...),
    escolaridade: str = Form(...),
    apresentacao: str = Form(...),
    
    # Disponibilidade (checkboxes - podem vir como None)
    manha: str = Form(None),
    tarde: str = Form(None), 
    noite: str = Form(None),
    madrugada: str = Form(None),
    finsemana: str = Form(None),
    feriados: str = Form(None),
    
    # Especialidades (checkboxes - podem vir como None)
    idosos: str = Form(None),
    deficiencia: str = Form(None),
    alzheimer: str = Form(None),
    medicamentos: str = Form(None),
    primeiros_socorros: str = Form(None),
    fisioterapia: str = Form(None),
    
    # Outros campos
    cursos: str = Form(None),
    status_agenda: str = Form(...),
    
    # Parâmetro de autenticação
    usuario_logado: dict = None
):
    try:
        id_usuario = usuario_logado['id']
        
        # Processar disponibilidade
        disponibilidade = []
        if manha: disponibilidade.append("manha")
        if tarde: disponibilidade.append("tarde") 
        if noite: disponibilidade.append("noite")
        if madrugada: disponibilidade.append("madrugada")
        if finsemana: disponibilidade.append("finsemana")
        if feriados: disponibilidade.append("feriados")
        
        # Processar especialidades
        especialidades = []
        if idosos: especialidades.append("idosos")
        if deficiencia: especialidades.append("deficiencia")
        if alzheimer: especialidades.append("alzheimer")
        if medicamentos: especialidades.append("medicamentos")
        if primeiros_socorros: especialidades.append("primeiros-socorros")
        if fisioterapia: especialidades.append("fisioterapia")
        
        # Validações básicas
        if len(apresentacao) > 500:
            raise ValueError("Apresentação deve ter no máximo 500 caracteres")
        
        if valor_hora < 15:
            raise ValueError("Valor por hora deve ser no mínimo R$ 15,00")
            
        if not disponibilidade:
            raise ValueError("Selecione pelo menos um período de disponibilidade")
            
        if not especialidades:
            raise ValueError("Selecione pelo menos uma especialidade")
        
        # Buscar cuidador atual no banco
        cuidador_atual = cuidador_repo.obter_por_id(id_usuario)
        if not cuidador_atual:
            raise ValueError("Usuário não encontrado.")
        
        # Verificar se o email já existe para outro usuário
        usuario_email = usuario_repo.obter_por_email(email)
        if usuario_email and usuario_email.id != id_usuario:
            raise ValueError("Este email já está sendo usado por outro usuário!")
        
        # Atualizar objeto Cuidador com os novos dados
        cuidador_atualizado = Cuidador(
            id=cuidador_atual.id,
            nome=nome,
            dataNascimento=data_nascimento,
            email=email,
            telefone=telefone,
            cpf=cuidador_atual.cpf,  # CPF não muda
            senha=cuidador_atual.senha,  # Senha não muda aqui
            perfil=cuidador_atual.perfil,
            foto=cuidador_atual.foto,
            token_redefinicao=cuidador_atual.token_redefinicao,
            data_token=cuidador_atual.data_token,
            data_cadastro=cuidador_atual.data_cadastro,
            cep=cep,
            logradouro=endereco,
            numero=numero,
            complemento=cuidador_atual.complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            ativo=cuidador_atual.ativo,
            experiencia=experiencia,
            valorHora=valor_hora,
            escolaridade=escolaridade,
            apresentacao=apresentacao,
            cursos=cursos,
            # Campos do cadastro que não mudam na edição
            confirmarSenha=cuidador_atual.confirmarSenha,
            termos=cuidador_atual.termos,
            verificacao=cuidador_atual.verificacao,
            comunicacoes=cuidador_atual.comunicacoes
        )
        
        # SALVAR NO BANCO DE DADOS
        sucesso = cuidador_repo.atualizar(cuidador_atualizado)
        
        if not sucesso:
            raise Exception("Erro ao atualizar dados no banco")
        
        # Se você tiver tabelas separadas para disponibilidade e especialidades:
        # cuidador_repo.atualizar_disponibilidade(id_usuario, disponibilidade)
        # cuidador_repo.atualizar_especialidades(id_usuario, especialidades)
        
        print(f"Perfil do cuidador {id_usuario} atualizado com sucesso!")
        
        # Atualizar dados da sessão
        criar_sessao(request, {
            "id": id_usuario,
            "nome": nome,
            "email": email,
            "perfil": usuario_logado["perfil"],
            "foto": usuario_logado.get("foto")
        })
        
        # Redirecionar com mensagem de sucesso
        response = RedirectResponse(url="/cuidador/perfil?sucesso=1", status_code=303)
        return response
        
    except ValueError as e:
        # Recarregar página com erro, mantendo os dados digitados
        perfil_cuidador = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "data_nascimento": data_nascimento,
            "cep": cep,
            "endereco": endereco,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "experiencia": experiencia,
            "valor_hora": str(valor_hora),
            "escolaridade": escolaridade,
            "apresentacao": apresentacao,
            "disponibilidade": disponibilidade,
            "especialidades": especialidades,
            "cursos": cursos or "",
            "status_agenda": status_agenda,
            "foto_perfil": "/static/img/default-avatar.jpg"
        }
        
        return templates.TemplateResponse(
            "cuidador/editar_perfil.html",
            {
                "request": request, 
                "perfil": perfil_cuidador,
                "erro": str(e)
            }
        )
    
    except Exception as e:
        print(f"Erro ao atualizar perfil: {e}")
        return templates.TemplateResponse(
            "cuidador/editar_perfil.html",
            {
                "request": request,
                "erro": "Erro interno. Tente novamente mais tarde."
            }
        )

# ======================
# ALTERAR FOTO DE PERFIL
# ======================
@router.post("/cuidador/alterar-foto")
@requer_autenticacao()
async def alterar_foto(
    request: Request,
    foto: UploadFile = File(...),  # ← Recebe arquivo de foto
    usuario_logado: dict = None
):
    # 1. Validar tipo de arquivo
    tipos_permitidos = ["image/jpeg", "image/png", "image/jpg"]
    if foto.content_type not in tipos_permitidos:
        return RedirectResponse("/cuidador/perfil?erro=tipo_invalido", status.HTTP_303_SEE_OTHER)

    # 2. Criar diretório se não existir
    upload_dir = "static/uploads/usuarios"
    os.makedirs(upload_dir, exist_ok=True)

    # 3. Gerar nome único para evitar conflitos
    extensao = foto.filename.split(".")[-1]
    nome_arquivo = f"{usuario_logado['id']}_{secrets.token_hex(8)}.{extensao}"
    caminho_arquivo = os.path.join(upload_dir, nome_arquivo)

    # 4. Salvar arquivo no sistema
    try:
        conteudo = await foto.read()  # ← Lê conteúdo do arquivo
        with open(caminho_arquivo, "wb") as f:
            f.write(conteudo)

        # 5. Salvar caminho no banco de dados
        caminho_relativo = f"/static/uploads/usuarios/{nome_arquivo}"
        usuario_repo.atualizar_foto(usuario_logado['id'], caminho_relativo)

        # 6. Atualizar sessão do usuário
        usuario_logado['foto'] = caminho_relativo
        criar_sessao(request, usuario_logado)

    except Exception as e:
        return RedirectResponse("/cuidador/perfil?erro=upload_falhou", status.HTTP_303_SEE_OTHER)

    return RedirectResponse("/cuidador/perfil?foto_sucesso=1", status.HTTP_303_SEE_OTHER)

# ======================
# UPLOAD DE CERTIFICADOS
# ======================
@router.post("/cuidador/upload_certificados")
@requer_autenticacao()
async def upload_certificados(
    request: Request,
    # Aqui usaria UploadFile do FastAPI para arquivos
    # certificados: List[UploadFile] = File(...)
    usuario_logado: dict = None
):
    try:
        id_usuario = usuario_logado['id']
        # Lógica para validar e salvar certificados
        # Validar formato (PDF, JPG, PNG)
        # Validar tamanho máximo
        # Salvar no storage
        
        documentos_salvos = [
            {"nome": "novo_certificado.pdf", "tipo": "pdf"},
            {"nome": "outro_documento.jpg", "tipo": "image"}
        ]
        
        return {"success": True, "documentos": documentos_salvos}
        
    except Exception as e:
        return {"success": False, "erro": "Erro ao fazer upload dos certificados"}