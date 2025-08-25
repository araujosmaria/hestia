from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# CHAT COM CUIDADOR
# ======================
@router.get("/contratante/chat/com_cuidador/{id_cuidador}")
async def get_chat_com_cuidador(request: Request, id_cuidador: int):
    # Exemplo de conversa fake (simulação de busca no banco)
    mensagens_fake = [
        {"remetente": "Você", "texto": "Olá, gostaria de mais informações."},
        {"remetente": f"Cuidador {id_cuidador}", "texto": "Claro, posso ajudar sim!"}
    ]
    return templates.TemplateResponse(
        "chat_com_cuidador.html",
        {"request": request, "mensagens": mensagens_fake, "id_cuidador": id_cuidador}
    )


# ======================
# ENVIAR MENSAGEM PARA CUIDADOR
# ======================
@router.post("/contratante/chat/com_cuidador/{id_cuidador}")
async def post_chat_com_cuidador(
    request: Request,
    id_cuidador: int,
    mensagem: str = Form(...)
):
    # Aqui entraria lógica de salvar no banco
    mensagens_fake = [
        {"remetente": "Você", "texto": mensagem},
        {"remetente": f"Cuidador {id_cuidador}", "texto": "Mensagem recebida!"}
    ]
    return templates.TemplateResponse(
        "chat_com_cuidador.html",
        {"request": request, "mensagens": mensagens_fake, "id_cuidador": id_cuidador}
    )


# ======================
# CHAT GERAL
# ======================
@router.get("/contratante/chat/geral")
async def get_chat_geral(request: Request):
    mensagens_fake = [
        {"remetente": "Admin", "texto": "Bem-vindo ao chat geral!"},
        {"remetente": "Usuário", "texto": "Olá a todos!"}
    ]
    return templates.TemplateResponse(
        "chat_geral.html",
        {"request": request, "mensagens": mensagens_fake}
    )


# ======================
# ENVIAR MENSAGEM NO CHAT GERAL
# ======================
@router.post("/contratante/chat/geral")
async def post_chat_geral(
    request: Request,
    mensagem: str = Form(...)
):
    mensagens_fake = [
        {"remetente": "Você", "texto": mensagem},
        {"remetente": "Admin", "texto": "Mensagem recebida no chat geral!"}
    ]
    return templates.TemplateResponse(
        "chat_geral.html",
        {"request": request, "mensagens": mensagens_fake}
    )