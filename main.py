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
from routes.public_routes import router as public_routes
from routes.admin import (
    admin_administradores_routes as admin_administradores_router,
    admin_avaliacoes_routes as admin_avaliacoes_router,
    admin_chamados_routes as admin_chamados_router,
    admin_relatorios_routes as admin_relatorios_router,
    admin_solicitacoes_verificacoes_routes as admin_solicitacoes_verificacoes_router
)
from routes.contratante import (
    contratante_avaliacao_realizada_routes as contratante_avaliacao_realizada_router,
    contratante_avaliacao_recebida_routes as contratante_avaliacao_recebida_router,
    contratante_chat_routes as contratante_chat_router,
    contratante_contratacao_routes as contratante_contratacao_router,
    contratante_cuidadores_routes as contratante_cuidadores_router
)
from routes.cuidador import (
    cuidador_agenda_routes as cuidador_agenda_router,
    cuidador_avaliacoes_realizadas_routes as cuidador_avaliacoes_realizadas_router,
    cuidador_avaliacoes_recebidas_routes as cuidador_avaliacoes_recebidas_router,
    cuidador_chats_routes as cuidador_chats_router,
    cuidador_contratacoes_recebidas_routes as cuidador_contratacoes_recebidas_router,
    cuidador_especializacoes_routes as cuidador_especializacoes_router,
    cuidador_solicitacoes_routes as cuidador_solicitacoes_router
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

app.include_router(public_routes)
app.include_router(admin_administradores_router)
app.include_router(admin_avaliacoes_router)
app.include_router(admin_chamados_router)
app.include_router(admin_relatorios_router)
app.include_router(admin_solicitacoes_verificacoes_router)
app.include_router(contratante_avaliacao_realizada_router)
app.include_router(contratante_avaliacao_recebida_router)
app.include_router(contratante_chat_router)
app.include_router(contratante_contratacao_router)
app.include_router(contratante_cuidadores_router)
app.include_router(cuidador_agenda_router)
app.include_router(cuidador_avaliacoes_realizadas_router)
app.include_router(cuidador_avaliacoes_recebidas_router)
app.include_router(cuidador_chats_router)
app.include_router(cuidador_contratacoes_recebidas_router)
app.include_router(cuidador_especializacoes_router)
app.include_router(cuidador_solicitacoes_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8082, reload=True)