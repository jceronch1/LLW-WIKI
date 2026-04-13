# 25 - 03 - Security Considerations for Artificial Intelligence Agents

## Resumen
Este documento, presentado como respuesta oficial de Perplexity al Request for Information (RFI) 2025-0035 del NIST/CAISI, detalla las observaciones y recomendaciones sobre la seguridad de los agentes de IA de frontera. Basado en la experiencia operativa de Perplexity con sistemas agénticos de propósito general en entornos abiertos, el texto advierte que las arquitecturas de agentes alteran supuestos fundamentales de la ciberseguridad tradicional, como la separación entre código y datos, los límites de autoridad y la previsibilidad de ejecución, generando nuevos modos de fallo en confidencialidad, integridad y disponibilidad.

El documento mapea las principales superficies de ataque a través de herramientas, conectores, límites de alojamiento y coordinación multi-agente. Presta especial atención a la inyección indirecta de prompts, el problema del "confused deputy" (diputado confundido) y los fallos en cascada en flujos de trabajo de larga duración. Estos riesgos se agravan en sistemas multi-agente, donde la delegación implícita y la escalada de privilegios a través de cadenas de agentes complican la auditoría y el control de acceso.

Como estrategia de defensa, se propone una arquitectura de defensa en profundidad organizada en capas: mitigaciones a nivel de entrada y de modelo, monitoreo de ejecución en entornos aislados (sandboxes) y, de manera crítica, una capa de aplicación de políticas deterministas como última línea de defensa. Se señala que las defensas probabilísticas basadas en modelos no son suficientes por sí solas debido a la naturaleza no determinista de los LLMs.

Finalmente, el documento identifica brechas críticas de investigación y estandarización. Insta a NIST a desarrollar arquitecturas de referencia, métricas de seguridad adaptativas y modelos de control de acceso que combinen RBAC (Control de Acceso Basado en Roles) con enfoques adaptativos al riesgo, además de abordar los factores humanos para evitar la fatiga de alertas en los usuarios.

## Datos clave
- **Fecha del documento**: 9 de marzo de 2026 (versión arXiv actualizada el 5 de abril de 2026).
- **Contexto**: Respuesta a NIST/CAISI Request for Information 2025-0035.
- **Autores**: Ninghui Li, Kaiyuan Zhang (Perplexity/Purdue University), Kyle Polley, Jerry Ma (Perplexity).
- **Vulnerabilidades citadas**: CVE-2026-25253 (ejecución remota de código por un clic en OpenClaw mediante fuga de tokens) y CVE-2026-26327 (verificación de autenticidad de datos insuficiente).
- **Marcos de trabajo citados**: CaMeL (separación de flujo de control y datos), AgentSandbox (aplicación de principios de Saltzer-Schroeder), BrowseSafe (prevención de inyección en navegadores).
- **Protocolos emergentes mencionados**: Model Context Protocol (MCP) y Agent2Agent Protocol (A2A), criticados por carecer de provisiones de seguridad de alto nivel.
- **Principios fundamentales**: Reevaluación de los 8 principios de diseño de Saltzer y Schroeder (1975) aplicados a agentes de IA.

## Temas principales
1. **Desdibujamiento código-datos**: Los prompts en LLMs actúan como código ejecutable, rompiendo el principio de seguridad fundamental de separación entre código y datos, lo que permite inyecciones similares a las de SQL o XSS pero en la capa del modelo.
2. **Automatización flexible y no determinista**: A diferencia del software tradicional, los agentes construyen flujos de trabajo dinámicamente, requiriendo privilegios amplios que aumentan la superficie de ataque y dificultan la verificación formal de la seguridad.
3. **Inadecuación de los mecanismos de seguridad actuales**: Las seguridad diseñada para humanos (lentos, auditable) o sistemas deterministas no escala para agentes que actúan a velocidad de máquina y con comportamiento probabilístico.
4. **Superficies de ataque en arquitecturas de agentes**: Riesgos en la lógica de selección de herramientas, límites de ejecución, ingesta de contenido web no confiable, cadenas de suministro de plugins y superficies de coordinación multi-agente.
5. **Inyección indirecta de prompts**: Adversarios incrustan instrucciones maliciosas en contenido recuperado por el agente (web, correo), explotando la incapacidad del LLM para distinguir entre instrucciones confiables y datos no confiables.
6. **Problemas en sistemas multi-agente**: Riesgo de diputado confundido ("confused deputy") donde un agente externo manipula a uno interno con más privilegios, y delegación implícita sin cadena de autorización clara.
7. **Defensa en profundidad para IA**: Necesidad de combinar defensas a nivel de entrada (detección), nivel de modelo (jerarquía de instrucciones), nivel de sistema (sandboxing) y una última línea de defensa determinista (listas de permitidos/bloqueados, límites de tasa).
8. **Brechas de investigación**: Necesidad de benchmarks de seguridad adaptativos y dinámicos, y modelos de control de acceso que combinen RBAC con gestión de riesgo adaptativo.

