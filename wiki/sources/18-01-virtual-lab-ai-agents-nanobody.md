# 18 - 01_virtual_lab_AI_agents_nanobody

## Resumen

El documento presenta un editorial que describe el "Virtual Lab", un marco de investigación biomédica impulsado por inteligencia artificial que utiliza agentes de Grandes Modelos de Lenguaje (LLM) organizados en equipos científicos coordinados. Este sistema trasciende el uso pasivo de la IA como herramienta de predicción, posicionándola como un colaborador activo capaz de generar hipótesis, diseñar experimentos y conducir descubrimientos validados experimentalmente. La arquitectura del Virtual Lab asigna roles específicos a cada agente: un investigador principal establece agendas y sintetiza estrategias, especialistas de dominio (inmunólogos, biólogos computacionales) aportan razonamiento experto, y un agente crítico científico examina supuestos e identifica errores lógicos y de codificación.

Como demostración de principio, los investigadores aplicaron este sistema al diseño de nanobodies (nanocuerpos) contra variantes emergentes de SARS-CoV-2, específicamente JN.1 y KP.3, descendientes del linaje Ómicron que presentan mutaciones en el dominio de unión al receptor de la proteína spike. El laboratorio virtual construyó autónomamente un pipeline computacional sofisticado que integró el modelo de lenguaje proteico ESM para evaluar plausibilidad evolutiva, AlphaFold-Multimer para modelado estructural y Rosetta para optimización energética, generando 92 candidatos de nanobodies. La intervención humana se limitó deliberadamente a supervisión de alto nivel y experimentación de laboratorio, representando aproximadamente solo el 1% del contenido total generado.

Los resultados experimentales validaron la eficacia del enfoque: más del 90% de los candidatos se expresaron como proteínas solubles en *Escherichia coli*, y ensayos de unión identificaron mutantes con actividades novedosas. Notablemente, un mutante Nb21 (con sustituciones I77V, L59E, Q87A y R37Q) adquirió capacidad de unión tanto a JN.1 como a KP.3 manteniendo afinidad por la cepa ancestral Wuhan, mientras que un mutante Ty1 (V32F, G59D, N54S y F32S) ganó unión a JN.1 donde el parental carecía de actividad. Estos hallazgos demuestran que los equipos de agentes de IA estructurados pueden generar descubrimientos biomédicos auténticos y experimentalmente validados.

El estudio tiene implicaciones profundas para la filosofía de la ciencia y la práctica investigativa. Al comprimir timelines tradicionales de meses a semanas y reducir barreras para instituciones con recursos limitados, el Virtual Lab sugiere un camino hacia la democratización del diseño terapéutico avanzado. Sin embargo, los autores reconocen limitaciones importantes, incluyendo los cortes de conocimiento de los LLMs, la dependencia del diseño de instrucciones y la necesidad de supervisión humana rigurosa para mitigar riesgos de generación de contenido erróneo. La visión prospectiva incluye la convergencia con computación cuántica (Quantum AI) para crear laboratorios virtuales aún más rápidos y precisos, extendiendo aplicaciones a oncología, modelos animales y consultas médicas especializadas.

## Datos clave

- **Publicación**: International Journal of Biological Sciences, Volumen 22, Número 2, páginas 618-621, DOI: 10.7150/ijbs.126093
- **Fechas**: Recibido 30 de septiembre de 2025; Aceptado 27 de octubre de 2025; Publicado 1 de enero de 2026
- **Autores**: Hakjin Kim, Taeho Kwon, Sun-Uk Kim, Seon-Kyu Kim
- **Instituciones**: Korea Research Institute of Bioscience and Biotechnology (KRIBB), Korea National University of Science and Technology (UST), Quantum AI Bio Research Laboratory (KJQI-JQL)
- **Candidatos generados**: 92 nanobodies diseñados completamente *in silico* por agentes de IA
- **Tasa de expresión**: Más del 90% de los candidatos expresados como proteínas solubles en *E. coli*
- **Intervención humana**: Aproximadamente 1% del contenido total generado
- **Variantes objetivo**: SARS-CoV-2 JN.1 y KP.3 (linaje Ómicron)
- **Mutaciones Nb21 exitosas**: I77V, L59E, Q87A, R37Q (ganó unión a JN.1 y KP.3, mantuvo afinidad por Wuhan)
- **Mutaciones Ty1 exitosas**: V32F, G59D, N54S, F32S (ganó unión a JN.1, mejoró reconocimiento de Wuhan)
- **Nanobodies de partida**: Ty1, H11-D4, Nb21, VHH-72
- **Herramientas computacionales**: ESM (Evolutionary-scale modeling), AlphaFold-Multimer, Rosetta

