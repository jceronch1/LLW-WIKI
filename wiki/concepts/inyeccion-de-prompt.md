# Inyeccion De Prompt

## Definición
La inyeccion de prompt es un ataque que introduce instrucciones maliciosas o conflictivas para alterar el comportamiento de un modelo. En agentes es critica porque una instruccion inyectada puede terminar en llamadas a herramientas, fuga de datos o acciones no autorizadas.

## Ideas clave
- inyeccion
- prompts
- seguridad
- ataque
- riesgos

## Uso en la wiki
- En [[sources/25-03-security-considerations-for-artificial-intelligence-agents]], se usa en este contexto: 1. **Desdibujamiento código-datos**: Los prompts en LLMs actúan como código ejecutable, rompiendo el principio de seguridad fundamental de separación entre código y datos, lo que permite inyecciones similares a las de SQL o XSS pero en la capa del modelo. 2. **Automatización flexible y no determinista**: A diferencia...
- En [[sources/31-15-fdd-ai-agent-security-comment]], se usa en este contexto: Los riesgos estratégicos asociados incluyen vectores de ataque como puertas traseras (backdoors), inyección de prompts indirecta y envenenamiento de datos, tácticas que Rusia, China e Irán ya han empleado en el contexto de LLMs convencionales. La IA agéntica amplifica el impacto y la sigilo de estos ataques. Por...

## Relación con otros conceptos
- [[concepts/inteligencia-artificial]]
- [[concepts/seguridad-informatica]]
- [[concepts/modelos-de-lenguaje-grandes]]
- [[concepts/sistemas-agentivos-ia]]
- [[concepts/defensa-en-profundidad]]
- [[concepts/control-de-acceso-basado-en-roles]]
- [[concepts/sistemas-multi-agente]]
- [[concepts/sandboxing]]

## Fuentes relacionadas
- [[sources/22-08-ieee-usa-nist-ai-agents]]
- [[sources/25-03-security-considerations-for-artificial-intelligence-agents]]
- [[sources/31-15-fdd-ai-agent-security-comment]]
