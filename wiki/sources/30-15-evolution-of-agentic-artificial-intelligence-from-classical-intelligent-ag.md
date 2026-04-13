# 30 - 15 - Evolution of Agentic Artificial Intelligence From Classical Intelligent Agents to LLM-Based Autonomous Systems

## Resumen
La Inteligencia Artificial Agéntica (Agentic AI) se refiere a sistemas de IA capaces de planificar, actuar y adaptar su comportamiento para lograr objetivos con supervisión humana limitada. Este documento traza la evolución de este campo, desde los agentes inteligentes clásicos y los sistemas multi-agente hasta los actuales sistemas autónomos basados en Modelos de Lenguaje Grande (LLMs) que integran herramientas, memoria y razonamiento de múltiples pasos. La revisión sintetiza las ideas clave, arquitecturas, tecnologías habilitadoras, métodos de evaluación y aplicaciones del mundo real, destacando cómo los sistemas agénticos modernos combinan planificación, uso de herramientas, recuperación, reflexión y coordinación.

La evolución se estructura en tres eras: la Era I (IA simbólica y agentes basados en planificación), la Era II (IA estadística y agentes impulsados por aprendizaje) y la Era III (modelos fundacionales y agencia centrada en el lenguaje). Este último paradigma marca un cambio radical donde el lenguaje natural se convierte en una interfaz general para objetivos, planes y entornos, transformando los LLMs de generadores de respuestas únicas a sistemas de decisión estructurados mediante ciclos iterativos de pensar-actuar-observar-reflexionar.

El documento detalla la "pila" moderna de IA Agéntica, que incluye interpretación de objetivos, planificación, uso de herramientas, memoria, reflexión y monitoreo de ejecución. Las arquitecturas se dividen en sistemas de agente único y modular (como MRKL), arquitecturas colaborativas multi-agente (como AutoGen y SWE-agent), y agentes autónomos generativos/corporizados (como Generative Agents y Voyager). Cada vez más, estos sistemas se aplican en automatización de tareas cognitivas y empresariales, así como en simulación y entornos autónomos.

Sin embargo, la creciente autonomía introduce riesgos críticos más allá de los chatbots tradicionales, como acciones alucinadas, inyección de prompts, exceso de autonomía y brechas de responsabilidad. Por ello, la investigación futura y el despliegue en entornos de alto riesgo dependen de lograr una "autonomía responsable": sistemas que no solo sean capaces y adaptables, sino también audibles, controlables y alineados con la supervisión institucional y marcos regulatorios como los de NIST y la UE.

## Datos clave
- **Autores:** Abhishek Sharma, Surjeet Sah, Mohammad Sayeed.
- **Publicación:** International Journal of Engineering and Techniques, Volumen 12, Issue 2, Marzo-Abril 2026.
- **Definición central:** La IA Agéntica se refiere a sistemas de IA que pueden planificar, tomar acciones y adaptar su comportamiento para lograr objetivos con supervisión humana limitada.
- **Eras de evolución:**
  - Era I: IA Simbólica y agentes basados en planificación (interpretables pero frágiles).
  - Era II: IA Estadística y agentes basados en aprendizaje (RL, adaptativos pero costosos y específicos de dominio).
  - Era III: Modelos fundacionales y agencia centrada en el lenguaje (LLMs como interfaz general).
- **Componentes del Stack Agéntico Moderno:** Interpretación de objetivos, Planificación, Uso de herramientas, Memoria y recuperación, Reflexión/autocorrección, Monitoreo de ejecución.
- **Dimensiones de evaluación:** Éxito de la tarea, Eficiencia, Robustez, Fundamentación (Groundedness), Seguridad, Supervisión humana.
- **Riesgos principales:** Acciones alucinadas, inyección de prompts, exceso de autonomía, brechas de responsabilidad.
- **Controles prácticos:** Permisos de herramientas (menor privilegio), humano-en-el-bucle (HITL), auditoría y rastreo, razonamiento fundamentado y verificación, entornos aislados (sandboxing).

