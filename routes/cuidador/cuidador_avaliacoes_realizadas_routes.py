from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Simulando banco de dados
avaliacoes = [
    {"id": 1, "contratante": "João", "nota": 4, "comentario": "Muito bom!"},
    {"id": 2, "contratante": "Maria", "nota": 5, "comentario": "Excelente trabalho!"},
]

@router.get("/cuidador/avaliacoes_realizadas")
async def listar_avaliacoes(request: Request):
    return templates.TemplateResponse("cuidador/avaliacoes_realizadas.html", {"request": request, "avaliacoes": avaliacoes})

# Alteração aqui: rota para confirmação de exclusão
@router.get("/cuidador/avaliacoes_realizadas/confirmar_exclusao/{id}")
async def confirmar_exclusao(request: Request, id: int):
    avaliacao = next((a for a in avaliacoes if a["id"] == id), None)
    return templates.TemplateResponse("cuidador/excluir_avaliacao.html", {"request": request, "avaliacao": avaliacao})

@router.post("/cuidador/avaliacoes_realizadas/excluir")
async def excluir_avaliacao(request: Request, id: int = Form(...)):
    global avaliacoes
    avaliacoes = [a for a in avaliacoes if a["id"] != id]
    return RedirectResponse("/cuidador/avaliacoes_realizadas", status_code=303)

@router.get("/cuidador/avaliacoes_realizadas/alterar/{id}")
async def get_alterar_avaliacao(request: Request, id: int):
    avaliacao = next((a for a in avaliacoes if a["id"] == id), None)
    return templates.TemplateResponse("cuidador/alterar_avaliacao.html", {"request": request, "avaliacao": avaliacao})

@router.post("/cuidador/avaliacoes_realizadas/alterar")
async def post_alterar_avaliacao(
    request: Request,
    id: int = Form(...),
    nota: int = Form(...),
    comentario: str = Form(...)
):
    for a in avaliacoes:
        if a["id"] == id:
            a["nota"] = nota
            a["comentario"] = comentario
    return RedirectResponse("/cuidador/avaliacoes_realizadas", status_code=303)
