#!/usr/bin/env python3
"""
Repair wiki links without requiring Ollama or optional PDF dependencies.

The web lint treats [[page]] links as broken when no matching markdown page
exists. This script normalizes broken links to canonical wiki paths, creates
minimal placeholder pages for referenced concepts/entities, and indexes them.
"""

import argparse
import re
import unicodedata
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = BASE_DIR / "wiki"


LINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]")


def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip().replace("_", " ")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def title_from_slug(slug):
    return slug.replace("-", " ").strip().title()


def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path, text, apply):
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def all_pages():
    return sorted(WIKI_DIR.rglob("*.md"))


def build_existing():
    existing = {}
    for path in all_pages():
        rel = path.relative_to(WIKI_DIR).as_posix()
        no_ext = rel[:-3] if rel.endswith(".md") else rel
        existing[rel] = rel
        existing[no_ext] = no_ext
        existing[path.stem] = no_ext
        existing[slugify(path.stem)] = no_ext
    return existing


def is_existing(link, existing):
    link = link.strip()
    with_md = link if link.endswith(".md") else f"{link}.md"
    return (
        link in existing
        or with_md in existing
        or (WIKI_DIR / with_md).exists()
        or (WIKI_DIR / link).with_suffix(".md").exists()
    )


def canonical_for(link, existing):
    raw = link.strip()
    parts = raw.split("/")
    if len(parts) > 1 and parts[0] in {"concepts", "entities", "sources", "faq", "comparisons", "timelines"}:
        folder = parts[0]
        stem = slugify(parts[-1])
    else:
        folder = "concepts"
        stem = slugify(raw)

    if not stem:
        stem = "concepto-pendiente"

    candidate = f"{folder}/{stem}"
    if candidate in existing:
        return candidate
    if stem in existing:
        return existing[stem]
    return candidate


def make_link(target, label, anchor):
    suffix = anchor or ""
    if label and label.strip() and label.strip() != target:
        return f"[[{target}{suffix}|{label.strip()}]]"
    return f"[[{target}{suffix}]]"


def repair_links(apply):
    existing = build_existing()
    created_targets = set()
    rewrites = 0
    broken_before = 0

    for path in all_pages():
        rel = path.relative_to(WIKI_DIR).as_posix()
        text = read_text(path)
        changed = False

        def replace(match):
            nonlocal changed, rewrites, broken_before
            link, anchor, label = match.group(1), match.group(2), match.group(3)
            if is_existing(link, existing):
                return match.group(0)

            broken_before += 1
            target = canonical_for(link, existing)
            created_targets.add(target)
            changed = True
            rewrites += 1
            return make_link(target, label or link, anchor)

        new_text = LINK_RE.sub(replace, text)
        if changed:
            write_text(path, new_text, apply)

    return broken_before, rewrites, sorted(created_targets)


def concept_page(title):
    return (
        f"# {title}\n\n"
        "## Definición\n"
        "Página creada automáticamente para resolver un enlace interno pendiente. "
        "Debe completarse con una definición precisa cuando se revise el documento "
        "fuente que introdujo este concepto.\n\n"
        "## Fuentes relacionadas\n"
        "- Pendiente de vincular a fuentes específicas.\n\n"
        "## Notas\n"
        "Este marcador evita enlaces rotos y conserva la navegación de la wiki.\n"
    )


def entity_page(title):
    return (
        f"# {title}\n\n"
        "## Descripción\n"
        "Página creada automáticamente para resolver una entidad mencionada pero "
        "todavía no desarrollada. Debe completarse con contexto, rol y referencias.\n\n"
        "## Fuentes\n"
        "- Pendiente de vincular a fuentes específicas.\n\n"
        "## Notas\n"
        "Este marcador evita enlaces rotos y conserva la navegación de la wiki.\n"
    )


def create_missing_pages(targets, apply):
    created = []
    for target in targets:
        path = WIKI_DIR / f"{target}.md"
        if path.exists():
            continue
        title = title_from_slug(Path(target).stem)
        if target.startswith("entities/"):
            content = entity_page(title)
        else:
            content = concept_page(title)
        write_text(path, content, apply)
        created.append(target)
    return created


def fix_accented_sections(apply):
    replacements = {
        "## Definicion": "## Definición",
        "## Descripcion": "## Descripción",
    }
    changed = 0
    for path in all_pages():
        text = read_text(path)
        new_text = text
        for old, new in replacements.items():
            new_text = new_text.replace(old, new)
        if new_text != text:
            write_text(path, new_text, apply)
            changed += 1
    return changed


def ensure_index_entries(targets, apply):
    index_path = WIKI_DIR / "index.md"
    index = read_text(index_path)
    additions = []

    for target in targets:
        if target in index:
            continue
        title = title_from_slug(Path(target).stem)
        additions.append(f"- [[{target}]]: {title}")

    if not additions:
        return 0

    block = "\n\n## Enlaces reparados\n" + "\n".join(additions) + "\n"
    write_text(index_path, index.rstrip() + block, apply)
    return len(additions)


def count_broken_links():
    existing = build_existing()
    count = 0
    for path in all_pages():
        text = read_text(path)
        for match in LINK_RE.finditer(text):
            if not is_existing(match.group(1), existing):
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write changes")
    args = parser.parse_args()

    broken_before, rewrites, targets = repair_links(args.apply)
    created = create_missing_pages(targets, args.apply)
    sections = fix_accented_sections(args.apply)
    indexed = ensure_index_entries(created, args.apply)
    broken_after = count_broken_links() if args.apply else None

    print(f"apply={args.apply}")
    print(f"broken_before={broken_before}")
    print(f"rewrites={rewrites}")
    print(f"unique_targets={len(targets)}")
    print(f"created_pages={len(created)}")
    print(f"section_files_changed={sections}")
    print(f"index_entries_added={indexed}")
    if broken_after is not None:
        print(f"broken_after={broken_after}")


if __name__ == "__main__":
    main()
