from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from data.administrador import administrador_repo
from data.agenda import agenda_repo
from data.atendimento import atendimento_repo
from data.avaliacao import avaliacao_repo
from data.chamado import chamado_repo
from data.chat import chat_repo
from data.cliente import cliente_repo
from data.cuidador import cuidador_repo
from data.especialidade import especialidade_repo
from data.especialidade_cuidador import especialidade_cuidador_repo
from data.usuario import usuario_repo
from routes import public_routes
from routes.admin import (
    admin_administradores_routes,
    admin_avaliacoes_routes,
    admin_chamados_routes,
    admin_relatorios_routes,
    admin_solicitacoes_verificacoes_routes
)
from routes.contratante import (
    contratante_avaliacao_realizada_routes,
    contratante_avaliacao_recebida_routes,
    contratante_chat_routes,
    contratante_contratacao_routes,
    contratante_cuidadores_routes
)
from routes.cuidador import (
    cuidador_agenda_routes,
    cuidador_avaliacoes_realizadas_routes,
    cuidador_avaliacoes_recebidas_routes,
    cuidador_chats_routes,
    cuidador_contratacoes_recebidas_routes,
    cuidador_especializacoes_routes,
    cuidador_solicitacoes_routes
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

administrador_repo.criar_tabela()
agenda_repo.criar_tabela()
atendimento_repo.criar_tabela()
avaliacao_repo.criar_tabela()
chamado_repo.criar_tabela()
chat_repo.criar_tabela()
cliente_repo.criar_tabela()
cuidador_repo.criar_tabela()
especialidade_repo.criar_tabela()
especialidade_cuidador_repo.criar_tabela()
usuario_repo.criar_tabela()

app.include_router(public_routes.router)
app.include_router(admin_administradores_routes.router)
app.include_router(admin_avaliacoes_routes.router)
app.include_router(admin_chamados_routes.router)
app.include_router(admin_relatorios_routes.router)
app.include_router(admin_solicitacoes_verificacoes_routes.router)
app.include_router(contratante_avaliacao_realizada_routes.router)
app.include_router(contratante_avaliacao_recebida_routes.router)
app.include_router(contratante_chat_routes.router)
app.include_router(contratante_contratacao_routes.router)
app.include_router(contratante_cuidadores_routes.router)
app.include_router(cuidador_agenda_routes.router)
app.include_router(cuidador_avaliacoes_realizadas_routes.router)
app.include_router(cuidador_avaliacoes_recebidas_routes.router)
app.include_router(cuidador_chats_routes.router)
# app.include_router(cuidador_contratacoes_recebidas_routes.router)
app.include_router(cuidador_especializacoes_routes.router)
# app.include_router(cuidador_solicitacoes_routes.router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8082, reload=True)