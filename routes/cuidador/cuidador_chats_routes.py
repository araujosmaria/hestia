from typing import Optional
from fastapi import APIRouter, Request, Form
from util.template_util import criar_templates
from fastapi.responses import RedirectResponse
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger

router = APIRouter()
templates = criar_templates("templates")

# Simula lista de chats disponíveis no chat geral
chats_geral = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"},
]

# Simula mensagens do chat geral (você pode expandir e adaptar)
mensagens_chat_geral = [
    {"autor": "João", "mensagem": "Olá, pessoal!"},
    {"autor": "Maria", "mensagem": "Oi, João! Tudo bem?"},
]

# Simulando dados para chat contratante (por contratante_id)
mensagens_chat_contratante = {
    1: [  # contratante_id = 1
        {"autor": "Cuidador", "mensagem": "Olá, tudo certo com o serviço?"},
        {"autor": "Contratante", "mensagem": "Sim, muito bom! Obrigado."}
    ],
    # Pode adicionar mais contratantes
}

# Rota para a home do cuidador
@router.get("/cuidador/home_cuidador")
async def home_cuidador(request: Request, mensagem: Optional[str] = None):
    return templates.TemplateResponse("cuidador/home_cuidador.html", {"request": request, "mensagem": mensagem})

# Rota para listar chats disponíveis no chat geral (lista de contatos)
@router.get("/cuidador/chat_geral")
async def lista_chats_geral(request: Request):
    return templates.TemplateResponse("cuidador/chat_geral.html", {"request": request, "chats": chats_geral})

# Rota para exibir mensagens do chat geral
@router.get("/cuidador/chat/geral")
async def exibir_chat_geral(request: Request):
    return templates.TemplateResponse("cuidador/chat_geral.html", {"request": request, "mensagens": mensagens_chat_geral})

# Rota para exibir chat contratante específico
@router.get("/cuidador/chat/contratante/{contratante_id}")
async def chat_contratante(request: Request, contratante_id: int):
    mensagens = mensagens_chat_contratante.get(contratante_id, [])
    return templates.TemplateResponse(
        "cuidador/chat_contratante.html",
        {"request": request, "mensagens": mensagens, "contratante_id": contratante_id, "mensagem_sucesso": None}
    )

# Rota para enviar mensagem no chat contratante (POST)
@router.post("/cuidador/chat/contratante/enviar")
async def enviar_mensagem_chat_contratante(
    contratante_id: int = Form(...),
    mensagem: str = Form(...),
):
    if contratante_id not in mensagens_chat_contratante:
        mensagens_chat_contratante[contratante_id] = []
    mensagens_chat_contratante[contratante_id].append({"autor": "Cuidador", "mensagem": mensagem})
    
    # Redireciona para o chat contratante (GET)
    return RedirectResponse(url=f"/cuidador/chat/contratante/{contratante_id}", status_code=303)
