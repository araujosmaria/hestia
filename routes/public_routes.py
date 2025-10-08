from datetime import datetime
from fastapi import APIRouter, File, Form, Request, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo
from data.usuario.usuario_model import *
from data.usuario import usuario_repo
from util.security import criar_hash_senha, verificar_senha
from util.auth_decorator import criar_sessao, obter_usuario_logado, esta_logado
from util.template_util import criar_templates
from dtos.login_dto import LoginDTO  
import json
import os
import uuid

router = APIRouter() 
templates = criar_templates("templates/auth")


# Função auxiliar para salvar imagem
async def salvar_imagem(foto: UploadFile):
    if foto is None:
        return None

    ext = foto.filename.split(".")[-1]
    nome_arquivo = f"{uuid.uuid4()}.{ext}"
    caminho = f"static/img/perfil/{nome_arquivo}"
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    with open(caminho, "wb") as buffer:
        buffer.write(await foto.read())

    return nome_arquivo


@router.get("/")
async def get_login(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login")
async def get_login(request: Request, redirect: str = None):
    # Se já está logado, redireciona conforme o perfil
    if esta_logado(request):
        usuario = obter_usuario_logado(request)
        if usuario["perfil"] == "cuidador":
            return RedirectResponse("/cuidador/home_cuidador", status.HTTP_303_SEE_OTHER)
        elif usuario["perfil"] == "contratante":
            return RedirectResponse("/contratante/home_contratante", status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse("/", status.HTTP_303_SEE_OTHER)
    
    return templates.TemplateResponse(
        "login.html", 
        {"request": request, "redirect": redirect}
    )


@router.post("/login")
async def post_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    redirect: str = Form(None)
):
    # Validação via DTO LoginDTO
    try:
        login_dto = LoginDTO(email=email, senha=senha)
    except Exception as e:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "erro": str(e),
                "email": email,
                "redirect": redirect
            }
        )

    usuario = usuario_repo.obter_por_email(login_dto.email)
    if not usuario or not verificar_senha(login_dto.senha, usuario.senha):
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "erro": "Email ou senha inválidos",
                "email": email,
                "redirect": redirect
            }
        )

    usuario_dict = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil,
        "foto": usuario.foto
    }
    criar_sessao(request, usuario_dict)

    if redirect:
        return RedirectResponse(redirect, status.HTTP_303_SEE_OTHER)

    if usuario.perfil == "cuidador":
        return RedirectResponse("/cuidador/home_cuidador", status.HTTP_303_SEE_OTHER)
    elif usuario.perfil == "contratante":
        return RedirectResponse("/contratante/home_contratante", status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse("/", status.HTTP_303_SEE_OTHER)


@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# -----------------------------
# CADASTRO CUIDADOR
# -----------------------------

@router.get("/cadastro_cuidador")
async def get_cadastro_cuidador(request: Request):
    return templates.TemplateResponse("cadastro_cuidador.html", {"request": request})

@router.post("/cadastro_cuidador")
async def post_cadastro_cuidador(
    # tirar as (...), roda f5, cadastra normalmente, vai dando f10 e vendo onde esta o erro no breakpoint 
    request: Request,
    nome: str = Form(),
    dataNascimento: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form(),
    senha: str = Form(),
    cep: str = Form(),
    logradouro: str = Form(),
    numero: str = Form(),
    complemento: str = Form(None),
    bairro: str = Form(),
    cidade: str = Form(),
    estado: str = Form(),
    experiencia: str = Form(),
    valorHora: float = Form(),
    escolaridade: str = Form(),
    apresentacao: str = Form(),
    cursos: str = Form(None),
    confirmarSenha: str = Form(),
    termos: bool = Form(...),
    verificacao: bool = Form(False),
    comunicacoes: bool = Form(False),
):
    try:
        if usuario_repo.obter_por_email(email):
            return templates.TemplateResponse(
                "cadastro_cuidador.html",
                {"request": request, "erro": "Email já cadastrado"}
            )

        senha_hash = criar_hash_senha(senha)


        cuidador = Cuidador(
            id=0,
            nome=nome,
            dataNascimento=dataNascimento,
            email=email,
            telefone=telefone,
            cpf=cpf,
            senha=senha_hash,
            perfil="cuidador",
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat(),
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            ativo=True,
            experiencia=experiencia,
            valorHora=valorHora,
            escolaridade=escolaridade,
            apresentacao=apresentacao,
            cursos=cursos,
            confirmarSenha=confirmarSenha,
            termos=termos,
            verificacao=verificacao,
            comunicacoes=comunicacoes
        )

        usuario_id = cuidador_repo.inserir(cuidador)
        
        if not usuario_id:
            return templates.TemplateResponse(
                "cadastro_cuidador.html",
                {"request": request, "erro": "Erro ao cadastrar usuário. Tente novamente."}
            )

        print(f"Cuidador cadastrado com sucesso! ID: {usuario_id}")
        return RedirectResponse("/login", status_code=303)
        
    except Exception as e:
        print(f"Erro ao cadastrar cuidador: {e}")
        return templates.TemplateResponse(
            "cadastro_cuidador.html",
            {"request": request, "erro": "Erro interno ao cadastrar. Tente novamente."}
        )

# -----------------------------
# CADASTRO CONTRATANTE
# -----------------------------

@router.get("/cadastro_contratante")
async def get_cadastro_contratante(request: Request):
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
    complemento: str = Form(None),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    parentesco_paciente: str = Form(...),
    fotoPerfil: UploadFile = File(None),
    confirmarSenha: str = Form(...),
    termos: bool = Form(...),
    verificacao: bool = Form(False),
    comunicacoes: bool = Form(False),
):
    try:
        if usuario_repo.obter_por_email(email):
            return templates.TemplateResponse(
                "cadastro_contratante.html",
                {"request": request, "erro": "Email já cadastrado"}
            )

        senha_hash = criar_hash_senha(senha)

        nome_arquivo_foto = await salvar_imagem(fotoPerfil)

        cliente = Cliente(
            id=0,
            nome=nome,
            dataNascimento=dataNascimento,
            email=email,
            telefone=telefone,
            cpf=cpf,
            senha=senha_hash,
            perfil="contratante",
            foto=nome_arquivo_foto,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat(),
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            ativo=True,
            parentesco_paciente=parentesco_paciente,
            termos=termos,
            verificacao=verificacao,
            comunicacoes=comunicacoes
        )

        print(f"Tentando cadastrar cliente com perfil: {cliente.perfil}")

        usuario_id = cliente_repo.inserir(cliente)

        if not usuario_id:
            return templates.TemplateResponse(
                "cadastro_contratante.html",
                {"request": request, "erro": "Erro ao cadastrar contratante. Tente novamente."}
            )

        print(f"Contratante cadastrado com sucesso! ID: {usuario_id}")

        return RedirectResponse("/login", status_code=303)

    except Exception as e:
        print(f"Erro ao cadastrar contratante: {e}")
        return templates.TemplateResponse(
            "cadastro_contratante.html",
            {"request": request, "erro": "Erro interno ao cadastrar. Tente novamente."}
        )


@router.get("/redefinicao_senha")
async def get_redefinicao_senha(request: Request):
    return templates.TemplateResponse("redefinicao_senha.html", {"request": request})

@router.get("/confirmar_redefinir_senha")
async def get_confirmar_redefinir_senha(request: Request):
    return templates.TemplateResponse("confirmar_redefinir_senha.html", {"request": request})
