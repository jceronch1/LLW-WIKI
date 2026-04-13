# 01 - 19_human_AI_agent_dynamics

## Resumen
El documento investiga la dinámica de las interacciones no cooperativas entre agentes de Inteligencia Artificial (IA) y tomadores de decisiones humanos en entornos estratégicos. Para lograr un modelado fiel, los agentes humanos se representan mediante la Teoría de las Perspectivas (Prospect Theory, PT), que incorpora heurísticas cognitivas como la dependencia de referencia y la aversión a la pérdida, mientras que los agentes de IA se modelan mediante la maximización de la Utilidad Esperada (Expected Utility, EU).

El estudio ejecuta simulaciones numéricas extensas en una suite de 7 juegos de matriz (5 clásicos y 2 anómalos) utilizando tres tipos de agentes: IA (EU), Humanos Conscientes (AH, con conocimiento completo) y Agentes de Perspectiva de Aprendizaje (LH, que usan Q-learning con transformaciones CPT). Se exploran los comportamientos emergentes en poblaciones mixtas bajo diferentes modelos de puntos de referencia adaptativos (EMA, V-Based, EMAOR).

Los resultados demuestran que los agentes con preferencias PT frecuentemente se desvían de la teoría clásica, encontrando cuencas de atracción mixtas subóptimas. Se observaron anomalías significativas, como la cooperación inesperada en el Dilema del Prisionero, políticas de proporción 9:1 en la Batalla de los Sexos, y desviaciones extremas en el Juego de la Moneda. Además, se verifican patologías de no existencia de equilibrio en juegos diseñados para tal fin (Ochs, Crawford). El trabajo concluye que las desviaciones conductuales motivadas por PT no siempre se correlacionan con cambios en las recompensas recibidas, y subraya la necesidad de modelar los sesgos humanos para la integración segura de la IA en la sociedad.

## Datos clave
- **Autores:** Dylan Waldner, Vyacheslav Kungurtsev, Mitchelle Ashimosi
- **Fecha de publicación:** 19 de marzo de 2026
- **Identificador:** arXiv:2603.16916v1 [cs.GT]
- **Parámetros CPT empíricos utilizados:** α = β = 0.88, λ = 2.25, γ = 0.61, δ = 0.69
- **Parámetros de simulación:** Tasa de aprendizaje α = 0.01; Exploración ε inicial 0.3, final 0.01 (decaimiento 0.995); Actualización de creencias y referencia λ = 0.95; Umbral de patología τ = 0.1; Temperatura Softmax T = 1.3
- **Duración de simulaciones:** 50,000 pasos por ejecución; 500 episodios por experimento
- **Tipos de agentes modelados:** IA (Maximizadora de Utilidad Esperada), AH (Humano Consciente), LH (Humano Aprendiz)
- **Modelos de punto de referencia:** Fijo, EMA (Expectativas Adaptativas), V-Based (Basado en Valor), EMAOR (Comparación Social)

## Temas principales
1. Modelado de agentes heterogéneos: Teoría de las Perspectivas (PT/CPT) para humanos vs. Utilidad Esperada (EU) para IA.
2. Aprendizaje por Refuerzo de Nash (Nash RL) y Q-learning modificado para preferencias CPT.
3. Equilibrio en Creencias de PT (PT-EB) y patologías de no existencia de equilibrio por violación del axioma de independencia.
4. Dinámicas de puntos de referencia adaptativos y su impacto en la toma de decisiones estratégicas.
5. Análisis empírico de comportamientos emergentes y anomalías en juegos clásicos (Dilema del Prisionero, Moneda, Caza del Ciervo, Batalla de los Sexos, Pollo).
6. Verificación de patologías teóricas en juegos anómalos (Juego de Ochs, Contraejemplo de Crawford).
7. Implicaciones prácticas en dominios críticos: trading algorítmico, vehículos autónomos, ciberseguridad y asignación de recursos.

## Actores y entidades mencionadas
- Dylan Waldner, Vyacheslav Kungurtsev, Mitchelle Ashimosi (Autores)
- Kahneman y Tversky (Creadores de la Teoría de las Perspectivas)
- Leclerc (Investigador fundamental de PT en juegos no cooperativos)
- Crawford (Autor del contraejemplo de equilibrio sin independencia)
- Ochs (Autor del juego patológico para PT)
- Keskin, Le Cadre, Phade, Anantharam, Borkar (Investigadores citados en trabajos previos)
- arXiv (Repositorio de preprints)

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/teoria-de-juegos|teoría-de-juegos]]
- [[concepts/teoria-de-las-perspectivas|teoría-de-las-perspectivas]]
- [[concepts/utilidad-esperada|utilidad-esperada]]
- [[concepts/aprendizaje-por-refuerzo|aprendizaje-por-refuerzo]]
- [[concepts/equilibrio-de-nash|equilibrio-de-nash]]
- [[concepts/seguridad-de-la-ia|seguridad-de-la-ia]]
- [[concepts/vehiculos-autonomos|vehículos-autónomos]]
- [[concepts/ciberseguridad|ciberseguridad]]
- [[concepts/trading-algoritmico|trading-algorítmico]]

## Citas textuales relevantes
> "Los agentes humanos se modelan de manera más fiel al estado del arte utilizando preferencias de la Teoría de las Perspectivas (Prospect Theory, PT), la cual incorpora heurísticas cognitivas conocidas como la dependencia de referencia y una mayor aversión a las pérdidas en relación con las ganancias relativas."

> "Introducir PT en juegos Nash puede hacer que el equilibrio tradicional sea patológico (sin existencia de equilibrio) debido a que las no linealidades rompen la propiedad 'betweenness' de la EU, creando no convexidades."

> "En el juego único, los agentes LH (aprendizaje humano) exhibieron un comportamiento inesperado e interesante contra agentes de aprendizaje en tipos de referencia EMA y EMAOR: convergieron a una política mixta subóptima de proporción 9:1, cediendo la mayor parte de la recompensa, pero no toda."

> "Las desviaciones conductuales no se correlacionaron necesariamente con cambios en la recompensa recibida, por lo que las conclusiones más amplias sobre el efecto de las preferencias PT en resultados competitivos no son claras."

> "Queda como pregunta abierta el comportamiento de la transformación CPT en juegos AH vs. LH respecto al agente LH. En casi todas las ejecuciones, el agente LH dominó la magnitud L2 cuando se enfrentó a AH. A pesar de esta métrica explosiva, su comportamiento fue poco notable."

## Notas
- La fecha del documento (2026) y el identificador arXiv sugieren un contexto de publicación futurista o un posible error tipográfico en el *paper* original; no obstante, se refleja fielmente según la fuente.
- El documento aborda una brecha crítica en la literatura: la escasez de estudios sobre interacciones repetidas entre agentes heterogéneos (PT vs. EU) en entornos no cooperativos.
- Se observó una posible desventaja competitiva sistemática en los agentes LH (Humanos Aprendices), aunque los autores mantienen esto como una pregunta abierta.
- El trabajo futuro propuesto incluye análisis de teoría de juegos evolutiva y diseño de mecanismos, alineados con las preocupaciones de seguridad de la IA frente a sesgos cognitivos humanos.