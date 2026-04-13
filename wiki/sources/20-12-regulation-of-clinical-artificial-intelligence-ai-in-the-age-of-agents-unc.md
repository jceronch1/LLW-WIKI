# 20 - 12 - Regulation of clinical Artificial Intelligence (AI) in the Age of Agents Unconfined Non-Deterministic Clinical Software (UNDCS) systems for healthcare

## Resumen
Este documento presenta una respuesta crítica a las propuestas de Weissman et al. sobre la necesidad de nuevas regulaciones para los sistemas de soporte a la decisión clínica (CDSS) basados en modelos de lenguaje de gran tamaño (LLM). Los autores argumentan que, si bien algunas preocupaciones sobre los usuarios finales ya están cubiertas por las directrices actuales de la FDA y otros organismos internacionales, existe un vacío regulatorio significativo respecto a los sistemas de IA "no confinados".

El núcleo del argumento reside en la distinción entre el software clínico tradicional —clasificado como Deterministic Clinical Software (DCS) o Confined Clinical Software (CCS)— y una nueva categoría denominada Unconfined Non-<strong>Deterministic</strong> Clinical Software (UNDCS). A diferencia de los sistemas anteriores, que operan con salidas predefinibles y relaciones de datos fijas, los sistemas UNDCS operan en un espacio semántico abierto y pueden presentar comportamientos estocásticos (no deterministas) debido a factores como la "temperatura" en la generación de texto, lo que introduce riesgos de "alucinaciones" y errores semánticos.

Finalmente, el artículo propone que el paradigma regulatorio actual, basado en el "etiquetado" (label-driven) y el uso previsto por el fabricante, es insuficiente para abordar los modelos de IA de propósito general disponibles directamente al consumidor (como ChatGPT o Claude). Se hace un llamado a implementar nuevas estrategias de mitigación de riesgos, tales como *red teaming*, *guardrails*, RAG (Generación Aumentada por Recuperación) y moderación entre agentes, para garantizar la seguridad del paciente en la era de los agentes de IA.

## Datos clave
- **Identificador del documento:** DOI: 10.1038/s41746-026-02420-z.
- **Categoría de software propuesta:** Unconfined Non-Deterministic Clinical Software (UNDCS).
- **Tipologías de software clínico analizadas:**
    - **DCS (Deterministic Clinical Software):** Algoritmos con relaciones entrada-salida fijas y predefinidas.
    - **CCS (Confined Clinical Software):** Uso de técnicas como *deep learning* con salidas limitadas a un espectro predecible.
    - **UNDCS (Unconfined Non-Deterministic Clinical Software):** Sistemas basados en transformadores/LLM con espacio semántico abierto y potencial de no-determinismo.
- **Estrategias de mitigación identificadas:** *Red teaming*, *guardrails* (ej. Llama Guard), RAG, moderación agente-agente (MAS), y modelos neuro-simbólicos.
- **Fecha de publicación/aceptación:** Recibido el 6 de mayo de 2025; Aceptado el 29 de enero de 2026.

## Temas principales
1. **Evaluación de marcos regulatorios existentes:** Análisis de la suficiencia de las directrices de la FDA para el *Software as a Medical Device* (SaMD) frente a los nuevos LLM.
2. **Taxonomía de la evolución del software clínico:** Diferenciación técnica entre sistemas deterministas, confinados y no confinados.
  3. **Riesgos de la IA no determinista:** Estudio de las alucinaciones, la estocasticidad por parámetros de temperatura y la dificultad de la evaluación mediante conjuntos de datos tradicionales.
4. **Brecha regulatoria en modelos directos al consumidor:** El problema de los modelos de propósito general que operan sin el control de fabricantes registrados y bajo descargos de responsabilidad genéricos.
5. **Propuestas de mitigación y seguridad:** Implementación de arquitectos de agentes, procesos de *LLM-as-a-Judge* y técnicas de recuperación de información para aumentar la fiabilidad.

## Actores y entidades mencionadas
- **Organizaciones Reguladoras:** FDA (Food and Drug Administration), IMDRF (International Medical Device Regulators Forum), Health Sciences Authority (Singapur).
- **Instituciones Académicas y de Salud:** National University of Singapore, Duke-NUS Medical School, Singapore National Eye Centre, Tsinghua University, Seoul National University Bundang Hospital.
- **Proveedores de Tecnología/Modelos:** OpenAI (ChatGPT), Anthropic (Claude), Grok.
- **Estudios y Referencias:** Weissman et al. (estudio sobre outputs de dispositivos médicos), Estudio APPRAISE (aceptación de CDSS en oftalmología).

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/llm|LLM]] (Large Language Models)
- [[concepts/samd|SaMD]] (Software as a Medical Device)
- [[concepts/cdss|CDSS]] (Clinical Decision Support Systems)
- [[concepts/rag|RAG]] (Retrieval-Augmented Generation)
- [[concepts/sistemas-agentivos-ia|Agentes de IA]]
- [[concepts/red-teaming|Red Teaming]]
- [[concepts/neuro-symbolic-ai|Neuro-symbolic AI]]
- [[concepts/determinismo-vs-no-determinismo|Determinismo vs No-determinismo]]

## Citas textuales relevantes
> "A new category of regulations may be required for novel general-purpose SaMD solutions developed using GenAI or other AI techniques for generalized CDS, which we term unconﬁned non-deterministic clinical software (UNDCS)."

> "Current regulations are label-driven, with device classiﬁcation based on manufacturer-designated intended use... These direct-to-consumer models are not addressed by regulations tied to labelling and manufacturer registration."

> "As UNDCS blurs the boundaries between intended uses and users, regulators have a challenging responsibility to adopt forward-looking frameworks as agile as the technologies they govern without stiﬂing advances in healthcare transformation."

## Notas
- El documento advierte que incluso las herramientas de IA que no se consideran "clínicas" (como los escribas de IA para documentación administrativa) pueden tener consecuencias clínicas indirectas graves, como errores en diagnósticos derivados de documentación errónea.
- Se destaca una limitación importante en la estrategia de RAG: aunque reduce riesgos, puede introducir omisiones si los materiales recuperados sobrepasan el contexto local de la consulta.