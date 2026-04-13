#!/usr/bin/env python3
"""
LLM Kiwi - Aplicación Web
Interfaz web para gestionar la wiki de conocimiento sobre IA en Colombia.

Uso:
    python scripts/app.py
    python scripts/app.py --port 5001
    python scripts/app.py --model qwen3.5:9b
"""

import os
import sys
import uuid
import threading
import argparse
import webbrowser
import traceback
from pathlib import Path
from datetime import datetime
import unicodedata
from collections import defaultdict

from flask import Flask, render_template, jsonify, request

# ─── Setup de rutas ──────────────────────────────────────────────────────────

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from utils import (
    BASE_DIR, DOCS_DIR, WIKI_DIR, SCHEMA_DIR, DEFAULT_MODEL,
    MAX_CONTEXT_CHARS, extract_pdf_text, chunk_text, call_ollama,
    clean_response, check_ollama, read_file, write_file, append_file,
    load_index, slugify, get_today, get_now, get_wiki_pages,
    extract_wiki_links, get_existing_concepts, get_existing_entities,
    list_pdf_status, load_config, save_config,
)
from ingest import (
    generate_source_page, extract_concepts_from_doc, extract_entities_from_doc,
    generate_faq, build_concept_page, build_entity_page, update_existing_page,
    update_index, append_log, summarize_chunk,
)
from query import select_relevant_pages, load_pages_content, answer_question, save_to_faq
from lint import (
    check_index_completeness, check_broken_links, check_orphan_pages,
    check_empty_pages, check_duplicate_concepts, check_page_structure,
    deep_analysis, fix_index, fix_broken_links,
)

# ─── Flask App ────────────────────────────────────────────────────────────────

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# ─── Manejo global de errores (siempre JSON, nunca HTML) ────────────────────

@app.errorhandler(404)
def handle_404(e):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(405)
def handle_405(e):
    return jsonify({'error': 'Método no permitido'}), 405

