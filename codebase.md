# .gitignore

```
.venv
__pycache__
*.pyc
*.pyo
*.pyd

```

# .pytest_cache\.gitignore

```
# Created by pytest automatically.
*

```

# .pytest_cache\CACHEDIR.TAG

```TAG
Signature: 8a477f597d28d172789f06886806bc55
# This file is a cache directory tag created by pytest.
# For information about cache directory tags, see:
#	https://bford.info/cachedir/spec.html

```

# .pytest_cache\README.md

```md
# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

```

# .pytest_cache\v\cache\lastfailed

```
{
  "tests/test_especialidade_repo.py::TestEspecialidadeRepo::test_criar_tabela_especialidades": true,
  "tests/test_especialidade_repo.py::test_inserir_categoria": true,
  "tests/test_especialidade_repo.py::TestEspecialidadeRepo": true,
  "tests/test_especialidade_repo.py::TestEspecialidadeRepo::test_inserir_especialidade": true
}
```

# .pytest_cache\v\cache\nodeids

```
[
  "tests/test_especialidade_repo.py::TestEspecialidadeRepo::test_criar_tabela_especialidades",
  "tests/test_especialidade_repo.py::TestEspecialidadeRepo::test_inserir_especialidade"
]
```

# .vscode\launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--host",
                "127.0.0.1",
                "--port",
                "8000",
                "--reload"
            ],
            "jinja": true,
            "justMyCode": true,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

# .vscode\settings.json

```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

# ATIVIDADE.md

```md
# Atividade

## Criar Listagem de Clientes
Id -> INTEGER PRIMARY KEY AUTOINCREMENT
Nome -> TEXT NOT NULL
CPF -> TEXT NOT NULL
Email -> TEXT NOT NULL
Telefone -> TEXT NOT NULL
Senha -> TEXT NOT NULL

### Artefatos Esperados
data/cliente_sql.py
data/cliente_model.py
data/cliente_repo.py
templates/clientes.html

```

# dados.db

This is a binary file of the type: Binary

# data\administrador\__init__.py

```py

```

# data\administrador\administrador_model.py

```py
from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Administrador(Usuario):
    id: int
```

# data\administrador\administrador_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.administrador.administrador_model import Administrador
from data.administrador.administrador_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ADMINISTRADOR)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de administradores: {e}")
        return False  

def inserir(administrador: Administrador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ADMINISTRADOR, (
            administrador.nome,  
            administrador.email, 
            administrador.senha,
            administrador.telefone, 
            administrador.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ADMINISTRADOR)
        rows = cursor.fetchall()
        administradores = [
            Administrador(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return administradores
```

# data\administrador\administrador_sql.py

```py
CRIAR_TABELA_ADMINISTRADOR = """
CREATE TABLE IF NOT EXISTS administrador (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL,
telefone TEXT NOT NULL,
endereco TEXT NOT NULL,
)
"""

INSERIR_ADMINISTRADOR = """
INSERT INTO administrador (nome, email, senha, telefone, endereco ) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_ADMINISTRADOR = """
SELECT 
id, nome, email, senha, telefone, endereco
FROM administrador
ORDER BY nome
""" 
```

# data\agenda\__init__.py

```py

```

# data\agenda\agenda_model.py

```py
from dataclasses import dataclass


@dataclass
class Agenda:
    id: int
    dataHora: datetime
    disponibilidade: boolean
    id_cuidador: int
    
```

# data\agenda\agenda_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.agenda.agenda_model import Agenda
from data.agenda.agenda_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_AGENDA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de agendas: {e}")
        return False  

def inserir(agenda: Agenda) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_AGENDA, (
            agenda.dataHrora,  
            agenda.disponibilidade))
        return cursor.lastrowid

def obter_todos() -> list[Agenda]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_AGENDA)
        rows = cursor.fetchall()
        agendas = [
            Agenda(
                id=row["id"], 
                dataHrora=row["dataHrora"], 
                disponibilidade=row["disponibilidade"]) 
                for row in rows]
        return agendas
```

# data\agenda\agenda_sql.py

```py
CRIAR_TABELA_AGENDA = """
CREATE TABLE IF NOT EXISTS agenda (
    id_agenda INTEGER PRIMARY KEY AUTOINCREMENT,
    dataHora DATETIME NOT NULL,
    disponibilidade BOOLEAN NOT NULL,
    id_cuidador INTEGER NOT NULL,
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador)
)
"""

