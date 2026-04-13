# aprendizaje-q-heterogeneo-para-poblaciones-mixtas

## Definición
Algoritmo de aprendizaje por refuerzo multiagente diseñado para interacciones estratégicas entre agentes de IA (maximizadores de utilidad esperada) y agentes humanos (con preferencias de Teoría de Perspectivas). Integra diferentes funciones de valor, manejo de empates por umbral de patología, y actualizaciones de creencias y puntos de referencia adaptativos para modelar la dinámica no cooperativa de poblaciones heterogéneas.

## Ideas clave
- Combina actualización Q estándar con transformación CPT en la política
- Maneja empates mediante muestreo Softmax bajo un umbral de patología
- Modela creencias sobre el oponente con media móvil exponencial
- Demuestra que las dinámicas de aprendizaje se acoplan de formas no abordadas por MARL estándar

## Relación con otros conceptos
- [[concepts/aprendiz-q-learning-cpt|agente-humano-aprendiz-con-preferencias]]
- [[concepts/teoria-de-las-perspectivas-en-dinamica-multiagente|teoria-de-las-perspectivas-en-dinamica-multiagente]]

## Fuentes relacionadas
- [[sources/01-19-human-ai-agent-dynamics]]

## Preguntas abiertas
- (pendiente de desarrollo)
