from datetime import datetime
from fastapi import APIRouter, File, Form, Request, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data.cliente.cliente_model import Cliente
from data.cliente import cliente_repo
from data.cuidador.cuidador_model import Cuidador
from data.cuidador import cuidador_repo
from data.usuario.usuario_model import Usuario
from data.usuario import usuario_repo
from util.security import criar_hash_senha, verificar_senha
from util.auth_decorator import criar_sessao, obter_usuario_logado, esta_logado
from util.template_util import criar_templates

router = APIRouter() 
templates = criar_templates("templates/auth")

@router.get("/")
async def get_login(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

# @router.get("/login")
# async def get_login(request: Request): 
#     return templates.TemplateResponse("login.html", {"request": request})
@router.get("/login")
async def get_login(request: Request, redirect: str = None):
    # Se já está logado, redirecionar conforme o perfil
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
    # Buscar usuário pelo email
    usuario = usuario_repo.obter_por_email(email)
    
    if not usuario or not verificar_senha(senha, usuario.senha):
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "erro": "Email ou senha inválidos",
                "email": email,
                "redirect": redirect
            }
        )
    
    # Criar sessão
    usuario_dict = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil,
        "foto": usuario.foto
    }
    criar_sessao(request, usuario_dict)
    
    # Redirecionar de acordo com o perfil ou redirect
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
    fotoPerfil: str = Form(None)
):
    try:
        # Verificar se o e-mail já está cadastrado
        if usuario_repo.obter_por_email(email):
            return templates.TemplateResponse(
                "cadastro_contratante.html",
                {"request": request, "erro": "Email já cadastrado"}
            )

        senha_hash = criar_hash_senha(senha)

        # Criar objeto Cliente
        cliente = Cliente(
            id=0,
            nome=nome,
            dataNascimento=dataNascimento,
            email=email,
            telefone=telefone,
            cpf=cpf,
            senha=senha_hash,
            perfil="contratante",  # Garantir que está como "contratante"
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
            parentesco_paciente=parentesco_paciente
        )

        # Fallback defensivo: garantir que perfil está definido
        if not cliente.perfil:
            cliente.perfil = "contratante"

        print(f"[DEBUG] Tentando cadastrar cliente com perfil: {cliente.perfil}")

        cliente_id = cliente_repo.inserir(cliente)

        if not cliente_id:
            return templates.TemplateResponse(
                "cadastro_contratante.html",
                {"request": request, "erro": "Erro ao cadastrar contratante. Tente novamente."}
            )

        print(f"[SUCESSO] Contratante cadastrado com sucesso! ID: {cliente_id}")
        return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)

    except Exception as e:
        print(f"[ERRO] Erro ao cadastrar contratante: {e}")
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