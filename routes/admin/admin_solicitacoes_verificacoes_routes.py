from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi import Form

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/solicitacao")
async def get_listar_solicitacoes(request: Request):
    # Dados fake para exibir no template
    solicitacoes_fake = [
        {"id": 1, "nome_contratante": "Carlos", "descricao": "Verificação de antecedentes", "status": "Pendente"},
        {"id": 2, "nome_contratante": "Ana", "descricao": "Confirmação de documentos", "status": "Em análise"},
    ]
    return templates.TemplateResponse(
        "administrador/solicitacao_verificacao.html",
        {"request": request, "solicitacoes": solicitacoes_fake}
    )

@router.get("/admin/solicitacao/analisar/{id}")
async def get_analisar_solicitacao(request: Request, id: int):
    return templates.TemplateResponse(
        "administrador/analisar_solicitacao.html",
        {"request": request, "solicitacao_id": id}
    )

@router.post("/admin/solicitacao/analisar")
async def post_analisar_solicitacao(
    request: Request,
    id: int = Form(...),
    aprovado: bool = Form(...)
):

    mensagem = "Solicitação analisada com sucesso!"
    solicitacoes_fake = [
        {"id": 1, "nome_contratante": "Carlos", "descricao": "Verificação de antecedentes", "status": "Pendente"},
        {"id": 2, "nome_contratante": "Ana", "descricao": "Confirmação de documentos", "status": "Em análise"},
    ]
    return templates.TemplateResponse(
        "administrador/solicitacao_verificacao.html",
        {"request": request, "mensagem": mensagem, "solicitacoes": solicitacoes_fake}
    )
