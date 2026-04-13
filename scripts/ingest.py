#!/usr/bin/env python3
"""
LLM Kiwi - Script de Ingesta
Procesa documentos PDF y los incorpora a la wiki de conocimiento.

Uso:
    python scripts/ingest.py                           # Muestra documentos disponibles
    python scripts/ingest.py "nombre-del-archivo.pdf"  # Ingesta un documento
    python scripts/ingest.py --todos                   # Ingesta todos los pendientes
    python scripts/ingest.py --model llama3.1:8b ...   # Usa un modelo específico
"""

import sys
import re
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import *  # noqa: includes load_config


# ─── Prompts del sistema ─────────────────────────────────────────────────────

def get_system_prompt():
    """Genera el prompt del sistema basado en la configuración actual."""
    cfg = load_config()
    topic = cfg.get('topic', 'Conocimiento')
    return (
        f"Eres el mantenedor de una wiki sobre {topic}.\n"
        "Tu trabajo es leer documentos y producir contenido wiki estructurado en español.\n"
        "Sé preciso, factual y exhaustivo. No inventes datos. Usa formato Markdown limpio."
    )


# Backward compat: módulos que importen SYSTEM_PROMPT obtienen el valor actual
SYSTEM_PROMPT = get_system_prompt()


# ─── Funciones de generación ─────────────────────────────────────────────────

def summarize_chunk(chunk, doc_name, chunk_num, total, model):
    """Resume un fragmento individual de un documento largo."""
    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": (
            f"Resume este fragmento ({chunk_num}/{total}) del documento '{doc_name}'.\n"
            f"Incluye TODOS los datos, cifras, fechas, nombres de entidades y hechos relevantes.\n"
            f"No omitas información importante.\n\n"
            f"FRAGMENTO:\n{chunk}"
        )}
    ]
    return call_ollama(messages, model=model, temperature=0.2)


def generate_source_page(doc_name, text, model):
    """Genera una página wiki de fuente a partir del texto del documento."""
    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": (
            f"Crea una página wiki estructurada para el documento '{doc_name}'.\n\n"
            f"USA EXACTAMENTE ESTE FORMATO:\n\n"
            f"# {doc_name}\n\n"
            f"## Resumen\n"
            f"[Resumen ejecutivo de 3-5 párrafos que capture la esencia del documento]\n\n"
            f"## Datos clave\n"
            f"- [Lista de datos, cifras, fechas y hechos concretos]\n\n"
            f"## Temas principales\n"
            f"[Lista numerada de los temas principales cubiertos]\n\n"
            f"## Actores y entidades mencionadas\n"
            f"- [Organizaciones, instituciones, personas mencionadas]\n\n"
            f"## Relación con otros conceptos\n"
            f"- [[inteligencia-artificial]]\n"
            f"- [Otros conceptos con enlaces tipo [[concepto]]]\n\n"
            f"## Citas textuales relevantes\n"
            f"> [Citas importantes del documento]\n\n"
            f"## Notas\n"
            f"[Observaciones, limitaciones o contexto adicional]\n\n"
            f"CONTENIDO DEL DOCUMENTO:\n{text[:MAX_CONTEXT_CHARS]}"
        )}
    ]
    return call_ollama(messages, model=model, temperature=0.2)


