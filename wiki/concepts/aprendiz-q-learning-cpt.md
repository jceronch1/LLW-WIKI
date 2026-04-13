# agente-humano-aprendiz-con-preferencias

## Definición
Arquetipo de agente en simulaciones de teoría de juegos que utiliza Q-learning estándar sobre recompensas no transformadas, pero aplica la transformación de la Teoría Cumulativa de las Perspectivas (CPT) a los valores Q durante la selección de su política. Representa a humanos que aprenden por ensayo y error con sesgos cognitivos, mostrando frecuentemente desventajas competitivas y convergencia a cuencas de estrategia mixta subóptimas frente a agentes de IA.

## Ideas clave
- Combina Q-learning estándar con toma de decisiones CPT en la política
- Actualiza creencias y puntos de referencia dinámicamente
- Tiende a converger a estrategias mixtas subóptimas por sensibilidad disminuida
- Experimenta picos en la magnitud de transformación CPT frente a agentes conscientes

## Relación con otros conceptos
- [[concepts/teoria-de-las-perspectivas-en-dinamica-multiagente|teoria-de-las-perspectivas-en-dinamica-multiagente]]
- [[concepts/punto-de-referencia-adaptativo-en-teoria-de-juegos|punto-de-referencia-adaptativo-en-teoria-de-juegos]]

## Fuentes relacionadas
- [[sources/01-19-human-ai-agent-dynamics]]

## Preguntas abiertas
- (pendiente de desarrollo)
