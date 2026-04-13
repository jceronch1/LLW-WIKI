# FAQ: 01 - 19_human_AI_agent_dynamics

## ¿Cómo se modelan las diferencias en la toma de decisiones entre agentes de IA y humanos en este estudio?
El documento modela a los agentes de IA y humanos con frameworks económicos distintos para reflejar la irracionalidad humana empíricamente observada:
*   **Agentes de IA:** Se modelan utilizando la maximización de la **Utilidad Esperada (EU)**, el estándar clásico que asume agentes perfectamente racionales que maximizan las recompensas medias esperadas.
*   **Agentes Humanos:** Se modelan utilizando la **Teoría de las Perspectivas (PT)** y su variante acumulativa (CPT), desarrollada por Kahneman y Tversky. Este marco incorpora heurísticas cognitivas reales como la dependencia de referencia (las decisiones se basan en ganancias/pérdidas relativas a un punto de referencia), la aversión a la pérdida (las pérdidas pesan más que las ganancias equivalentes), la sensibilidad decreciente y la transformación no lineal de probabilidades (sobrepesar pequeñas probabilidades y subpesar grandes).

## ¿Qué tipos de agentes se simulan y cuáles son sus características principales?
El estudio simula tres tipos de agentes en poblaciones mixtas para observar las dinámicas emergentes:
1.  **Agente de IA (EU):** Utiliza Q-learning estándar basado en la ecuación de Bellman para maximizar la recompensa media. Su selección de acción es ε-greedy sobre los valores Q.
2.  **Humano Consciente (AH - Aware Human):** Tiene conocimiento completo de la estructura y pagos del juego. Calcula la mejor respuesta exacta utilizando la función de valor CPT (sin función de ponderación de probabilidad, ya que la mejor respuesta hace la lotería degenerada).
3.  **Humano Aprendiz (LH - Learning Human):** Representa a un humano que aprende por ensayo y error. Utiliza Q-learning sobre recompensas no transformadas, pero aplica la transformación CPT a los valores Q en el momento de seleccionar la política (maximizando el prospecto esperado en lugar de la recompensa esperada). Su estado interno incluye el punto de referencia y sus creencias sobre el oponente.

## ¿Qué papel juegan los "puntos de referencia" en la Teoría de las Perspectivas y cómo se calculan en las simulaciones?
En la Teoría de las Perspectivas, el valor de un resultado no es absoluto, sino relativo a un "punto de referencia" (ej. expectativas históricas). Un mismo resultado puede percibirse como ganancia o pérdida dependiendo de este punto. El estudio evalúa cuatro modelos dinámicos de puntos de referencia para los agentes humanos:
1.  **Fijo:** El punto de referencia es estático (típicamente 0).
2.  **EMA (Expectativas Adaptativas):** Se actualiza como una Media Móvil Exponencial de las recompensas pasadas del propio agente.
3.  **Basado en V (V-Based):** Se deriva directamente de los valores Q (para LH) o de la tabla de pagos (para AH), reflejando las expectativas de valor del agente.
4.  **EMAOR (Comparación Social):** Sigue los pagos del oponente, modelando la envidia o el impacto de ver ganar al otro.

## ¿Qué es el Equilibrio en Creencias de la Teoría de las Perspectivas (PT-EB) y por qué es necesario?
En la teoría de juegos clásica, el Equilibrio de Nash asume preferencias de Utilidad Esperada (EU). Sin embargo, las no linealidades de la CPT violan el axioma de "intermediación" (betweenness), lo que destruye la convexidad del espacio de estrategias y puede hacer que el equilibrio de Nash tradicional sea patológico o inexistente (como se demuestra en el Contraejemplo de Crawford y el Juego de Ochs). 
El **PT-EB (Equilibrio en Creencias)** resuelve este problema matemático haciendo que los agentes mezclen sobre las acciones del oponente en lugar de las propias, y tomando la envoltura convexa (convexificando el espacio) para garantizar la existencia de un equilibrio en juegos finitos simultáneos.

## ¿Qué anomalías o comportamientos emergentes inesperados se observaron en las simulaciones?
El estudio encontró múltiples desviaciones severas respecto a la teoría clásica de juegos, impulsadas por la interacción de preferencias EU y CPT:
*   **Batalla de los Sexos (Juego Único):** El agente Humano Aprendiz (LH) adoptó una política mixta subóptima de proporción 9:1 contra agentes de aprendizaje, cediendo la mayor parte de la recompensa. Esto fue causado por la sensibilidad disminuida de CPT cuando los valores Q superaban ampliamente el punto de referencia.
*   **Juego del Gallina (Chicken):** En el juego repetido, emergieron cuencas de atracción de estrategia mixta no predichas (≈0.8, 0.8 y ≈0.6, 0.6). Además, LH a veces superó a la IA, demostrando que la aversión a la pérdida no siempre genera una desventaja competitiva.
*   **Dilema del Prisionero:** En configuraciones V-based, los agentes CPT alcanzaron distancias L2 > 30, disparando sus puntos de referencia a extremos de +20 y -30, causando inestabilidad.
*   **Pico de Norma L2:** Se observó un pico masivo en la transformación CPT (norma L2 CPT/EU) cuando LH se enfrentaba a AH, aunque esto paradójicamente no se correlacionó con cambios conductuales significativos, dejando abierta la pregunta de por qué transformaciones tan grandes no alteran el comportamiento final.

## ¿Cómo se integra el Q-learning con la Teoría de las Perspectivas en el agente Humano Aprendiz (LH)?
El agente LH combina el aprendizaje por refuerzo clásico con la toma de decisiones conductuales en dos fases:
1.  **Actualización del Valor:** La tabla Q se actualiza utilizando la regla estándar de Q-learning con recompensas medias no transformadas y la ecuación de Bellman. El estado se expande para incluir contenedores (*bins*) que representan el punto de referencia normalizado del agente.
2.  **Selección de Acción (Política):** En lugar de seleccionar la acción que maximiza el valor Q (como hace la IA), LH calcula el prospecto esperado utilizando las funciones de valor y ponderación de probabilidad de la CPT sobre sus creencias del oponente. Si la diferencia entre las mejores acciones es menor a un umbral de patología (τ = 0.1), se aplica un muestreo Softmax para evitar ciclos infinitos; de lo contrario, elige la acción que maximiza el valor CPT.

## ¿Cuáles son las implicaciones prácticas de estas dinámicas para la interacción humano-IA en el mundo real?
Modelar a los humanos con Utilidad Esperada en lugar de Teoría de las Perspectivas puede llevar a predicciones erróneas sobre el comportamiento del sistema. Las implicaciones incluyen:
*   **Trading Algorítmico:** Las IA optimizan retornos esperados, mientras los humanos exhiben aversión a la pérdida, lo que puede causar el "efecto disposición" (mantener inversiones perdedoras y vender ganadoras rápido) y generar volatilidad excesiva.
*   **Vehículos Autónomos:** Los coches autónomos (EU) deben coexistir con conductores humanos que enmarcan las decisiones de forma dependiente al punto de referencia (ej. "ganar tiempo" vs. "evitar llegar tarde").
*   **Ciberseguridad:** Los atacantes humanos evalúan riesgos con sesgos CPT, creando patrones de ataque y vulnerabilidades que no surgirían en simulaciones con agentes puramente racionales.
*   **Asignación de Recursos:** Los planificadores de IA optimizan la eficiencia global, pero los usuarios humanos muestran fuerte aversión a la pérdida frente a reducciones de sus asignaciones, percibiendo recortes relativos como pérdidas absolutas.

## Fuentes
- [[sources/01-19-human-ai-agent-dynamics]]