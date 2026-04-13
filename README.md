# LLM Wiki

LLM Wiki es una aplicación local para convertir una colección de PDFs sobre IA y agentes en una wiki Markdown consultable. El flujo principal ingesta documentos, crea páginas fuente, extrae conceptos y entidades, mantiene enlaces internos y expone una interfaz web en Flask.

## Componentes

- `scripts/app.py`: servidor Flask e interfaz web.
- `scripts/ingest.py`: CLI de ingestión de PDFs hacia la wiki.
- `scripts/query.py`: consulta de la wiki con selección local de páginas y respuesta asistida por Ollama.
- `scripts/lint.py`: revisión de salud de la wiki, enlaces rotos, páginas huérfanas y duplicados.
- `scripts/repair_wiki_links.py`: reparación de enlaces internos.
- `scripts/resolve_duplicate_warnings.py`: consolidación de páginas duplicadas.
- `scripts/enrich_placeholder_concepts.py`: enriquecimiento offline de páginas marcador usando el contenido local de la wiki.
- `wiki/`: contenido Markdown generado y curado.
- `schema/AGENTS.md`: reglas operativas del mantenedor de la wiki.

## Requisitos

- Python 3.11 o superior.
- Ollama ejecutándose localmente si se usarán ingestión o consulta con modelo.
- Modelo por defecto: `qwen2.5:7b`, configurable desde la interfaz o editando `scripts/utils.py`.

Instalación:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

Arrancar la interfaz web:

```powershell
python .\scripts\app.py --port 5001
```

Ingestar un PDF específico:

```powershell
python .\scripts\ingest.py "archivo.pdf"
```

Ingestar todos los PDFs pendientes:

```powershell
python .\scripts\ingest.py --todos
```

Consultar la wiki desde CLI:

```powershell
python .\scripts\query.py "Que son los Agentes Autonomos?"
```

Revisar salud de la wiki:

```powershell
python .\scripts\lint.py --deep
```

## Datos locales

Las carpetas `Documentos/`, `papers/`, `raw/` y `outputs/` están excluidas de Git por defecto porque pueden contener PDFs pesados, fuentes privadas o salidas locales. Para compartir documentos fuente, súbelos de forma explícita y revisa licencias/permisos antes de publicarlos.

## Estado de la wiki

La wiki actual contiene páginas Markdown bajo `wiki/` para fuentes, conceptos, entidades, FAQ, alias y páginas generales. El flujo recomendado antes de publicar cambios es:

```powershell
python .\scripts\lint.py --deep
```