INSERIR_AGENDA = """
INSERT INTO agenda (dataHora, disponibilidade, id_cuidador) 
VALUES (?, ?, ?)
"""

OBTER_TODOS_AGENDA = """
SELECT 
    id_agenda, dataHora, disponibilidade, id_cuidador
FROM agenda
ORDER BY dataHora
"""

```

# data\atendimento\__init__.py

```py

```

# data\atendimento\atendimento_model.py

```py
from dataclasses import dataclass


@dataclass
class Atendimento:
    id: int
    dataInicio: datetime
    dataFim: datetime
    id_cliente: int
    id_cuidador: int
    
    
```

# data\atendimento\atendimento_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.atendimento.atendimento_model import Atendimento
from data.atendimento.atendimento_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ATENDIMENTO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de atendimentos: {e}")
        return False  

def inserir(atendimento: Atendimento) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ATENDIMENTO, (
            atendimento.dataInicio,  
            atendimento.dataFim))
        return cursor.lastrowid

def obter_todos() -> list[Atendimento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ATENDIMENTO)
        rows = cursor.fetchall()
        atendimentos = [
            Atendimento(
                id=row["id"], 
                dataInicio=row["dataInicio"], 
                dataFim=row["dataFim"]) 
                for row in rows]
        return atendimentos
```

# data\atendimento\atendimento_sql.py

```py
CRIAR_TABELA_ATENDIMENTO = """
CREATE TABLE IF NOT EXISTS atendimento (
    id_atendimento INTEGER PRIMARY KEY AUTOINCREMENT,
    dataInicio DATETIME NOT NULL,
    dataFim DATETIME NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_cuidador INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador)
)
"""

INSERIR_ATENDIMENTO = """
INSERT INTO atendimento (dataInicio, dataFim, id_cliente, id_cuidador) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_ATENDIMENTO = """
SELECT 
    id_atendimento, dataInicio, dataFim, id_cliente, id_cuidador
FROM atendimento
ORDER BY dataInicio
"""

```

# data\avaliacao\__init__.py

```py

```

# data\avaliacao\avaliacao_model.py

```py
from dataclasses import dataclass


@dataclass
class Avaliação:
    id: int
    nota: float
    comentario: str
    dataAvaliacao: date
    id_atendimento: int
   
    
    
```

# data\avaliacao\avaliacao_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.avaliacao.avaliacao_model import Avaliacao
from data.avaliacao.avaliacao_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_AVALIACAO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de avaliações: {e}")
        return False  

def inserir(avaliacao: Avaliacao) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_AVALIACAO, (
            avaliacao.nota,  
            avaliacao.comentario, 
            avaliacao.dataAvaliacao))
        return cursor.lastrowid

def obter_todos() -> list[Avaliacao]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_AVALIACAO)
        rows = cursor.fetchall()
        avaliacoes = [
            Avaliacao(
                id=row["id"], 
                nota=row["nota"], 
                comentario=row["comentario"],
                dataAvaliacao=row["dataAvaliacao"]) 
                for row in rows]
        return avaliacoes
```

# data\avaliacao\avaliacao_sql.py

```py
CRIAR_TABELA_AVALIACAO = """
CREATE TABLE IF NOT EXISTS avaliacao (
id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
nota FLOAT,
comentario TEXT NOT NULL,
dataAvaliacao DATE,
id_atendimento INTEGER NOT NULL,
FOREIGN KEY (id_atendimento) REFERENCES atendimento(id_atendimento)
);
"""


INSERIR_AVALIACAO = """
INSERT INTO avaliacao (nota, comentario, dataAvaliacao, id_atendimento) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_AVALIACAO = """
SELECT 
    id_avaliacao, nota, comentario, dataAvaliacao, id_atendimento
