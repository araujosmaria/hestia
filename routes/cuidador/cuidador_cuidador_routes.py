from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# TELA INICIAL
# ======================
@router.get("/cuidador/home_cuidador")
async def get_home_cuidador(request: Request):
    return templates.TemplateResponse(
        "cuidador/home_cuidador.html",
        {"request": request, "mensagem": "Bem-vindo ao painel do cuidador!"}
    )

# ======================
# ALTERAR SENHA (GET)
# ======================
@router.get("/cuidador/alterar_senha")
async def get_alterar_senha(request: Request):
    return templates.TemplateResponse(
        "cuidador/alterar_senha.html",
        {"request": request}
    )

# ======================
# ALTERAR SENHA (POST)
# ======================
@router.post("/cuidador/alterar_senha")
async def post_alterar_senha(
    request: Request,
    senha_atual: str = Form(...),
    nova_senha: str = Form(...),
    confirmar_senha: str = Form(...)
):
    if nova_senha != confirmar_senha:
        mensagem = "As senhas não coincidem!"
        return templates.TemplateResponse(
            "cuidador/alterar_senha.html",
            {"request": request, "mensagem": mensagem}
        )
    response = RedirectResponse(url="/home_cuidador", status_code=303)
    return response

# ======================
# ABERTURA DE CHAMADOS (GET)
# ======================
@router.get("/cuidador/chamados/abrir")
async def get_abertura_chamados(request: Request):
    return templates.TemplateResponse(
        "abertura_chamados.html",
        {"request": request}
    )

# ======================
# ABERTURA DE CHAMADOS (POST)
# ======================
@router.post("/cuidador/chamados/abrir")
async def post_abertura_chamados(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(...)
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
async def get_chamados_abertos(request: Request):
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
async def get_dados_perfil(request: Request):
    perfil_fake = {
        "nome": "João Silva",
        "email": "joao@exemplo.com",
        "especialidade": "Cuidados com idosos",
        "experiencia": "5 anos de experiência em cuidados domiciliares"
    }
    return templates.TemplateResponse(
        "dados_perfil.html",
        {"request": request, "perfil": perfil_fake}
    )

# ======================
# EDITAR PERFIL (GET)
# ======================
@router.get("/cuidador/editar_perfil")
async def get_editar_perfil(request: Request):
    perfil_cuidador = {
        "nome": "João Silva Santos",
        "email": "joao.silva@email.com", 
        "telefone": "(28) 99999-9999",
        "cpf": "123.456.789-00",
        "data_nascimento": "1990-03-15",
        "cep": "29300-123",
        "endereco": "Rua das Flores",
        "numero": "123",
        "bairro": "Centro", 
        "cidade": "Cachoeiro de Itapemirim",
        "estado": "ES",
        "experiencia": "3-5",
        "valor_hora": "30.00",
        "escolaridade": "tecnico",
        "apresentacao": "Profissional dedicado com mais de 5 anos de experiência no cuidado de idosos e pessoas com deficiência. Possuo formação técnica em enfermagem e especialização em cuidados geriátricos.",
        "disponibilidade": ["manha", "tarde", "finsemana"],
        "especialidades": ["idosos", "alzheimer", "medicamentos", "primeiros-socorros"],
        "cursos": "- Técnico em Enfermagem - SENAC (2018)\n- Certificação em Cuidados Geriátricos - Hospital São Lucas (2020)\n- Curso de Primeiros Socorros - Cruz Vermelha (2021)",
        "status_agenda": "disponivel",
        "foto_perfil": "/static/img/default-avatar.jpg",
        "documentos": [
            {"nome": "Certificado_Tecnico_Enfermagem.pdf", "tipo": "pdf"},
            {"nome": "Certificado_Primeiros_Socorros.pdf", "tipo": "pdf"}
        ],
        "avaliacao": "4.8",
        "total_atendimentos": 15,
        "anos_experiencia_display": "5"
    }
    
    return templates.TemplateResponse(
        "cuidador/editar_perfil.html",
        {"request": request, "perfil": perfil_cuidador}
    )

# ======================
# EDITAR PERFIL (POST)
# ======================
@router.post("/cuidador/editar_perfil")
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
    status_agenda: str = Form(...)
):
    try:
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
        
        # Aqui entraria a lógica para salvar no banco de dados
        dados_atualizados = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "data_nascimento": data_nascimento,
            "endereco": {
                "cep": cep,
                "logradouro": endereco,
                "numero": numero,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            },
            "dados_profissionais": {
                "experiencia": experiencia,
                "valor_hora": valor_hora,
                "escolaridade": escolaridade,
                "apresentacao": apresentacao,
                "cursos": cursos
            },
            "disponibilidade": disponibilidade,
            "especialidades": especialidades,
            "status_agenda": status_agenda
        }
        
        # Simular salvamento no banco
        print(f"Atualizando perfil do cuidador: {dados_atualizados}")
        
        # Redirecionar com mensagem de sucesso
        response = RedirectResponse(url="/cuidador/perfil?sucesso=1", status_code=303)
        return response
        
    except ValueError as e:
        # Recarregar página com erro
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
        # Erro genérico
        return templates.TemplateResponse(
            "cuidador/editar_perfil.html",
            {
                "request": request,
                "erro": "Erro interno. Tente novamente mais tarde."
            }
        )

# ======================
# UPLOAD DE FOTO DE PERFIL
# ======================
@router.post("/cuidador/upload_foto")
async def upload_foto_perfil(
    request: Request,
    foto: str = Form(...)  # Base64 da imagem
):
    try:
        # Aqui entraria a lógica para salvar a foto
        # Por exemplo, decodificar base64, validar formato, salvar no storage
        
        # Simular salvamento
        novo_caminho = f"/static/img/perfil/cuidador_{request.user.id}.jpg"
        
        return {"success": True, "foto_url": novo_caminho}
        
    except Exception as e:
        return {"success": False, "erro": "Erro ao fazer upload da foto"}

# ======================
# UPLOAD DE CERTIFICADOS
# ======================
@router.post("/cuidador/upload_certificados")
async def upload_certificados(
    request: Request,
    # Aqui usaria UploadFile do FastAPI para arquivos
    # certificados: List[UploadFile] = File(...)
):
    try:
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

# ======================
# VISUALIZAR PERFIL (READONLY)
# ======================
@router.get("/cuidador/perfil")
async def get_perfil_cuidador(request: Request, sucesso: str = None):
    # Buscar dados do perfil do banco
    perfil_cuidador = {
        "nome": "João Silva Santos",
        "email": "joao.silva@email.com",
        "telefone": "(28) 99999-9999", 
        "especialidades_principais": ["Cuidados com Idosos", "Alzheimer/Demência"],
        "avaliacao": "4.8",
        "total_atendimentos": 15,
        "anos_experiencia": "5",
        "valor_hora": "30.00",
        "status_agenda": "disponivel",
        "apresentacao": "Profissional dedicado com mais de 5 anos de experiência...",
        "foto_perfil": "/static/img/default-avatar.jpg"
    }
    
    mensagem_sucesso = None
    if sucesso:
        mensagem_sucesso = "Perfil atualizado com sucesso!"
    
    return templates.TemplateResponse(
        "cuidador/perfil.html",
        {
            "request": request, 
            "perfil": perfil_cuidador,
            "mensagem": mensagem_sucesso
        }
    )