"""
LLM Kiwi - Utilidades compartidas
Wiki de conocimiento local basada en el patrón LLM Wiki de Karpathy.
"""

import os
import re
import json
import requests
import anthropic
import fitz  # PyMuPDF
from pathlib import Path
from datetime import datetime

# ─── Configuración ───────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "papers"
WIKI_DIR = BASE_DIR / "wiki"
SCHEMA_DIR = BASE_DIR / "schema"
OUTPUTS_DIR = BASE_DIR / "outputs"

CONFIG_PATH = BASE_DIR / "config.json"

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "qwen2.5:7b"
DEFAULT_CLAUDE_MODEL = "claude-sonnet-4-6"
DEFAULT_PROVIDER = "claude"

# Límites de texto (en caracteres).
MAX_CONTEXT_CHARS = 60000
CHUNK_SIZE = 20000
CHUNK_OVERLAP = 800


# ─── Colores para terminal ───────────────────────────────────────────────────

class C:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BLUE   = "\033[94m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    END    = "\033[0m"


def info(msg):
    print(f"  {C.GREEN}✓{C.END} {msg}")

def warn(msg):
    print(f"  {C.YELLOW}⚠{C.END} {msg}")

def error(msg):
    print(f"  {C.RED}✗{C.END} {msg}")

def step(msg):
    print(f"\n  {C.CYAN}►{C.END} {C.BOLD}{msg}{C.END}")

def header(title):
    width = 60
    print(f"\n{C.BOLD}{C.BLUE}{'─' * width}")
    print(f"  {title}")
    print(f"{'─' * width}{C.END}")

def dim(msg):
    print(f"    {C.DIM}{msg}{C.END}")


# ─── Extracción de PDF ───────────────────────────────────────────────────────

def extract_pdf_text(pdf_path):
    """Extrae texto completo de un PDF usando PyMuPDF."""
    doc = fitz.open(str(pdf_path))
    pages = []
    for page in doc:
        text = page.get_text()
        if text.strip():
            pages.append(text.strip())
    doc.close()
    full_text = "\n\n".join(pages)
    # Limpiar saltos de línea excesivos y espacios
    full_text = re.sub(r'\n{3,}', '\n\n', full_text)
    full_text = re.sub(r' {2,}', ' ', full_text)
    return full_text


# ─── Chunking ────────────────────────────────────────────────────────────────

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Divide texto largo en chunks con overlap entre ellos."""
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 > chunk_size and current:
            chunks.append(current.strip())
            # Mantener overlap del final del chunk anterior
            words = current.split()
            overlap_text = " ".join(words[-overlap // 5:]) if len(words) > overlap // 5 else ""
            current = overlap_text + "\n\n" + para
        else:
            current = (current + "\n\n" + para) if current else para

    if current.strip():
        chunks.append(current.strip())

    return chunks


# ─── LLM API ─────────────────────────────────────────────────────────────────

def call_claude(messages, model=None, temperature=0.3):
    """Llama a la API de Claude (Anthropic) y retorna el contenido de la respuesta."""
    model = model or DEFAULT_CLAUDE_MODEL
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        error("No se encontró ANTHROPIC_API_KEY en las variables de entorno.")
        raise SystemExit(1)

    client = anthropic.Anthropic(api_key=api_key)

    system_msg = ""
    chat_messages = []
    for m in messages:
        if m["role"] == "system":
            system_msg = m["content"]
        else:
            chat_messages.append({"role": m["role"], "content": m["content"]})

    kwargs = {
        "model": model,
        "max_tokens": 8192,
        "messages": chat_messages,
    }
    if system_msg:
        kwargs["system"] = system_msg

    try:
        response = client.messages.create(**kwargs)
        return clean_response(response.content[0].text)
    except anthropic.AuthenticationError:
        error("API key de Claude inválida. Verifica ANTHROPIC_API_KEY.")
        raise SystemExit(1)
    except anthropic.RateLimitError:
        error("Límite de uso de Claude alcanzado. Intenta más tarde.")
        raise
    except Exception as e:
        error(f"Error con Claude API: {e}")
        raise


def _call_ollama_direct(messages, model=None, temperature=0.3, timeout=300):
    """Llama directamente a Ollama (uso interno)."""
    model = model or DEFAULT_MODEL
    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_ctx": 32768,
            }
        }, timeout=timeout)
        resp.raise_for_status()
        content = resp.json()["message"]["content"]
        return clean_response(content)
    except requests.ConnectionError:
        error("No se puede conectar a Ollama. ¿Está corriendo?")
        error("Ejecuta: ollama serve")
        raise SystemExit(1)
    except requests.Timeout:
        error(f"Timeout ({timeout}s) al llamar a Ollama.")
        raise
    except KeyError:
        error(f"Respuesta inesperada de Ollama: {resp.text[:200]}")
        raise
    except Exception as e:
        error(f"Error con Ollama: {e}")
        raise


def call_ollama(messages, model=None, temperature=0.3, timeout=300):
    """Llama al proveedor configurado en config.json (Claude o Ollama)."""
    cfg = load_config()
    provider = cfg.get("provider", DEFAULT_PROVIDER)
    if provider == "claude":
        claude_model = cfg.get("model", DEFAULT_CLAUDE_MODEL)
        return call_claude(messages, model=claude_model, temperature=temperature)
    else:
        ollama_model = cfg.get("model", DEFAULT_MODEL)
        return _call_ollama_direct(messages, model=ollama_model, temperature=temperature, timeout=timeout)


def clean_response(text):
    """Limpia la respuesta del modelo: quita bloques <think>, espacios extra."""
    # Quitar bloques de pensamiento (qwen3.5, deepseek, etc.)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'<\|.*?\|>', '', text)  # tokens especiales
    return text.strip()


def check_ollama():
    """Verifica que Ollama esté corriendo y el modelo esté disponible."""
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        r.raise_for_status()
        models = [m["name"] for m in r.json().get("models", [])]
        return models
    except Exception:
        return None


# ─── Archivo I/O ─────────────────────────────────────────────────────────────

def read_file(path):
    """Lee un archivo. Retorna string vacío si no existe."""
    try:
        with open(str(path), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def write_file(path, content):
    """Escribe contenido a un archivo, creando directorios si es necesario."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w", encoding="utf-8") as f:
        f.write(content)


