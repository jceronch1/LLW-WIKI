# Aislamiento de flujo de control y datos en agentes

## Definición
Estrategia de defensa a nivel de sistema que separa explícitamente el flujo de control, procesado por un LLM privilegiado usando consultas de usuario confiables, del flujo de datos, manejado por un LLM en cuarentena que procesa datos externos no confiables. Un sistema de seguimiento de flujo de datos basado en capacidades asegura que las variables contaminadas por datos no confiables no puedan influir en las operaciones privilegiadas.

## Ideas clave
- Separa el flujo de control del flujo de datos
- Un LLM privilegiado procesa la consulta del usuario y genera un plan
- Un LLM en cuarentena maneja datos externos no confiables
- El seguimiento de flujo de datos evita que variables contaminadas influyan en operaciones privilegiadas

## Relación con otros conceptos
- [[concepts/inyeccion-de-prompts|inyeccion-de-prompts]]
- [[concepts/defensa-en-profundidad-para-ia-agentiva|defensa-en-profundidad-para-ia-agentiva]]
- [[concepts/arquitectura-hibrida-rl-rag|arquitectura-hibrida-rl-rag]]

## Fuentes relacionadas
- [[sources/25-03-security-considerations-for-artificial-intelligence-agents]]

## Preguntas abiertas
- (pendiente de desarrollo)
