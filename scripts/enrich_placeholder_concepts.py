#!/usr/bin/env python3
"""
Replace automatically-created concept placeholders with substantive pages.

The script uses only local wiki content: inbound links, source summaries and
existing concept/entity pages. It does not call Ollama.
"""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = BASE_DIR / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"

MARKERS = (
    "Página creada automáticamente",
    "Pagina creada automaticamente",
    "Este marcador evita enlaces rotos",
)
ENRICHED_MARKER = "Página enriquecida offline"

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")

STOPWORDS = {
    "de", "del", "la", "el", "los", "las", "en", "para", "por", "con", "sin",
    "y", "o", "a", "un", "una", "unos", "unas", "que", "como", "ia", "ai",
    "agente", "agentes", "artificial", "inteligencia", "sistema", "sistemas",
    "concepto", "conceptos", "wiki", "pagina", "paginas", "fuente", "fuentes",
    "este", "esta", "estos", "estas", "son", "sobre", "desde", "entre", "hacia",
    "tambien", "ademas", "segun", "sera", "mas", "puede", "pueden", "uso", "usa",
    "usado", "usada", "basado", "basada", "texto", "completo", "estudio",
    "estudios", "documento", "documentos", "resumen", "datos", "clave", "tema",
    "temas", "principal", "principales", "analiza", "presenta", "explora",
    "relacion", "relaciona", "relacionado", "relacionada", "otros", "otras",
    "relevante", "relevantes",
}