FROM avaliacao
ORDER BY dataAvaliacao DESC
""" 
```

# data\chamado\__init__.py

```py

```

# data\chamado\chamado_model.py

```py
from dataclasses import dataclass


@dataclass
class Chamado:
    id: int
    titulo: str
    descricao: str
    status: str
    data_criacao: datetime
    id_administrador: int
    
```

# data\chamado\chamado_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.chamado.chamado_model import Chamado
from data.chamado.chamado_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CHAMADO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de chamados: {e}")
        return False  

def inserir(chamado: Chamado) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CHAMADO, (
            chamado.titulo,  
            chamado.descricao, 
            chamado.status,
            chamado.dataCriacao))
        return cursor.lastrowid

def obter_todos() -> list[Chamado]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CHAMADOS)
        rows = cursor.fetchall()
        chamados = [
            Chamado(
                id=row["id"], 
                titulo=row["titulo"], 
                descricao=row["descricao"],
                status=row["status"],
                dataCriacao=row["dataCriacao"]) 
                for row in rows]
        return chamados
```

# data\chamado\chamado_sql.py

```py
CRIAR_TABELA_CHAMADO = """
CREATE TABLE IF NOT EXISTS chamado (
    id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL,
    dataCriacao DATETIME NOT NULL,
    id_administrador INTEGER NOT NULL,
    FOREIGN KEY (id_administrador) REFERENCES administrador(id)
)
"""

INSERIR_CHAMADO = """
INSERT INTO chamado (titulo, descricao, status, dataCriacao, id_administrador) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_CHAMADOS = """
SELECT 
    id_chamado, titulo, descricao, status, dataCriacao, id_administrador
FROM chamado
ORDER BY dataCriacao DESC
"""

```

# data\chat\__init__.py

```py

```

# data\chat\chat_model.py

```py
from dataclasses import dataclass


@dataclass
class Chat:
    id: int
    conteudo: txt
    dataHora: datetime
    id_remetente: int
    id_destinatario: int
    
     
     
```

# data\chat\chat_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.chat.chat_model import Chat
from data.chat.chat_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CHAT)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de chat: {e}")
        return False  

def inserir(chat: Chat) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CHAT, (
            chat.conteudo,  
            chat.dataHora))
        return cursor.lastrowid

def obter_todos() -> list[Chat]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CHATS)
        rows = cursor.fetchall()
        chamados = [
            Chat(
                id=row["id"], 
                conteudo=row["conteudo"], 
                dataHor=row["dataHora"]) 
                for row in rows]
        return chamados
```

# data\chat\chat_sql.py

```py
CRIAR_TABELA_CHAT = """
CREATE TABLE IF NOT EXISTS chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    dataHora TEXT NOT NULL,
    id_remetente INTEGER NOT NULL,
    id_destinatario INTEGER NOT NULL
)
"""

INSERIR_CHAT = """
INSERT INTO chat (conteudo, dataHora, id_remetente, id_destinatario) 
VALUES (?, ?, ?, ?)
"""

OBTER_TODOS_CHATS = """
SELECT 
    id, conteudo, dataHora, id_remetente, id_destinatario 
FROM chat
ORDER BY dataHora
""" 
```

# data\cliente\__init__.py

```py

```

# data\cliente\cliente_model.py

```py
from dataclasses import dataclass
from data.usuario_model import Usuario

@dataclass
class Cliente(Usuario):
    id: int
    
```

# data\cliente\cliente_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CLIENTE)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de clientes: {e}")
        return False  

def inserir(cliente: Cliente) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CLIENTE, (
            cliente.nome,  
            cliente.email, 
            cliente.senha,
            cliente.telefone, 
            cliente.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CLIENTE)
        rows = cursor.fetchall()
        clientes = [
            Cliente(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return clientes
```

# data\cliente\cliente_sql.py

```py
CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY,
    FOREIGN KEY (id_cliente) REFERENCES usuario(id_usuario)
)
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (id_cliente)
VALUES (?)
"""

OBTER_TODOS_CLIENTE = """
SELECT 
c.id_cliente, u.nome, u.email
FROM cliente c
JOIN usuario u ON c.id_cliente = u.id_usuario
ORDER BY u.nome
"""
```

# data\cuidador\__init__.py

```py

```

# data\cuidador\cuidador_model.py

```py
from dataclasses import dataclass
from data.usuario_model import Usuario

@dataclass
class Cuidador(Usuario):
    experiencia: int
    
```

# data\cuidador\cuidador_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.cuidador.cuidador_model import Cuidador
from data.cuidador.cuidador_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_CUIDADOR)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de cuidadores: {e}")
        return False  

def inserir(cuidador: Cuidador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CUIDADOR, (
            cuidador.nome,  
            cuidador.email, 
            cuidador.senha,
            cuidador.telefone, 
            cuidador.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Cuidador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_CUIDADOR)
        rows = cursor.fetchall()
        cuidadores = [
            Cuidador(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return cuidadores
    
def adicionar_especialidade(cuidador_id: int, especialidade: str) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cuidador_especialidades (cuidador_id, especialidade)
            VALUES (?, ?)
        """, (cuidador_id, especialidade))
        return cursor.rowcount > 0

