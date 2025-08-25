from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ======================
# SOLICITAR CONTRATAÇÃO (GET)
# ======================
@router.get("/contratante/solicitar-contratacao")
async def get_solicitar_contratacao(request: Request):
    return templates.TemplateResponse(
        "contratante/solicitar_contratação.html",
        {"request": request}
    )

# ======================
# SOLICITAR CONTRATAÇÃO (POST)
# ======================
@router.post("/contratante/solicitar-contratacao")
async def post_solicitar_contratacao(
    request: Request,
    nome_projeto: str = Form(...),
    descricao: str = Form(...)
):
    # Aqui entraria a lógica de salvar a solicitação no banco
    mensagem = f"Solicitação do projeto '{nome_projeto}' enviada com sucesso!"
    return templates.TemplateResponse(
        "contratante/solicitar_contratação.html",
        {"request": request, "mensagem": mensagem}
    )

# ======================
# AVALIAÇÃO DE CONTRATAÇÃO
# ======================
@router.get("/contratante/avaliacao-contratacao")
async def get_avaliacao_contratacao(request: Request):
    # Aqui você buscaria avaliações de contratações do banco
    avaliacoes_fake = [
        {"id": 1, "contratado": "João", "nota": 5, "comentario": "Ótimo profissional!"},
        {"id": 2, "contratado": "Maria", "nota": 4, "comentario": "Bom trabalho!"}
    ]
    return templates.TemplateResponse(
        "contratante/avaliacao_contratação.html",
        {"request": request, "avaliacoes": avaliacoes_fake}
    )

# ======================
# CONTRATAÇÕES REALIZADAS
# ======================
@router.get("/contratante/contratacoes-realizadas")
async def get_contratacoes_realizadas(request: Request):
    # Aqui você buscaria as contratações realizadas no banco
    contratacoes_fake = [
        {"id": 1, "projeto": "Website", "contratado": "João", "status": "Concluído"},
        {"id": 2, "projeto": "App Mobile", "contratado": "Maria", "status": "Em andamento"}
    ]
    return templates.TemplateResponse(
        "contratante/contratações_realizadas.html",
        {"request": request, "contratacoes": contratacoes_fake}
    )