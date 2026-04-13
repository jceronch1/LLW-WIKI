# verificacion-de-microsegmentacion-mediante-rl

## Definición
Aplicación de agentes de aprendizaje por refuerzo para probar y auditar entornos de arquitectura de confianza cero, donde el agente intenta moverse lateralmente entre microsegmentos de red. El agente recibe una recompensa positiva si logra conectar segmentos que deberían estar aislados, identificando así fallas en las políticas de microsegmentación.

## Ideas clave
- El agente identifica zonas y selecciona pares origen-destino para probar
- Intenta conexiones entre zonas restringidas para auditar su aislamiento
- Recompensa positiva si la conexión indebida tiene éxito (indicando una falla)
- Utiliza RAG para recuperar reglas de microsegmentación actuales
- Permite la auditoría automatizada de políticas de red de confianza cero

## Relación con otros conceptos
- [[concepts/pruebas-de-penetracion-autonomas-internas|pruebas-de-penetracion-autonomas-internas]]
- [[concepts/uso-de-herramientas-en-ia|uso-de-herramientas-en-ia]]

## Fuentes relacionadas
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]

## Preguntas abiertas
- (pendiente de desarrollo)
