# arquitectura-hibrida-rl-rag

## Definición
Modelo de sistema que integra el aprendizaje por refuerzo (RL) para la toma de decisiones y exploración del entorno, con la generación aumentada por recuperación (RAG) para inyectar conocimiento externo y contexto en tiempo real antes de la selección de acciones. Esta sinergia permite que el agente base sus acciones de ciberseguridad en información actualizada y políticas específicas, reduciendo la exploración ciega.

## Ideas clave
- Combina la exploración estocástica de RL con el conocimiento factual de RAG
- El estado del agente se aumenta con documentos recuperados antes de la acción
- Reduce alucinaciones y acciones sin fundamento en ciberseguridad
- Permite actualización de conocimiento sin reentrenar la política de RL
- Utiliza bases de datos vectoriales para el contexto de ciberseguridad

## Relación con otros conceptos
- [[concepts/generacion-aumentada-por-recuperacion-para-agentes|generacion-aumentada-por-recuperacion-para-agentes]]
- [[concepts/razonamiento-y-accion-intercalados|razonamiento-y-accion-intercalados]]
- [[concepts/planificacion-dinamica-en-ia|planificacion-dinamica-en-ia]]

## Fuentes relacionadas
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]

## Preguntas abiertas
- (pendiente de desarrollo)