CURATED = {
    "agentes-autonomos": (
        "Los agentes autonomos son sistemas de IA que perciben informacion de un entorno, "
        "razonan sobre un objetivo, planifican pasos y ejecutan acciones con supervision humana limitada. "
        "En esta wiki el termino cubre agentes basados en LLM, sistemas multiagente, agentes con memoria, "
        "uso de herramientas y arquitecturas capaces de operar en ciclos percepcion-razonamiento-accion."
    ),
    "sistemas-agentivos-ia": (
        "Los sistemas agentivos de IA son arquitecturas que combinan modelos, memoria, herramientas, "
        "planificacion, control de ejecucion y politicas de seguridad para actuar sobre tareas abiertas. "
        "Se diferencian de un chatbot simple porque no solo responden texto: tambien pueden decidir pasos, "
        "invocar recursos externos, coordinar componentes y mantener estado durante una tarea."
    ),
    "ia-agentica": (
        "La IA agentica designa sistemas de IA orientados a objetivos que planifican, usan herramientas, "
        "mantienen memoria y ajustan su conducta durante la ejecucion. En la wiki aparece como puente entre "
        "modelos fundacionales, automatizacion cognitiva, sistemas multiagente y debates de seguridad."
    ),
    "inteligencia-artificial": (
        "La inteligencia artificial es el campo de sistemas computacionales que realizan tareas asociadas con "
        "capacidades cognitivas como percepcion, lenguaje, razonamiento, aprendizaje, planificacion y decision. "
        "En esta wiki opera como concepto paraguas para modelos de lenguaje, agentes, IA generativa, IA clinica, "
        "seguridad y gobernanza."
    ),
    "agi": (
        "La inteligencia artificial general, o AGI, es la aspiracion de sistemas capaces de generalizar entre "
        "dominios, aprender nuevas tareas y resolver problemas abiertos con flexibilidad comparable a la humana. "
        "La wiki la conecta con IA agentica porque los agentes autonomos orientados a objetivos simulan funciones "
        "ejecutivas como planificacion, memoria y autocorreccion."
    ),
    "llm": (
        "Un LLM es un modelo de lenguaje grande entrenado sobre grandes corpus para predecir y generar texto, "
        "seguir instrucciones y operar como nucleo de aplicaciones conversacionales o agentivas. En agentes, el "
        "LLM suele funcionar como motor de razonamiento, planificacion y seleccion de herramientas."
    ),
    "large-language-models": (
        "Los large language models son modelos neuronales de lenguaje a gran escala capaces de generar texto, "
        "interpretar instrucciones, resumir informacion y apoyar razonamiento. En la wiki aparecen como base tecnica "
        "de agentes modernos, sistemas RAG, asistentes clinicos y arquitecturas de automatizacion."
    ),
    "modelos-de-lenguaje-grandes": (
        "Los modelos de lenguaje grandes son modelos fundacionales entrenados para procesar y generar lenguaje natural. "
        "En sistemas agentivos sirven como componente cognitivo que interpreta objetivos, produce planes, invoca "
        "herramientas y sintetiza resultados."
    ),
    "rag": (
        "RAG, generacion aumentada por recuperacion, combina un modelo generativo con recuperacion de informacion "
        "externa para producir respuestas ancladas en documentos o bases de conocimiento. En agentes, RAG reduce "
        "alucinaciones y permite incorporar contexto actualizado antes de decidir acciones."
    ),
    "aprendizaje-automatico": (
        "El aprendizaje automatico es el conjunto de metodos que permiten a un sistema ajustar su comportamiento "
        "a partir de datos. En la wiki aparece como base de modelos predictivos, agentes adaptativos, aprendizaje "
        "por refuerzo y aplicaciones en salud, seguridad y automatizacion."
    ),
    "aprendizaje-por-refuerzo": (
        "El aprendizaje por refuerzo entrena agentes mediante recompensas y penalizaciones obtenidas al actuar en "
        "un entorno. Es relevante para agentes autonomos porque modela el ciclo accion-retroalimentacion y permite "
        "optimizar politicas de decision a lo largo del tiempo."
    ),
    "sistemas-multiagente": (
        "Un sistema multiagente coordina multiples agentes que interactuan, cooperan o compiten para resolver tareas "
        "que exceden la capacidad de un solo componente. En la wiki aparece en salud, seguridad, simulacion, "
        "orquestacion y evaluacion de riesgos."
    ),
    "sistemas-multi-agente": (
        "Los sistemas multi-agente son arquitecturas en las que varios agentes especializados comparten informacion, "
        "delegan subtareas y coordinan decisiones. Su valor esta en distribuir razonamiento y accion, pero tambien "
        "introducen riesgos de propagacion de errores, colusion y fallas en cascada."
    ),
    "multi-agent-systems": (
        "Multi-agent systems es el termino ingles para sistemas compuestos por multiples agentes autonomos o "
        "semiautonomos que interactuan bajo reglas, roles o protocolos compartidos."
    ),
    "arquitectura-multi-agente": (
        "Una arquitectura multi-agente organiza roles, memoria, comunicacion, permisos y flujos de control entre "
        "varios agentes. Permite especializacion y colaboracion, pero requiere gobernanza explicita para evitar "
        "duplicidad, conflicto y propagacion de fallos."
    ),
    "arquitecturas-multi-agente": (
        "Las arquitecturas multi-agente describen patrones de diseno para coordinar varios agentes: jerarquias, "
        "equipos especializados, debate, revision cruzada, orquestadores y flujos con supervision humana."
    ),
    "uso-de-herramientas": (
        "El uso de herramientas permite que un agente invoque APIs, bases de datos, navegadores, calculadoras, "
        "sistemas de archivos u otros servicios externos. Esta capacidad transforma una respuesta textual en accion, "
        "por lo que exige permisos, trazabilidad y controles de seguridad."
    ),
    "planificacion-ia": (
        "La planificacion en IA es la capacidad de descomponer un objetivo en pasos ordenados, elegir acciones, "
        "monitorear resultados y ajustar el plan. En agentes LLM, suele combinar prompts, memoria, uso de herramientas "
        "y evaluacion iterativa."
    ),
    "ciclo-percepcion-razonamiento-accion": (
        "El ciclo percepcion-razonamiento-accion describe el bucle central de un agente: observar el entorno, "
        "interpretar informacion, decidir un curso de accion y ejecutar una respuesta que cambia el estado del entorno."
    ),
    "memoria-cognitiva-edge-native": (
        "La memoria cognitiva edge-native es una arquitectura de memoria local, de baja latencia y orientada a agentes "
        "que mantiene contexto entre interacciones sin depender de servicios remotos permanentes."
    ),
    "toma-de-decisiones-autonoma": (
        "La toma de decisiones autonoma es la capacidad de seleccionar acciones sin aprobacion humana paso a paso. "
        "En agentes de IA implica evaluar objetivos, restricciones, contexto, riesgos y efectos de la accion."
    ),
    "seguridad-informatica": (
        "La seguridad informatica protege sistemas, redes, datos y operaciones frente a accesos no autorizados, "
        "fallos, abuso y ataques. En agentes de IA se vuelve mas compleja porque los modelos pueden actuar, delegar "
        "credenciales y conectar multiples herramientas."
    ),
    "ciberseguridad": (
        "La ciberseguridad agrupa practicas, controles y marcos para proteger infraestructura digital. En la wiki se "
        "relaciona con agentes autonomos, pruebas de penetracion, inyeccion de prompt, seguridad por diseno y "
        "gobernanza de sistemas agentivos."
    ),
    "inyeccion-de-prompt": (
        "La inyeccion de prompt es un ataque que introduce instrucciones maliciosas o conflictivas para alterar el "
        "comportamiento de un modelo. En agentes es critica porque una instruccion inyectada puede terminar en llamadas "
        "a herramientas, fuga de datos o acciones no autorizadas."
    ),
    "confused-deputy": (
        "Confused deputy describe una falla donde un componente con privilegios es inducido por otro actor a ejecutar "
        "acciones que no deberia autorizar. En sistemas multiagente puede aparecer cuando un agente de bajo privilegio "
        "usa a otro con mas permisos como intermediario."
    ),
    "seguridad-por-diseno": (
        "Seguridad por diseno significa incorporar controles, permisos, trazabilidad y evaluacion de riesgos desde la "
        "arquitectura inicial del sistema, no como parche posterior. Es clave en agentes porque sus capacidades de "
        "accion amplifican fallos de diseno."
    ),
    "red-teaming": (
        "Red teaming es la evaluacion adversarial de sistemas para descubrir vulnerabilidades, abusos y modos de fallo. "
        "En agentes de IA debe cubrir prompts, herramientas, memoria, credenciales, interacciones entre agentes y "
        "acciones externas."
    ),
    "sandboxing": (
        "Sandboxing es aislar la ejecucion de codigo, herramientas o acciones dentro de un entorno controlado. En agentes "
        "reduce el impacto de instrucciones maliciosas, errores de razonamiento o invocaciones inseguras."
    ),
    "telemetria": (
        "La telemetria registra eventos, trazas, decisiones, llamadas de herramientas y resultados operativos. En agentes "
        "autonomos es necesaria para auditoria y seguridad, pero puede tensionar privacidad y cumplimiento normativo."
    ),
    "gobernanza-de-ia": (
        "La gobernanza de IA es el conjunto de normas, procesos y responsabilidades que orientan el diseno, despliegue "
        "y supervision de sistemas de inteligencia artificial. En agentes debe incluir accountability, trazabilidad, "
        "gestion de riesgo y limites de autonomia."
    ),
    "gobernanza-etica-agentiva": (
        "La gobernanza etica agentiva aplica principios de responsabilidad, transparencia, justicia, supervision humana "
        "y control de riesgos a sistemas que no solo predicen, sino que tambien planifican y actuan."
    ),
    "gestion-de-riesgos-en-ia": (
        "La gestion de riesgos en IA identifica, evalua, mitiga y monitorea danos potenciales asociados con modelos y "
        "sistemas. En agentes incluye riesgos de accion, delegacion, herramienta, datos, privacidad y comportamiento emergente."
    ),
    "nist-ai-rmf": (
        "NIST AI RMF es el marco de gestion de riesgos de IA del NIST. En la wiki sirve como referencia para clasificar, "
        "medir y mitigar riesgos en sistemas de IA, incluyendo agentes con capacidades autonomas."
    ),
    "infraestructura-de-ia": (
        "La infraestructura de IA incluye computo, centros de datos, redes, datos, modelos, herramientas y controles que "
        "permiten entrenar, desplegar y operar sistemas de IA a escala."
    ),
    "centros-de-datos-ia": (
        "Los centros de datos de IA son instalaciones de computo intensivo optimizadas para entrenamiento e inferencia "
        "de modelos. Su relevancia aparece en la wiki por energia, soberania tecnologica, concentracion industrial e "
        "infraestructura critica."
    ),
    "descubrimiento-de-farmacos": (
        "El descubrimiento de farmacos es el proceso de identificar blancos, disenar moleculas, optimizar candidatos y "
        "validarlos experimentalmente. Los agentes de IA pueden acelerar este ciclo coordinando literatura, simulacion, "
        "diseño molecular y planificacion experimental."
    ),
    "diseno-de-farmacos": (
        "El diseno de farmacos usa conocimiento biologico, quimico y computacional para proponer moleculas o biologicos "
        "con propiedades terapeuticas. En la wiki se conecta con laboratorios virtuales, nanobodies, oncologia y agentes "
        "cientificos."
    ),
    "bioinformatica": (
        "La bioinformatica aplica computacion y analisis de datos a problemas biologicos, genomicos, proteicos y clinicos. "
        "Es un dominio donde agentes de IA pueden apoyar busqueda bibliografica, diseño experimental y analisis de datos."
    ),
    "salud-digital": (
        "La salud digital integra software, datos, dispositivos y sistemas inteligentes para mejorar atencion, vigilancia, "
        "diagnostico, tratamiento y gestion sanitaria."
    ),
    "cdss": (
        "Un CDSS, sistema de soporte a decisiones clinicas, ayuda a profesionales de salud a interpretar datos y tomar "
        "decisiones. En el contexto de IA agentiva, su regulacion depende de si el software es determinista, confinado "
        "o capaz de operar con salidas abiertas."
    ),
    "samd": (
        "SaMD significa software como dispositivo medico. Es una categoria regulatoria para software usado con fines "
        "clinicos, relevante cuando modelos o agentes influyen en diagnostico, tratamiento o decisiones medicas."
    ),
    "vigilancia-en-salud-publica": (
        "La vigilancia en salud publica recolecta, integra y analiza señales epidemiologicas para detectar amenazas, "
        "evaluar riesgos y activar respuestas. Los agentes de IA pueden automatizar monitoreo, alerta temprana y soporte "
        "a intervenciones."
    ),
    "inteligencia-epidemica": (
        "La inteligencia epidemica combina vigilancia, evaluacion de riesgo, alerta temprana y soporte a decisiones para "
        "detectar y responder a brotes. En la wiki se expande con agentes de IA que operan como epidemiologos digitales."
    ),
    "vehiculos-autonomos": (
        "Los vehiculos autonomos son sistemas fisicos que perciben su entorno y toman decisiones de conduccion sin control "
        "humano continuo. En la wiki aparecen como ejemplo de interaccion entre agentes artificiales, humanos y riesgos "
        "de decision en entornos reales."
    ),
    "sesgo-algoritmico": (
        "El sesgo algoritmico es una distorsion sistematica en datos, objetivos, modelos o procesos de despliegue que produce "
        "resultados injustos, no representativos o de impacto desigual sobre grupos de personas. En la wiki se conecta con "
        "justicia algoritmica, transparencia, discriminacion por impacto dispar y desviaciones de modelos de lenguaje."
    ),
    "discriminacion-por-impacto-dispar": (
        "La discriminacion por impacto dispar ocurre cuando una regla, modelo o decision aparentemente neutral afecta de forma "
        "desproporcionada a un grupo protegido o vulnerable. En IA se usa para evaluar si un sistema produce efectos injustos "
        "aunque no use explicitamente variables sensibles."
    ),
    "teoria-de-juegos": (
        "La teoria de juegos estudia decisiones estrategicas entre agentes con objetivos, incentivos y restricciones. "
        "La wiki la usa para modelar poblaciones mixtas de agentes humanos y artificiales, colusion y equilibrio."
    ),
    "equilibrio-de-nash": (
        "El equilibrio de Nash es un estado estrategico donde ningun participante mejora unilateralmente cambiando su "
        "decision. En contextos de multiples agentes, ayuda a analizar estabilidad, incentivos y posibles patrones de colusion."
    ),
    "procesos-de-decision-de-markov": (
        "Los procesos de decision de Markov modelan decisiones secuenciales bajo incertidumbre, donde el estado actual "
        "resume la informacion relevante para elegir acciones futuras. Son base teorica para aprendizaje por refuerzo."
    ),
    "cadenas-de-markov": (
        "Las cadenas de Markov modelan transiciones probabilisticas entre estados donde el siguiente estado depende del "
        "estado actual. En la wiki aparecen como herramienta para analizar dinamicas de agentes y distribuciones estacionarias."
    ),
    "utilidad-esperada": (
        "La utilidad esperada calcula el valor promedio ponderado de resultados posibles bajo incertidumbre. En modelos "
        "de decision sirve como referencia para comparar politicas de agentes y preferencias humanas."
    ),
    "utilidad-marginal": (
        "La utilidad marginal mide el cambio de utilidad producido por una unidad adicional de recurso, recompensa o resultado. "
        "En teoria de juegos y agentes ayuda a explicar decisiones no lineales y sensibilidad a ganancias o perdidas."
    ),
}

