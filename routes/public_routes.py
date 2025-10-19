from datetime import datetime
from urllib import request
from fastapi import APIRouter, File, Form, Request, UploadFile, status
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data import cuidador
from data import cliente
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.cuidador import cuidador_repo
import sqlite3 
from data.cuidador.cuidador_model import Cuidador
from data.usuario import usuario_repo
from util.security import criar_hash_senha, salvar_foto, verificar_senha
from util.auth_decorator import criar_sessao, obter_usuario_logado, esta_logado
from util.template_util import criar_templates
from dtos.login_dto import LoginDTO  
import json
import os
import uuid
from fastapi.responses import RedirectResponse, HTMLResponse
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import inserir as inserir_usuario, obter_por_cpf
from data.cliente.cliente_repo import inserir as inserir_cliente
from passlib.context import CryptContext
from util.auth_decorator import criar_sessao, destruir_sessao 

router = APIRouter() 
templates = criar_templates("templates/auth")

# async def salvar_imagem(foto: UploadFile):
#     if foto is None:
#         return None

#     ext = foto.filename.split(".")[-1]
#     nome_arquivo = f"{uuid.uuid4()}.{ext}"
#     caminho = f"static/img/perfil/{nome_arquivo}"
#     os.makedirs(os.path.dirname(caminho), exist_ok=True)

#     with open(caminho, "wb") as buffer:
#         buffer.write(await foto.read())

#     return nome_arquivo


@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/login")
async def get_login(request: Request, redirect: str = None):
   
    if esta_logado(request):
        usuario = obter_usuario_logado(request)
        if usuario.perfil == "cuidador":
            return RedirectResponse("/cuidador/home_cuidador", status_code=303)
        elif usuario.perfil == "contratante":
            return RedirectResponse("/contratante/home_contratante", status_code=303)
        else:
            return RedirectResponse("/", status_code=303)
    
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "redirect": redirect}
    )

@router.post("/login")
async def post_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    usuario = usuario_repo.obter_por_email(email)  
    if not usuario or not verificar_senha(senha, usuario.senha):
        return templates.TemplateResponse("login.html", {"request": request, "erro": "Usuário ou senha incorretos"})
    
    usuario_dict = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil
    }
    criar_sessao(request, usuario_dict)  
    if usuario.perfil == "contratante":
        return RedirectResponse("/contratante/home_contratante", status_code=303)
    else:
        return RedirectResponse("/cuidador/home_cuidador", status_code=303)
 # ou o nome da tua função para encerrar a sessão

@router.get("/logout")
async def logout(request: Request):
    destruir_sessao(request)  # limpa a sessão
    return RedirectResponse("/login", status_code=303)

@router.get("/cadastro", response_class=HTMLResponse)
async def escolher_tipo_usuario(request: Request):
    # Renderiza página para escolher cuidador ou contratante
    return templates.TemplateResponse("cadastro.html", {"request": request})


@router.get("/cadastro_cuidador", response_class=HTMLResponse)
async def cadastro_cuidador_form(request: Request):
    return templates.TemplateResponse("cadastro_cuidador.html", {"request": request})

@router.post("/cadastro_cuidador")
async def cadastro_cuidador_post(
    request: Request,
    nome: str = Form(...),
    dataNascimento: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...),
    senha: str = Form(...),
    cep: str = Form(...),
    logradouro: str = Form(...),
    numero: str = Form(...),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    experiencia: str = Form(...),
    escolaridade: str = Form(...),
    apresentacao: str = Form(...),
    cursos: bool = Form(...),
    data_cadastro: str = Form(...),
    fotoPerfil: UploadFile | None = File(None)
):

    senha_hash = criar_hash_senha(senha)

    if fotoPerfil and fotoPerfil.filename:
        conteudo_foto = await fotoPerfil.read()
        foto_path = salvar_foto(conteudo_foto, fotoPerfil.filename)
    else:
        foto_path = None

    cuidador_obj = Cuidador(
        id=0,
        nome=nome,
        dataNascimento=dataNascimento,
        email=email,
        telefone=telefone,
        cpf=cpf,
        senha=senha_hash,      
        foto=foto_path,        
        cep=cep,
        logradouro=logradouro,
        numero=numero,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
        perfil="cuidador",
        experiencia=experiencia,
        escolaridade=escolaridade,
        apresentacao=apresentacao,
        cursos=cursos,
        data_cadastro=data_cadastro
    )

    usuario_id = cuidador_repo.inserir(cuidador)  
    cuidador_obj.id = usuario_id

    usuario_dict = {
        "id": cuidador_obj.id,
        "nome": cuidador_obj.nome,
        "email": cuidador_obj.email,
        "perfil": cuidador_obj.perfil,
        "foto": cuidador_obj.foto
    }

    return RedirectResponse("/cuidador/home_cuidador", status_code=303)


@router.get("/cadastro_contratante", response_class=HTMLResponse)
async def cadastro_contratante_form(request: Request):
    return templates.TemplateResponse("cadastro_contratante.html", {"request": request})

@router.post("/cadastro_contratante")
async def post_cadastro_contratante(
    request: Request,
    nome: str = Form(...),
    dataNascimento: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...),
    senha: str = Form(...),
    cep: str = Form(...),
    logradouro: str = Form(...),
    numero: str = Form(...),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    parentesco_paciente: str = Form(...),
    fotoPerfil: UploadFile | None = File(None)
):
    # Cria hash da senha
    senha_hash = criar_hash_senha(senha)

    if fotoPerfil and fotoPerfil.filename:
        conteudo_foto = await fotoPerfil.read()
        foto_path = salvar_foto(conteudo_foto, fotoPerfil.filename)
    else:
        foto_path = None
    
    cliente_obj = Cliente(
        id=0,
        nome=nome,
        dataNascimento=dataNascimento,
        email=email,
        telefone=telefone,
        cpf=cpf,
        senha=senha_hash,
        cep=cep,
        logradouro=logradouro,
        numero=numero,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
        perfil="contratante",
        parentesco_paciente=parentesco_paciente,
        foto=foto_path
        )

    # Insere no banco e atualiza o ID
    usuario_id = cliente_repo.inserir(cliente_obj)
    cliente_obj.id = usuario_id

    # Cria sessão
    criar_sessao(request, {
        "id": cliente_obj.id,
        "nome": cliente_obj.nome,
        "email": cliente_obj.email,
        "perfil": cliente_obj.perfil,
        "foto":cliente_obj.foto
    })

    # Redireciona
    return RedirectResponse("/contratante/home_contratante", status_code=303)


@router.get("/redefinicao_senha")
async def get_redefinicao_senha(request: Request):
    return templates.TemplateResponse("redefinicao_senha.html", {"request": request})

@router.get("/confirmar_redefinir_senha")
async def get_confirmar_redefinir_senha(request: Request):
    return templates.TemplateResponse("confirmar_redefinir_senha.html", {"request": request})
