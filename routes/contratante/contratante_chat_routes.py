from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# CHAT COM CUIDADOR
# ======================
@router.get("/contratante/chat_com_cuidador/{id_cuidador}")
async def get_chat_com_cuidador(request: Request, id_cuidador: int):
    mensagens_fake = [
        {"remetente": "Você", "texto": "Olá, gostaria de mais informações."},
        {"remetente": f"Cuidador {id_cuidador}", "texto": "Claro, posso ajudar sim!"}
    ]
    return templates.TemplateResponse(
        "contratante/chat_com_cuidador.html",
        {"request": request, "mensagens": mensagens_fake, "id_cuidador": id_cuidador}
    )

# ======================
# ENVIAR MENSAGEM PARA CUIDADOR
# ======================
@router.post("/contratante/chat_com_cuidador/{id_cuidador}")
async def post_chat_com_cuidador(
    request: Request,
    id_cuidador: int,
    mensagem: str = Form(...)
):
    mensagens_fake = [
        {"remetente": "Você", "texto": mensagem},
        {"remetente": f"Cuidador {id_cuidador}", "texto": "Mensagem recebida!"}
    ]
    return templates.TemplateResponse(
        "contratante/chat_com_cuidador.html",
        {"request": request, "mensagens": mensagens_fake, "id_cuidador": id_cuidador}
    )

# ======================
# ENVIAR MENSAGEM NO CHAT GERAL
# ======================
@router.post("/contratante/chat_geral")
async def post_chat_geral(
    request: Request,
    mensagem: str = Form(...)
):
    mensagens_fake = [
        {"remetente": "Você", "texto": mensagem},
        {"remetente": "Admin", "texto": "Mensagem recebida no chat geral!"}
    ]
    return templates.TemplateResponse(
        "contratante/chat_geral.html",
        {"request": request, "mensagens": mensagens_fake}
    )

# ======================
# CHAT GERAL
# =====================
@router.get("/contratante/chat_geral")
async def get_chat_geral(request: Request):
    mensagens_fake = [
        {"remetente": "Admin", "texto": "Bem-vindo ao chat geral!"},
        {"remetente": "Usuário", "texto": "Olá a todos!"}
    ]
    cuidadores_fake = [
        {"id": 1, "nome": "Ana", "especialidade": "Cuidados com idosos"},
        {"id": 2, "nome": "Carlos", "especialidade": "Enfermagem domiciliar"},
        {"id": 3, "nome": "Fernanda", "especialidade": "Acompanhamento hospitalar"},
    ]
    return templates.TemplateResponse(
        "contratante/chat_geral.html",
        {"request": request, "mensagens": mensagens_fake, "cuidadores": cuidadores_fake}
    )

@router.post("/contratante/chat_geral")
async def post_chat_geral(request: Request, mensagem: str = Form(...)):
    mensagens_fake = [
        {"remetente": "Você", "texto": mensagem},
        {"remetente": "Admin", "texto": "Mensagem recebida no chat geral!"}
    ]
    cuidadores_fake = [
        {"id": 1, "nome": "Ana", "especialidade": "Cuidados com idosos"},
        {"id": 2, "nome": "Carlos", "especialidade": "Enfermagem domiciliar"},
        {"id": 3, "nome": "Fernanda", "especialidade": "Acompanhamento hospitalar"},
    ]
    return templates.TemplateResponse(
        "contratante/chat_geral.html",
        {"request": request, "mensagens": mensagens_fake, "cuidadores": cuidadores_fake}
    )