CURATED_IDEAS = {
    "agentes-autonomos": [
        "Percepcion, razonamiento y accion",
        "Planificacion orientada a objetivos",
        "Uso de herramientas y memoria",
        "Supervision humana limitada",
        "Riesgos de autonomia operacional",
    ],
    "sistemas-agentivos-ia": [
        "Modelos, memoria y herramientas",
        "Ejecucion con estado",
        "Planificacion y control",
        "Politicas de seguridad",
        "Trazabilidad de acciones",
    ],
    "ia-agentica": [
        "Orientacion a objetivos",
        "Planificacion adaptativa",
        "Uso de herramientas",
        "Memoria y contexto",
        "Gobernanza de autonomia",
    ],
    "sistemas-multiagente": [
        "Multiples agentes coordinados",
        "Roles especializados",
        "Comunicacion entre agentes",
        "Propagacion de errores",
        "Colusion y fallas emergentes",
    ],
    "sistemas-multi-agente": [
        "Delegacion de subtareas",
        "Coordinacion y competencia",
        "Protocolos compartidos",
        "Fallas en cascada",
        "Controles de orquestacion",
    ],
    "arquitectura-multi-agente": [
        "Roles y permisos",
        "Memoria compartida",
        "Orquestacion de agentes",
        "Revision cruzada",
        "Gobernanza del flujo",
    ],
    "arquitecturas-multi-agente": [
        "Equipos de agentes",
        "Jerarquias y debate",
        "Especializacion funcional",
        "Supervision humana",
        "Mitigacion de conflictos",
    ],
    "sesgo-algoritmico": [
        "Datos no representativos",
        "Impacto desigual",
        "Justicia algoritmica",
        "Transparencia y auditoria",
        "Mitigacion de sesgos",
    ],
}


