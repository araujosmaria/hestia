#!/usr/bin/env python3
"""
Script para atualizar heranças de templates ({% extends %}) após reorganização.
"""
import re
from pathlib import Path

# Mapeamentos de heranças
EXTENDS_MAPPINGS = {
    '{% extends "base_public_form.html" %}': '{% extends "base/form.html" %}',
    "{% extends 'base_public_form.html' %}": "{% extends 'base/form.html' %}",
}

def update_template_file(file_path: Path):
    """Atualiza heranças de templates em um arquivo HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Aplicar substituições
        for old_extends, new_extends in EXTENDS_MAPPINGS.items():
            content = content.replace(old_extends, new_extends)

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
    """Atualiza todas as heranças de templates no projeto."""
    project_root = Path("/Volumes/Externo/Ifes/hestia")
    templates_dir = project_root / "templates"

    updated_files = 0
    total_files = 0

    # Processar arquivos HTML em templates/
    for html_file in templates_dir.rglob("*.html"):
        total_files += 1
        if update_template_file(html_file):
            updated_files += 1

    print(f"\n{'='*60}")
    print(f"Resumo: {updated_files} de {total_files} arquivos atualizados")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
