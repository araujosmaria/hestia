from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from data.agenda.agenda_model import Agenda
from data.agenda import agenda_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/cuidador/agenda")
async def listar_agenda(request: Request):
    agendas = agenda_repo.obter_por_cuidador()
    return templates.TemplateResponse(
        "cuidador/listar_agenda.html",
        {"request": request, "agendas": agendas}
    )


@router.get("/cuidador/agenda/cadastrar")
async def get_cadastrar_agenda(request: Request):
    return templates.TemplateResponse(
        "cuidador/cadastrar_agenda.html",
        {"request": request}
    )


@router.post("/cuidador/agenda/cadastrar")
async def post_cadastrar_agenda(
    request: Request,
    dataHora: str,
    disponibilidade: bool
):
    try:
        nova_agenda = Agenda(
            id_agenda=0,
            dataHora=datetime.fromisoformat(dataHora),
            disponibilidade=disponibilidade,
            id_cuidador=1  # depois pega do login do cuidador
        )
        if agenda_repo.inserir(nova_agenda):
            mensagem = "Horário cadastrado com sucesso!"
        else:
            mensagem = "Erro ao cadastrar horário."
    except Exception as e:
        mensagem = f"Erro: {e}"

    agendas = agenda_repo.obter_por_cuidador()
    return templates.TemplateResponse(
        "cuidador/listar_agenda.html",
        {"request": request, "agendas": agendas, "mensagem": mensagem}
    )


@router.get("/cuidador/agenda/alterar/{id_agenda}")
async def get_alterar_agenda(request: Request, id_agenda: int):
    agenda = agenda_repo.obter_por_id(id_agenda)
    return templates.TemplateResponse(
        "cuidador/alterar_agenda.html",
        {"request": request, "agenda": agenda}
    )


@router.post("/cuidador/agenda/alterar")
async def post_alterar_agenda(
    request: Request,
    id_agenda: int,
    dataHora: str,
    disponibilidade: bool
):
    try:
        agenda_atualizada = Agenda(
            id_agenda=id_agenda,
            dataHora=datetime.fromisoformat(dataHora),
            disponibilidade=disponibilidade,
            id_cuidador=1
        )
        if agenda_repo.atualizar(agenda_atualizada):
            mensagem = "Horário alterado com sucesso!"
        else:
            mensagem = "Erro ao alterar horário."
    except Exception as e:
        mensagem = f"Erro: {e}"

    agendas = agenda_repo.obter_por_cuidador()
    return templates.TemplateResponse(
        "cuidador/listar_agenda.html",
        {"request": request, "agendas": agendas, "mensagem": mensagem}
    )


@router.get("/cuidador/agenda/excluir/{id_agenda}")
async def excluir_agenda(request: Request, id_agenda: int):
    if agenda_repo.excluir(id_agenda):
        mensagem = "Horário removido com sucesso!"
    else:
        mensagem = "Erro ao remover horário."

    agendas = agenda_repo.obter_por_cuidador()
    return templates.TemplateResponse(
        "cuidador/listar_agenda.html",
        {"request": request, "agendas": agendas, "mensagem": mensagem}
    )
