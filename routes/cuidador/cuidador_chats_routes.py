from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# CHAT GERAL
# ======================
@router.get("/cuidador/chat/geral")
async def get_chat_geral(request: Request):
    mensagens_fake = [
        {"id": 1, "autor": "Sistema", "mensagem": "Bem-vindo ao chat geral!"},
        {"id": 2, "autor": "Carlos", "mensagem": "Olá, tudo bem?"},
        {"id": 3, "autor": "Cuidador João", "mensagem": "Oi Carlos, tudo sim e você?"}
    ]
    return templates.TemplateResponse(
        "chat_geral.html",
        {"request": request, "mensagens": mensagens_fake}
    )


# ======================
# CHAT COM CONTRATANTE (GET)
# ======================
@router.get("/cuidador/chat/contratante/{id}")
async def get_chat_contratante(request: Request, id: int):
    mensagens_fake = [
        {"id": 1, "autor": "Contratante Ana", "mensagem": "Oi, gostaria de conversar sobre horários."},
        {"id": 2, "autor": "Cuidador João", "mensagem": "Claro, quais dias você precisa?"}
    ]
    return templates.TemplateResponse(
        "chat_contratante.html",
        {"request": request, "mensagens": mensagens_fake, "contratante_id": id}
    )


# ======================
# CHAT COM CONTRATANTE (POST)
# ======================
@router.post("/cuidador/chat/contratante/enviar")
async def post_chat_contratante(
    request: Request,
    contratante_id: int = Form(...),
    mensagem: str = Form(...)
):
    # Aqui entraria a lógica para salvar a mensagem no banco
    return templates.TemplateResponse(
        "chat_contratante.html",
        {
            "request": request,
            "mensagem_sucesso": f"Mensagem enviada para o contratante {contratante_id}!",
            "contratante_id": contratante_id
        }
    )