def extract_concepts_from_doc(text, doc_name, existing_concepts, model):
    """Extrae conceptos clave del documento."""
    existing_str = ", ".join(existing_concepts) if existing_concepts else "(ninguno aún)"

    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": (
            f"Del documento '{doc_name}', identifica los 5-10 conceptos más importantes.\n\n"
            f"Conceptos que YA EXISTEN en la wiki (reutilízalos si aplican): {existing_str}\n\n"
            f"Para CADA concepto nuevo, escribe EXACTAMENTE en este formato:\n\n"
            f"---CONCEPTO---\n"
            f"nombre: [nombre del concepto]\n"
            f"definicion: [definición clara de 2-3 oraciones]\n"
            f"relaciones: [conceptos relacionados separados por coma]\n"
            f"ideas: [3-5 ideas principales separadas por |]\n"
            f"---FIN---\n\n"
            f"IMPORTANTE: Usa el delimitador ---CONCEPTO--- y ---FIN--- exactamente como se muestra.\n"
            f"NO incluyas conceptos que ya existen, a menos que tengas información nueva sustancial.\n\n"
            f"CONTENIDO DEL DOCUMENTO:\n{text[:MAX_CONTEXT_CHARS]}"
        )}
    ]
    response = call_ollama(messages, model=model, temperature=0.2)

    # Parsear conceptos
    concepts = []
    blocks = re.split(r'---\s*CONCEPTO\s*---', response)
    for block in blocks:
        if '---FIN---' not in block and '--- FIN ---' not in block:
            continue
        block = re.split(r'---\s*FIN\s*---', block)[0]

        concept = {}
        for line in block.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace('í', 'i').replace('ó', 'o')
                concept[key] = value.strip()

        if 'nombre' in concept and 'definicion' in concept:
            concepts.append(concept)

    return concepts


def extract_entities_from_doc(text, doc_name, existing_entities, model):
    """Extrae entidades (organizaciones, leyes, personas) del documento."""
    existing_str = ", ".join(existing_entities) if existing_entities else "(ninguna aún)"

    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": (
            f"Del documento '{doc_name}', identifica las entidades más importantes:\n"
            f"organizaciones, instituciones, leyes, normas o personas clave.\n\n"
            f"Entidades que YA EXISTEN en la wiki: {existing_str}\n\n"
            f"Para CADA entidad nueva, escribe EXACTAMENTE:\n\n"
            f"---ENTIDAD---\n"
            f"nombre: [nombre de la entidad]\n"
            f"tipo: [organizacion|ley|persona|programa|otro]\n"
            f"descripcion: [descripción breve de 1-2 oraciones]\n"
            f"rol: [rol en el ecosistema de IA]\n"
            f"---FIN---\n\n"
            f"CONTENIDO DEL DOCUMENTO:\n{text[:MAX_CONTEXT_CHARS]}"
        )}
    ]
    response = call_ollama(messages, model=model, temperature=0.2)

    entities = []
    blocks = re.split(r'---\s*ENTIDAD\s*---', response)
    for block in blocks:
        if '---FIN---' not in block and '--- FIN ---' not in block:
            continue
        block = re.split(r'---\s*FIN\s*---', block)[0]

        entity = {}
        for line in block.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                entity[key.strip().lower()] = value.strip()

        if 'nombre' in entity and 'descripcion' in entity:
            entities.append(entity)

    return entities


def generate_faq(text, doc_name, source_slug, model):
    """Genera preguntas frecuentes basadas en el documento."""
    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": (
            f"Basándote en el documento '{doc_name}', genera 5-8 preguntas frecuentes\n"
            f"con respuestas detalladas y útiles.\n\n"
            f"Formato Markdown:\n\n"
            f"# FAQ: {doc_name}\n\n"
            f"## ¿Pregunta 1?\n"
            f"Respuesta detallada...\n\n"
            f"## ¿Pregunta 2?\n"
            f"Respuesta detallada...\n\n"
            f"(continúa con más preguntas)\n\n"
            f"## Fuentes\n"
            f"- [[sources/{source_slug}]]\n\n"
            f"CONTENIDO DEL DOCUMENTO:\n{text[:MAX_CONTEXT_CHARS]}"
        )}
    ]
    return call_ollama(messages, model=model, temperature=0.3)


# ─── Creación de páginas ─────────────────────────────────────────────────────