## Temas principales

1. Arquitectura multi-agente de IA para investigación científica autónoma
2. Diseño y optimización computacional de nanobodies antivirales
3. Respuesta terapéutica rápida a variantes emergentes de SARS-CoV-2
4. Validación experimental de predicciones generadas por IA
5. Democratización del acceso a estrategias avanzadas de diseño biomolecular
6. Filosofía de la ciencia: IA como colaborador activo vs herramienta pasiva
7. Limitaciones y riesgos de sistemas autónomos de investigación
8. Convergencia de inteligencia artificial y computación cuántica (Quantum AI)
9. Aplicaciones potenciales en oncología y medicina personalizada

## Actores y entidades mencionadas

- **Hakjin Kim**, **Taeho Kwon**, **Sun-Uk Kim**, **Seon-Kyu Kim** (autores y correspondencia)
- **Korea Research Institute of Bioscience and Biotechnology (KRIBB)**
- **Korea National University of Science and Technology (UST)**
- **Quantum AI Bio Research Laboratory (KJQI-JQL)**
- **In Quantio, Gene on Biotech** (Daejeon)
- **Futuristic Animal Resource and Research Center** (Cheongju)
- **Genomic Medicine Research Center** (Daejeon)
- **KRIBB Research Initiative Program** (financiación: JHM0022511, KGM4252533, KGM5192531)
- **National Research Foundation (NRF)** de Corea (MSIT)
- **National Research Council of Science & Technology (NST)** (Corea)
- **Korea Basic Science Institute**
- **Korea Joint Quantum Institute of KRISS**
- **ESM** (Evolutionary-scale modeling, Meta AI)
- **AlphaFold-Multimer** (DeepMind)
- **Rosetta** (plataforma de modelado molecular)

## Relación con otros conceptos

- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/large-language-models|large-language-models]]
- [[concepts/multi-agent-systems|multi-agent-systems]]
- [[concepts/nanobodies|nanobodies]]
- [[concepts/sars-cov-2|SARS-CoV-2]]
- [[entities/alphafold|alphaFold]]
- [[concepts/protein-design|protein-design]]
- [[concepts/biologia-computacional|biología-computacional]]
- [[concepts/terapia-antiviral|terapia-antiviral]]
- [[concepts/quantum-ai|quantum-AI]]
- [[concepts/inmunoterapia|inmunoterapia]]
- [[concepts/descubrimiento-de-farmacos|descubrimiento-de-fármacos]]
- [[concepts/variantes-omicron|variantes-omicron]]
- [[concepts/laboratorio-virtual|laboratorio-virtual]]

## Citas textuales relevantes

> "The Virtual Lab exemplifies this transformation, assembling large language model (LLM) agents into coordinated scientific teams functioning as investigators, specialists, and critics."

> "Human involvement was deliberately minimized and limited to providing high-level oversight and performing laboratory experiments, accounting for only approximately 1% of the total content generated."

> "An Nb21 mutant carrying the substitutions I77V, L59E, Q87A, and R37Q gained binding activity against both JN.1, and KP.3, while retaining a strong affinity for the ancestral Wuhan strain."

> "Virtual Lab reframes artificial intelligence from a passive tool to an active collaborator capable of hypothesis generation, debate, and discovery."

> "Agent teams with clearly defined specialist roles and dedicated critic agents generated coherent and biologically grounded strategies... In contrast, groups composed of generic, non-specialized agents engaged in redundant debates and often failed to converge on effective strategies."

> "As technology continues to advance, the convergence of artificial intelligence and quantum computing is expected to give rise to a new era of Quantum AI enabled biomedical research."

## Notas

Este documento es un editorial que comenta y expande los hallazgos del estudio "The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies" publicado por Swanson et al. en *Nature* (2025). El trabajo debe considerarse una prueba de concepto (proof-of-principle) más que un desarrollo terapéutico maduro. Aunque los ensayos de unión confirmaron actividad contra dominios de unión al receptor, los autores enfatizan que se requiere evaluación adicional de neutralización viral, farmacocinética, inmunogenicidad y seguridad antes de considerar aplicaciones clínicas. La mención de Quantum AI representa una visión prospectiva sobre la convergencia futura de tecnologías, no una implementación actual del estudio presentado.