def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path, text, apply):
    if apply:
        path.write_text(text, encoding="utf-8")


def strip_links(text):
    def repl(match):
        return match.group(2) or Path(match.group(1)).stem.replace("-", " ")
    text = LINK_RE.sub(repl, text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def nice_title(slug):
    special = {
        "agi": "AGI",
        "llm": "LLM",
        "rag": "RAG",
        "samd": "SaMD",
        "cdss": "CDSS",
        "nist-ai-rmf": "NIST AI RMF",
        "rgpd": "RGPD",
        "sars-cov-2": "SARS-CoV-2",
    }
    if slug in special:
        return special[slug]
    return slug.replace("-", " ").title()


def is_placeholder(path):
    text = read_text(path)
    return any(marker in text for marker in MARKERS)


def is_generated_concept_page(text):
    required = (
        "## Definición",
        "## Ideas clave",
        "## Uso en la wiki",
        "## Relación con otros conceptos",
        "## Fuentes relacionadas",
    )
    return all(section in text for section in required) and (
        "- En [[" in text or "Se usa como nodo de navegacion conceptual" in text
    )


def all_md_files():
    return sorted(WIKI_DIR.rglob("*.md"))


def all_links_in(text):
    return [(m.group(1).strip(), m.group(2)) for m in LINK_RE.finditer(text)]


def target_matches(link, target):
    stem = Path(target).stem
    clean = link.strip()
    return clean == target or clean == stem or clean.endswith("/" + stem)


def extract_blocks(text):
    blocks = []
    parts = re.split(r"\n\s*\n", text)
    for part in parts:
        clean = strip_links(part)
        if len(clean) < 80:
            continue
        if any(marker in clean for marker in MARKERS):
            continue
        blocks.append(clean)
    return blocks


def section_text(text, heading):
    pattern = rf"^## {re.escape(heading)}\s*(.+?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.S | re.M)
    return match.group(1).strip() if match else ""


def collect_context(target):
    contexts = []
    linked_sources = []
    linked_pages = []
    target_stem = Path(target).stem
    target_words = [w for w in target_stem.split("-") if w not in STOPWORDS and len(w) > 2]

    for path in all_md_files():
        rel = path.relative_to(WIKI_DIR).as_posix()
        if rel in {"index.md", "log.md", "overview.md"} or rel.startswith("aliases/") or rel.startswith("faq/"):
            continue
        text = read_text(path)
        if rel.startswith("concepts/") and (ENRICHED_MARKER in text or is_generated_concept_page(text)):
            continue
        links = all_links_in(text)
        explicit = any(target_matches(link, target) for link, _ in links)
        lexical = False
        lower = strip_links(text).lower()
        if target_words and len(target_words) <= 3:
            lexical = all(w in lower for w in target_words)

        if not explicit and not lexical:
            continue

        if rel == target + ".md":
            continue

        linked_pages.append(rel)
        if rel.startswith("sources/"):
            linked_sources.append(rel[:-3])

        blocks = []
        if rel.startswith("sources/"):
            resumen = section_text(text, "Resumen")
            datos = section_text(text, "Datos clave")
            temas = section_text(text, "Temas principales")
            blocks.extend(extract_blocks(resumen)[:2])
            blocks.extend(extract_blocks(datos)[:2])
            blocks.extend(extract_blocks(temas)[:2])
        else:
            blocks.extend(extract_blocks(text)[:4])

        for block in blocks:
            score = 0
            low = block.lower()
            for w in target_words:
                if w in low:
                    score += 1
            if explicit:
                score += 3
            contexts.append((score, rel, block[:650]))

    contexts = sorted(contexts, key=lambda x: (-x[0], x[1]))
    return contexts[:8], sorted(set(linked_sources)), sorted(set(linked_pages))


def related_concepts(contexts, target):
    target_stem = Path(target).stem
    counts = Counter()
    for _, rel, _ in contexts:
        path = WIKI_DIR / rel
        if not path.exists():
            continue
        text = read_text(path)
        for link, label in all_links_in(text):
            if not link.startswith("concepts/"):
                continue
            stem = Path(link).stem
            if stem == target_stem:
                continue
            counts[link] += 1
    return [link for link, _ in counts.most_common(8)]


def classify_domain(slug):
    tests = [
        (("seguridad", "ciber", "ataque", "inyeccion", "red", "sandbox", "telemetria", "advers"), "seguridad y riesgo de sistemas agentivos"),
        (("clin", "salud", "medic", "farmaco", "oncologia", "bio", "terapia", "virus", "sars", "nanob"), "salud, biomedicina e investigacion cientifica"),
        (("gobernanza", "regul", "derecho", "etica", "privacidad", "nist", "rgpd", "estandar"), "gobernanza, regulacion y cumplimiento"),
        (("aprendizaje", "markov", "utilidad", "nash", "juegos", "refuerzo", "modelo"), "modelado, aprendizaje y toma de decisiones"),
        (("multi", "agente", "agent", "herramient", "planificacion", "memoria", "autonom"), "arquitectura y operacion de agentes"),
        (("datos", "infraestructura", "comput", "centros", "stargate", "silica", "energia"), "infraestructura, datos y capacidad computacional"),
        (("economia", "productividad", "capital", "cadena"), "impacto economico y organizacional"),
    ]
    for needles, label in tests:
        if any(n in slug for n in needles):
            return label
    return "marco conceptual de la wiki"


def fallback_definition(slug, contexts):
    title = nice_title(slug)
    domain = classify_domain(slug)
    if contexts:
        best = contexts[0][2]
        best = re.sub(r"^[#*\-\d\.\s]+", "", best)
        if len(best) > 260:
            best = best[:260].rsplit(" ", 1)[0] + "."
        return (
            f"{title} es un concepto usado en la wiki dentro del dominio de {domain}. "
            f"A partir de las fuentes relacionadas, se refiere a: {best}"
        )
    return (
        f"{title} es un concepto de soporte dentro del dominio de {domain}. "
        "Se usa para organizar referencias cruzadas entre documentos, riesgos, arquitecturas y aplicaciones de agentes de IA."
    )


def keywords_from(slug, contexts):
    words = Counter()
    text = slug.replace("-", " ") + " " + " ".join(c[2] for c in contexts[:4])
    for word in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]{4,}", text.lower()):
        clean = (
            word.replace("á", "a").replace("é", "e").replace("í", "i")
            .replace("ó", "o").replace("ú", "u").replace("ñ", "n")
        )
        if clean not in STOPWORDS:
            words[clean] += 1
    return [w for w, _ in words.most_common(7)]


