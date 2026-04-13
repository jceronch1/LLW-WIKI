# envenenamiento-de-ventana-de-contexto

## Definición
Vulnerabilidad en sistemas de agentes donde una única fuente de datos comprometida a principios de un flujo de trabajo agéntico puede influir en todo el razonamiento posterior sin activar filtros de contenido. La instrucción maliciosa se acumula y se convierte en parte del contexto de confianza a través de las llamadas a herramientas.

## Ideas clave
- A diferencia de la inyección tradicional, el contexto acumula estado a través de múltiples iteraciones
- La instrucción maliciosa se enmascara como contexto confiable en pasos posteriores
- Se mitiga mediante la transferencia de capital (contexto verificado) en lugar de acumulación en una sola ventana

## Relación con otros conceptos
- [[concepts/inyeccion-de-prompts|inyeccion-de-prompts]]
- [[concepts/propagacion-de-vulnerabilidades-en-sistemas-multi-agente|propagacion-de-vulnerabilidades-en-sistemas-multi-agente]]
- [[concepts/capital-de-modelo-mundial-wmc|capital-de-modelo-mundial-wmc]]

## Fuentes relacionadas
- [[sources/35-06-security-considerations-for-artificial-intelligence-agents-rfi-response-do]]

## Preguntas abiertas
- (pendiente de desarrollo)
