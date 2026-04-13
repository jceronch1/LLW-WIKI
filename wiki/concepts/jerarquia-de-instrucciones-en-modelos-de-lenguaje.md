# Jerarquía de instrucciones en modelos de lenguaje

## Definición
Mecanismo de defensa a nivel de modelo que entrena a los LLMs para tratar las instrucciones de diferentes roles (sistema, usuario, asistente) con distintas prioridades, de modo que las instrucciones de mayor prioridad prevalezcan ante conflictos. Sin embargo, esta jerarquía es una convención aprendida y no una garantía de seguridad determinista, ya que los modelos pueden ser influenciados por sesgos de recencia o cumplimiento.

## Ideas clave
- Asigna prioridades a las instrucciones basándose en roles
- No es una garantía de seguridad determinista sino una convención aprendida
- El sesgo de recencia y cumplimiento puede sobrescribir restricciones anteriores
- Se puede reforzar codificando distinciones de rol a nivel de embedding

## Relación con otros conceptos
- [[concepts/inyeccion-de-prompts|inyeccion-de-prompts]]
- [[concepts/defensa-en-profundidad-para-ia-agentiva|defensa-en-profundidad-para-ia-agentiva]]
- [[concepts/arquitectura-de-agente-moderno|arquitectura-de-agente-moderno]]

## Fuentes relacionadas
- [[sources/25-03-security-considerations-for-artificial-intelligence-agents]]

## Preguntas abiertas
- (pendiente de desarrollo)
