from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/chamados")
async def get_listar_chamados(request: Request):
    chamados_fake = [
        {"id": 1, "titulo": "Erro no login", "status": "Aberto", "descricao": "Usuário não consegue logar"},
        {"id": 2, "titulo": "Atualizar perfil", "status": "Em análise", "descricao": "Não consegue salvar alterações"},
    ]
    return templates.TemplateResponse("administrador/chamados.html", {
        "request": request,
        "chamados": chamados_fake
    })

@router.get("/admin/chamados/responder/{chamado_id}")
async def get_responder_chamado(request: Request, chamado_id: int):
    return templates.TemplateResponse("administrador/responder_chamado.html", {
        "request": request,
        "chamado_id": chamado_id
    })

# Página para responder um chamado específico
@router.post("/admin/chamados/responder")
async def post_responder_chamado(
    request: Request,
    id: int = Form(...),
    resposta: str = Form(...),
    status: str = Form(...)
):
    chamados_fake = [
        {"id": 1, "titulo": "Erro no login", "status": "Aberto", "descricao": "Usuário não consegue logar"},
        {"id": 2, "titulo": "Atualizar perfil", "status": "Em análise", "descricao": "Não consegue salvar alterações"},
    ]

    return templates.TemplateResponse(
        "administrador/chamados.html",
        {
            "request": request,
            "chamados": chamados_fake,
            "mensagem": f"Resposta enviada para o chamado #{id}. Status atualizado para '{status}'."
        }
    )