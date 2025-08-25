from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# TELA INICIAL
# ======================
@router.get("/contratante/tela_inicial")
async def get_tela_inicial(request: Request):
    return templates.TemplateResponse(
        "contratante/tela_inicial.html",
        {"request": request}
    )

# ======================
# PÁGINA CONTRATANTE
# ======================
@router.get("/contratante")
async def get_contratante(request: Request):
    return templates.TemplateResponse(
        "contratante/contratante.html",
        {"request": request}
    )

# ======================
# PERFIL
# ======================
@router.get("/contratante/dados_perfil/{id}")
async def get_dados_perfil(request: Request, id: int):
    perfil_fake = {"id": id, "nome": "Usuário Teste", "email": "teste@teste.com"}
    return templates.TemplateResponse(
        "contratante/dados_perfil.html",
        {"request": request, "perfil": perfil_fake}
    )

# ======================
# ALTERAR SENHA
# ======================
@router.get("/contratante/alterar_senha/{id}")
async def get_alterar_senha(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/alterar_senha.html",
        {"request": request, "id": id}
    )

@router.post("/contratante/alterar_senha")
async def post_alterar_senha(
    request: Request,
    id: int = Form(...),
    senha_atual: str = Form(...),
    nova_senha: str = Form(...)
):
    return templates.TemplateResponse(
        "contratante/contratante.html",
        {"request": request, "mensagem": "Senha alterada com sucesso!"}
    )

# ======================
# SOLICITAR VERIFICAÇÃO
# ======================
@router.get("/contratante/solicitar_verificacao/{id}")
async def get_solicitar_verificacao(request: Request, id: int):
    return templates.TemplateResponse(
        "contratante/solicitar_verificação.html",
        {"request": request, "id": id}
    )

@router.post("/contratante/solicitar_verificacao")
async def post_solicitar_verificacao(
    request: Request,
    id: int = Form(...),
    documento: str = Form(...)
):
    return templates.TemplateResponse(
        "contratante/contratante.html",
        {"request": request, "mensagem": "Verificação solicitada com sucesso!"}
    )

# ======================
# ABERTURA DE CHAMADO
# ======================
@router.get("/contratante/chamados/abrir")
async def get_abertura_chamado(request: Request):
    return templates.TemplateResponse(
        "contratante/abertura_chamado.html",
        {"request": request}
    )

@router.post("/contratante/chamados/abrir")
async def post_abertura_chamado(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(...)
):
    return templates.TemplateResponse(
        "contratante/chamados_abertos.html",
        {"request": request, "mensagem": "Chamado aberto com sucesso!"}
    )

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# CHAMADOS ABERTOS
# ======================
@router.get("/contratante/chamados_abertos")
async def get_chamados_abertos(request: Request):
    chamados_fake = [
        {"id": 1, "titulo": "Erro no sistema", "status": "Aberto"},
        {"id": 2, "titulo": "Problema no pagamento", "status": "Resolvido"}
    ]
    return templates.TemplateResponse(
        "contratante/chamados_abertos.html",
        {"request": request, "chamados": chamados_fake}
    )
