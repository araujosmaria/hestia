from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

administradores = [
    {"id": 1, "nome": "João", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria", "email": "maria@email.com"}
]

# ======================
# TELA INICIAL
# ======================
@router.get("/admin/administradores/tela_inicial")
async def get_tela_inicial_admin(request: Request):
    return templates.TemplateResponse(
        "administrador/tela_inicial.html",
        {"request": request}
    )

# ======================
# LISTAR ADMINISTRADORES
# ======================
@router.get("/admin/administradores")
async def get_listar_administradores(request: Request):
    return templates.TemplateResponse(
        "administrador/administradores.html",
        {"request": request, "administradores": administradores}
    )

# ======================
# CADASTRAR ADMINISTRADOR
# ======================
@router.get("/admin/administradores/cadastrar")
async def get_cadastrar_administrador(request: Request):
    return templates.TemplateResponse(
        "administrador/cadastrar_administrador.html",
        {"request": request}
    )

@router.post("/admin/administradores/cadastrar")
async def post_cadastrar_administrador(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    novo_id = max([a["id"] for a in administradores], default=0) + 1
    administradores.append({"id": novo_id, "nome": nome, "email": email})
    return templates.TemplateResponse(
        "administrador/administradores.html",
        {"request": request, "administradores": administradores, "mensagem": "Administrador cadastrado com sucesso!"}
    )

# ======================
# CONFIRMAR EXCLUSÃO + EXCLUIR
# ======================
@router.get("/admin/administradores/confirmar_exclusao/{id}")
async def get_confirmar_exclusao_administrador(request: Request, id: int):
    return templates.TemplateResponse(
        "administrador/confirmar_exclusao_administrador.html",
        {"request": request, "id": id}
    )

@router.get("/admin/administradores/excluir/{id}")
async def get_excluir_administrador(request: Request, id: int):
    global administradores
    administradores = [a for a in administradores if a["id"] != id]
    return templates.TemplateResponse(
        "administrador/administradores.html",
        {"request": request, "administradores": administradores, "mensagem": f"Administrador {id} excluído com sucesso!"}
    )

# ======================
# PERFIL
# ======================
@router.get("/admin/administradores/perfil/{id}")
async def get_dados_perfil(request: Request, id: int):
    perfil_fake = {"id": id, "nome": "Admin Teste", "email": "admin@teste.com"}
    return templates.TemplateResponse(
        "administrador/dados_perfil.html",
        {"request": request, "perfil": perfil_fake}
    )

# ======================
# ALTERAR SENHA
# ======================
@router.get("/admin/administradores/alterar_senha")
async def get_alterar_senha(request: Request):
    return templates.TemplateResponse(
        "administrador/alterar_senha.html",
        {"request": request}
    )

@router.post("/admin/administradores/alterar_senha")
async def post_alterar_senha(
    request: Request,
    id: int = Form(...),
    senha_atual: str = Form(...),
    nova_senha: str = Form(...)
):
    return templates.TemplateResponse(
        "administrador/tela_inicial.html",
        {"request": request, "mensagem": "Senha alterada com sucesso!"}
    )