def build_page(target, contexts, sources):
    slug = Path(target).stem
    title = nice_title(slug)
    definition = CURATED.get(slug) or fallback_definition(slug, contexts)
    keys = CURATED_IDEAS.get(slug) or keywords_from(slug, contexts)
    rels = related_concepts(contexts, target)

    if not rels:
        rels = []
        for candidate in ["concepts/sistemas-agentivos-ia", "concepts/inteligencia-artificial", "concepts/ia-agentica"]:
            if candidate != target:
                rels.append(candidate)

    if not sources:
        sources = []
        for _, rel, _ in contexts:
            if rel.startswith("sources/"):
                sources.append(rel[:-3])
        sources = sorted(set(sources))

    evidence = []
    seen = set()
    for _, rel, snippet in contexts:
        if rel in seen:
            continue
        seen.add(rel)
        snippet = snippet.replace("\n", " ").strip()
        if len(snippet) > 320:
            snippet = snippet[:320].rsplit(" ", 1)[0] + "..."
        evidence.append((rel, snippet))
        if len(evidence) >= 4:
            break

    lines = [
        f"# {title}",
        "",
        "## Definición",
        definition,
        "",
        "## Ideas clave",
    ]
    if keys:
        for key in keys[:5]:
            lines.append(f"- {key.replace('-', ' ')}")
    else:
        lines.extend([
            f"- Concepto ubicado en {classify_domain(slug)}.",
            "- Relevante para conectar fuentes y conceptos de la wiki.",
            "- Debe interpretarse junto con las paginas fuente enlazadas.",
        ])

    lines.extend(["", "## Uso en la wiki"])
    if evidence:
        for rel, snippet in evidence:
            lines.append(f"- En [[{rel[:-3]}]], se usa en este contexto: {snippet}")
    else:
        lines.append("- Se usa como nodo de navegacion conceptual para agrupar referencias relacionadas.")

    lines.extend(["", "## Relación con otros conceptos"])
    for rel in rels[:8]:
        lines.append(f"- [[{rel}]]")

    lines.extend(["", "## Fuentes relacionadas"])
    if sources:
        for src in sources[:10]:
            lines.append(f"- [[{src}]]")
    else:
        lines.append("- No hay una fuente directa unica; la pagina se deriva de referencias cruzadas internas.")

    lines.append("")
    return "\n".join(lines)