## Temas principales
1. Fundamentos conceptuales de agentes y agencia (definiciones clásicas, planificación inspirada en humanos, aprendizaje por refuerzo).
2. Evolución histórica de la IA Agéntica (desde agentes simbólicos hasta LLMs).
3. La pila tecnológica de la IA Agéntica moderna basada en LLMs.
4. Integración de razonamiento, uso de herramientas y memoria (ReAct, Toolformer, RAG).
5. Reflexión, autocorrección y control adaptativo (Reflexion).
6. Arquitecturas de agentes: Patrones de diseño y taxonomía (Agente único/MRKL, Multi-agente/AutoGen, Generativos/Embodied).
7. Evaluación de sistemas de IA Agéntica.
8. Aplicaciones en automatización cognitiva-empresarial y entornos interactivos-autónomos.
9. Seguridad, riesgos y gobernanza de la IA Agéntica.
10. Desafíos abiertos y direcciones de investigación (autonomía responsable, marcos regulatorios).

## Actores y entidades mencionadas
- **Instituciones Académicas:** Shivalik College of Engineering (Dehradun), JBIT College (Dehradun).
- **Organizaciones y Reguladores:** NIST (National Institute of Standards and Technology), European Union, OpenAI, IBM, University of Cincinnati, International Journal of Engineering and Techniques.
- **Investigadores y Referencias Clave:** 
  - Russell & Norvig (2020) - IA clásica.
  - Wooldridge (2009) - Sistemas multi-agente.
  - Bratman (1987) - Filosofía de la planificación.
  - Sutton & Barto (2018) - Aprendizaje por refuerzo.
  - Yao et al. (2022) - ReAct (Razonamiento y actuación intercalados).
  - Shinn et al. (2023) - Reflexion (Aprendizaje basado en reflexión verbal).
  - Wang et al. (2023) - Voyager (Agente embodied en Minecraft) y Survey de agentes autónomos basados en LLM.
  - Wu et al. (2023) - AutoGen (Conversaciones multi-agente).
  - Yang et al. (2024) - SWE-agent (Interfaz agente-computadora).
  - Park et al. (2023) - Generative Agents (Simulación social).
  - Karpas et al. (2022) - MRKL (Arquitectura neuro-simbólica modular).
  - Schick et al. (2023) - Toolformer.
  - Lewis et al. (2020) - RAG (Generación Aumentada por Recuperación).

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/agentes-autonomos|agentes-autonomos]]
- [[concepts/modelos-de-lenguaje-grandes|modelos-de-lenguaje-grandes]] (LLMs)
- [[concepts/sistemas-multi-agente|sistemas-multi-agente]]
- [[concepts/aprendizaje-por-refuerzo|aprendizaje-por-refuerzo]]
- [[concepts/planificacion-ia|planificacion-ia]]
- [[concepts/uso-de-herramientas|uso-de-herramientas]] (Tool use / Function calling)
- [[concepts/generacion-aumentada-por-recuperacion-para-agentes|generacion-aumentada-por-recuperacion]] (RAG)
- [[concepts/seguridad-ia|seguridad-ia]]
- [[concepts/gobernanza-de-ia|gobernanza-ia]]
- [[concepts/arquitectura-neuro-simbolica|arquitectura-neuro-simbolica]]

## Citas textuales relevantes
> "Agentic Artificial Intelligence (Agentic AI) refers to AI systems that can plan, take actions and adapt their behavior to achieve goals with limited human supervision."

> "LLMs introduced a major shift: natural language became a general interface for goals, plans, tools and environments."

> "Reasoning + tools + retrieval + memory transform LLMs into structured decision systems."

> "Architectural Shift: From single-response generation → to iterative think–act–observe–reflect cycles."

> "Agentic AI introduces risks beyond typical chatbots because it can take actions, trigger workflows and interact with external systems."

> "Future advancement depends on achieving responsible autonomy systems that are not only capable and adaptive but also auditable, controllable, and aligned with institutional oversight."

## Notas
- El documento es un artículo de revisión publicado en 2026, lo que indica una perspectiva actualizada sobre el estado del arte de los agentes autónomos basados en LLMs.
- Propone una clara distinción de riesgo entre la IA tradicional (error a nivel de salida) y la IA Agéntica (riesgo de sistema a nivel de acción).
- Subraya que la evaluación de sistemas agénticos es significativamente más compleja que la de modelos de un solo turno, requiriendo métricas de eficiencia, robustez y supervisión humana.
- El enfoque en la "autonomía responsable" refleja una preocupación creciente en la comunidad de IA por alinear la alta capacidad de acción de los LLMs con marcos regulatorios emergentes (NIST RMF, EU AI Act).