def build_concept_page(concept, source_slug):
    """Construye el Markdown de una página de concepto."""
    name = concept.get('nombre', 'Sin nombre')
    definition = concept.get('definicion', '(pendiente)')
    relations_raw = concept.get('relaciones', '')
    ideas_raw = concept.get('ideas', '')

    # Formatear relaciones como enlaces wiki
    rel_lines = []
    for r in relations_raw.split(','):
        r = r.strip()
        if r:
            rel_lines.append(f"- [[concepts/{slugify(r)}|{r}]]")

    # Formatear ideas
    idea_lines = []
    for idea in ideas_raw.split('|'):
        idea = idea.strip()
        if idea:
            idea_lines.append(f"- {idea}")

    return (
        f"# {name}\n\n"
        f"## Definición\n{definition}\n\n"
        f"## Ideas clave\n"
        f"{chr(10).join(idea_lines) if idea_lines else '- (pendiente de desarrollo)'}\n\n"
        f"## Relación con otros conceptos\n"
        f"{chr(10).join(rel_lines) if rel_lines else '- (sin relaciones identificadas aún)'}\n\n"
        f"## Fuentes relacionadas\n"
        f"- [[sources/{source_slug}]]\n\n"
        f"## Preguntas abiertas\n"
        f"- (pendiente de desarrollo)\n"
    )


def build_entity_page(entity, source_slug):
    """Construye el Markdown de una página de entidad."""
    name = entity.get('nombre', 'Sin nombre')
    tipo = entity.get('tipo', 'otro')
    desc = entity.get('descripcion', '(pendiente)')
    rol = entity.get('rol', '(pendiente)')

    return (
        f"# {name}\n\n"
        f"**Tipo:** {tipo}\n\n"
        f"## Descripción\n{desc}\n\n"
        f"## Rol en el ecosistema de IA\n{rol}\n\n"
        f"## Documentos relacionados\n"
        f"- [[sources/{source_slug}]]\n\n"
        f"## Fuentes\n"
        f"- [[sources/{source_slug}]]\n"
    )


def update_existing_page(content, source_slug):
    """Agrega una nueva fuente a una página existente si no está ya referenciada."""
    link = f"[[sources/{source_slug}]]"
    if link in content:
        return content, False

    if "## Fuentes relacionadas" in content:
        content = content.replace(
            "## Fuentes relacionadas\n",
            f"## Fuentes relacionadas\n- {link}\n"
        )
    elif "## Fuentes" in content:
        content = content.replace(
            "## Fuentes\n",
            f"## Fuentes\n- {link}\n"
        )
    else:
        content += f"\n\n## Fuentes relacionadas\n- {link}\n"

    return content, True


# ─── Actualización de index.md y log.md ──────────────────────────────────────

def update_index(new_entries):
    """Actualiza index.md con nuevas entradas. Cada entrada: (tipo, slug, descripción)."""
    index_path = WIKI_DIR / "index.md"
    index = read_file(index_path)

    for page_type, slug, description in new_entries:
        # No duplicar
        if f"[[{page_type}/{slug}]]" in index:
            continue

        entry = f"- [[{page_type}/{slug}]]: {description}"

        # Mapear tipo a sección
        section_map = {
            "sources": "## Sources",
            "concepts": "## Concepts",
            "entities": "## Entities",
            "faq": "## FAQ",
            "comparisons": "## Comparisons",
            "timelines": "## Timelines",
        }
        section = section_map.get(page_type, f"## {page_type.capitalize()}")

        if section in index:
            index = index.replace(section, f"{section}\n{entry}")
        else:
            index += f"\n{section}\n{entry}\n"

    write_file(index_path, index)


def append_log(doc_name, created, updated):
    """Registra la ingesta en log.md."""
    lines = [f"\n## [{get_today()}] ingest | {doc_name}"]

    if created:
        for p in created:
            lines.append(f"- Se creó: [[{p}]]")
    if updated:
        for p in updated:
            lines.append(f"- Se actualizó: [[{p}]]")

    lines.append("")
    append_file(WIKI_DIR / "log.md", "\n".join(lines))


# ─── Flujo principal de ingesta ──────────────────────────────────────────────

