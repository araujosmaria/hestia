from fastapi import APIRouter, Request
from util.template_util import criar_templates
from fastapi import Form
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger

router = APIRouter()
templates = criar_templates("templates")

@router.get("/admin/solicitacao")
async def get_listar_solicitacoes(request: Request):
    # Dados fake para exibir no template
    solicitacoes_fake = [
        {"id": 1, "nome_contratante": "Carlos", "descricao": "Verificação de antecedentes", "status": "Pendente"},
        {"id": 2, "nome_contratante": "Ana", "descricao": "Confirmação de documentos", "status": "Em análise"},
    ]
    return templates.TemplateResponse(
        "administrador/verificacao/solicitacoes.html",
        {"request": request, "solicitacoes": solicitacoes_fake}
    )

@router.get("/admin/solicitacao/analisar/{id}")
async def get_analisar_solicitacao(request: Request, id: int):
    return templates.TemplateResponse(
        "administrador/verificacao/analisar_solicitacao.html",
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
        "administrador/verificacao/solicitacoes.html",
        {"request": request, "mensagem": mensagem, "solicitacoes": solicitacoes_fake}
    )
