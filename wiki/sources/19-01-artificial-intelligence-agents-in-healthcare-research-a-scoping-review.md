# 19 - 01 - Artificial intelligence agents in healthcare research A scoping review

## Resumen

Los agentes de Inteligencia Artificial (IA) están transformando rápidamente la prestación de servicios de salud, permitiendo soporte de decisiones en tiempo real e interacciones sofisticadas con pacientes a escala. Esta revisión de alcance (*scoping review*) siguiendo las directrices PRISMA-ScR analizó la literatura científica desde enero de 2015 hasta el 7 de diciembre de 2025, identificando 1,070 registros de los cuales 43 estudios fueron finalmente incluidos. Los resultados revelan un campo en explosiva expansión: 36 de los 43 estudios (83.7%) fueron publicados únicamente en el año 2025, evidenciando la velocidad sin precedentes de la innovación técnica.

El análisis identificó tres categorías funcionales principales de sistemas agenticos: 8 agentes conversacionales (18.6%), 17 asistentes de flujo de trabajo o automatización (39.5%), y 18 agentes de soporte de decisiones multimodales (41.9%). Los mecanismos técnicos centrales que confieren agencia incluyen el uso de herramientas externas —como generación aumentada por recuperación (RAG) o ejecución de código— para *grounding* (anclaje en datos verificables), así como mecanismos de auto-corrección iterativa —como debate multi-agente o bucles de auto-depuración— para refinamiento continuo. Sin embargo, persiste una brecha crítica entre la innovación técnica y la implementación clínica real: la evaluación predominante ocurre en entornos simulados o estudios de laboratorio, con escasos pilotos clínicos o despliegues en el mundo real.

Los resultados reportados se centran principalmente en medidas de proceso (eficiencia) y precisión diagnóstica, mientras que los resultados clínicos y endpoints de seguridad fueron raramente abordados. Los sistemas enfrentan desafíos persistentes como alucinaciones en modelos de lenguaje grandes (LLMs), "over-flagging" diagnóstico, pobre usabilidad e integración con registros electrónicos de salud (EHR), y latencias de hasta 4.7 segundos por consulta. La investigación futura debe priorizar ensayos clínicos prospectivos rigurosos y la evaluación robusta de seguridad, usabilidad y eficacia clínica antes de una adopción generalizada.

## Datos clave

- **1,070** registros identificados inicialmente en las búsquedas
- **43** estudios finalmente incluidos tras revisión de texto completo
- **52** duplicados eliminados (3 manuales + 49 vía Covidence)
- **1,018** estudios únicos sometidos a screening de títulos y abstracts
- **694** estudios excluidos en etapa de título/abstract
- **324** estudios evaluados a texto completo
- **281** estudios excluidos en evaluación de texto completo
- **36 de 43** estudios (83.7%) publicados en **2025**
- **8** agentes conversacionales identificados (18.6%)
- **17** asistentes de flujo de trabajo/automatización (39.5%)
- **18** agentes de soporte de decisiones multimodales (41.9%)
- Período de búsqueda: **Enero 2015 - 7 de diciembre de 2025**
- Fecha de publicación: **10 de febrero de 2026**
- DOI: **10.1371/journal.pone.0342182**
- Editor: **Barry L. Bentley** (Cardiff Metropolitan University, Reino Unido)
- Latencia reportada en sistemas LLM: hasta **4.7 segundos** por consulta simple

## Temas principales

1. **Definición conceptual y características de agentes de IA en salud**: Semi-autonomía, conciencia de contexto y capacidades de aprendizaje adaptativo que distinguen a los agentes de algoritmos estáticos tradicionales.

2. **Metodología de revisión de alcance (PRISMA-ScR)**: Estrategia de búsqueda en cuatro fuentes (PubMed, Web of Science, arXiv, medRxiv) con inclusión deliberada de preprints para capturar innovaciones emergentes.

