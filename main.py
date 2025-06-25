from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data.administrador import administrador_repo


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
 
 
administrador_repo.criar_tabela()


@app.get("/")
async def get_root():
    administradores = administrador_repo.obter_todos()
    response = templates.TemplateResponse("home.html", {"request": {}, "administradores": administradores})
    return response


@app.get("/admin/administradores")
async def get_administradores():
    administradores = administrador_repo.obter_todos()
    response = templates.TemplateResponse("administradores.html", {"request": {}, "administradores": administradores})
    return response


@app.get("/administradores/{id}")
async def get_administrador_por_id(id: int):
    administrador = administrador_repo.obter_por_id(id)
    response = templates.TemplateResponse("administrador.html", {"request": {}, "administrador": administrador})
    return response


@app.get("/admin/administradores/cadastrar")
async def get_administrador_cadastrar():
    response = templates.TemplateResponse("cadastrar_administrador.html", {"request": {}})
    return response


@app.post("/admin/administradores/cadastrar")
async def post_administrador_cadastrar(
    nome: str = Form(...),
    email: str = Form(...),
    senha: float = Form(...),
    telefone: int = Form(...),
    endereco: str = Form(...)
):
    administrador = administrador(0, nome, email, senha, telefone, endereco)  # 0 = autoincremento
    id_administrador = administrador_repo.inserir(administrador)
    if id_administrador == None:
        raise Exception("Erro ao inserir administrador.")
    else:
        return RedirectResponse("/administradors", status_code=303)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)