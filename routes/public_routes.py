from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from data.usuario import usuario_repo

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
    senha: str = Form(...)
):
    usuario = usuario_repo.obter_por_email(email)

    if usuario and usuario["senha"] == senha:
        response = RedirectResponse(url="/painel", status_code=HTTP_302_FOUND)
        response.set_cookie("usuario_id", str(usuario["id_usuario"]))
        return response
    else:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "erro": "Email ou senha inválidos. Tente novamente."
            }
        )


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
async def get_cadastro_contratante(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...),
    endereco: str = Form(...),
    cpf: str = Form(...),
    parentesco_paciente: str = Form(...)):
    return templates.TemplateResponse("cadastro_contratante.html", {"request": request})


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

