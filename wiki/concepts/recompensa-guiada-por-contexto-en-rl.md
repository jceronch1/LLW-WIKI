# recompensa-guiada-por-contexto-en-rl

## Definición
Mecanismo en el que la señal de recompensa de un agente de aprendizaje por refuerzo se modifica o pondera según la información contextual recuperada externamente, como la criticidad de una vulnerabilidad CVE o las políticas de seguridad internas. Esto alinea el objetivo de exploración del agente con las prioridades reales de la organización.

## Ideas clave
- Aumenta la recompensa si el agente referencia una vulnerabilidad crítica recuperada
- Penaliza acciones que violan políticas de seguridad recuperadas
- Conecta el conocimiento factual externo con la función de utilidad del agente
- Evita que el agente explote vulnerabilidades de baja importancia
- Alinea el objetivo del agente con las prioridades de seguridad específicas

## Relación con otros conceptos
- [[concepts/generacion-aumentada-por-recuperacion-para-agentes|generacion-aumentada-por-recuperacion-para-agentes]]
- [[concepts/razonamiento-y-accion-intercalados|razonamiento-y-accion-intercalados]]

## Fuentes relacionadas
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]

## Preguntas abiertas
- (pendiente de desarrollo)