def enrich(apply):
    targets = []
    for path in sorted(CONCEPTS_DIR.glob("*.md")):
        text = read_text(path)
        if is_placeholder(path) or ENRICHED_MARKER in text or is_generated_concept_page(text):
            targets.append(path)

    prepared = []
    for path in targets:
        target = path.relative_to(WIKI_DIR).as_posix()[:-3]
        contexts, sources, _ = collect_context(target)
        content = build_page(target, contexts, sources)
        prepared.append((path, target, content))

    updated = []
    for path, target, content in prepared:
        write_text(path, content, apply)
        updated.append(target)
    return updated


def update_index_descriptions(apply):
    index_path = WIKI_DIR / "index.md"
    index = read_text(index_path)

    descriptions = {}
    for path in CONCEPTS_DIR.glob("*.md"):
        rel = path.relative_to(WIKI_DIR).as_posix()[:-3]
        text = read_text(path)
        match = re.search(r"## Definición\s+(.+?)(?:\n\n##|\Z)", text, re.S)
        if match:
            desc = strip_links(match.group(1))
            desc = re.sub(r"\s+", " ", desc).strip()
            descriptions[rel] = desc[:120]

    def replace_line(match):
        rel = match.group(1)
        label = match.group(2) or ""
        if rel not in descriptions:
            return match.group(0)
        return f"- [[{rel}{label}]]: {descriptions[rel]}"

    new_index = re.sub(r"^- \[\[(concepts/[^\]|]+)(\|[^\]]+)?\]\]: .*$", replace_line, index, flags=re.M)
    if new_index != index:
        write_text(index_path, new_index, apply)
        return 1
    return 0


def count_remaining():
    return sum(1 for p in CONCEPTS_DIR.glob("*.md") if is_placeholder(p))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    before = count_remaining()
    updated = enrich(args.apply)
    index_changed = update_index_descriptions(args.apply)
    after = count_remaining() if args.apply else before

    print(f"apply={args.apply}")
    print(f"placeholders_before={before}")
    print(f"concepts_enriched={len(updated)}")
    print(f"index_changed={index_changed}")
    print(f"placeholders_after={after}")
    for target in updated[:20]:
        print(target)


if __name__ == "__main__":
    main()