def obter_especialidades(cuidador_id: int) -> list[str]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT especialidade FROM cuidador_especialidades
            WHERE cuidador_id = ?
        """, (cuidador_id,))
        rows = cursor.fetchall()
        return [row["especialidade"] for row in rows]

```

# data\cuidador\cuidador_sql.py

```py
CRIAR_TABELA_CUIDADOR = """
CREATE TABLE IF NOT EXISTS cuidador (
    id_cuidador INTEGER PRIMARY KEY,
    FOREIGN KEY (id_cuidador) REFERENCES usuario(id_usuario)
)
"""

INSERIR_CUIDADOR = """
INSERT INTO cuidador (id_cuidador, experiencia)
VALUES (?, ?)
"""

OBTER_TODOS_CUIDADOR = """
SELECT 
cu.id_cuidador, u.nome, cu.experiencia
FROM cuidador cu
JOIN usuario u ON cu.id_cuidador = u.id_usuario
ORDER BY u.nome
"""

```

# data\especialidade_cuidador\__init__.py

```py

```

# data\especialidade_cuidador\especialidade_cuidador_model.py

```py
from dataclasses import dataclass


@dataclass
class Especialidade_Cuidador:
    id_cuidador: int
    id_especialidade: int
    
    
```

# data\especialidade_cuidador\especialidade_cuidador_sql.py

```py
CRIAR_TABELA_ESPECIALIDADE_CUIDADOR = """
CREATE TABLE IF NOT EXISTS especialidade_cuidador (
    id_cuidador INTEGER,
    id_especialidade INTEGER,
    PRIMARY KEY (id_cuidador, id_especialidade),
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador) ON DELETE CASCADE,
    FOREIGN KEY (id_especialidade) REFERENCES especialidade(id_especialidade) ON DELETE CASCADE
)
"""

INSERIR_ESPECIALIDADE_CUIDADOR = """
INSERT INTO especialidade_cuidador (id_cuidador, id_especialidade)
VALUES (?, ?)
"""    

OBTER_TODOS_ESPECIALIDADE_CUIDADOR = """
SELECT 
    ec.id_cuidador,
    c.experiencia,
    ec.id_especialidade,
    e.nome AS nome_especialidade
FROM 
    especialidade_cuidador ec
JOIN 
    cuidador c ON ec.id_cuidador = c.id_cuidador
JOIN 
    especialidade e ON ec.id_especialidade = e.id_especialidade
ORDER BY 
    c.id_cuidador;
"""
```

# data\especialidade\__init__.py

```py

```

# data\especialidade\especialidade_model.py

```py
from dataclasses import dataclass


@dataclass
class Especialidade:
    id: int
    nome: str
    
    
```

# data\especialidade\especialidade_repo.py

```py
from asyncio import open_connection
import sqlite3
from typing import Optional

from data.especialidade.especialidade_model import Especialidade
from data.especialidade.especialidade_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_ESPECIALIDADE) 
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de especialidades: {e}")
        return False  

def inserir(especialidade: Especialidade) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ESPECIALIDADE, (
            especialidade.nome))
        return cursor.lastrowid
    
def obter_por_id(especialidade_id: int) -> Optional[Especialidade]:
    with open_connection() as conn:
        conn.row_factory = sqlite3.Row  # garante acesso por nome de coluna
        cursor = conn.cursor()
        cursor.execute(OBTER_ESPECIALIDADE_POR_ID, (especialidade_id,))
        row = cursor.fetchone()
        if row:
            return Especialidade(
                id=row["id"],
                nome=row["nome"]
            )
        return None


def obter_todos() -> list[Especialidade]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ESPECIALIDADE)
        rows = cursor.fetchall()
        especialidade = [
            Especialidade(
                id=row["id"], 
                nome=row["nome"]) 
                for row in rows]
        return especialidade
```

# data\especialidade\especialidade_sql.py

```py
CRIAR_TABELA_ESPECIALIDADE = """
CREATE TABLE IF NOT EXISTS especialidade (
id_especialidade INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR NOT NULL
)
"""

INSERIR_ESPECIALIDADE = """
INSERT INTO especialidade (nome) 
VALUES (?)
"""

OBTER_TODOS_ESPECIALIDADE = """
SELECT 
id_especialidade, nome
FROM especialidade
ORDER BY nome ASC
""" 

OBTER_ESPECIALIDADE_POR_ID = """
SELECT 
id_especialidade, nome
FROM especialidade
WHERE id_especialidade = ?
"""
```

# data\usuario\__init__.py

```py

```

# data\usuario\usuario_model.py

```py
from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nome: str
    endereco: str
    email: str
    telefone: str
    senha: str
```

# data\usuario\usuario_repo.py

```py
from asyncio import open_connection
from typing import Optional

from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *


def criar_tabela() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_USUARIO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de usuarios: {e}")
        return False  

def inserir(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO, (
            usuario.nome,  
            usuario.email, 
            usuario.senha,
            usuario.telefone, 
            usuario.endereco))
        return cursor.lastrowid

def obter_todos() -> list[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_USUARIO)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                endereco=row["endereco"]) 
                for row in rows]
        return usuarios
```

# data\usuario\usuario_sql.py

```py
CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);
"""

INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, endereco)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_USUARIO = """ 
SELECT 
id_usuario, nome, email, telefone, endereco
FROM usuario
ORDER BY nome;
"""
```

# data\util.py

```py
import sqlite3
import os

def open_connection():
    database_path = os.environ.get('TEST_DATABASE_PATH', 'dados.db')
    conexao = sqlite3.connect(database_path)
    conexao.row_factory = sqlite3.Row
    return conexao
```

# main.py

```py
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
```

# pytest.ini

```ini
# pytest.ini
[tool:pytest]
# Diretórios onde o pytest deve procurar por testes
testpaths = tests
# Padrões de arquivos de teste
python_files = test_*.py *_test.py
# Padrões de classes de teste
python_classes = Test*
# Padrões de funções de teste
python_functions = test_*
# Marcadores personalizados
markers =
    slow: marca testes que demoram para executar
    integration: marca testes de integração
    unit: marca testes unitários
# Opções padrão do pytest
addopts = 
    -v
    --strict-markers
    --disable-warnings
    --color=yes
# Filtros de warnings
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
```

# README.md

```md
# Aula 21/05/2025

Biblioteca da Hestia
```

# requirements.txt

```txt
# pip install -r .\requirements.txt
fastapi[standard]
uvicorn[standard]
jinja2
Babel
python-multipart
itsdangerous

# Dependências de teste
pytest
pytest-asyncio
pytest-cov
```

# static\css\style.css

```css
body {
  font-family: 'Segoe UI', sans-serif;
}

h1, h2 {
  color: #2e4d41;
}

.btn-success {
  background-color: #4CAF50;
  border: none;
}

footer {
  font-size: 0.85rem;
}

