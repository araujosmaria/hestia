from datetime import datetime
from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data.cliente.cliente_model import Cliente
from data.cuidador import cuidador_repo
from data.cuidador.cuidador_model import Cuidador
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from util.auth_decorator import criar_sessao
from util.security import criar_hash_senha, verificar_senha

router = APIRouter() 
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_login(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/login")
async def get_login(request: Request): 
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def post_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    redirect: str = Form(None)
):
    usuario = usuario_repo.obter_por_email(email)

    if not usuario or not verificar_senha(senha, usuario["senha"]):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "erro": "Email ou senha inválidos. Tente novamente."}
        )

    # Criar sessão ou cookie
    usuario_dict = {
        "id": usuario["id_usuario"],
        "nome": usuario["nome"],
        "email": usuario["email"],
        "perfil": usuario["perfil"],
        "foto": usuario.get("foto")
    }
    criar_sessao(request, usuario_dict)

    # Redirecionar de acordo com perfil ou redirect
    if redirect:
        return RedirectResponse(redirect, status_code=303)

    if usuario["perfil"] == "cuidador":
        url_destino = "cuidador/home_cuidador"
    elif usuario["perfil"] == "contratante":
        url_destino = "contratante/home_contratante"
    else:
        url_destino = "/painel"

    return RedirectResponse(url=url_destino, status_code=303)

@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.get("/cadastro_cuidador")
async def get_cadastro_cuidador(request: Request):
    return templates.TemplateResponse("cadastro_cuidador.html", {"request": request})

@router.post("/cadastro_cuidador")
async def post_cadastro_cuidador(
    request: Request,
    nome: str = Form(...),
    dataNascimento: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...),
    fotoPerfil: str = Form(None),
    senha: str = Form(...),
    cep: str = Form(...),
    logradouro: str = Form(...),
    numero: str = Form(...),
    complemento: str = Form(None),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    experiencia: str = Form(...),
    valorHora: float = Form(...),
    escolaridade: str = Form(...),
    apresentacao: str = Form(...),
    cursos: str = Form(None),
    confirmarSenha: str = Form(...),
    termos: bool = Form(...),
    verificacao: bool = Form(False),
    comunicacoes: bool = Form(False),
):
    try:
        # Verificar se email já existe
        if usuario_repo.obter_por_email(email):
            return templates.TemplateResponse(
                "cadastro_cuidador.html",
                {"request": request, "erro": "Email já cadastrado"}
            )

        # Criar hash da senha
        senha_hash = criar_hash_senha(senha)

        # Criar usuário cuidador
        cuidador = Cuidador(
            id=0,
            nome=nome,
            dataNascimento=dataNascimento,
            email=email,
            telefone=telefone,
            cpf=cpf,
            senha=senha_hash,
            perfil="cuidador",
            foto=fotoPerfil,
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

        # Inserir usuário no banco
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

@router.get("/cadastro_contratante")
async def get_cadastro_contratante(request: Request):
    return templates.TemplateResponse("cadastro_contratante.html", {"request": request})

@router.post("/cadastro_contratante")
async def post_cadastro_contratante(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    endereco: str = Form(...),
    cpf: str = Form(...),
    parentesco_paciente: str = Form(...)
):
    try:
        # Verificar se email já existe
        if usuario_repo.obter_por_email(email):
            return templates.TemplateResponse(
                "cadastro_contratante.html",  # Corrigido: estava retornando cadastro.html
                {"request": request, "erro": "Email já cadastrado"}
            )

        # Criar hash da senha
        senha_hash = criar_hash_senha(senha)

        # Criar usuário contratante
        usuario = Usuario(
            id=0,
            nome=nome,
            email=email,
            senha=senha_hash,
            telefone=telefone,
            endereco=endereco,
            cpf=cpf,
            parentesco_paciente=parentesco_paciente,
            perfil="contratante"
        )

        # Inserir usuário no banco com verificação
        usuario_id = usuario_repo.inserir(usuario)
        
        if not usuario_id:
            return templates.TemplateResponse(
                "cadastro_contratante.html",
                {"request": request, "erro": "Erro ao cadastrar usuário. Tente novamente."}
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