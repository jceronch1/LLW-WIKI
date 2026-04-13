#!/usr/bin/env python3
"""
LLM Kiwi - Script de Mantenimiento (Lint)
Revisa la salud y consistencia de la wiki.

Uso:
    python scripts/lint.py              # Revisión completa
    python scripts/lint.py --fix        # Intenta corregir problemas automáticamente
    python scripts/lint.py --deep       # Incluye análisis con LLM (más lento)
    python scripts/lint.py --model X    # Usa un modelo específico para --deep
"""

import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from utils import *
from ingest import update_index


# ─── Análisis estructural ────────────────────────────────────────────────────

def check_index_completeness():
    """Verifica que todas las páginas estén listadas en index.md."""
    issues = []
    index = load_index()
    pages = get_wiki_pages()

    skip = {"index.md", "log.md", "overview.md"}

    for page in pages:
        if page in skip:
            continue
        page_ref = page.replace('.md', '')
        if page_ref not in index and page.replace('.md', '') not in index:
            issues.append(("index_missing", page, f"No está en index.md"))

    return issues


def check_broken_links():
    """Detecta enlaces [[pagina]] que apuntan a páginas inexistentes."""
    issues = []
    pages = get_wiki_pages()

    # Construir set de páginas existentes (con y sin extensión, con y sin ruta)
    existing = set()
    for p in pages:
        existing.add(p)
        existing.add(p.replace('.md', ''))
        # Solo nombre sin carpeta
        existing.add(Path(p).stem)

    for page in pages:
        content = read_file(WIKI_DIR / page)
        links = extract_wiki_links(content)

        for link in links:
            # Normalizar el link
            link_clean = link.strip()
            link_with_md = link_clean + '.md' if not link_clean.endswith('.md') else link_clean

            # Verificar existencia
            found = (
                link_clean in existing
                or link_with_md in existing
                or (WIKI_DIR / link_with_md).exists()
                or (WIKI_DIR / link_clean).with_suffix('.md').exists()
            )

            if not found:
                issues.append(("broken_link", page, f"Enlace roto: [[{link}]]"))

    return issues


def check_orphan_pages():
    """Detecta páginas sin enlaces entrantes (huérfanas)."""
    issues = []
    pages = get_wiki_pages()
    skip = {"index.md", "log.md", "overview.md"}

    # Recolectar todos los enlaces de todas las páginas
    all_links = set()
    for page in pages:
        content = read_file(WIKI_DIR / page)
        links = extract_wiki_links(content)
        for link in links:
            all_links.add(link.strip())
            # Agregar variantes
            all_links.add(Path(link.strip()).stem)

    for page in pages:
        if page in skip:
            continue
        page_stem = Path(page).stem
        page_no_ext = page.replace('.md', '')

        if (page_stem not in all_links
                and page_no_ext not in all_links
                and page not in all_links):
            issues.append(("orphan", page, "Página huérfana (sin enlaces entrantes)"))

    return issues


def check_empty_pages():
    """Detecta páginas vacías o con muy poco contenido."""
    issues = []
    pages = get_wiki_pages()

    for page in pages:
        content = read_file(WIKI_DIR / page)
        # Contar contenido real (sin títulos ni líneas vacías)
        real_content = re.sub(r'^#.*$', '', content, flags=re.MULTILINE)
        real_content = re.sub(r'\s+', ' ', real_content).strip()

        if len(real_content) < 50:
            issues.append(("empty", page, f"Contenido muy escaso ({len(real_content)} chars)"))

    return issues


def check_duplicate_concepts():
    """Detecta posibles conceptos duplicados con nombres similares."""
    issues = []
    concepts = get_existing_concepts()

    for i, c1 in enumerate(concepts):
        for c2 in concepts[i + 1:]:
            # Comparar similitud básica
            words1 = set(c1.split('-'))
            words2 = set(c2.split('-'))
            common = words1 & words2
            total = words1 | words2

            if total and len(common) / len(total) > 0.6:
                issues.append(("duplicate_suspect", f"concepts/{c1}.md",
                               f"Posible duplicado con: concepts/{c2}.md"))

    return issues