.benefit-card {
  min-height: 180px; /* ou outro valor conforme desejado */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

```

# static\img\cuidador.jpg

This is a binary file of the type: Image

# static\img\logo2.png

This is a binary file of the type: Image

# templates\home.html

```html
<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hestia - Marketplace para Cuidadores</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    html {
      scroll-behavior: smooth;
    }
  </style>
</head>

<body>

  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom shadow-sm">
    <div class="container">
      <a class="navbar-brand" href="#">
        <img src="logo2.png" alt="Logo Hestia" width="60">
      </a>
      <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a class="nav-link" href="#">Início</a></li>
          <li class="nav-item"><a class="nav-link" href="#sobre">Sobre</a></li>
          <li class="nav-item"><a class="btn btn-success ms-3" href="#">Entrar</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6 text-md-start">
          <h1 class="display-5 fw-bold">Conectando cuidadores e famílias com segurança e empatia.</h1>
          <p class="lead">Encontre profissionais qualificados para cuidar de quem você ama.</p>
          <a href="#" class="btn btn-success btn-lg mt-3" data-bs-toggle="modal" data-bs-target="#cadastroModal">
            Cadastre-se agora
          </a>
        </div>
        <div class="col-md-6">
          <img src="cuidador.jpg" alt="Imagem Cuidador" class="img-fluid rounded" width="1000px">
        </div>
      </div>
    </div>
  </section>

  <!-- BENEFÍCIOS -->
  <section class="py-5">
    <div class="container">
      <div class="text-center mb-4">
        <h2 class="fw-bold">Por que escolher a Hestia?</h2>
      </div>
      <div class="row text-center">
        <div class="col-md-4 d-flex">
          <div class="p-4 border rounded shadow-sm w-100 h-100 benefit-card">
            <h5 class="fw-bold">Segurança</h5>
            <p>Verificação de antecedentes e avaliações reais.</p>
          </div>
        </div>
        <div class="col-md-4 d-flex">
          <div class="p-4 border rounded shadow-sm w-100 h-100 benefit-card">
            <h5 class="fw-bold">Praticidade</h5>
            <p>Filtros inteligentes por localização, jornada e especialização.</p>
          </div>
        </div>
        <div class="col-md-4 d-flex">
          <div class="p-4 border rounded shadow-sm w-100 h-100 benefit-card">
            <h5 class="fw-bold">Pagamento Seguro</h5>
            <p>Gerencie sua contratação e pagamentos pela própria plataforma.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SOBRE -->
  <section id="sobre" class="py-5 bg-light">
    <div class="container">
      <div class="text-center mb-4">
        <h2 class="fw-bold">Sobre o Hestia</h2><br><br>
        <p class="lead">O Hestia é um marketplace que conecta cuidadores de idosos e pessoas com deficiência a famílias que precisam de assistência. Nosso compromisso é oferecer uma plataforma segura, prática e empática, onde é possível contratar profissionais qualificados com confiança e facilidade.</p><br>
        <p class="lead">Nosso objetivo é facilitar o encontro entre quem precisa de cuidado e quem oferece esse serviço com amor e profissionalismo. Verificamos todos os perfis e oferecemos um ambiente seguro para contratação, comunicação e pagamento.</p><br>
        <p class="lead">Seja você um cuidador em busca de oportunidades ou uma família em busca de apoio, o Hestia está aqui para tornar esse processo mais simples, transparente e humano.</p>
      </div>
    </div>
  </section>

  <!-- MODAL CADASTRO -->
  <div class="modal fade" id="cadastroModal" tabindex="-1" aria-labelledby="cadastroModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-success text-white">
          <h5 class="modal-title" id="cadastroModalLabel">Como deseja se cadastrar?</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Fechar"></button>
        </div>
        <div class="modal-body text-center">
          <p>Escolha uma opção:</p>
          <div class="d-grid gap-2">
            <a href="/cadastro/cuidador" class="btn btn-outline-success">Sou Cuidador</a>
            <a href="/cadastro/familia" class="btn btn-outline-primary">Preciso do Serviço</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="bg-success text-white py-3 mt-5">
    <div class="container text-center">
      <p class="mb-1 small">© 2025 Hestia. Todos os direitos reservados.</p>
      <small>Desenvolvido por Esther, Fernanda, Maria Clara e Roberta</small>
    </div>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>

```

# tests\__init__.py

```py

```

# tests\conftest.py

```py
import pytest
import os
import sys
import tempfile

# Adiciona o diretório raiz do projeto ao PYTHONPATH
# Isso permite importar módulos do projeto nos testes
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Fixture para criar um banco de dados temporário para testes
@pytest.fixture
def test_db():
    # Cria um arquivo temporário para o banco de dados
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    # Configura a variável de ambiente para usar o banco de teste
    os.environ['TEST_DATABASE_PATH'] = db_path
    # Retorna o caminho do banco de dados temporário
    yield db_path    
    # Remove o arquivo temporário ao concluir o teste
    os.close(db_fd)
    if os.path.exists(db_path):
        os.unlink(db_path)
```

# tests\test_especialidade_repo.py

```py
import sys
import os
from data.especialidade.especialidade_repo import *
from data.especialidade.especialidade_model import Especialidade

class TestEspecialidadeRepo:
    def test_criar_tabela_especialidades(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir_especialidade(self, test_db): 
        # Arrange
        criar_tabela()
        especialidade_teste =  Especialidade(0, "Especialidade Teste")
        # Act
        id_especialidade_inserida = inserir(especialidade_teste)
        # Assert
        especialidade_db = obter_por_id (id_especialidade_inserida) 
        assert especialidade_db is not None, "A especialidade inserida não deveria ser None"
        assert especialidade_db.id == 1, "A especialidade inserida deveria ter um ID igual a 1"
        assert especialidade_db.nome == "Especialidade Teste", "O nome da especialidade inserida não confere"

    
        
```

