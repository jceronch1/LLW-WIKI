# patron-del-inspector-grunon

## Definición
Patrón de seguridad donde cada transición de estado en un flujo de trabajo de un agente es validada por un agente auditor separado y más simple con capacidades restringidas. Este auditor no puede ser comprometido a través de la misma ventana de contexto que el agente principal y tiene un mandato estricto: verificar, aprobar/rechazar y registrar.

## Ideas clave
- Proporciona validación entre pares en lugar de monitorización centralizada
- Evita puntos únicos de fallo en la supervisión
- La separación arquitectónica garantiza la independencia del auditor frente a compromisos en el agente principal

## Relación con otros conceptos
- [[concepts/capital-de-modelo-mundial-wmc|capital-de-modelo-mundial-wmc]]
- [[concepts/evaluacion-de-riesgos-a-nivel-de-sistema|evaluacion-de-riesgos-a-nivel-de-sistema]]
- [[concepts/orquestacion-de-agentes|orquestacion-de-agentes]]

## Fuentes relacionadas
- [[sources/35-06-security-considerations-for-artificial-intelligence-agents-rfi-response-do]]

## Preguntas abiertas
- (pendiente de desarrollo)