def ingest_document(pdf_path, model):
    """Ejecuta el flujo completo de ingesta para un documento PDF."""
    pdf_path = Path(pdf_path)
    doc_name = pdf_path.stem
    source_slug = slugify(doc_name)

    header(f"INGESTA: {doc_name}")

    # Verificar si ya fue ingestado
    if (WIKI_DIR / "sources" / f"{source_slug}.md").exists():
        warn(f"Ya existe: wiki/sources/{source_slug}.md")
        try:
            resp = input("  ¿Re-ingestar? (s/n): ").strip().lower()
            if resp != 's':
                info("Saltado.")
                return
        except (EOFError, KeyboardInterrupt):
            return

    created = []
    updated = []
    index_entries = []

    # ── Paso 1: Extraer texto ────────────────────────────────────────────
    step("Extrayendo texto del PDF...")
    text = extract_pdf_text(pdf_path)

    if not text.strip():
        error(f"No se pudo extraer texto de {pdf_path.name}")
        error("El PDF puede ser un escaneo sin OCR.")
        return

    word_count = len(text.split())
    info(f"{len(text):,} caracteres | {word_count:,} palabras extraídas")

    # ── Paso 2: Manejar documentos largos ────────────────────────────────
    if len(text) > MAX_CONTEXT_CHARS:
        step(f"Documento grande ({len(text):,} chars). Resumiendo por chunks...")
        chunks = chunk_text(text)
        info(f"Dividido en {len(chunks)} fragmentos")

        summaries = []
        for i, chunk in enumerate(chunks, 1):
            dim(f"Resumiendo fragmento {i}/{len(chunks)}...")
            summary = summarize_chunk(chunk, doc_name, i, len(chunks), model)
            summaries.append(summary)

        text_for_analysis = "\n\n---\n\n".join(summaries)
        info(f"Resumen consolidado: {len(text_for_analysis):,} caracteres")
    else:
        text_for_analysis = text

    # ── Paso 3: Generar página de fuente ─────────────────────────────────
    step("Generando página de fuente...")
    source_content = generate_source_page(doc_name, text_for_analysis, model)
    source_path = f"sources/{source_slug}.md"
    write_file(WIKI_DIR / source_path, source_content)
    created.append(source_path)
    index_entries.append(("sources", source_slug, f"Resumen de '{doc_name}'"))
    info(f"Creada: wiki/{source_path}")

    # ── Paso 4: Extraer y crear páginas de conceptos ─────────────────────
    step("Extrayendo conceptos clave...")
    existing_concepts = get_existing_concepts()
    concepts = extract_concepts_from_doc(text_for_analysis, doc_name, existing_concepts, model)
    info(f"{len(concepts)} conceptos identificados")

    for concept in concepts:
        name = concept.get('nombre', '')
        slug = slugify(name)
        if not slug:
            continue

        concept_file = WIKI_DIR / "concepts" / f"{slug}.md"

        if concept_file.exists():
            existing = read_file(concept_file)
            updated_content, changed = update_existing_page(existing, source_slug)
            if changed:
                write_file(concept_file, updated_content)
                updated.append(f"concepts/{slug}.md")
                dim(f"Actualizado: concepts/{slug}.md")
        else:
            content = build_concept_page(concept, source_slug)
            write_file(concept_file, content)
            created.append(f"concepts/{slug}.md")
            desc = concept.get('definicion', '')[:80]
            index_entries.append(("concepts", slug, desc))
            dim(f"Creado: concepts/{slug}.md")

    # ── Paso 5: Extraer entidades ────────────────────────────────────────
    step("Extrayendo entidades...")
    existing_entities = get_existing_entities()
    entities = extract_entities_from_doc(text_for_analysis, doc_name, existing_entities, model)
    info(f"{len(entities)} entidades identificadas")

    for entity in entities:
        name = entity.get('nombre', '')
        slug = slugify(name)
        if not slug:
            continue

        entity_file = WIKI_DIR / "entities" / f"{slug}.md"

        if entity_file.exists():
            existing = read_file(entity_file)
            updated_content, changed = update_existing_page(existing, source_slug)
            if changed:
                write_file(entity_file, updated_content)
                updated.append(f"entities/{slug}.md")
                dim(f"Actualizado: entities/{slug}.md")
        else:
            content = build_entity_page(entity, source_slug)
            write_file(entity_file, content)
            created.append(f"entities/{slug}.md")
            desc = entity.get('descripcion', '')[:80]
            index_entries.append(("entities", slug, desc))
            dim(f"Creado: entities/{slug}.md")

    # ── Paso 6: Generar FAQ ──────────────────────────────────────────────
    step("Generando preguntas frecuentes...")
    faq_content = generate_faq(text_for_analysis, doc_name, source_slug, model)
    faq_slug = f"{source_slug}-faq"
    faq_path = f"faq/{faq_slug}.md"
    write_file(WIKI_DIR / faq_path, faq_content)
    created.append(faq_path)
    index_entries.append(("faq", faq_slug, f"Preguntas frecuentes: '{doc_name}'"))
    info(f"Creada: wiki/{faq_path}")

    # ── Paso 7: Actualizar índice y log ──────────────────────────────────
    step("Actualizando índice y log...")
    update_index(index_entries)
    append_log(doc_name, created, updated)
    info("index.md y log.md actualizados")

    # ── Resumen final ────────────────────────────────────────────────────
    header("INGESTA COMPLETADA")
    info(f"Documento: {doc_name}")
    info(f"Páginas creadas:     {len(created)}")
    info(f"Páginas actualizadas: {len(updated)}")
    if created:
        print()
        for p in created:
            print(f"    {C.GREEN}+{C.END} {p}")
    if updated:
        print()
        for p in updated:
            print(f"    {C.YELLOW}~{C.END} {p}")
    print()


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="LLM Kiwi - Ingesta de documentos a la wiki",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            '  python scripts/ingest.py "Documento CONPES 4144 de Inteligencia Artificial Colombia.pdf"\n'
            "  python scripts/ingest.py --todos\n"
            "  python scripts/ingest.py --model qwen3.5:9b --todos\n"
        )
    )
    parser.add_argument("archivo", nargs="?", help="Nombre o ruta del PDF a ingestar")
    parser.add_argument("--todos", action="store_true", help="Ingestar todos los PDFs pendientes")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Modelo Ollama (default: {DEFAULT_MODEL})")

    args = parser.parse_args()

    header("LLM KIWI - SISTEMA DE INGESTA")

    # Verificar Ollama
    models = check_ollama()
    if models is None:
        error("Ollama no está corriendo. Ejecuta: ollama serve")
        return
    if args.model not in [m.split(":")[0] + ":" + m.split(":")[1] if ":" in m else m for m in models]:
        available = [m for m in models if not m.startswith("nomic") and not m.startswith("embed")]
        warn(f"Modelo '{args.model}' puede no estar disponible.")
        dim(f"Modelos detectados: {', '.join(available[:8])}")

    if args.todos:
        # Procesar todos los PDFs pendientes
        statuses = list_pdf_status()
        pending = [(pdf, slug) for pdf, slug, ingested in statuses if not ingested]

        if not pending:
            info("Todos los documentos ya fueron ingestados.")
            return

        info(f"{len(pending)} documentos pendientes de {len(statuses)} totales")
        print()
        for pdf, slug in pending:
            ingest_document(pdf, args.model)

    elif args.archivo:
        pdf_path = Path(args.archivo)
        if not pdf_path.exists():
            pdf_path = DOCS_DIR / args.archivo
        if not pdf_path.exists():
            error(f"Archivo no encontrado: {args.archivo}")
            dim(f"Buscado en: {DOCS_DIR}")
            return
        ingest_document(pdf_path, args.model)

    else:
        # Mostrar estado de documentos
        parser.print_help()
        print()
        header("DOCUMENTOS DISPONIBLES")
        statuses = list_pdf_status()
        for pdf, slug, ingested in statuses:
            status = f"{C.GREEN}✓ ingestado{C.END}" if ingested else f"{C.DIM}○ pendiente{C.END}"
            print(f"  [{status}] {pdf.name}")
        print()
        pending = sum(1 for _, _, i in statuses if not i)
        if pending:
            info(f"Usa --todos para ingestar los {pending} documentos pendientes")


if __name__ == "__main__":
    main()
