from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# LISTAR ESPECIALIZAÇÕES
# ======================
@router.get("/cuidador/especializacoes")
async def get_listar_especializacoes(request: Request):
    especializacoes_fake = [
        {"id": 1, "nome": "Cuidados com idosos", "descricao": "Experiência com cuidados diários"},
        {"id": 2, "nome": "Enfermagem básica", "descricao": "Aplicação de medicamentos e curativos"}
    ]
    return templates.TemplateResponse(
        "especializações.html",
        {"request": request, "especializacoes": especializacoes_fake}
    )

# ======================
# CADASTRAR ESPECIALIZAÇÃO (GET)
# ======================
@router.get("/cuidador/especializacoes/cadastro")
async def get_cadastro_especializacao(request: Request):
    return templates.TemplateResponse(
        "cadastro_especialização.html",
        {"request": request}
    )

# ======================
# CADASTRAR ESPECIALIZAÇÃO (POST)
# ======================
@router.post("/cuidador/especializacoes/cadastro")
async def post_cadastro_especializacao(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...)
):
    return templates.TemplateResponse(
        "especializações.html",
        {"request": request, "mensagem": f"Especialização '{nome}' cadastrada com sucesso!"}
    )

# ======================
# ALTERAR ESPECIALIZAÇÃO (GET)
# ======================
@router.get("/cuidador/especializacoes/alteracao/{id}")
async def get_alteracao_especializacao(request: Request, id: int):
    especializacao_fake = {"id": id, "nome": "Enfermagem básica", "descricao": "Aplicação de medicamentos"}
    return templates.TemplateResponse(
        "alteração_especialização.html",
        {"request": request, "especializacao": especializacao_fake}
    )

# ======================
# ALTERAR ESPECIALIZAÇÃO (POST)
# ======================
@router.post("/cuidador/especializacoes/alteracao")
async def post_alteracao_especializacao(
    request: Request,
    id: int = Form(...),
    nome: str = Form(...),
    descricao: str = Form(...)
):
    return templates.TemplateResponse(
        "especializações.html",
        {"request": request, "mensagem": f"Especialização {id} atualizada com sucesso!"}
    )

# ======================
# EXCLUIR ESPECIALIZAÇÃO (GET)
# ======================
@router.get("/cuidador/especializacoes/exclusao/{id}")
async def get_exclusao_especializacao(request: Request, id: int):
    especializacao_fake = {"id": id, "nome": "Cuidados com idosos"}
    return templates.TemplateResponse(
        "exclusão_especialização.html",
        {"request": request, "especializacao": especializacao_fake}
    )

# ======================
# EXCLUIR ESPECIALIZAÇÃO (POST)
# ======================
@router.post("/cuidador/especializacoes/exclusao")
async def post_exclusao_especializacao(
    request: Request,
    id: int = Form(...)
):
    return templates.TemplateResponse(
        "especializações.html",
        {"request": request, "mensagem": f"Especialização {id} excluída com sucesso!"}
    )