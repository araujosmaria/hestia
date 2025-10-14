from starlette.middleware.sessions import SessionMiddleware
import secrets 
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
from data.contratacao import contratacao_repo 
from data.cuidador import cuidador_repo
from data.especialidade import especialidade_repo
from data.especialidade_cuidador import especialidade_cuidador_repo
from data.solicitacao import solicitacao_repo
from data.usuario import usuario_repo
from routes.public_routes import router as public_routes
from routes import perfil_routes
from routes.perfil_routes import router as perfil_dados_router
from routes.perfil_routes import perfil_router

from routes.admin import (
    admin_administradores_routes,
    admin_avaliacoes_routes,
    admin_chamados_routes,
    admin_relatorios_routes,
    admin_solicitacoes_verificacoes_routes
)
from routes.contratante import (
    contratante_avaliacoes_realizadas_routes,
    contratante_avaliacoes_recebidas_routes,
    contratante_chat_routes,
    contratante_contratacao_routes,
    contratante_contratante_routes,
    contratante_cuidadores_routes
)
from routes.cuidador import (
    cuidador_agenda_routes,
    cuidador_avaliacoes_realizadas_routes,
    cuidador_avaliacoes_recebidas_routes,
    cuidador_chats_routes,
    cuidador_contratacoes_recebidas_routes,
    cuidador_cuidador_routes,
    cuidador_especializacoes_routes,
    cuidador_solicitacoes_routes
)



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="uma_chave_secreta_aleatoria")
SECRET_KEY = secrets.token_urlsafe(32)

# # Adicionar middleware de sessão
# app.add_middleware(
#     SessionMiddleware, 
#     secret_key=SECRET_KEY,
#     max_age=3600,  # Sessão expira em 1 hora
#     same_site="lax",
#     https_only=False  # Em produção, mude para True com HTTPS
# )

administrador_repo.criar_tabela()
agenda_repo.criar_tabela()
atendimento_repo.criar_tabela()
avaliacao_repo.criar_tabela()
chamado_repo.criar_tabela()
chat_repo.criar_tabela()
cliente_repo.criar_tabela()
contratacao_repo.criar_tabela()
cuidador_repo.criar_tabela()
especialidade_repo.criar_tabela()
especialidade_cuidador_repo.criar_tabela()
solicitacao_repo.criar_tabela()
usuario_repo.criar_tabela()

app.include_router(public_routes)
app.include_router(admin_administradores_routes.router)
app.include_router(admin_avaliacoes_routes.router)
app.include_router(admin_chamados_routes.router)
app.include_router(admin_relatorios_routes.router)
app.include_router(admin_solicitacoes_verificacoes_routes.router)
app.include_router(contratante_avaliacoes_realizadas_routes.router)
app.include_router(contratante_avaliacoes_recebidas_routes.router)
app.include_router(contratante_chat_routes.router)
app.include_router(contratante_contratacao_routes.router)
app.include_router(contratante_cuidadores_routes.router)
app.include_router(contratante_contratante_routes.router)
app.include_router(cuidador_agenda_routes.router)
app.include_router(cuidador_avaliacoes_realizadas_routes.router)
app.include_router(cuidador_avaliacoes_recebidas_routes.router)
app.include_router(cuidador_chats_routes.router)
app.include_router(cuidador_contratacoes_recebidas_routes.router)
app.include_router(cuidador_cuidador_routes.router)
app.include_router(cuidador_especializacoes_routes.router)
app.include_router(cuidador_solicitacoes_routes.router)
app.include_router(perfil_router)        # para upload de foto
app.include_router(perfil_dados_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8082, reload=True)

