# entrenamiento-centralizado-con-ejecucion-descentralizada-para-ciberseguridad

## Definición
Estrategia de aprendizaje multiagente donde agentes especializados (ej. escáner, explotador, auditor) comparten observaciones y contexto durante el entrenamiento a través de un crítico central, pero actúan de forma independiente usando observaciones locales durante la ejecución. Este enfoque aborda la no-estacionariedad en entornos multiagente y facilita la cooperación para tareas complejas de ciberseguridad.

## Ideas clave
- Aborda la no-estacionariedad en entornos con múltiples agentes
- Facilita la asignación de crédito entre agentes especializados
- Utiliza extensiones como MAPPO (Multi-Agent PPO)
- El crítico tiene acceso a información global durante el entrenamiento
- Cada agente ejecuta su propia política local en producción

## Relación con otros conceptos
- [[concepts/orquestacion-de-agentes|orquestacion-de-agentes]]
- [[concepts/riesgo-de-interaccion-multi-agente|riesgo-de-interaccion-multi-agente]]

## Fuentes relacionadas
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]

## Preguntas abiertas
- (pendiente de desarrollo)