## Actores y entidades mencionadas
- **Perplexity AI / Perplexity Secure Intelligence Institute**: Autores del documento y operadores de sistemas agénticos.
- **NIST / CAISI**: Organismos gubernamentales que emitieron la solicitud de información.
- **Purdue University**: Afiliación académica de los autores principales.
- **OpenClaw**: Plataforma de agentes de código abierto utilizada como caso de estudio de vulnerabilidades (CVEs).
- **Anthropic**: Referenciada por sus documentos sobre uso de computadora y ejecución de código con MCP.
- **OpenAI**: Referenciada por sus herramientas de agentes (AgentKit, herramientas de código).
- **ProtectAI y Meta**: Mencionadas como desarrolladores de sistemas de detección de prompts maliciosos.
- **Saltzer y Schroeder**: Investigadores clásicos de seguridad informática (1975), cuyos principios se abogan por readaptar.

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/sistemas-agentivos-ia|agentes-de-ia]]
- [[concepts/seguridad-informatica|seguridad-informatica]]
- [[concepts/inyeccion-de-prompt|inyeccion-de-prompt]]
- [[concepts/defensa-en-profundidad|defensa-en-profundidad]]
- [[concepts/control-de-acceso-basado-en-roles|control-de-acceso-basado-en-roles]]
- [[concepts/modelos-de-lenguaje-grandes|modelos-de-lenguaje-grandes]]
- [[concepts/sistemas-multi-agente|sistemas-multi-agente]]
- [[concepts/sandboxing|sandboxing]]
- [[concepts/confused-deputy|confused-deputy]]

## Citas textuales relevantes
> "Agent architectures change core assumptions around code-data separation, authority boundaries, and execution predictability, creating new confidentiality, integrity, and availability failure modes."

> "Each generation of computing platforms introduces new code-data separation problems; Large Language Model (LLM)-powered agent systems represent the latest and perhaps most severe instance of this recurring challenge."

> "Because absolute security is unattainable, security mechanisms must be designed for the specific computing environments in which they operate, balancing usability, functionality, and risk."

> "Unlike input-level and model-level defenses, whose effectiveness depends on statistical properties of the model, deterministic enforcement layers use conventional, verifiable code to block prohibited actions regardless of what the LLM produces."

> "No single layer is sufficient on its own; the non-deterministic nature of LLM reasoning ensures that any individual defense can be circumvented under sufficiently adaptive attack strategies."

> "Role boundaries remain a learned convention rather than a hard security guarantee, leaving them vulnerable to adversarial influence."

## Notas
- El documento sirve como un puente entre la seguridad informática tradicional y la seguridad específica de la IA, insistiendo en que los principios clásicos (como mínimo privilegio) siguen siendo válidos pero deben readaptarse a sistemas no deterministas.
- Se hace un análisis crítico de la "falacia de la tasa base" (base-rate fallacy) en las defensas a nivel de entrada: en sistemas agénticos con alto volumen de entradas benignas, incluso una tasa muy baja de falsos positivos genera una cantidad inmanejable de alertas, degradando la utilidad del sistema.
- La propuesta de "última línea de defensa determinista" es presentada como un imperativo técnico innegociable; las políticas de seguridad críticas no deben depender de la interpretación probabilística de un LLM.
- Aunque existen protocolos emergentes como MCP y A2A, el documento advierte que actualmente solo abordan seguridad a nivel de transporte y autenticación, descuidando la delegación y la gestión de privilegios entre agentes.