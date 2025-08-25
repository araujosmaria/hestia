from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# TELA INICIAL
# ======================
@router.get("/cuidador")
async def get_tela_inicial(request: Request):
    return templates.TemplateResponse(
        "tela_inicial.html",
        {"request": request, "mensagem": "Bem-vindo ao painel do cuidador!"}
    )

# ======================
# ALTERAR SENHA (GET)
# ======================
@router.get("/cuidador/alterar_senha")
async def get_alterar_senha(request: Request):
    return templates.TemplateResponse(
        "alterar_senha.html",
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
    # Aqui entraria a lógica para validar e atualizar a senha no banco
    if nova_senha != confirmar_senha:
        mensagem = "As senhas não coincidem!"
    else:
        mensagem = "Senha alterada com sucesso!"
    
    return templates.TemplateResponse(
        "alterar_senha.html",
        {"request": request, "mensagem": mensagem}
    )

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
    # Aqui entraria a lógica de salvar no banco
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