def check_missing_sections(page, content, page_type):
    """Verifica que una página tenga las secciones esperadas según su tipo."""
    issues = []

    required_sections = {
        "sources": ["## Resumen", "## Datos clave", "## Temas principales"],
        "concepts": ["## Definición", "## Fuentes relacionadas"],
        "entities": ["## Descripción", "## Fuentes"],
        "faq": [],  # Formato libre con preguntas
    }

    expected = required_sections.get(page_type, [])
    for section in expected:
        if section not in content:
            issues.append(("missing_section", page, f"Falta sección: {section}"))

    return issues


def check_page_structure():
    """Verifica la estructura de todas las páginas."""
    issues = []
    pages = get_wiki_pages()

    for page in pages:
        if page in ("index.md", "log.md", "overview.md"):
            continue

        content = read_file(WIKI_DIR / page)
        parts = page.replace('.md', '').split('/')

        if len(parts) >= 2:
            page_type = parts[0]
            issues.extend(check_missing_sections(page, content, page_type))

        # Verificar que tenga al menos un título H1
        if not re.search(r'^# ', content, re.MULTILINE):
            issues.append(("no_title", page, "No tiene título H1"))

    return issues


# ─── Análisis profundo con LLM ──────────────────────────────────────────────

def deep_analysis(model):
    """Usa el LLM para detectar contradicciones y sugerir mejoras."""
    issues = []
    pages = get_wiki_pages()
    skip = {"index.md", "log.md"}

    # Cargar todo el contenido relevante
    all_content = []
    total_chars = 0
    for page in pages:
        if page in skip:
            continue
        content = read_file(WIKI_DIR / page)
        if content.strip():
            entry = f"--- {page} ---\n{content}"
            if total_chars + len(entry) < MAX_CONTEXT_CHARS:
                all_content.append(entry)
                total_chars += len(entry)

    if not all_content:
        return []

    wiki_text = "\n\n".join(all_content)

    step("Analizando contradicciones y completitud con LLM...")
    messages = [
        {"role": "system", "content": (
            "Eres un auditor de calidad de una wiki. Analiza el contenido y reporta:\n"
            "1. Contradicciones entre páginas\n"
            "2. Información que debería cruzarse pero no lo está\n"
            "3. Temas importantes que faltan por cubrir\n"
            "4. Conceptos mencionados pero sin página propia\n"
            "5. Sugerencias de comparaciones o líneas de tiempo útiles\n\n"
            "Para cada hallazgo, usa el formato:\n"
            "- [TIPO] descripción (páginas: X, Y)\n\n"
            "Tipos: CONTRADICCION, FALTA_ENLACE, TEMA_FALTANTE, CONCEPTO_SIN_PAGINA, SUGERENCIA"
        )},
        {"role": "user", "content": (
            f"CONTENIDO COMPLETO DE LA WIKI:\n\n{wiki_text}\n\n"
            f"Analiza la wiki y reporta hallazgos:"
        )}
    ]

    response = call_ollama(messages, model=model, temperature=0.2)

    # Parsear hallazgos
    for line in response.split('\n'):
        line = line.strip()
        if line.startswith('- ['):
            match = re.match(r'- \[(\w+)\] (.+)', line)
            if match:
                tipo = match.group(1).lower()
                desc = match.group(2)
                issues.append((f"llm_{tipo}", "wiki", desc))

    return issues


# ─── Corrección automática ───────────────────────────────────────────────────

def fix_index(issues):
    """Agrega páginas faltantes al index.md."""
    index_issues = [i for i in issues if i[0] == "index_missing"]
    if not index_issues:
        return 0

    entries = []
    for _, page, _ in index_issues:
        parts = page.replace('.md', '').split('/')
        if len(parts) >= 2:
            page_type, slug = parts[0], parts[-1]
            # Leer el título de la página
            content = read_file(WIKI_DIR / page)
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            desc = title_match.group(1) if title_match else slug.replace('-', ' ').title()
            entries.append((page_type, slug, desc))

    if entries:
        update_index(entries)

    return len(entries)


