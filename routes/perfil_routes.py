import os
import secrets
from io import BytesIO
from typing import Optional, Union
from fastapi import APIRouter, FastAPI, Request, status, UploadFile, File
from fastapi.responses import RedirectResponse
# Flash messages (preparado para uso futuro)
# from util.flash_messages import informar_sucesso, informar_erro
# Logger (preparado para uso futuro)
# from util.logger_config import logger
from PIL import Image, ImageDraw
from PIL.Image import Image as ImageType
from data.cuidador import cuidador_repo
from data.cliente import cliente_repo
from data.usuario import usuario_repo
from util.auth_decorator import criar_sessao, requer_autenticacao
from util.template_util import criar_templates

perfil_router = APIRouter()
templates = criar_templates("templates/perfil/dados.html")
app = FastAPI()
router = APIRouter()

@perfil_router.post("/upload_foto_perfil")
async def upload_foto_perfil(fotoPerfil: UploadFile = File(...)):
    # Verifique o tipo do arquivo
    if fotoPerfil.content_type is None or not fotoPerfil.content_type.startswith('image/'):
        return {"error": "Arquivo deve ser uma imagem (JPG, JPEG, PNG)."}

    # Diretório onde a foto será salva
    upload_dir = "uploads/fotos_perfil"
    os.makedirs(upload_dir, exist_ok=True)

    # Caminho do arquivo onde será salvo
    if fotoPerfil.filename is None:
        return {"error": "Nome do arquivo inválido."}
    file_path = os.path.join(upload_dir, fotoPerfil.filename)

    # Salve o arquivo no diretório especificado
    with open(file_path, "wb") as f:
        f.write(fotoPerfil.file.read())

    return {"filename": fotoPerfil.filename, "file_path": file_path}

# ======================
# DADOS DO PERFIL (CLIENTE E CUIDADOR)
# ======================
@router.route("/perfil/dados", methods=["GET", "POST"])
@requer_autenticacao()
async def perfil_dados(
    request: Request,
    usuario_logado: Optional[dict] = None,
    foto: UploadFile = File(None),
    sucesso: Optional[str] = None,
    erro: Optional[str] = None,
    foto_sucesso: Optional[str] = None
):
    if usuario_logado is None:
        return RedirectResponse("/login", status_code=303)

    id_usuario = usuario_logado["id"]

    # Verificar se é cliente ou cuidador
    cliente = cliente_repo.obter_por_id(id_usuario)
    cuidador = cuidador_repo.obter_por_id(id_usuario)

    # Se não encontrar o usuário (cliente ou cuidador), redireciona para login
    if not cliente and not cuidador:
        return RedirectResponse("/login", status_code=303)

    # Definindo qual perfil será usado
    perfil_usuario: object
    perfil_tipo: str
    if cliente:
        perfil_usuario = cliente
        perfil_tipo = 'cliente'
    elif cuidador:
        perfil_usuario = cuidador
        perfil_tipo = 'cuidador'
    else:
        # Este bloco nunca será executado devido à verificação anterior
        return RedirectResponse("/login", status_code=303)

    mensagem_sucesso = None
    mensagem_erro = None

    if request.method == "POST" and foto:
        tipos_permitidos = ["image/jpeg", "image/png", "image/jpg"]
        
        # Verifica se o tipo da imagem é válido
        if foto.content_type not in tipos_permitidos:
            mensagem_erro = "Tipo de arquivo inválido. Use apenas JPG, JPEG ou PNG."
        else:
            try:
                # Processamento da foto para deixar redonda
                conteudo = await foto.read()
                imagem = Image.open(BytesIO(conteudo))

                # Definir o diâmetro e calcular a parte central da imagem
                largura, altura = imagem.size
                diametro = min(largura, altura)
                margem = (largura - diametro) // 2, (altura - diametro) // 2

                # Criar máscara circular
                mascara = Image.new('L', (diametro, diametro), 0)
                draw = ImageDraw.Draw(mascara)
                draw.ellipse((0, 0, diametro, diametro), fill=255)

                # Cortar a imagem para o centro e aplicar a máscara circular
                imagem_cortada = imagem.crop((margem[0], margem[1], margem[0] + diametro, margem[1] + diametro))
                imagem_cortada.putalpha(mascara)

                # Criar diretório de upload se não existir
                upload_dir = "static/uploads/usuarios"
                os.makedirs(upload_dir, exist_ok=True)

                # Gerar nome único para o arquivo
                if foto.filename:
                    extensao = foto.filename.split(".")[-1].lower()
                else:
                    extensao = "png"
                nome_arquivo = f"{id_usuario}_{secrets.token_hex(8)}.png"
                caminho_arquivo = os.path.join(upload_dir, nome_arquivo)

                # Salvar a imagem processada
                buffer = BytesIO()
                imagem_cortada.save(buffer, format="PNG")  # Salvar como PNG para manter transparência
                conteudo_redondo = buffer.getvalue()

                with open(caminho_arquivo, "wb") as f:
                    f.write(conteudo_redondo)

                # Caminho relativo para salvar no banco
                caminho_relativo = f"/static/uploads/usuarios/{nome_arquivo}"

                # Atualizar foto no banco de dados
                usuario_repo.atualizar_foto(id_usuario, caminho_relativo)

                # Atualizar foto na sessão
                usuario_logado['foto'] = caminho_relativo
                criar_sessao(request, usuario_logado)

                mensagem_sucesso = "Foto de perfil atualizada com sucesso!"

            except Exception:
                mensagem_erro = "Erro no upload da foto. Tente novamente."

    # Dados do perfil a serem exibidos
    perfil_dados = {
        "nome": perfil_usuario.nome,
        "email": perfil_usuario.email,
        "telefone": perfil_usuario.telefone,
        "foto_perfil": perfil_usuario.foto or "/static/img/default-avatar.jpg"
    }

    # Mensagens de sucesso/erro
    if sucesso:
        mensagem_sucesso = "Perfil atualizado com sucesso!"
    if foto_sucesso:
        mensagem_sucesso = "Foto de perfil atualizada com sucesso!"
    if erro == "tipo_invalido":
        mensagem_erro = "Tipo de arquivo inválido. Use apenas JPG, PNG ou JPEG."
    elif erro == "upload_falhou":
        mensagem_erro = "Erro no upload da foto. Tente novamente."

    # Retorno do template
    return templates.TemplateResponse(
        "perfil/dados.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "cuidador_dados": cuidador if perfil_tipo == 'cuidador' else None,
            "cliente_dados": cliente if perfil_tipo == 'cliente' else None,
            "mensagem": mensagem_sucesso,
            "erro": mensagem_erro
        }
    )

