# Desdibujamiento de la separación código-datos en agentes de IA

## Definición
En los sistemas de agentes basados en LLM, la distinción fundamental entre código y datos se difumina, ya que las instrucciones en texto plano actúan como código que dirige el flujo de control, y el texto generado dinámicamente puede convertirse en una instrucción en tiempo de ejecución. Esto elimina la separación binaria tradicional entre instrucciones ejecutables y datos pasivos, creando nuevas superficies de ataque.

## Ideas clave
- Los prompts actúan como código que da forma al flujo de control
- El texto dinámico puede convertirse en un prompt en tiempo de ejecución
- No existe una distinción binaria entre código y datos en la capa computacional de los LLM
- Las habilidades del agente funcionan como bibliotecas de código para esta nueva interfaz

## Relación con otros conceptos
- [[concepts/inyeccion-de-prompts|inyeccion-de-prompts]]
- [[concepts/ia-agentiva|ia-agentiva]]
- [[concepts/arquitectura-de-agente-moderno|arquitectura-de-agente-moderno]]

## Fuentes relacionadas
- [[sources/25-03-security-considerations-for-artificial-intelligence-agents]]

## Preguntas abiertas
- (pendiente de desarrollo)