# ─── Reporte ─────────────────────────────────────────────────────────────────

def print_report(all_issues):
    """Imprime el reporte de problemas encontrados."""
    if not all_issues:
        info("La wiki está en buen estado. No se encontraron problemas.")
        return

    # Agrupar por tipo
    by_type = defaultdict(list)
    for issue_type, page, desc in all_issues:
        by_type[issue_type].append((page, desc))

    type_labels = {
        "index_missing": ("Páginas sin indexar", C.YELLOW),
        "broken_link": ("Enlaces rotos", C.RED),
        "orphan": ("Páginas huérfanas", C.YELLOW),
        "empty": ("Páginas vacías", C.RED),
        "duplicate_suspect": ("Posibles duplicados", C.YELLOW),
        "missing_section": ("Secciones faltantes", C.YELLOW),
        "no_title": ("Sin título H1", C.YELLOW),
    }

    total = len(all_issues)
    errors = sum(1 for t, _, _ in all_issues if t in ("broken_link", "empty"))
    warnings = total - errors

    header("REPORTE DE SALUD DE LA WIKI")

    for issue_type, items in by_type.items():
        label, color = type_labels.get(issue_type, (issue_type, C.CYAN))
        print(f"\n  {color}{C.BOLD}{label} ({len(items)}){C.END}")
        for page, desc in items:
            print(f"    {color}•{C.END} {page}: {desc}")

    print(f"\n{'─' * 60}")
    if errors:
        print(f"  {C.RED}{C.BOLD}{errors} errores{C.END} | {C.YELLOW}{warnings} advertencias{C.END}")
    else:
        print(f"  {C.GREEN}0 errores{C.END} | {C.YELLOW}{warnings} advertencias{C.END}")
    print()


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="LLM Kiwi - Revisión de salud de la wiki",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            "  python scripts/lint.py           # Revisión rápida\n"
            "  python scripts/lint.py --fix     # Corregir problemas automáticamente\n"
            "  python scripts/lint.py --deep    # Incluir análisis con LLM\n"
        )
    )
    parser.add_argument("--fix", action="store_true", help="Corregir problemas automáticamente")
    parser.add_argument("--deep", action="store_true", help="Análisis profundo con LLM")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Modelo Ollama (default: {DEFAULT_MODEL})")

    args = parser.parse_args()

    header("LLM KIWI - REVISIÓN DE SALUD")

    # Verificar que hay contenido
    pages = get_wiki_pages()
    info(f"Total de páginas en la wiki: {len(pages)}")

    if len(pages) <= 3:  # Solo index, log, overview
        warn("La wiki tiene muy pocas páginas. Ingesta documentos primero.")
        return

    # Ejecutar todas las verificaciones
    all_issues = []

    step("Verificando completitud del índice...")
    all_issues.extend(check_index_completeness())

    step("Buscando enlaces rotos...")
    all_issues.extend(check_broken_links())

    step("Detectando páginas huérfanas...")
    all_issues.extend(check_orphan_pages())

    step("Revisando páginas vacías...")
    all_issues.extend(check_empty_pages())

    step("Buscando posibles duplicados...")
    all_issues.extend(check_duplicate_concepts())

    step("Verificando estructura de páginas...")
    all_issues.extend(check_page_structure())

    # Análisis profundo con LLM (opcional)
    if args.deep:
        if check_ollama() is None:
            warn("Ollama no disponible. Saltando análisis profundo.")
        else:
            deep_issues = deep_analysis(args.model)
            all_issues.extend(deep_issues)

    # Mostrar reporte
    print_report(all_issues)

    # Corrección automática
    if args.fix and all_issues:
        step("Aplicando correcciones automáticas...")
        fixed = fix_index(all_issues)
        if fixed:
            info(f"{fixed} páginas agregadas al índice")
        else:
            info("No se pudieron aplicar correcciones automáticas adicionales.")
        info("Para problemas más complejos, revisa manualmente.")


if __name__ == "__main__":
    main()
