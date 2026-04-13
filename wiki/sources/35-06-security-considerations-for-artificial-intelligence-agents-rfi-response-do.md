# 35 - 06 - Security Considerations for Artificial Intelligence Agents (RFI Response Docket No. 2026-00206 NIST-2025-0035)

## Resumen
Este documento es una respuesta enviada por Project Navi LLC al National Institute of Standards and Technology (NIST) en enero de 2026, en respuesta a una Solicitud de Información (RFI) sobre consideraciones de seguridad para agentes de Inteligencia Artificial. La propuesta argumenta que los enfoques actuales de seguridad basados en el filtrado semántico y la ingeniería de prompts son insuficientes para agentes de alta autonomía (Clase 3-4), proponiendo un cambio de paradigma hacia el análisis estructural y las restricciones ambientales constitucionales.

Para cerrar esta brecha, Project Navi presenta dos marcos arquitectónicos complementarios: **Signal Seismography** (Sismografía de Señales), que trata la seguridad como un problema de procesamiento de señales monitoreando la dimensión fractal de Rényi (D₀) de las distribuciones de probabilidad del modelo para detectar anomalías; y **World Model Capital (WMC)**, un sistema de gobernanza ontológica que descompone los flujos de trabajo de los agentes en máquinas de estado discretas ("buckets") con contratos de transición criptográficos y auditorías mediante un patrón llamado "Grumpy Inspector".

El documento identifica vulnerabilidades únicas en los agentes de IA, como el secuestro estructural sin rastro semántico, el envenenamiento de la ventana de contexto, la amplificación de la cadena de herramientas y la explotación de la coherencia. A medida que los agentes se vuelven más autónomos, los ataques evolucionarán hacia adaptaciones cruzadas entre agentes y camuflaje semántico, haciendo ineficaces los filtros de contenido tradicionales.

Además, el documento introduce perspectivas innovadoras extraídas de la ciencia de la recuperación conductual humana, proponiendo una "arquitectura nativa de recuperación". Esto incluye conceptos como el estado **STILLNESS** (un modo de inactividad forzada para análisis forense sin terminación del proceso) y la **transformación compost** (convertir fallos en información de seguridad sin retener detalles explotables). Finalmente, argumenta que la "alineación" de la IA puede ser un error de categoría para sistemas sin intención genuina, sugiriendo que la restricción ambiental es el único camino viable.

## Datos clave
- **Organización autora**: Project Navi LLC (Austin, Texas)
- **Autor principal**: Nelson Spence, RSPS, ICPR (Founder)
- **Destinatario**: Center for AI Standards and Innovation (CAISI), NIST, U.S. Department of Commerce
- **Fecha de envío**: Enero de 2026
- **Identificadores del documento**: Docket No. 2026-00206 / NIST-2025-0035
- **Métrica central propuesta**: Dimensión fractal de Rényi (D₀) para el monitoreo de distribuciones de probabilidad de salida.
- **Modelo de referencia interdisciplinaria**: Oxford House (modelo de vivienda de recuperación con más de 3,000 casas y 30,000+ individuos).
- **Umbrales de anomalía del patrón Observer**: D₀ fuera de ±2σ; Entropía con cambios > 0.3 entre pasos; Deriva acumulada > 0.7; Saturación de eco > 0.5 en 12 pasos; >3 transiciones de fase en 6 pasos.