@app.errorhandler(500)
def handle_500(e):
    return jsonify({'error': f'Error interno del servidor: {e}'}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Captura cualquier excepción no manejada y devuelve JSON."""
    import traceback
    traceback.print_exc()
    return jsonify({'error': f'Error inesperado: {str(e)}'}), 500

# Almacén global de tareas en background
tasks = {}
active_model = DEFAULT_MODEL


# ─── Helpers ──────────────────────────────────────────────────────────────────

def count_pages_by_type():
    """Cuenta páginas agrupadas por tipo (sources, concepts, etc.)."""
    pages = get_wiki_pages()
    counts = {}
    for p in pages:
        parts = p.split('/')
        ptype = parts[0] if len(parts) > 1 else 'root'
        counts[ptype] = counts.get(ptype, 0) + 1
    return counts


def get_recent_log(n=10):
    """Obtiene las últimas N entradas del log."""
    log = read_file(WIKI_DIR / "log.md")
    entries = []
    current = []
    for line in log.split('\n'):
        if line.startswith('## ['):
            if current:
                entries.append('\n'.join(current))
            current = [line]
        elif current:
            current.append(line)
    if current:
        entries.append('\n'.join(current))
    return entries[-n:] if entries else []


# ─── Rutas de la página ──────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


# ─── API: Estado general ─────────────────────────────────────────────────────

@app.route('/api/status')
def api_status():
    try:
        pages = get_wiki_pages()
        docs = list_pdf_status()
        ollama_models = check_ollama()

        return jsonify({
            'total_pages': len(pages),
            'total_documents': len(docs),
            'ingested': sum(1 for _, _, i in docs if i),
            'pending': sum(1 for _, _, i in docs if not i),
            'pages_by_type': count_pages_by_type(),
            'recent_log': get_recent_log(5),
            'ollama_ok': ollama_models is not None,
            'model': active_model,
            'available_models': [m for m in (ollama_models or [])
                                if not any(m.startswith(x) for x in ('nomic', 'embed'))],
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'total_pages': 0, 'total_documents': 0, 'ingested': 0,
            'pending': 0, 'pages_by_type': {}, 'recent_log': [],
            'ollama_ok': False, 'model': active_model, 'available_models': [],
        }), 500


# ─── API: Documentos ─────────────────────────────────────────────────────────

@app.route('/api/documents')
def api_documents():
    docs = list_pdf_status()
    result = []
    for pdf, slug, ingested in docs:
        size = pdf.stat().st_size
        result.append({
            'name': pdf.name,
            'stem': pdf.stem,
            'slug': slug,
            'ingested': ingested,
            'size': size,
            'size_human': f"{size/1024:.0f} KB" if size < 1048576 else f"{size/1048576:.1f} MB",
        })
    return jsonify(result)


# ─── API: Upload PDFs ────────────────────────────────────────────────────────

@app.route('/api/upload', methods=['POST'])
def api_upload():
    """Sube uno o más PDFs al directorio de papers."""
    if 'files' not in request.files:
        return jsonify({'error': 'No se enviaron archivos'}), 400

    files = request.files.getlist('files')
    uploaded = []
    errors = []

    for f in files:
        if not f.filename:
            continue
        if not f.filename.lower().endswith('.pdf'):
            errors.append(f'{f.filename}: no es un PDF')
            continue
        dest = DOCS_DIR / f.filename
        try:
            f.save(str(dest))
            uploaded.append(f.filename)
        except Exception as e:
            errors.append(f'{f.filename}: {str(e)}')

    return jsonify({'uploaded': uploaded, 'errors': errors})


# ─── API: Delete Document ────────────────────────────────────────────────────

@app.route('/api/documents/<path:filename>', methods=['DELETE'])
def api_delete_document(filename):
    """Elimina un PDF y todas las páginas wiki generadas a partir de él."""
    import re as _re

    pdf_path = DOCS_DIR / filename
    if not pdf_path.exists():
        return jsonify({'error': f'Archivo no encontrado: {filename}'}), 404

    source_slug = slugify(Path(filename).stem)
    source_link = f"[[sources/{source_slug}]]"
    deleted_pages = []

    # 1. Borrar la página de fuente
    source_file = WIKI_DIR / "sources" / f"{source_slug}.md"
    if source_file.exists():
        source_file.unlink()
        deleted_pages.append(f"sources/{source_slug}.md")

    # 2. Borrar FAQ asociado
    faq_file = WIKI_DIR / "faq" / f"{source_slug}-faq.md"
    if faq_file.exists():
        faq_file.unlink()
        deleted_pages.append(f"faq/{source_slug}-faq.md")

    # 3. Buscar concepts y entities que referencian este source y limpiar
    for subdir in ["concepts", "entities"]:
        wiki_subdir = WIKI_DIR / subdir
        if not wiki_subdir.exists():
            continue
        for page_file in list(wiki_subdir.glob("*.md")):
            content = read_file(page_file)
            if source_link in content:
                # Verificar si esta es la ÚNICA fuente
                other_sources = [
                    line for line in content.split('\n')
                    if line.strip().startswith('- [[sources/') and source_link not in line
                ]
                if not other_sources:
                    # Única fuente → borrar la página
                    page_file.unlink()
                    deleted_pages.append(f"{subdir}/{page_file.name}")
                else:
                    # Múltiples fuentes → solo quitar la referencia
                    new_content = content.replace(f"- {source_link}\n", "")
                    new_content = new_content.replace(f"- {source_link}", "")
                    write_file(page_file, new_content)

    # 4. Limpiar index.md
    index_path = WIKI_DIR / "index.md"
    index_content = read_file(index_path)
    new_index_lines = []
    for line in index_content.split('\n'):
        # Quitar líneas que referencian páginas borradas
        skip = False
        for dp in deleted_pages:
            dp_ref = dp.replace('.md', '')
            if f"[[{dp_ref}]]" in line:
                skip = True
                break
        if not skip:
            new_index_lines.append(line)
    write_file(index_path, '\n'.join(new_index_lines))

    # 5. Borrar el PDF
    pdf_path.unlink()

    # 6. Log
    append_file(WIKI_DIR / "log.md",
                f"\n## [{get_today()}] delete | {filename}\n"
                f"- PDF eliminado: {filename}\n"
                f"- Páginas eliminadas: {len(deleted_pages)}\n")

    return jsonify({
        'deleted_pdf': filename,
        'deleted_pages': deleted_pages,
        'total_deleted': len(deleted_pages),
    })


# ─── API: Reset completo ────────────────────────────────────────────────────

@app.route('/api/reset', methods=['POST'])
def api_reset():
    """Borra todos los PDFs y toda la wiki para empezar de cero."""
    deleted_pdfs = []
    deleted_pages = []

    # 1. Borrar todos los PDFs
    for pdf in DOCS_DIR.glob("*.pdf"):
        pdf.unlink()
        deleted_pdfs.append(pdf.name)

    # 2. Borrar todo el contenido wiki (todas las subcarpetas)
    for item in WIKI_DIR.iterdir():
        if item.is_dir():
            for f in item.glob("*.md"):
                deleted_pages.append(f"{item.name}/{f.name}")
                f.unlink()

    # 3. Borrar archivos .md sueltos en la raíz de wiki (excepto los de estructura)
    keep = {"index.md", "log.md", "overview.md"}
    for f in WIKI_DIR.glob("*.md"):
        if f.name not in keep:
            deleted_pages.append(f.name)
            f.unlink()

    # 4. Leer configuración actual
    cfg = load_config()
    topic = cfg.get('topic', 'Conocimiento')

    # 5. Resetear index.md
    write_file(WIKI_DIR / "index.md",
        f"# Índice del Wiki - LLM Kiwi\n\n"
        f"> Wiki de conocimiento sobre {topic}.\n"
        "> Mantenida por un LLM local siguiendo el patrón "
        "[LLM Wiki de Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\n\n"
        "## Overview\n- [[overview]]: Visión general del dominio, mapa del conocimiento y prioridades.\n\n"
        "## Sources\n\n## Concepts\n\n## Entities\n\n## FAQ\n\n## Comparisons\n\n## Timelines\n")

    # 6. Resetear overview.md
    write_file(WIKI_DIR / "overview.md",
        f"# Overview - LLM Kiwi\n\n"
        f"## Dominio\nEsta wiki compila y estructura conocimiento sobre **{topic}**.\n\n"
        f"## Fuentes principales\nLos documentos fuente se encuentran en `/papers/`.\n\n"
        f"## Estado actual\n- Wiki inicializada. Pendiente de ingesta de documentos.\n")

    # 7. Resetear log.md
    write_file(WIKI_DIR / "log.md",
        "# Log del Wiki - LLM Kiwi\n\n"
        "> Historial cronológico de ingestas, consultas y revisiones.\n"
        "> Formato: `## [FECHA] tipo | descripción`\n\n"
        f"## [{get_today()}] reset | Reset completo\n"
        f"- Se eliminaron {len(deleted_pdfs)} PDFs y {len(deleted_pages)} páginas wiki\n")

    return jsonify({
        'deleted_pdfs': len(deleted_pdfs),
        'deleted_pages': len(deleted_pages),
    })


# ─── API: Configuración ──────────────────────────────────────────────────────

@app.route('/api/config')
def api_config_get():
    """Retorna la configuración actual."""
    return jsonify(load_config())


@app.route('/api/config', methods=['POST'])
def api_config_post():
    """Guarda la configuración y regenera archivos base."""
    data = request.json or {}
    cfg = load_config()
    cfg['topic'] = data.get('topic', cfg['topic']).strip()
    cfg['description'] = data.get('description', cfg['description']).strip()
    cfg['domain'] = data.get('domain', cfg['domain']).strip()
    save_config(cfg)

    topic = cfg['topic']
    description = cfg['description']
    domain = cfg['domain']

    # Regenerar overview.md
    write_file(WIKI_DIR / "overview.md",
        f"# Overview - LLM Kiwi\n\n"
        f"## Dominio\nEsta wiki compila y estructura conocimiento sobre **{topic}**.\n\n"
        f"{description}\n\n"
        f"## Fuentes principales\nLos documentos fuente se encuentran en `/papers/`.\n\n"
        f"## Estado actual\n- Wiki inicializada. Pendiente de ingesta de documentos.\n")

    # Regenerar index.md header (solo si está en estado limpio)
    index = read_file(WIKI_DIR / "index.md")
    old_header_end = index.find("## Overview")
    if old_header_end > 0:
        write_file(WIKI_DIR / "index.md",
            f"# Índice del Wiki - LLM Kiwi\n\n"
            f"> Wiki de conocimiento sobre {topic}.\n"
            "> Mantenida por un LLM local siguiendo el patrón "
            "[LLM Wiki de Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\n\n"
            + index[old_header_end:])

    # Regenerar schema/AGENTS.md
    write_file(SCHEMA_DIR / "AGENTS.md",
        f"# Reglas del LLM Kiwi - Wiki de {topic}\n\n"
        f"## Rol\n"
        f"Eres el mantenedor de una wiki local en Markdown sobre {topic}.\n"
        f"No eres un chatbot genérico. Tu trabajo es compilar, estructurar y mantener conocimiento.\n\n"
        f"## Dominio\n{domain}\n\n"
        f"## Objetivo\n"
        f"Mantener una base de conocimiento coherente, enlazada y acumulativa a partir de\n"
        f"documentos locales. Cada ingesta debe dejar la wiki más completa y mejor conectada.\n\n"
        f"## Idioma\n"
        f"Escribe siempre en español. Mantén términos técnicos en su idioma original cuando\n"
        f"sea la convención (e.g., \"machine learning\", \"deep learning\", \"RAG\", \"agentic AI\").\n\n"
        "---\n\n"
        "## Reglas de Ingesta (ingest)\n\n"
        "1. **Nunca** modificar archivos dentro de `/papers/` ni `/raw/`. Son fuentes inmutables.\n"
        "2. Leer la fuente completa y crear o actualizar páginas en `/wiki/`.\n"
        "3. Crear una página de fuente en `/wiki/sources/` con resumen estructurado.\n"
        "4. Identificar conceptos clave y crear o actualizar páginas en `/wiki/concepts/`.\n"
        "5. Identificar entidades (organizaciones, personas, leyes) y usar `/wiki/entities/`.\n"
        "6. Generar preguntas frecuentes en `/wiki/faq/`.\n"
        "7. **Siempre** actualizar `/wiki/index.md` con las nuevas páginas.\n"
        "8. **Siempre** registrar la ingesta en `/wiki/log.md` con fecha y cambios.\n"
        "9. Reutilizar páginas existentes antes de crear nuevas. Evitar duplicados.\n"
        "10. Usar enlaces internos tipo `[[pagina]]` para conectar conceptos.\n\n"
        "## Reglas de Consulta (query)\n\n"
        "1. Leer primero `/wiki/index.md` para orientarse.\n"
        "2. Leer las páginas más relevantes según la pregunta.\n"
        "3. Responder **usando la wiki como fuente principal**, no inventar.\n"
        "4. Citar las páginas consultadas con enlaces `[[fuente]]`.\n"
        "5. Si falta contexto, indicarlo claramente: \"La wiki no contiene información sobre X.\"\n"
        "6. Si la respuesta aporta valor duradero, sugerir guardarla en `/wiki/faq/` o `/wiki/comparisons/`.\n\n"
        "## Reglas de Mantenimiento (lint)\n\n"
        "1. Detectar páginas huérfanas (sin enlaces entrantes).\n"
        "2. Detectar enlaces rotos (apuntan a páginas inexistentes).\n"
        "3. Detectar conceptos mencionados pero sin página propia.\n"
        "4. Verificar que todas las páginas estén en `index.md`.\n"
        "5. Detectar posibles duplicados o solapamientos.\n"
        "6. Detectar contradicciones entre fuentes.\n"
        "7. Sugerir nuevas páginas, comparaciones o líneas de tiempo.\n\n"
        "## Convenciones de Escritura\n\n"
        "- Markdown claro y simple.\n"
        "- Títulos con `#`, subtítulos con `##`.\n"
        "- Enlaces internos: `[[nombre-pagina]]` o `[[ruta/nombre-pagina]]`.\n"
        "- Listas con `-` para items, `1.` para pasos ordenados.\n"
        "- Citas textuales con `>`.\n"
        "- **No inventar hechos.** Si algo es inferencia, marcarlo como tal.\n"
        "- **Marcar incertidumbre** cuando exista: \"(dato no confirmado)\" o \"(requiere verificación)\".\n"
        "- Nombres de archivo en minúsculas, sin tildes, separados por guiones: `ejemplo-concepto.md`.\n\n"
        "## Estructura de Páginas\n\n"
        "Cada página debe seguir una estructura consistente según su tipo:\n\n"
        "### Página de Fuente (sources/)\n```\n# [Título del documento]\n## Resumen\n## Datos clave\n"
        "## Temas principales\n## Relación con otros conceptos\n## Citas textuales relevantes\n## Notas\n```\n\n"
        "### Página de Concepto (concepts/)\n```\n# [Nombre del concepto]\n## Definición\n## Ideas clave\n"
        "## Relación con otros conceptos\n## Fuentes relacionadas\n## Preguntas abiertas\n```\n\n"
        "### Página de Entidad (entities/)\n```\n# [Nombre de la entidad]\n## Descripción\n"
        "## Rol en el ecosistema\n## Documentos relacionados\n## Fuentes\n```\n\n"
        "### Página de FAQ (faq/)\n```\n# FAQ: [Tema]\n## ¿Pregunta?\nRespuesta...\n## Fuentes\n```\n\n"
        "### Página de Comparación (comparisons/)\n```\n# Comparación: [X] vs [Y]\n## Contexto\n"
        "## Similitudes\n## Diferencias\n## Conclusión\n## Fuentes\n```\n\n"
        "### Página de Línea de Tiempo (timelines/)\n```\n# Línea de tiempo: [Tema]\n"
        "## [Año/Fecha] - [Evento]\nDescripción...\n## Fuentes\n```\n")

    return jsonify({'saved': True, 'config': cfg})


# ─── API: Modelo ──────────────────────────────────────────────────────────────

@app.route('/api/model', methods=['POST'])
def api_set_model():
    global active_model
    data = request.json or {}
    model = data.get('model', DEFAULT_MODEL)
    active_model = model
    return jsonify({'model': active_model})


# ─── API: Ingesta ────────────────────────────────────────────────────────────

@app.route('/api/ingest', methods=['POST'])
def api_ingest():
    data = request.json or {}
    model = data.get('model', active_model)

    if data.get('all'):
        docs = list_pdf_status()
        pending = [(pdf, slug) for pdf, slug, ingested in docs if not ingested]
        if not pending:
            return jsonify({'error': 'Todos los documentos ya fueron ingestados'}), 400

        task_id = str(uuid.uuid4())[:8]
        tasks[task_id] = {
            'id': task_id, 'type': 'ingest_all', 'status': 'running',
            'steps': [], 'current_step': 'Iniciando...',
            'files': [p.name for p, _ in pending],
            'current_file_idx': 0, 'total_files': len(pending),
            'created': [], 'updated': [],
        }
        t = threading.Thread(target=_run_ingest_all, args=(task_id, pending, model), daemon=True)
        t.start()
        return jsonify({'task_id': task_id})

    elif data.get('file'):
        filename = data['file']
        pdf_path = DOCS_DIR / filename
        if not pdf_path.exists():
            return jsonify({'error': f'Archivo no encontrado: {filename}'}), 404

        task_id = str(uuid.uuid4())[:8]
        tasks[task_id] = {
            'id': task_id, 'type': 'ingest_single', 'status': 'running',
            'steps': [], 'current_step': 'Iniciando...',
            'files': [filename],
            'current_file_idx': 0, 'total_files': 1,
            'created': [], 'updated': [],
        }
        t = threading.Thread(target=_run_ingest_single, args=(task_id, pdf_path, model), daemon=True)
        t.start()
        return jsonify({'task_id': task_id})

    return jsonify({'error': 'Especifica "file" o "all"'}), 400


@app.route('/api/ingest/status/<task_id>')
def api_ingest_status(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    return jsonify(task)


def _add_step(task_id, name, detail=''):
    tasks[task_id]['steps'].append({'name': name, 'detail': detail, 'done': True})


def _run_ingest_single(task_id, pdf_path, model):
    """Ingesta de un solo documento en background."""
    task = tasks[task_id]
    doc_name = pdf_path.stem
    source_slug = slugify(doc_name)

    try:
        # 1. Extraer texto
        task['current_step'] = f'Extrayendo texto: {pdf_path.name}'
        text = extract_pdf_text(pdf_path)
        if not text.strip():
            task['status'] = 'error'
            task['error'] = 'No se pudo extraer texto del PDF (puede ser un escaneo sin OCR)'
            return
        _add_step(task_id, 'Texto extraido', f'{len(text):,} caracteres')

        # 2. Chunking si es necesario
        if len(text) > MAX_CONTEXT_CHARS:
            task['current_step'] = 'Resumiendo documento largo...'
            chunks = chunk_text(text)
            summaries = []
            for i, chunk in enumerate(chunks, 1):
                task['current_step'] = f'Resumiendo fragmento {i}/{len(chunks)}...'
                s = summarize_chunk(chunk, doc_name, i, len(chunks), model)
                summaries.append(s)
            text_for_analysis = "\n\n---\n\n".join(summaries)
            _add_step(task_id, 'Resumen de chunks', f'{len(chunks)} fragmentos')
        else:
            text_for_analysis = text

        created = []
        updated = []
        index_entries = []

        # 3. Pagina de fuente
        task['current_step'] = 'Generando pagina de fuente...'
        source_content = generate_source_page(doc_name, text_for_analysis, model)
        source_path = f"sources/{source_slug}.md"
        write_file(WIKI_DIR / source_path, source_content)
        created.append(source_path)
        index_entries.append(("sources", source_slug, f"Resumen de '{doc_name}'"))
        _add_step(task_id, 'Pagina de fuente', source_path)

        # 4. Conceptos
        task['current_step'] = 'Extrayendo conceptos clave...'
        existing_concepts = get_existing_concepts()
        concepts = extract_concepts_from_doc(text_for_analysis, doc_name, existing_concepts, model)

        for concept in concepts:
            name = concept.get('nombre', '')
            slug = slugify(name)
            if not slug:
                continue
            cfile = WIKI_DIR / "concepts" / f"{slug}.md"
            if cfile.exists():
                old = read_file(cfile)
                new, changed = update_existing_page(old, source_slug)
                if changed:
                    write_file(cfile, new)
                    updated.append(f"concepts/{slug}.md")
            else:
                write_file(cfile, build_concept_page(concept, source_slug))
                created.append(f"concepts/{slug}.md")
                index_entries.append(("concepts", slug, concept.get('definicion', '')[:80]))

        _add_step(task_id, 'Conceptos', f'{len(concepts)} identificados')

        # 5. Entidades
        task['current_step'] = 'Extrayendo entidades...'
        existing_entities = get_existing_entities()
        entities = extract_entities_from_doc(text_for_analysis, doc_name, existing_entities, model)

        for entity in entities:
            name = entity.get('nombre', '')
            slug = slugify(name)
            if not slug:
                continue
            efile = WIKI_DIR / "entities" / f"{slug}.md"
            if efile.exists():
                old = read_file(efile)
                new, changed = update_existing_page(old, source_slug)
                if changed:
                    write_file(efile, new)
                    updated.append(f"entities/{slug}.md")
            else:
                write_file(efile, build_entity_page(entity, source_slug))
                created.append(f"entities/{slug}.md")
                index_entries.append(("entities", slug, entity.get('descripcion', '')[:80]))

        _add_step(task_id, 'Entidades', f'{len(entities)} identificadas')

        # 6. FAQ
        task['current_step'] = 'Generando FAQ...'
        faq_content = generate_faq(text_for_analysis, doc_name, source_slug, model)
        faq_slug = f"{source_slug}-faq"
        write_file(WIKI_DIR / f"faq/{faq_slug}.md", faq_content)
        created.append(f"faq/{faq_slug}.md")
        index_entries.append(("faq", faq_slug, f"FAQ: '{doc_name}'"))
        _add_step(task_id, 'FAQ generado')

        # 7. Index + Log
        task['current_step'] = 'Actualizando indice y log...'
        update_index(index_entries)
        append_log(doc_name, created, updated)
        _add_step(task_id, 'Indice y log actualizados')

        task['created'] = created
        task['updated'] = updated
        task['status'] = 'completed'
        task['current_step'] = 'Completado'

    except Exception as e:
        task['status'] = 'error'
        task['error'] = str(e)
        task['traceback'] = traceback.format_exc()


def _run_ingest_all(task_id, pending, model):
    """Ingesta de múltiples documentos en secuencia."""
    task = tasks[task_id]
    all_created = []
    all_updated = []

    for idx, (pdf, slug) in enumerate(pending):
        task['current_file_idx'] = idx
        task['current_step'] = f'[{idx+1}/{len(pending)}] Procesando: {pdf.name}'

        # Crear sub-task temporal
        sub_id = f"{task_id}_sub"
        tasks[sub_id] = {
            'id': sub_id, 'status': 'running', 'steps': [],
            'current_step': '', 'files': [pdf.name],
            'current_file_idx': 0, 'total_files': 1,
            'created': [], 'updated': [],
        }
        _run_ingest_single(sub_id, pdf, model)
        sub = tasks.pop(sub_id)

        if sub['status'] == 'error':
            task['steps'].append({
                'name': f'{pdf.name}', 'detail': f"Error: {sub.get('error', '?')}", 'done': False
            })
        else:
            all_created.extend(sub.get('created', []))
            all_updated.extend(sub.get('updated', []))
            task['steps'].append({
                'name': pdf.name,
                'detail': f"+{len(sub.get('created',[]))} ~{len(sub.get('updated',[]))}",
                'done': True,
            })

    task['created'] = all_created
    task['updated'] = all_updated
    task['status'] = 'completed'
    task['current_step'] = f'Completado: {len(pending)} documentos procesados'


# ─── API: Consulta ───────────────────────────────────────────────────────────

@app.route('/api/query', methods=['POST'])
def api_query():
    data = request.json or {}
    question = data.get('question', '').strip()
    model = data.get('model', active_model)
    save = data.get('save', False)

    if not question:
        return jsonify({'error': 'Escribe una pregunta'}), 400

    pages = get_wiki_pages()
    content_pages = [p for p in pages if p not in ("index.md", "log.md", "overview.md")]
    if not content_pages:
        return jsonify({'error': 'La wiki esta vacia. Ingesta documentos primero.'}), 400

    try:
        selected = select_relevant_pages(question, model)
        pages_content = load_pages_content(selected)
        answer = answer_question(question, pages_content, model)

        if save:
            save_to_faq(question, answer)

        return jsonify({
            'answer': answer,
            'pages_consulted': selected,
            'saved': save,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/query/save-faq', methods=['POST'])
def api_save_faq():
    """Guarda una respuesta existente en FAQ (post-hoc)."""
    try:
        data = request.json or {}
        question = data.get('question', '').strip()
        answer = data.get('answer', '').strip()
        if not question or not answer:
            return jsonify({'error': 'Faltan question o answer'}), 400
        save_to_faq(question, answer)
        return jsonify({'saved': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ─── API: Wiki Browser ───────────────────────────────────────────────────────

@app.route('/api/wiki/pages')
def api_wiki_pages():
    pages = get_wiki_pages()
    result = []
    for p in pages:
        content = read_file(WIKI_DIR / p)
        # Extraer titulo
        import re
        title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_m.group(1) if title_m else p.replace('.md', '').replace('-', ' ').title()
        parts = p.split('/')
        ptype = parts[0] if len(parts) > 1 else 'root'
        result.append({
            'path': p,
            'type': ptype,
            'title': title,
            'size': len(content),
        })
    return jsonify(result)


@app.route('/api/wiki/page/<path:page_path>')
def api_wiki_page(page_path):
    if not page_path.endswith('.md'):
        page_path += '.md'
    full_path = WIKI_DIR / page_path
    content = read_file(full_path)
    if not content:
        return jsonify({'error': f'Pagina no encontrada: {page_path}'}), 404
    return jsonify({'path': page_path, 'content': content})


# ─── API: Lint ────────────────────────────────────────────────────────────────

@app.route('/api/lint', methods=['POST'])
def api_lint():
    try:
        data = request.json or {}
        do_deep = data.get('deep', False)
        do_fix = data.get('fix', False)
        model = data.get('model', active_model)

        issues = []

        try:
            issues.extend(check_index_completeness())
        except Exception as e:
            issues.append(("lint_error", "check_index", f"Error al verificar índice: {e}"))

        try:
            issues.extend(check_broken_links())
        except Exception as e:
            issues.append(("lint_error", "check_links", f"Error al verificar enlaces: {e}"))

        try:
            issues.extend(check_orphan_pages())
        except Exception as e:
            issues.append(("lint_error", "check_orphans", f"Error al verificar huérfanas: {e}"))

        try:
            issues.extend(check_empty_pages())
        except Exception as e:
            issues.append(("lint_error", "check_empty", f"Error al verificar vacías: {e}"))

        try:
            issues.extend(check_duplicate_concepts())
        except Exception as e:
            issues.append(("lint_error", "check_duplicates", f"Error al verificar duplicados: {e}"))

        try:
            issues.extend(check_page_structure())
        except Exception as e:
            issues.append(("lint_error", "check_structure", f"Error al verificar estructura: {e}"))

        if do_deep:
            try:
                issues.extend(deep_analysis(model))
            except Exception as e:
                issues.append(("lint_error", "deep_analysis", f"Error en análisis profundo: {e}"))

        fixed_count = 0
        if do_fix:
            try:
                fixed_count += fix_broken_links(issues)
            except Exception as e:
                issues.append(("lint_error", "fix_broken_links", f"Error al corregir enlaces rotos: {e}"))
            try:
                fixed_count += fix_index(issues)
            except Exception as e:
                issues.append(("lint_error", "fix_index", f"Error al corregir índice: {e}"))

        # Agrupar por tipo
        grouped = {}
        for itype, page, desc in issues:
            grouped.setdefault(itype, []).append({'page': page, 'description': desc})

        errors = sum(1 for t, _, _ in issues if t in ("broken_link", "empty"))
        warnings = len(issues) - errors

        return jsonify({
            'total': len(issues),
            'errors': errors,
            'warnings': warnings,
            'fixed': fixed_count,
            'issues': grouped,
        })

    except Exception as e:
        return jsonify({'error': f'Error en el análisis de salud: {str(e)}'}), 500


# ─── API: Log ────────────────────────────────────────────────────────────────

@app.route('/api/log')
def api_log():
    content = read_file(WIKI_DIR / "log.md")
    return jsonify({'content': content})


# ─── API: Overview ────────────────────────────────────────────────────────────

@app.route('/api/overview')
def api_overview():
    content = read_file(WIKI_DIR / "overview.md")
    return jsonify({'content': content})


# ─── API: Graph ──────────────────────────────────────────────────────────

@app.route('/api/graph')
def api_graph():
    """Genera datos de grafo: nodos y aristas entre páginas wiki."""
    import re
    pages = get_wiki_pages()
    skip = {'index.md', 'log.md', 'overview.md'}
    pages = [p for p in pages if p not in skip]

    # Lookup: slug y path completo -> path sin .md
    slug_to_path = {}
    for p in pages:
        pne = p.replace('.md', '')
        slug = pne.split('/')[-1]
        if slug not in slug_to_path:
            slug_to_path[slug] = pne
        slug_to_path[pne] = pne

    nodes = []
    edges = []
    edge_set = set()

    for p in pages:
        pne = p.replace('.md', '')
        parts = pne.split('/')
        node_type = parts[0] if len(parts) > 1 else 'root'

        content = read_file(WIKI_DIR / p)
        title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_m.group(1) if title_m else parts[-1].replace('-', ' ').title()

        links = extract_wiki_links(content)

        nodes.append({
            'id': pne,
            'label': title,
            'type': node_type,
            'links': len(links),
        })

        for link in links:
            target = link.strip()
            resolved = slug_to_path.get(target) or slug_to_path.get(target.replace('.md', ''))
            if resolved and resolved != pne:
                edge_key = (pne, resolved)
                if edge_key not in edge_set:
                    edge_set.add(edge_key)
                    edges.append({'source': pne, 'target': resolved})

    return jsonify({'nodes': nodes, 'edges': edges})


# ─── API: Graph Explore ─────────────────────────────────────────────────

def _norm(s):
    """Normaliza texto: sin acentos, minúsculas."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.lower()


def _build_graph_data():
    """Construye la estructura completa del grafo."""
    import re as _re
    pages = get_wiki_pages()
    skip = {'index.md', 'log.md', 'overview.md'}
    pages = [p for p in pages if p not in skip]

    slug_map = {}
    for p in pages:
        pne = p.replace('.md', '')
        slug = pne.split('/')[-1]
        if slug not in slug_map:
            slug_map[slug] = pne
        slug_map[pne] = pne

    nodes = {}
    all_edges = []
    adj = defaultdict(set)
    edge_set = set()

    for p in pages:
        pne = p.replace('.md', '')
        parts = pne.split('/')
        ntype = parts[0] if len(parts) > 1 else 'root'
        content = read_file(WIKI_DIR / p)
        tm = _re.search(r'^# (.+)$', content, _re.MULTILINE)
        title = tm.group(1) if tm else parts[-1].replace('-', ' ').title()
        links = extract_wiki_links(content)

        nodes[pne] = {
            'id': pne, 'label': title, 'type': ntype,
            'links': len(links), 'snippet': content[:500],
        }

        for lnk in links:
            target = lnk.strip()
            resolved = slug_map.get(target) or slug_map.get(target.replace('.md', ''))
            if resolved and resolved != pne:
                ek = (pne, resolved)
                if ek not in edge_set:
                    edge_set.add(ek)
                    all_edges.append({'source': pne, 'target': resolved})
                adj[pne].add(resolved)
                adj[resolved].add(pne)

    return nodes, all_edges, adj


def _search_nodes(query, nodes, max_results=15):
    """Busca nodos por coincidencia de texto."""
    terms = _norm(query).split()
    if not terms:
        return []
    scored = []
    for nid, nd in nodes.items():
        ln = _norm(nd['label'])
        idn = _norm(nid)
        sn = _norm(nd.get('snippet', ''))
        score = sum(
            (10 if t in ln else 0) + (5 if t in idn else 0) + (2 if t in sn else 0)
            for t in terms
        )
        if score > 0:
            scored.append((nid, score))
    scored.sort(key=lambda x: -x[1])
    return [nid for nid, _ in scored[:max_results]]


def _subgraph(nodes, edges, adj, seeds, depth=1, max_n=40):
    """Extrae subgrafo alrededor de nodos semilla."""
    seed_set = set(s for s in seeds if s in nodes)
    inc = set(seed_set)
    front = set(seed_set)
    for _ in range(depth):
        nf = set()
        for nid in front:
            for nb in adj.get(nid, set()):
                if nb not in inc and nb in nodes:
                    nf.add(nb)
        inc.update(nf)
        front = nf
        if len(inc) >= max_n:
            break
    if len(inc) > max_n:
        rest = sorted(
            [n for n in inc if n not in seed_set],
            key=lambda n: sum(1 for s in seed_set if n in adj.get(s, set())),
            reverse=True,
        )
        inc = seed_set | set(rest[:max(0, max_n - len(seed_set))])
    sub_n = []
    for nid in inc:
        nd = {k: v for k, v in nodes[nid].items() if k != 'snippet'}
        nd['is_seed'] = nid in seed_set
        sub_n.append(nd)
    sub_e = [e for e in edges if e['source'] in inc and e['target'] in inc]
    return sub_n, sub_e


def _cluster_overview(nodes, edges):
    """Vista de clusters por categoría."""
    cats = {}
    for nid, nd in nodes.items():
        c = nd['type']
        if c not in cats:
            cats[c] = {'count': 0, 'top': []}
        cats[c]['count'] += 1
        if len(cats[c]['top']) < 5:
            cats[c]['top'].append(nd['label'])

    ce = defaultdict(int)
    for e in edges:
        st = nodes.get(e['source'], {}).get('type', '')
        tt = nodes.get(e['target'], {}).get('type', '')
        if st and tt:
            ce[tuple(sorted([st, tt]))] += 1

    on = [{'id': f'__c_{c}', 'label': c, 'type': c, 'links': d['count'],
           'is_cluster': True, 'count': d['count'], 'top': d['top']}
          for c, d in cats.items()]
    oe = [{'source': f'__c_{a}', 'target': f'__c_{b}', 'weight': n, 'label': str(n)}
          for (a, b), n in ce.items()]
    return on, oe


@app.route('/api/graph/explore', methods=['POST'])
def api_graph_explore():
    """Exploración inteligente del grafo con subgrafos enfocados."""
    data = request.json or {}
    query = data.get('query', '').strip()
    mode = data.get('mode', 'overview')
    node_id = data.get('node_id', '')
    category = data.get('category', '')
    max_nodes = min(int(data.get('max_nodes', 40)), 80)
    depth = min(int(data.get('depth', 1)), 3)
    analyze = data.get('analyze', False)
    model = data.get('model', active_model)

    nodes, edges, adj = _build_graph_data()
    insights = ''
    seeds = []

    if mode == 'overview':
        sub_n, sub_e = _cluster_overview(nodes, edges)

    elif mode == 'smart_search' and query:
        # Búsqueda inteligente: usa LLM para identificar páginas relevantes
        try:
            page_list = "\n".join(
                f"- {nid}: {nd['label']} ({nd['type']})"
                for nid, nd in nodes.items()
            )
            select_prompt = (
                f"Dada esta pregunta: \"{query}\"\n\n"
                f"Y estas páginas de wiki disponibles:\n{page_list}\n\n"
                f"Selecciona las 5-10 páginas MÁS RELEVANTES para responder la pregunta.\n"
                f"Responde SOLO con los IDs de las páginas (uno por línea, sin explicaciones)."
            )
            llm_resp = call_ollama([
                {"role": "system", "content": "Seleccionas páginas relevantes de una wiki. Solo responde con IDs."},
                {"role": "user", "content": select_prompt}
            ], model=model, temperature=0.1)
            smart_seeds = []
            for line in llm_resp.strip().split('\n'):
                line = line.strip().lstrip('-').lstrip('*').strip().strip('`')
                # Buscar coincidencia con nodos existentes
                if line in nodes:
                    smart_seeds.append(line)
                else:
                    for nid in nodes:
                        if nid in line or line in nid:
                            smart_seeds.append(nid)
                            break
            if smart_seeds:
                seeds = list(dict.fromkeys(smart_seeds))[:12]
            else:
                seeds = _search_nodes(query, nodes, max_results=max(5, max_nodes // 3))
        except Exception:
            seeds = _search_nodes(query, nodes, max_results=max(5, max_nodes // 3))

        if not seeds:
            return jsonify({'nodes': [], 'edges': [], 'insights': '', 'seeds': [],
                            'total_nodes': len(nodes), 'total_edges': len(edges)})
        sub_n, sub_e = _subgraph(nodes, edges, adj, seeds, depth, max_nodes)

    elif mode == 'search' and query:
        seeds = _search_nodes(query, nodes, max_results=max(5, max_nodes // 3))
        if not seeds:
            return jsonify({'nodes': [], 'edges': [], 'insights': '', 'seeds': [],
                            'total_nodes': len(nodes), 'total_edges': len(edges)})
        sub_n, sub_e = _subgraph(nodes, edges, adj, seeds, depth, max_nodes)

    elif mode == 'neighborhood' and node_id:
        if node_id not in nodes:
            return jsonify({'nodes': [], 'edges': [], 'insights': 'Nodo no encontrado.',
                            'seeds': [], 'total_nodes': len(nodes), 'total_edges': len(edges)})
        seeds = [node_id]
        sub_n, sub_e = _subgraph(nodes, edges, adj, seeds, depth, max_nodes)

    elif mode == 'query_pages':
        # Grafo desde páginas específicas de una consulta
        page_seeds = data.get('seeds', [])
        valid_seeds = [s for s in page_seeds if s in nodes]
        if valid_seeds:
            seeds = valid_seeds
            sub_n, sub_e = _subgraph(nodes, edges, adj, seeds, depth=1, max_n=max_nodes)
        else:
            sub_n, sub_e = [], []

    elif mode == 'category' and category:
        cat_nodes = [(nid, len(adj.get(nid, set())))
                     for nid, nd in nodes.items() if nd['type'] == category]
        cat_nodes.sort(key=lambda x: -x[1])
        seeds = [nid for nid, _ in cat_nodes[:max(5, max_nodes // 2)]]
        if seeds:
            sub_n, sub_e = _subgraph(nodes, edges, adj, seeds, depth=1, max_n=max_nodes)
        else:
            sub_n, sub_e = [], []

    else:
        sub_n, sub_e = _cluster_overview(nodes, edges)

    # Análisis LLM opcional
    if analyze and sub_n and query:
        try:
            descs = []
            for n in sub_n[:25]:
                nid = n['id']
                snip = nodes.get(nid, {}).get('snippet', '')[:200] if nid in nodes else ''
                descs.append(f"- {n['label']} ({n['type']})" + (f": {snip}" if snip else ""))
            edescs = [
                f"  {nodes.get(e['source'], {}).get('label', e['source'])} -> "
                f"{nodes.get(e['target'], {}).get('label', e['target'])}"
                for e in sub_e[:40]
            ]
            prompt = (
                f"Analiza este subgrafo de conocimiento sobre IA y agentes.\n\n"
                f"Consulta: {query}\n\n"
                f"Nodos ({len(sub_n)}):\n" + "\n".join(descs) + "\n\n"
                f"Conexiones ({len(sub_e)}):\n" + "\n".join(edescs) + "\n\n"
                "Genera un análisis breve:\n"
                "1. **Resumen**: Qué muestra este subgrafo (2-3 oraciones)\n"
                "2. **Hallazgos clave**: 3-5 patrones o relaciones importantes\n"
                "3. **Nodos centrales**: Conceptos/entidades más conectados y por qué importan\n"
                "4. **Recomendaciones**: 2-3 preguntas o acciones para profundizar\n\n"
                "Responde en español, conciso y orientado a decisiones."
            )
            insights = call_ollama([
                {"role": "system", "content": "Eres un analista de grafos de conocimiento. "
                 "Encuentra patrones e insights accionables."},
                {"role": "user", "content": prompt}
            ], model=model, temperature=0.3)
        except Exception as e:
            insights = f"Error en análisis: {str(e)}"

    return jsonify({
        'nodes': sub_n, 'edges': sub_e, 'insights': insights,
        'seeds': seeds, 'total_nodes': len(nodes), 'total_edges': len(edges),
    })


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    global active_model
    parser = argparse.ArgumentParser(description="LLM Kiwi - Aplicacion Web")
    parser.add_argument('--port', type=int, default=5001, help='Puerto (default: 5001)')
    parser.add_argument('--model', default=DEFAULT_MODEL, help=f'Modelo Ollama (default: {DEFAULT_MODEL})')
    parser.add_argument('--no-browser', action='store_true', help='No abrir navegador automaticamente')
    args = parser.parse_args()

    active_model = args.model

    print(f"\n  LLM Kiwi - Wiki de Agentes de IA")
    print(f"  {'-' * 40}")
    print(f"  Modelo:  {active_model}")
    print(f"  Puerto:  {args.port}")
    print(f"  Wiki:    {WIKI_DIR}")
    print(f"  Docs:    {DOCS_DIR}")

    ollama = check_ollama()
    if ollama:
        print(f"  Ollama:  OK ({len(ollama)} modelos)")
    else:
        print(f"  Ollama:  NO DISPONIBLE - ejecuta 'ollama serve'")

    print(f"  {'-' * 40}")
    print(f"  http://localhost:{args.port}\n")

    if not args.no_browser:
        threading.Timer(1.5, lambda: webbrowser.open(f'http://localhost:{args.port}')).start()

    app.run(host='0.0.0.0', port=args.port, debug=False)


if __name__ == '__main__':
    main()
