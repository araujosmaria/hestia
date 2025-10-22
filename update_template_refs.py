#!/usr/bin/env python3
"""
Script para atualizar referências de templates após reorganização.
"""
import os
import re
from pathlib import Path

# Mapeamento de caminhos antigos para novos
TEMPLATE_MAPPINGS = {
    # Auth templates
    '"auth/login.html"': '"auth/login.html"',
    "'auth/login.html'": "'auth/login.html'",
    '"auth/cadastro.html"': '"auth/cadastro.html"',
    "'auth/cadastro.html'": "'auth/cadastro.html'",
    '"auth/cadastro_contratante.html"': '"auth/cadastro_contratante.html"',
    "'auth/cadastro_contratante.html'": "'auth/cadastro_contratante.html'",
    '"auth/cadastro_cuidador.html"': '"auth/cadastro_cuidador.html"',
    "'auth/cadastro_cuidador.html'": "'auth/cadastro_cuidador.html'",
    '"auth/redefinir_senha.html"': '"auth/redefinir_senha.html"',
    "'auth/redefinir_senha.html'": "'auth/redefinir_senha.html'",
    '"auth/confirmar_redefinir_senha.html"': '"auth/confirmar_redefinir_senha.html"',
    "'auth/confirmar_redefinir_senha.html'": "'auth/confirmar_redefinir_senha.html'",

    # Public templates
    '"public/index.html"': '"public/index.html"',
    "'public/index.html'": "'public/index.html'",

    # Profile templates
    '"profile/dados.html"': '"profile/dados.html"',
    "'profile/dados.html'": "'profile/dados.html'",

    # Administrador templates
    '"administrador/home.html"': '"administrador/home.html"',
    "'administrador/home.html'": "'administrador/home.html'",
    '"administrador/perfil.html"': '"administrador/perfil.html"',
    "'administrador/perfil.html'": "'administrador/perfil.html'",
    '"administrador/verificacao/solicitacoes.html"': '"administrador/verificacao/solicitacoes.html"',
    "'administrador/verificacao/solicitacoes.html'": "'administrador/verificacao/solicitacoes.html'",
    '"administrador/verificacao/analisar_solicitacao.html"': '"administrador/verificacao/analisar_solicitacao.html"',
    "'administrador/verificacao/analisar_solicitacao.html'": "'administrador/verificacao/analisar_solicitacao.html'",
    '"administrador/avaliacoes/listagem.html"': '"administrador/avaliacoes/listagem.html"',
    "'administrador/avaliacoes/listagem.html'": "'administrador/avaliacoes/listagem.html'",
    '"administrador/avaliacoes/moderar.html"': '"administrador/avaliacoes/moderar.html"',
    "'administrador/avaliacoes/moderar.html'": "'administrador/avaliacoes/moderar.html'",
    '"administrador/chamados/listagem.html"': '"administrador/chamados/listagem.html"',
    "'administrador/chamados/listagem.html'": "'administrador/chamados/listagem.html'",
    '"administrador/chamados/responder.html"': '"administrador/chamados/responder.html"',
    "'administrador/chamados/responder.html'": "'administrador/chamados/responder.html'",

    # Contratante templates
    '"contratante/home.html"': '"contratante/home.html"',
    "'contratante/home.html'": "'contratante/home.html'",
    '"contratante/contratacoes/solicitar.html"': '"contratante/contratacoes/solicitar.html"',
    "'contratante/contratacoes/solicitar.html'": "'contratante/contratacoes/solicitar.html'",
    '"contratante/contratacoes/realizadas.html"': '"contratante/contratacoes/realizadas.html"',
    "'contratante/contratacoes/realizadas.html'": "'contratante/contratacoes/realizadas.html'",
    '"contratante/avaliacoes/realizar.html"': '"contratante/avaliacoes/realizar.html"',
    "'contratante/avaliacoes/realizar.html'": "'contratante/avaliacoes/realizar.html'",
    '"contratante/avaliacoes/realizadas.html"': '"contratante/avaliacoes/realizadas.html"',
    "'contratante/avaliacoes/realizadas.html'": "'contratante/avaliacoes/realizadas.html'",
    '"contratante/avaliacoes/recebidas.html"': '"contratante/avaliacoes/recebidas.html"',
    "'contratante/avaliacoes/recebidas.html'": "'contratante/avaliacoes/recebidas.html'",
    '"contratante/avaliacoes/alterar.html"': '"contratante/avaliacoes/alterar.html"',
    "'contratante/avaliacoes/alterar.html'": "'contratante/avaliacoes/alterar.html'",
    '"contratante/avaliacoes/excluir.html"': '"contratante/avaliacoes/excluir.html"',
    "'contratante/avaliacoes/excluir.html'": "'contratante/avaliacoes/excluir.html'",
    '"contratante/chamados/listagem.html"': '"contratante/chamados/listagem.html"',
    "'contratante/chamados/listagem.html'": "'contratante/chamados/listagem.html'",
    '"contratante/chamados/abertos.html"': '"contratante/chamados/abertos.html"',
    "'contratante/chamados/abertos.html'": "'contratante/chamados/abertos.html'",
    '"contratante/chamados/abrir.html"': '"contratante/chamados/abrir.html"',
    "'contratante/chamados/abrir.html'": "'contratante/chamados/abrir.html'",
    '"contratante/chat/com_cuidador.html"': '"contratante/chat/com_cuidador.html"',
    "'contratante/chat/com_cuidador.html'": "'contratante/chat/com_cuidador.html'",
    '"contratante/chat/geral.html"': '"contratante/chat/geral.html"',
    "'contratante/chat/geral.html'": "'contratante/chat/geral.html'",
    '"contratante/verificacao/solicitar.html"': '"contratante/verificacao/solicitar.html"',
    "'contratante/verificacao/solicitar.html'": "'contratante/verificacao/solicitar.html'",

    # Cuidador templates
    '"cuidador/home.html"': '"cuidador/home.html"',
    "'cuidador/home.html'": "'cuidador/home.html'",
    '"cuidador/especializacoes/listagem.html"': '"cuidador/especializacoes/listagem.html"',
    "'cuidador/especializacoes/listagem.html'": "'cuidador/especializacoes/listagem.html'",
    '"cuidador/especializacoes/cadastrar.html"': '"cuidador/especializacoes/cadastrar.html"',
    "'cuidador/especializacoes/cadastrar.html'": "'cuidador/especializacoes/cadastrar.html'",
    '"cuidador/especializacoes/alterar.html"': '"cuidador/especializacoes/alterar.html"',
    "'cuidador/especializacoes/alterar.html'": "'cuidador/especializacoes/alterar.html'",
    '"cuidador/agenda/visualizar.html"': '"cuidador/agenda/visualizar.html"',
    "'cuidador/agenda/visualizar.html'": "'cuidador/agenda/visualizar.html'",
    '"cuidador/agenda/editar.html"': '"cuidador/agenda/editar.html"',
    "'cuidador/agenda/editar.html'": "'cuidador/agenda/editar.html'",
    '"cuidador/agenda/adicionar_disponibilidade.html"': '"cuidador/agenda/adicionar_disponibilidade.html"',
    "'cuidador/agenda/adicionar_disponibilidade.html'": "'cuidador/agenda/adicionar_disponibilidade.html'",
    '"cuidador/agenda/remover_disponibilidade.html"': '"cuidador/agenda/remover_disponibilidade.html"',
    "'cuidador/agenda/remover_disponibilidade.html'": "'cuidador/agenda/remover_disponibilidade.html'",
    '"cuidador/contratacoes/solicitacoes.html"': '"cuidador/contratacoes/solicitacoes.html"',
    "'cuidador/contratacoes/solicitacoes.html'": "'cuidador/contratacoes/solicitacoes.html'",
    '"cuidador/contratacoes/recebidas.html"': '"cuidador/contratacoes/recebidas.html"',
    "'cuidador/contratacoes/recebidas.html'": "'cuidador/contratacoes/recebidas.html'",
    '"cuidador/contratacoes/detalhes.html"': '"cuidador/contratacoes/detalhes.html"',
    "'cuidador/contratacoes/detalhes.html'": "'cuidador/contratacoes/detalhes.html'",
    '"cuidador/avaliacoes/realizar.html"': '"cuidador/avaliacoes/realizar.html"',
    "'cuidador/avaliacoes/realizar.html'": "'cuidador/avaliacoes/realizar.html'",
    '"cuidador/avaliacoes/realizadas.html"': '"cuidador/avaliacoes/realizadas.html"',
    "'cuidador/avaliacoes/realizadas.html'": "'cuidador/avaliacoes/realizadas.html'",
    '"cuidador/avaliacoes/recebidas.html"': '"cuidador/avaliacoes/recebidas.html"',
    "'cuidador/avaliacoes/recebidas.html'": "'cuidador/avaliacoes/recebidas.html'",
    '"cuidador/avaliacoes/alterar.html"': '"cuidador/avaliacoes/alterar.html"',
    "'cuidador/avaliacoes/alterar.html'": "'cuidador/avaliacoes/alterar.html'",
    '"cuidador/avaliacoes/excluir.html"': '"cuidador/avaliacoes/excluir.html"',
    "'cuidador/avaliacoes/excluir.html'": "'cuidador/avaliacoes/excluir.html'",
    '"cuidador/chamados/abertos.html"': '"cuidador/chamados/abertos.html"',
    "'cuidador/chamados/abertos.html'": "'cuidador/chamados/abertos.html'",
    '"cuidador/chamados/abrir.html"': '"cuidador/chamados/abrir.html"',
    "'cuidador/chamados/abrir.html'": "'cuidador/chamados/abrir.html'",
    '"cuidador/chat/com_contratante.html"': '"cuidador/chat/com_contratante.html"',
    "'cuidador/chat/com_contratante.html'": "'cuidador/chat/com_contratante.html'",
    '"cuidador/chat/geral.html"': '"cuidador/chat/geral.html"',
    "'cuidador/chat/geral.html'": "'cuidador/chat/geral.html'",
    '"cuidador/verificacao/solicitacao.html"': '"cuidador/verificacao/solicitacao.html"',
    "'cuidador/verificacao/solicitacao.html'": "'cuidador/verificacao/solicitacao.html'",

    # Base templates
    '"base/form.html"': '"base/form.html"',
    "'base/form.html'": "'base/form.html'",
}

def update_file(file_path: Path):
    """Atualiza referências de templates em um arquivo."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Aplicar substituições
        for old_ref, new_ref in TEMPLATE_MAPPINGS.items():
            content = content.replace(old_ref, new_ref)

        # Só reescrever se houve mudanças
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Atualizado: {file_path}")
            return True
        return False

    except Exception as e:
        print(f"✗ Erro ao processar {file_path}: {e}")
        return False

def main():
    """Atualiza todas as referências de templates no projeto."""
    project_root = Path("/Volumes/Externo/Ifes/hestia")
    routes_dir = project_root / "routes"

    updated_files = 0
    total_files = 0

    # Processar arquivos Python em routes/
    for py_file in routes_dir.rglob("*.py"):
        total_files += 1
        if update_file(py_file):
            updated_files += 1

    # Processar outros arquivos Python no projeto que possam referenciar templates
    for py_file in project_root.glob("*.py"):
        total_files += 1
        if update_file(py_file):
            updated_files += 1

    print(f"\n{'='*60}")
    print(f"Resumo: {updated_files} de {total_files} arquivos atualizados")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