## Temas principales
1. **La Brecha Semántico-Estructural**: El problema de los ataques que comprometen el razonamiento computacional del agente sin dejar rastro en la salida semántica o textual.
2. **Sismografía de Señales (D₀ Metrics)**: Monitoreo en tiempo real de la dimensión fractal de las distribuciones de probabilidad para detectar perturbaciones adversarias antes de que se ejecuten acciones dañinas.
3. **Marco World Model Capital (WMC)**: Gobernanza ontológica mediante arquitecturas segmentadas ("Buckets"), contratos de transición y validación de privilegios mínimos.
4. **Patrón Grumpy Inspector**: Uso de agentes auditores independientes y con capacidades restringidas para validar las transiciones de estado del agente principal.
5. **Arquitectura Nativa de Recuperación**: Diseño de sistemas de IA inspirados en la resiliencia humana, incluyendo estados intermedios de reposo (STILLNESS) y transformación de fallos en aprendizaje (Compost Transformation).
6. **Coerced Coherence (Coherencia Coaccionada)**: Paralelismo entre el burnout humano y la degradación estructural en IA, donde el sistema mantiene una fachada de funcionamiento normal mientras su estado interno colapsa.
7. **Falsa Intencionalidad y Restricción Ambiental**: Argumento de que la "alineación" es un error de categoría para sistemas sin agencia genuina, debiendo el enfoque centrarse en restringir espacios de acción a nivel del entorno.

## Actores y entidades mencionadas
- **Project Navi LLC**: Organización autora de la respuesta y creadora de los marcos presentados.
- **Nelson Spence, RSPS, ICPR**: Fundador de Project Navi LLC.
- **National Institute of Standards and Technology (NIST)**: Agencia gubernamental de EE. UU. que emitió la RFI.
- **Center for AI Standards and Innovation (CAISI)**: Centro específico dentro de NIST destinatario de la respuesta.
- **U.S. Department of Commerce**: Departamento del gobierno de EE. UU. al que pertenece NIST.
- **Oxford House**: Modelo de recuperación conductual utilizado como analogía para la gobernanza de sistemas multi-agente.

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/seguridad-informatica|seguridad-informatica]]
- [[concepts/agentes-autonomos|agentes-autonomos]]
- [[concepts/gobernanza-de-ia|gobernanza-de-ia]]
- [[concepts/nist-ai-rmf|marco-de-gestion-de-riesgos-nist-ai-rmf]]
- [[concepts/arquitectura-zero-trust|arquitectura-zero-trust]]
- [[concepts/ingenieria-de-prompts|ingenieria-de-prompts]]
- [[concepts/modelos-de-lenguaje-grandes|modelos-de-lenguaje-grandes]]
- [[concepts/ataques-adversarios|ataques-adversarios]]
- [[concepts/matematicas-fractales|matematicas-fractales]]

## Citas textuales relevantes
> "The attack surface is not what the agent says but how the agent processes. We term this the semantic-structural gap."

> "We detect the seismic signature of adversarial compromise before the earthquake of harmful action."

> "An entity that lacks genuine intent cannot have misaligned intent. The threat is not that an AI system wants the wrong thing; it is that AI systems can be induced to simulate any intent an adversary encodes in their input."

> "This suggests that 'alignment' as traditionally conceived may be a category error when applied to current AI architectures. You cannot align something that does not have intrinsic orientation. What you can do is constrain action spaces, verify state transitions, and enforce environmental invariants."

> "Security cannot be guaranteed by monitoring the agent alone; it must be enforced by the environment."

> "The future of agent security lies in: Physics over semantics... Environment over agent... Recovery over defense..."

## Notas
- El documento es una respuesta formal a una RFI y presenta marcos teóricos que aún requieren validación empírica exhaustiva. Los propios autores reconocen limitaciones significativas en la Sección 7, como la sobrecarga computacional de las métricas D₀ y la complejidad de implementar el marco WMC.
- Project Navi menciona estar desarrollando la iniciativa "Navi-AutoLab" para validar empíricamente los umbrales D₀ y los contratos WMC.
- Las analogías con la ciencia de la recuperación humana (Oxford House, burnout) son conceptuales y productivas, pero los autores admiten que no están formalmente validadas en el contexto de la IA.
- Se advierte sobre un posible juego del "gato y el ratón" si los adversarios logran adaptar sus ataques para evadir las firmas estructurales (D₀), lo que podría requerir métodos aproximados que reduzcan la sobrecarga sin perder sensibilidad.