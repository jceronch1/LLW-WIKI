#!/usr/bin/env python3
"""
LLM Kiwi - Script de Consulta
Responde preguntas usando la wiki como fuente de conocimiento.

Uso:
    python scripts/query.py "¿Cuál es la política de IA en Colombia?"
    python scripts/query.py --guardar "¿Qué dice el CONPES 4144?"
    python scripts/query.py --interactivo
    python scripts/query.py --model qwen3.5:9b "pregunta"
"""

import sys
import re
import argparse
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import *
from ingest import update_index


# ─── Selección de páginas relevantes ─────────────────────────────────────────

def normalize_for_search(text):
    """Normaliza texto para comparar consultas con títulos/rutas sin depender de acentos."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def index_lines_by_page(index):
    """Mapea cada página referenciada en index.md con su línea descriptiva."""
    lines = {}
    for line in index.splitlines():
        match = re.search(r"\[\[([^\]|#]+)", line)
        if match:
            page = match.group(1).strip()
            if not page.endswith(".md"):
                page = page + ".md"
            lines[page] = line
    return lines


def token_variants(token):
    variants = {token}
    if token.endswith("es") and len(token) > 5:
        variants.add(token[:-2])
    if token.endswith("s") and len(token) > 4:
        variants.add(token[:-1])
    return variants


def contains_any_variant(text, variants):
    return any(variant in text for variant in variants)


def rank_pages_locally(question, content_pages, index, limit=8):
    """Ranking lexical local para garantizar que conceptos directos entren al contexto."""
    normalized_question = normalize_for_search(question)
    tokens = [t for t in normalized_question.split() if len(t) >= 4]
    if not tokens:
        return []
    token_groups = [token_variants(token) for token in tokens]
    token_phrase = " ".join(tokens)

    index_lines = index_lines_by_page(index)
    scored = []

    for page in content_pages:
        stem_text = normalize_for_search(Path(page).stem)
        path_text = normalize_for_search(page.replace(".md", "").replace("/", " "))
        index_text = normalize_for_search(index_lines.get(page, ""))
        score = 0

        if token_phrase and stem_text == token_phrase:
            score += 120
        elif token_phrase and token_phrase in stem_text:
            score += 70

        if len(token_groups) == 1:
            variants = token_groups[0]
            if any(stem_text in {f"sistema {v}", f"sistemas {v}"} for v in variants):
                score += 80
            elif contains_any_variant(stem_text, variants):
                score += max(0, 60 - len(stem_text.split()) * 6)

        if normalized_question and normalized_question in path_text:
            score += 80
        if all(contains_any_variant(path_text, group) for group in token_groups):
            score += 45
            score += max(0, 30 - len(stem_text.split()) * 4)
        score += sum(12 for group in token_groups if contains_any_variant(path_text, group))

        if normalized_question and normalized_question in index_text:
            score += 35
        if all(contains_any_variant(index_text, group) for group in token_groups):
            score += 20
        score += sum(4 for group in token_groups if contains_any_variant(index_text, group))

        if page.startswith("concepts/"):
            score += 8
        elif page.startswith("sources/"):
            score += 4
        elif page.startswith("faq/"):
            score -= 8

        if score > 0:
            scored.append((score, page))

    scored.sort(key=lambda item: (-item[0], item[1]))
    return [page for _, page in scored[:limit]]


def merge_selected_pages(*groups, limit=8):
    selected = []
    for group in groups:
        for page in group:
            if page not in selected:
                selected.append(page)
            if len(selected) >= limit:
                return selected
    return selected


def select_relevant_pages(question, model):
    """Usa el índice de la wiki para identificar las páginas más relevantes."""
    index = load_index()
    all_pages = get_wiki_pages()

    # Filtrar páginas de contenido (no index, log)
    content_pages = [
        p for p in all_pages
        if p not in ("index.md", "log.md", "overview.md") and not p.startswith("aliases/")
    ]
    local_selected = rank_pages_locally(question, content_pages, index)

    messages = [
        {"role": "system", "content": (
            "Eres un asistente que selecciona páginas relevantes de una wiki.\n"
            "Dado un índice y una pregunta, responde SOLO con los nombres de archivo\n"
            "de las páginas más relevantes, uno por línea.\n"
            "Máximo 8 páginas. Solo nombres de archivo, sin explicaciones."
        )},
        {"role": "user", "content": (
            f"ÍNDICE DE LA WIKI:\n{index}\n\n"
            f"PÁGINAS DISPONIBLES:\n" + "\n".join(content_pages) + "\n\n"
            f"PREGUNTA: {question}\n\n"
            f"Lista las páginas más relevantes (solo nombres de archivo):"
        )}
    ]

    response = call_ollama(messages, model=model, temperature=0.1)

    # Parsear nombres de archivo de la respuesta
    llm_selected = []
    for line in response.strip().split('\n'):
        line = line.strip().lstrip('-').lstrip('*').strip()
        line = line.strip('`').strip()
        # Buscar si alguna página coincide
        for page in content_pages:
            if page in line or page.replace('.md', '') in line:
                if page not in llm_selected:
                    llm_selected.append(page)
                break

    selected = merge_selected_pages(local_selected, llm_selected)

    return selected[:8]


def load_pages_content(page_list):
    """Carga el contenido de las páginas seleccionadas."""
    contents = []
    total_chars = 0
    max_total = MAX_CONTEXT_CHARS - 5000  # Dejar espacio para prompt y respuesta

    for page in page_list:
        content = read_file(WIKI_DIR / page)
        if not content:
            continue

        if total_chars + len(content) > max_total:
            # Truncar si es necesario
            remaining = max_total - total_chars
            if remaining > 500:
                content = content[:remaining] + "\n\n...(truncado)"
            else:
                break

        contents.append(f"--- {page} ---\n{content}")
        total_chars += len(content)

    return "\n\n".join(contents)


# ─── Generación de respuesta ─────────────────────────────────────────────────

def answer_question(question, pages_content, model):
    """Genera una respuesta basada en el contenido de la wiki."""
    agents_rules = (
        "- Responde basándote SOLO en la información de la wiki.\n"
        "- Cita las fuentes con [[nombre-pagina]].\n"
        "- Si la wiki no contiene información suficiente, dilo claramente.\n"
        "- No inventes datos que no estén en las páginas proporcionadas.\n"
        "- Sé preciso, conciso y útil. Responde en español."
    )

    messages = [
        {"role": "system", "content": (
            "Eres el asistente de consulta de una wiki sobre Agentes de Inteligencia Artificial.\n"
            f"{agents_rules}"
        )},
        {"role": "user", "content": (
            f"PÁGINAS DE LA WIKI:\n\n{pages_content}\n\n"
            f"{'─' * 40}\n\n"
            f"PREGUNTA: {question}"
        )}
    ]

    return call_ollama(messages, model=model, temperature=0.3)


# ─── Guardar respuesta en FAQ ────────────────────────────────────────────────

def save_to_faq(question, answer):
    """Guarda una pregunta y respuesta valiosa en la wiki."""
    faq_path = WIKI_DIR / "faq" / "consultas-wiki.md"
    existing = read_file(faq_path)

    if not existing:
        existing = "# FAQ: Consultas a la Wiki\n\n> Respuestas valiosas generadas por consultas.\n"

    entry = f"\n## {question}\n{answer}\n\n*Registrado: {get_now()}*\n"
    write_file(faq_path, existing + entry)

    # Actualizar index si es nuevo
    index = load_index()
    if "[[faq/consultas-wiki]]" not in index:
        update_index([("faq", "consultas-wiki", "Respuestas valiosas de consultas")])

    # Registrar en log
    append_file(WIKI_DIR / "log.md",
                f"\n## [{get_today()}] query | {question[:60]}\n"
                f"- Respuesta guardada en: [[faq/consultas-wiki]]\n")


# ─── Flujo principal ─────────────────────────────────────────────────────────

def process_query(question, model, save=False):
    """Ejecuta el flujo completo de consulta."""
    header("LLM KIWI - CONSULTA")

    # Verificar que hay contenido en la wiki
    pages = get_wiki_pages()
    content_pages = [p for p in pages if p not in ("index.md", "log.md", "overview.md")]
    if not content_pages:
        warn("La wiki está vacía. Primero ingesta documentos con: python scripts/ingest.py --todos")
        return

    # Paso 1: Seleccionar páginas relevantes
    step("Buscando páginas relevantes...")
    selected = select_relevant_pages(question, model)

    if not selected:
        warn("No se encontraron páginas relevantes en la wiki.")
        return

    info(f"{len(selected)} páginas seleccionadas:")
    for p in selected:
        dim(p)

    # Paso 2: Cargar contenido
    step("Cargando contenido...")
    pages_content = load_pages_content(selected)
    info(f"{len(pages_content):,} caracteres de contexto")

    # Paso 3: Generar respuesta
    step("Generando respuesta...")
    answer = answer_question(question, pages_content, model)

    # Mostrar respuesta
    print(f"\n{'─' * 60}")
    print(f"\n{answer}\n")
    print(f"{'─' * 60}")
    print(f"{C.DIM}Páginas consultadas: {', '.join(selected)}{C.END}\n")

    # Guardar si se solicitó
    if save:
        save_to_faq(question, answer)
        info("Respuesta guardada en wiki/faq/consultas-wiki.md")

    return answer


def interactive_mode(model):
    """Modo interactivo: preguntas y respuestas en bucle."""
    header("LLM KIWI - MODO INTERACTIVO")
    info("Escribe tu pregunta y presiona Enter.")
    info("Comandos: 'salir' para terminar, 'guardar' antes de la pregunta para guardar la respuesta.")
    print()

    while True:
        try:
            raw = input(f"  {C.CYAN}?{C.END} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            info("Sesión terminada.")
            break

        if not raw:
            continue
        if raw.lower() in ('salir', 'exit', 'quit', 'q'):
            info("Sesión terminada.")
            break

        save = False
        if raw.lower().startswith('guardar '):
            save = True
            raw = raw[8:].strip()

        process_query(raw, model, save=save)


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="LLM Kiwi - Consulta a la wiki de conocimiento",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            '  python scripts/query.py "¿Cuál es la política de IA en Colombia?"\n'
            '  python scripts/query.py --guardar "¿Qué dice el CONPES 4144?"\n'
            "  python scripts/query.py --interactivo\n"
        )
    )
    parser.add_argument("pregunta", nargs="?", help="La pregunta a responder")
    parser.add_argument("--guardar", action="store_true", help="Guardar la respuesta en la wiki como FAQ")
    parser.add_argument("--interactivo", "-i", action="store_true", help="Modo interactivo (chat)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Modelo Ollama (default: {DEFAULT_MODEL})")

    args = parser.parse_args()

    # Verificar Ollama
    if check_ollama() is None:
        error("Ollama no está corriendo. Ejecuta: ollama serve")
        return

    if args.interactivo:
        interactive_mode(args.model)
    elif args.pregunta:
        process_query(args.pregunta, args.model, save=args.guardar)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