def append_file(path, content):
    """Agrega contenido al final de un archivo."""
    with open(str(path), "a", encoding="utf-8") as f:
        f.write(content)


# ─── Wiki Helpers ────────────────────────────────────────────────────────────

def load_agents_md():
    """Carga el archivo AGENTS.md con las reglas del sistema."""
    return read_file(SCHEMA_DIR / "AGENTS.md")


def load_index():
    """Carga el índice de la wiki."""
    return read_file(WIKI_DIR / "index.md")


def get_today():
    return datetime.now().strftime("%Y-%m-%d")


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def slugify(text):
    """Convierte texto a nombre de archivo seguro (sin tildes, minúsculas, guiones)."""
    text = text.lower().strip()
    replacements = {
        'á': 'a', 'à': 'a', 'ä': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ë': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'ï': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ö': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'ü': 'u', 'û': 'u',
        'ñ': 'n', 'ç': 'c',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace('_', ' ')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def get_wiki_pages():
    """Retorna lista de rutas relativas de todas las páginas .md en la wiki."""
    pages = []
    for root, _, files in os.walk(str(WIKI_DIR)):
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), str(WIKI_DIR))
                pages.append(rel.replace("\\", "/"))
    return sorted(pages)


def extract_wiki_links(content):
    """Extrae todos los enlaces [[pagina]] del contenido Markdown."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)


def get_existing_concepts():
    """Retorna lista de slugs de conceptos existentes en la wiki."""
    d = WIKI_DIR / "concepts"
    if not d.exists():
        return []
    return [f.stem for f in d.glob("*.md")]


def get_existing_sources():
    """Retorna lista de slugs de fuentes existentes en la wiki."""
    d = WIKI_DIR / "sources"
    if not d.exists():
        return []
    return [f.stem for f in d.glob("*.md")]


def get_existing_entities():
    """Retorna lista de slugs de entidades existentes en la wiki."""
    d = WIKI_DIR / "entities"
    if not d.exists():
        return []
    return [f.stem for f in d.glob("*.md")]


def load_config():
    """Carga la configuración desde config.json."""
    default = {
        'topic': 'Conocimiento',
        'description': 'Wiki de conocimiento local.',
        'domain': 'Documentos y conocimiento general.',
    }
    try:
        with open(str(CONFIG_PATH), "r", encoding="utf-8") as f:
            cfg = json.load(f)
            return {**default, **cfg}
    except (FileNotFoundError, json.JSONDecodeError):
        return dict(default)


def save_config(cfg):
    """Guarda la configuración en config.json."""
    with open(str(CONFIG_PATH), "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def list_pdf_status():
    """Lista los PDFs disponibles y su estado de ingesta."""
    pdfs = sorted(DOCS_DIR.glob("*.pdf"))
    existing = get_existing_sources()
    result = []
    for pdf in pdfs:
        slug = slugify(pdf.stem)
        ingested = slug in existing
        result.append((pdf, slug, ingested))
    return result