3. **Categorización funcional de sistemas agenticos**: Clasificación en agentes conversacionales (interacción paciente/educación), asistentes de flujo de trabajo/automatización, y agentes de soporte de decisiones multimodales.

4. **Mecanismos técnicos centrales**: Uso de herramientas externas (RAG, APIs, ejecución de código) para *grounding*; auto-corrección iterativa mediante debate multi-agente, bucles de auto-depuración y *Chain-of-Thought*.

5. **Arquitecturas multi-agente vs. single-agente**: Sistemas colaborativos (MedARC, MAC, BioResearcher) versus agentes individuales con capacidades de auto-verificación (GeneAgent, ESCARGOT).

6. **Brechas críticas en validación clínica**: Dependencia de datos retrospectivos, casos simulados y benchmarks estandarizados; ausencia de ensayos clínicos prospectivos con resultados reales de pacientes.

7. **Desafíos de seguridad y confiabilidad**: Persistencia de alucinaciones en LLMs, errores factuales, "over-flagging" en diagnóstico microbiológico, y necesidad de supervisión humana obligatoria.

8. **Barreras de integración operativa**: Pobre usabilidad, interfaces complejas, incapacidad para integración seamless con EHR existentes, costos computacionales elevados y latencia en respuestas.

9. **Implicaciones regulatorias y éticas**: Ausencia de aprobación regulatoria explícita para muchos agentes LLM en diagnóstico clínico, restricciones de soberanía de datos, y naturaleza "caja negra" de la toma de decisiones.

10. **Direcciones futuras y evolución tecnológica**: Necesidad de ensayos clínicos rigurosos, desarrollo de *Verifier Agents*, integración de flujos multimodales, gemelos digitales y agentes de monitoreo continuo.

## Actores y entidades mencionadas

- **Basile Njei** (Yale University, autor correspondiente)
- **Yazan A. Al-Ajlouni** (Euclid University, University of Cumbria)
- **Ulrick Sidney Kanmounye** (Association of Future African Neurosurgeons)
- **Sarpong Boateng** (Yale Affiliated Hospitals Program)
- **Guy Loic Nguefang** (Texas Tech University Health Science Center)
- **Nelvis Njei** (Yale Liver Center)
- **Shadi Hamouri** (Al-Balqa Applied University)
- **Ahmad F. Al-Ajlouni** (Jordan University of Science and Technology)
- **Barry L. Bentley** (Cardiff Metropolitan University, editor)
- **Yale University** (Section of Digestive Diseases, Yale Liver Center, Yale Medicine)
- **Euclid University** (Engelhardt School of Global Health and Bioethics, Bangui)
- **University of Cumbria** (Artificial Intelligence Programme, Carlisle)
- **Ohio University Heritage College of Osteopathic Medicine**
- **Montefiore Medical Center/Einstein School of Medicine** (Bronx, New York)
- **Texas Tech University Health Science Center** (Odessa)
- **Al-Balqa Applied University** (Salt, Jordania)
- **Jordan University of Science and Technology** (Irbid)
- **Cardiff Metropolitan University** (Reino Unido)
- **PLOS One** (revista de publicación)
- **Covidence** (plataforma de gestión de revisiones sistemáticas)
- **Sistemas específicos**: MedARC, MAC (Multi-Agent Conversation), BioResearcher, PrimeGen, BiomedKAI, GPT-Plan, ADAM-1, AI-HOPE, ARMOA, MedScrubCrew, PRINCE, ESCARGOT, GeneAgent, MEDIC, CARE-RAG, GIVE

## Relación con otros conceptos

- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/sistemas-agentivos-ia|agentes-de-ia]]
- [[concepts/large-language-models|large-language-models]]
- [[concepts/revision-de-alcance|revision-de-alcance]]
- [[prisma-scr]]
- [[concepts/salud-digital|salud-digital]]
- [[concepts/soporte-de-decisiones-clinicas|soporte-de-decisiones-clinicas]]
- [[concepts/rag|RAG]]
- [[concepts/arquitecturas-multi-agente|arquitecturas-multi-agente]]
- [[concepts/auto-correccion-iterativa|auto-correccion-iterativa]]
- [[concepts/registros-electronicos-salud|registros-electronicos-salud]]
- [[concepts/alucinaciones-llm|alucinaciones-llm]]
- [[concepts/medicina-de-precision|medicina-de-precision]]
- [[concepts/bioinformatica|bioinformatica]]
- [[concepts/radioterapia|radioterapia]]
- [[concepts/salud-mental|salud-mental]]
- [[concepts/descubrimiento-de-farmacos|descubrimiento-farmacos]]
- [[concepts/ensayos-clinicos|ensayos-clinicos]]
- [[concepts/gobernanza-etica-agentiva|gobernanza-etica-ia]]
- [[concepts/interoperabilidad|interoperabilidad]]

## Citas textuales relevantes

> "Los agentes de Inteligencia Artificial (IA) están transformando rápidamente la prestación de servicios de salud, permitiendo soporte de decisiones en tiempo real e interacciones sofisticadas con pacientes a escala."

> "Sin embargo, el panorama científico de este campo multidisciplinario en rápido crecimiento permanece fragmentado, con la innovación técnica superando a la investigación traslacional y al establecimiento de marcos de gobernanza ética."

> "De los 43 estudios incluidos, 36 fueron publicados en 2025."

> "Los sistemas de IA agentica evolucionan rápidamente de marcos conceptuales a prototipos funcionales, orientados principalmente a la toma de decisiones complejas y la automatización de flujos de trabajo."

> "Persistencia de alucinaciones e inconsistencias en LLMs a pesar de RAG (Retrieval-Augmented Generation) y auto-corrección, requiriendo supervisión humana obligatoria para seguridad del paciente."

> "La investigación futura debe priorizar los ensayos clínicos y la evaluación robusta de seguridad, usabilidad y eficacia clínica antes de una adopción generalizada."

> "El componente LLM puede introducir tiempos de procesamiento de hasta 4.7 segundos por consulta simple, considerado aceptable solo para usos clínicos rutinarios, no para emergencias."

## Notas

- **Fecha de publicación**: El documento indica fecha de publicación 10 de febrero de 2026, lo cual sugiere que se trata de un manuscrito aceptado o publicado con fecha futura respecto al período de revisión (que incluye estudios hasta diciembre de 2025).

- **Inclusión de preprints**: Los autores tomaron la decisión metodológica deliberada de incluir servidores de preprints (arXiv y medRxiv) para capturar la velocidad e interdisciplinariedad sin precedentes de la investigación en IA agentica, reconociendo que la revisión por pares formal puede retrasar la disponibilidad de evidencia relevante.

- **Evaluación de calidad**: Como es característico de las revisiones de alcance (*scoping reviews*), no se realizó evaluación formal de riesgo de sesgo ni síntesis de efectos, enfocándose el estudio en mapear y cuantificar el panorama científico existente.

- **Discrepancia numérica**: Aunque el texto metodológico indica 43 estudios incluidos, la Tabla 1 presenta 44 entradas documentadas; esta inconsistencia menor no afecta los hallazgos principales pero merece notarse.

- **Limitaciones metodológicas del estudio**: Los resultados dependen principalmente de datos retrospectivos, casos de pacientes simulados o benchmarks estandarizados, con evaluaciones manuales frecuentemente basadas en muestras pequeñas y ausencia de clínicos practicantes como evaluadores. La rápida evolución tecnológica implica que algunos sistemas incluidos pueden estar ya obsoletos.

- **Aspectos éticos**: No hubo involucramiento de pacientes ni público en el diseño, conducta o reporte del estudio. Los autores declararon no tener conflictos de interés ni financiamiento específico para el trabajo.

- **Uso de IA en el manuscrito**: Las herramientas de IA fueron utilizadas únicamente para refinar lenguaje, sintaxis y formato durante la redacción, basándose en datos generados por humanos, no para búsqueda, screening, selección o extracción de datos.