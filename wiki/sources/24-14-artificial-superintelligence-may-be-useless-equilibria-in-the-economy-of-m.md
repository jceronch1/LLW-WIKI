# 24 - 14 - Artificial Superintelligence May be Useless Equilibria in the Economy of Multiple AI Agents

## Resumen
Este documento investiga las interacciones económicas y los equilibrios en una economía compuesta por múltiples agentes, incluyendo tanto humanos como agentes de Inteligencia Artificial (IA). A diferencia de estudios anteriores que se centran en beneficios a corto plazo, los autores utilizan un modelo basado en la distribución estacionaria de cadenas de Markov para evaluar la utilidad asintótica a largo plazo generada por las actividades económicas de compra y venta de productos o servicios.

Para el caso de dos agentes, el estudio caracteriza exhaustivamente todos los equilibrios económicos posibles. Un hallazgo contraintuitivo y central es que, a menos que un agente pueda al menos duplicar (y no solo aumentar) su utilidad marginal al comprar los productos del otro agente, no se producirá ninguna transacción en el equilibrio. Dependiendo de si se cumple esta condición de "duplicación", pueden surgir equilibrios de no adopción, adopción parcial bilateral, adopción completa bilateral o adopción completa unilateral.

Al extender el modelo a tres o más agentes, los resultados revelan dinámicas aún más complejas. Se demuestra que en ciertos equilibrios, los agentes de IA "más poderosos" (superinteligencia artificial) aportan cero utilidad a los agentes "menos capaces" o humanos. Esto ocurre porque la estructura de la red de flujo de moneda impide que los agentes menos capaces se beneficien de los más poderosos en un estado estacionario.

En conclusión, el documento subraya que la adopción de tecnologías de IA no siempre es la decisión óptima. Los beneficios económicos de adoptar agentes de IA dependen no solo de sus capacidades o productividades inmediatas, sino fundamentalmente de la estructura de la red productor-consumidor y de cómo esta afecta la distribución estacionaria de la riqueza a largo plazo.

## Datos clave
- **Fecha de publicación**: 3 de marzo de 2026.
- **Autores**: Huan Cai, Ziqing Lu, Catherine Xu, Weiyu Xu, Jie Zheng (listados alfabéticamente).
- **Modelo matemático**: Matriz de gasto como matriz de transición de cadenas de Markov y matriz de utilidad.
- **Umbral crítico de adopción**: La utilidad marginal debe al menos duplicarse ($b \ge 2a$ o $c \ge 2d$ en el modelo de dos agentes) para que exista un equilibrio con comercio; de lo contrario, el único equilibrio es el de no adopción ($p=q=0$).
- **Tipos de equilibrio para dos agentes**: Sin adopción, adopción parcial bilateral, adopción completa bilateral y adopción completa unilateral.
- **Paradoja de la superinteligencia**: Los agentes "más poderosos" pueden aportar cero utilidad a los agentes "menos capaces" en los equilibrios económicos.
- **Optimización**: El problema de maximización de la utilidad asintótica se puede resolver mediante programación lineal realizando una búsqueda unidimensional sobre la variable de distribución estacionaria.

## Temas principales
1. Modelado de economías multi-agente mediante cadenas de Markov.
2. Análisis de equilibrio de Nash en juegos de intercambio económico.
3. Utilidad asintótica a largo plazo frente a beneficios miopes a corto plazo.
4. Condiciones matemáticas para la adopción de tecnologías de IA.
5. Impacto de la estructura de red productor-consumidor en la utilidad estacionaria.
6. Limitaciones de la superinteligencia artificial en economías de mercado cerradas.

## Actores y entidades mencionadas
- **Cornell College** (Departamento de Economía y Empresa)
- **University of Iowa** (Programa de Ciencias Matemáticas y Computacionales Aplicadas; Departamento de Ingeniería Eléctrica y Computacional)
- **Iowa City Math Circle and Club**
- **Shandong University** (Centro de Investigación Económica)
- **Agentes humanos**
- **Agentes de Inteligencia Artificial (IA)**
- **Agentes de Inteligencia Artificial Superinteligente** ("más poderosos")

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/superinteligencia-artificial|superinteligencia-artificial]]
- [[concepts/equilibrio-de-nash|equilibrio-de-nash]]
- [[concepts/cadenas-de-markov|cadenas-de-markov]]
- [[concepts/teoria-de-juegos|teoria-de-juegos]]
- [[concepts/economia-computacional|economia-computacional]]
- [[concepts/utilidad-marginal|utilidad-marginal]]
- [[concepts/distribucion-estacionaria|distribucion-estacionaria]]

## Citas textuales relevantes
> "Interestingly, we show that unless each agent can at least double (not merely increase) its marginal utility by purchasing the other agent’s products/services, purchasing the other agent’s products/services will not happen in any economic equilibrium."

> "We find that in some equilibria, the “more powerful” AI agents contribute zero utility to “less capable” agents."

> "On the surface, it seems always beneficial for an AI agent or a human to use the help of other powerful AI agents and to adopt AI technologies for boosting productivity or for increasing its own obtained utility. But a fundamental question remains: is it always optimal to adopt AI agents when they are available?"

> "Our results show that the benefits of adopting AI agents depend not only on their capabilities/productivities but also on the graph structure of the producer-consumer network consisting of human and AI agents as nodes."

> "One particular interesting result is that if the artificial superintelligence (the “more powerful”) agents are more powerful than the “less capable” AI agents and human agents, in any economic equilibrium, the artificial superintelligence agents will contribute no economic benefits to the “less capable” AI agents or human agents."

## Notas
- El modelo asume que la cantidad total de moneda en el sistema se conserva a lo largo del tiempo y que los agentes no cambian sus patrones de gasto relativos a medida que evoluciona el tiempo.
- La utilidad a largo plazo se calcula sobre la base de la distribución estacionaria de la moneda, lo que significa que las decisiones miope (comprar al vendedor que ofrece la mayor utilidad por dólar inmediato) no siempre son óptimas.
- Los autores sugieren que esta metodología puede aplicarse a otras áreas como el comercio internacional, políticas arancelarias, sanciones económicas y políticas de compra local.
- El estudio se centra en la utilidad asintótica por episodio; los autores señalan como trabajo futuro la consideración de utilidades descontadas que equilibren beneficios a corto y largo plazo, así como escenarios donde la cantidad total de moneda aumenta.