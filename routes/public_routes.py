from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data.cliente.cliente_model import Cliente
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
    criar_sessao(request, usuario_dict)  # se tiver função de sessão

    # Redirecionar de acordo com perfil ou redirect
    if redirect:
        return RedirectResponse(redirect, status_code=303)

    if usuario["perfil"] == "cuidador":
        url_destino = "/cuidador/home_cuidador"
    elif usuario["perfil"] == "contratante":
        url_destino = "/contratante/home_contratante"
    else:
        url_destino = "/painel"  # fallback

    return RedirectResponse(url=url_destino, status_code=303)




@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


@router.get("/cadastro_cuidador")
async def get_cadastro_cuidador(request: Request):
    return templates.TemplateResponse("cadastro_cuidador.html", {"request": request})

@router.post("/cadastro_cuidador")
async def get_cadastro_cuidador(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    endereco: str = Form(...),
    cpf: str = Form(...),
    inicio_profissional: str = Form(...)):
    return templates.TemplateResponse("cadastro_cuidador.html", {"request": request})

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
    # Verificar se email já existe
    if usuario_repo.obter_por_email(email):
        return templates.TemplateResponse(
            "cadastro.html",
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
        perfil="contratante"  # perfil diferente do cliente
    )

    # Inserir usuário no banco
    usuario_id = usuario_repo.inserir(usuario)

    return RedirectResponse("/login", status_code=303)

   


@router.get("/redefinicao_senha")
async def get_redefinicao_senha(request: Request):
    return templates.TemplateResponse("redefinicao_senha.html", {"request": request})

# @router.post("/redefinicao_senha")
# async def post_redefinicao_senha(
#     request: Request,
#     email: str = Form(...),
#     nova_senha: str = Form(...)
# ):
#     try:
#         sucesso = usuario_repo.atualizar_senha(email, nova_senha)
#         if sucesso:
#             return RedirectResponse(
#                 url="/confirmar_redefinir_senha", status_code=status.HTTP_303_SEE_OTHER
#             )
#         else:
#             return templates.TemplateResponse("redefinicao_senha.html", {
#                 "request": request,
#                 "erro": "Não foi possível atualizar a senha. Verifique o email informado."
#             })
#     except Exception as e:
#         print(f"Erro ao redefinir senha: {e}")
#         return templates.TemplateResponse("redefinicao_senha.html", {
#             "request": request,
#             "erro": "Erro interno ao tentar redefinir a senha."
#         })


@router.get("/confirmar_redefinir_senha")
async def get_confirmar_redefinir_senha(request: Request):
    return templates.TemplateResponse("confirmar_redefinir_senha.html", {"request": request})

