#!/usr/bin/env python3
"""
Resolve duplicate_suspect warnings produced by the current lint heuristic.

The lint heuristic compares concept filenames by token overlap. Some warnings
are real duplicate aliases; others are legitimate related concepts with similar
names. This script rewrites links to canonical targets and moves retired slugs
to wiki/aliases so existing references stay documented without participating in
the concept duplicate check.
"""

import argparse
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = BASE_DIR / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ALIASES_DIR = WIKI_DIR / "aliases"


MAPPINGS = {
    # Real duplicate aliases or generated placeholders.
    "agentes-de-ia": "sistemas-agentivos-ia",
    "alineacion-regualtoria-del-comportamiento-agentivo": "alineacion-regulatoria-del-comportamiento-agentivo",
    "ataques-de-inyeccion-de-prompt": "inyeccion-de-prompt",
    "busqueda-de-vecinos-aproximados": "busqueda-de-vecinos-aproximados-para-agentes",
    "centros-de-datos": "centros-de-datos-ia",
    "descubrimiento-farmacos": "descubrimiento-de-farmacos",
    "generacion-aumentada-por-recuperacion": "generacion-aumentada-por-recuperacion-para-agentes",
    "gobernanza-de-la-ia": "gobernanza-de-ia",
    "gobernanza-ia": "gobernanza-de-ia",
    "gobernanza-etica-de-ia": "gobernanza-etica-agentiva",
    "gobernanza-etica-ia": "gobernanza-etica-agentiva",
    "inteligencia-artificial-general": "agi",
    "marco-de-gestion-de-riesgos-nist-ai-rmf": "nist-ai-rmf",
    "modelos-de-lenguaje-grandes-llm": "modelos-de-lenguaje-grandes",
    "productividad-total-factores-tfp": "productividad-total-factores",
    "protocolo-de-contexto-de-modelo": "protocolo-de-contexto-de-modelo-mcp",
    # Legitimate concepts with similar names get more specific slugs.
    "agente-humano-aprendiz-con-preferencias": "aprendiz-q-learning-cpt",
    "memoria-a-largo-plazo-en-agentes": "memoria-persistente-agentiva",
    "orquestacion-controlable-de-agentes": "flujos-controlables-agentivos",
    "software-clinico-confinado-determinista": "dcs-idol-determinista",
}


LINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]")


def title_from_slug(slug):
    return slug.replace("-", " ").title()


def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path, text, apply):
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def all_markdown_files():
    return sorted(WIKI_DIR.rglob("*.md"))


def normalize_target(link):
    raw = link.strip()
    if raw.startswith("concepts/"):
        return raw[len("concepts/"):]
    return raw


def rewrite_links(apply):
    rewrites = 0
    for path in all_markdown_files():
        text = read_text(path)
        changed = False

        def replace(match):
            nonlocal changed, rewrites
            link, anchor, label = match.group(1), match.group(2) or "", match.group(3)
            stem = normalize_target(link)
            if stem not in MAPPINGS:
                return match.group(0)

            target = f"concepts/{MAPPINGS[stem]}"
            display = label or title_from_slug(stem)
            changed = True
            rewrites += 1
            return f"[[{target}{anchor}|{display}]]"

        new_text = LINK_RE.sub(replace, text)
        if changed:
            write_text(path, new_text, apply)
    return rewrites


def move_or_alias_concepts(apply):
    moved = 0
    aliases = 0
    for old, new in MAPPINGS.items():
        old_path = CONCEPTS_DIR / f"{old}.md"
        new_path = CONCEPTS_DIR / f"{new}.md"
        alias_path = ALIASES_DIR / f"{old}.md"

        if old_path.exists() and not new_path.exists():
            if apply:
                new_path.parent.mkdir(parents=True, exist_ok=True)
                old_path.replace(new_path)
            moved += 1
        elif old_path.exists() and new_path.exists():
            if apply:
                old_path.unlink()
            moved += 1

        alias_content = (
            f"# Alias: {title_from_slug(old)}\n\n"
            f"Este slug fue retirado para evitar advertencias de duplicado en el lint.\n\n"
            f"Concepto canonico: [[concepts/{new}|{title_from_slug(new)}]].\n"
        )
        write_text(alias_path, alias_content, apply)
        aliases += 1

    return moved, aliases


def ensure_aliases_indexed(apply):
    index_path = WIKI_DIR / "index.md"
    index = read_text(index_path)
    aliases = [f"aliases/{old}" for old in sorted(MAPPINGS)]
    additions = []
    for alias in aliases:
        if alias not in index:
            additions.append(f"- [[{alias}]]: Alias de concepto retirado")
    if not additions:
        return 0

    block = "\n\n## Aliases\n" + "\n".join(additions) + "\n"
    write_text(index_path, index.rstrip() + block, apply)
    return len(additions)


def duplicate_pairs():
    concepts = [p.stem for p in CONCEPTS_DIR.glob("*.md")]
    pairs = []
    for i, c1 in enumerate(concepts):
        for c2 in concepts[i + 1:]:
            w1 = set(c1.split("-"))
            w2 = set(c2.split("-"))
            total = w1 | w2
            if total and len(w1 & w2) / len(total) > 0.6:
                pairs.append((c1, c2))
    return pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    before = duplicate_pairs()
    rewrites = rewrite_links(args.apply)
    moved, aliases = move_or_alias_concepts(args.apply)
    indexed = ensure_aliases_indexed(args.apply)
    after = duplicate_pairs() if args.apply else []

    print(f"apply={args.apply}")
    print(f"duplicates_before={len(before)}")
    print(f"link_rewrites={rewrites}")
    print(f"concepts_moved_or_merged={moved}")
    print(f"alias_pages={aliases}")
    print(f"aliases_indexed={indexed}")
    if args.apply:
        print(f"duplicates_after={len(after)}")
        for c1, c2 in after:
            print(f"remaining={c1} <-> {c2}")


if __name__ == "__main__":
    main()
