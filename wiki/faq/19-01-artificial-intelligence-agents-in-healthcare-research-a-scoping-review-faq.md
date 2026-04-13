# FAQ: 19 - 01 - Artificial intelligence agents in healthcare research A scoping review

## ¿Qué define operacionalmente a un "agente de IA" en el contexto de esta revisión?

Según el marco de elegibilidad PCC (Population-Concept-Context) de esta revisión, un agente de IA se define operacionalmente como un sistema construido alrededor de un Modelo de Lenguaje Grande (LLM) que **planifica autónomamente, razona y actúa hacia una meta compleja mediante un bucle de auto-corrección**. Específicamente, debe incorporar tres componentes esenciales:

1. **Módulo de planificación**: Capacidad para descomponer tareas complejas en pasos ejecutables.
2. **Capa de memoria**: Retención de estados intermedios y contexto durante la ejecución.
3. **Ejecutor**: Capacidad para invocar herramientas externas o APIs más allá de las capacidades intrínsecas del LLM base.

Esta definición distingue a los agentes de simples sistemas de *prompt engineering*, RAG sin orquestación autónoma, o arquitecturas multi-agente basadas únicamente en reglas tradicionales. Los autores enfatizan que estos sistemas se caracterizan por su **semi-autonomía**, **conciencia de contexto** y **capacidades de aprendizaje adaptativo**, permitiéndoles interactuar dinámicamente con entornos clínicos evolutivos.

## ¿Cuáles son las principales categorías de agentes de IA identificadas y en qué se diferencian?

La revisión clasificó los 43 sistemas incluidos en tres arquetipos funcionales principales:

**1. Agentes conversacionales (8 sistemas, 18.6%)**
Diseñados para interacción directa con pacientes o fines educativos. Ejemplos incluyen simulaciones de pacientes virtuales para entrenamiento médico, apoyo en salud mental (terapia conversacional), y chatbots multilingües para educación sanitaria.

**2. Asistentes de flujo de trabajo y automatización (17 sistemas, 39.5%)**
Orientados a optimizar procesos administrativos y clínicos. Incluyen generación automatizada de registros médicos electrónicos (EHR), redacción clínica bilingüe, extracción de condiciones experimentales de bioensayos, gestión de citas y triaje (ej. *MedScrubCrew*), y desarrollo de protocolos de investigación.

**3. Agentes de soporte de decisiones multimodales (18 sistemas, 41.9%)**
Sistemas más complejos que integran múltiples fuentes de datos (imágenes, genómica, texto clínico) para asistencia diagnóstica y terapéutica. Ejemplos incluyen optimización de planes de radioterapia (*GPT-Plan*), análisis de vías oncológicas (*AI-HOPE*), diagnóstico de enfermedades raras mediante consenso multi-agente, y sistemas de análisis de microbioma para predicción de Alzheimer (*ADAM-1*).

## ¿Qué mecanismos técnicos específicos utilizan estos agentes para mejorar su precisión y confiabilidad?

Los sistemas revisados emplean dos mecanismos centrales para el *grounding* (anclaje en datos verificables) y el refinamiento:

**Uso de herramientas externas (*external tool use*)**:
- **RAG (Generación Aumentada por Recuperación)**: Casi ubicua en los sistemas, sirve como memoria externa utilizando grafos de conocimiento biomédico actualizados dinámicamente, bases de datos vectoriales con guías clínicas, o APIs especializadas (OncoKB, DrugBank, KEGG, RxNorm).
- **Ejecución de código**: Sistemas como *ESCARGOT* y *GeneAgent* generan y ejecutan código Python autónomamente para cálculos complejos o análisis de datos.
- **Text-to-SQL**: Para consultas a bases de datos estructuradas preclínicas.
- **Modelos especializados**: Integración con herramientas como MedSAM para segmentación de imágenes médicas.

**Auto-corrección iterativa**:
- **Debate multi-agente**: Sistemas como *MedARC* y *MAC* simulan discusiones de equipo multidisciplinario donde agentes especializados critican y refinan iterativamente las respuestas hasta alcanzar consenso.
- **Bucles de auto-depuración**: *ESCARGOT* incorpora bucles de auto-depuración cuando el código generado falla.
- **Verificación basada en reglas**: *MEDIC* utiliza guardrails de seguridad determinísticos para detener sugerencias si los parámetros entran en conflicto.
- **Validación continua**: *GIVE* (*Grouped Iterative Validation*) utiliza chequeos de similitud semántica para asegurar consistencia factual en la minería de literatura.

## ¿Cuál es el estado actual de la evidencia clínica sobre eficacia y seguridad de estos sistemas?

La revisión identificó una **brecha crítica traslacional**: la evidencia se basa predominantemente en entornos simulados o estudios de laboratorio, con escasos pilotos clínicos o despliegues en el mundo real. Específicamente:

- **Temporalidad**: 36 de 43 estudios (83.7%) fueron publicados en 2025, indicando un campo muy reciente.
- **Configuración de evaluación**: La mayoría utilizan datos clínicos retrospectivos, casos de pacientes simulados o benchmarks estandarizados (PubMedQA, BioASQ) en lugar de ensayos prospectivos.
- **Resultados reportados**: Enfoque casi exclusivo en medidas de proceso (eficiencia) y precisión diagnóstica. Los **resultados clínicos a largo plazo y endpoints de seguridad fueron raramente abordados**.
- **Validación**: Evaluaciones manuales frecuentemente involucran muestras pequeñas y carecen de clínicos practicantes como evaluadores.

Los autores concluyen que la eficacia clínica real permanece en gran medida no confirmada, requiriendo estudios de validación rigurosos antes de una adopción generalizada.

## ¿Cuáles son los principales riesgos y barreras para la implementación clínica identificados?

La revisión documentó múltiples limitaciones críticas:

**Seguridad y confiabilidad**:
- **Alucinaciones persistentes**: A pesar de mecanismos de RAG y auto-corrección, los LLMs continúan produciendo errores factuales e inconsistencias, requiriendo supervisión humana obligatoria.
- **"Over-flagging"**: Tendencia en sistemas de diagnóstico microbiológico a marcar excesivamente mecanismos de resistencia sospechados, generando pruebas de confirmación innecesarias, retrasos y aumento de costos.
- **Sesgos operacionales**: Tendencia observada a sobrestimar la urgencia del paciente comparado con clínicos humanos.

**Barreras técnicas y operativas**:
- **Latencia**: El procesamiento puede tomar hasta 4.7 segundos por consulta, aceptable solo para usos rutinarios, no para emergencias.
- **Integración con EHR**: Pobre usabilidad, interfaces complejas e incapacidad para integración *seamless* con sistemas existentes, resultando en bajas tasas de adopción.
- **Costos computacionales**: Overhead sustancial asociado con arquitecturas multi-agente complejas.

**Privacidad y regulación**:
- **Soberanía de datos**: LLMs basados en nube frecuentemente son inadecuados para datos sensibles de pacientes en regiones con leyes estrictas.
- **Marco regulatorio**: Ausencia de aprobación regulatoria explícita para muchos agentes en diagnóstico clínico y estándares aún en desarrollo para sistemas adaptativos.

## ¿Qué diferencias existen entre los sistemas multi-agente y los de agente único?

La revisión distingue claramente ambas arquitecturas:

**Sistemas Multi-Agente**:
- **Mecanismo**: Emplean múltiples agentes especializados que colaboran mediante debate estructurado, simulando equipos multidisciplinarios humanos.
- **Ventajas**: Mayor precisión en diagnóstico complejo mediante refinamiento iterativo y consenso; capacidad para descomponer problemas complejos en sub-tareas especializadas.
- **Ejemplos**: *MedARC* (debate multi-agente para razonamiento médico), *GPT-Plan* (optimización de radioterapia con validación cruzada), *BioResearcher* (orquestación de agentes en investigación biomédica), y sistemas de triaje de emergencias que simulan personal médico.

**Sistemas Single-Agente**:
- **Mecanismo**: Un único agente que demuestra agencia mediante uso sofisticado de herramientas y ejecución en bucle cerrado.
- **Características**: Mayor simplicidad arquitectónica pero capacidad limitada de validación cruzada interna.
- **Ejemplos**: *ESCARGOT* (generación y auto-depuración de código), *GeneAgent* (interacción con 18 bases de datos biológicas vía APIs con pipeline de auto-verificación), y *CARE-RAG* (adaptación de estrategia de recuperación basada en intención de consulta).

Los autores notan que los sistemas multi-agente, aunque más complejos computacionalmente, demuestran superioridad en tareas que requieren razonamiento colaborativo y validación cruzada.

## ¿Qué recomendaciones hacen los autores para la investigación y desarrollo futuro?

Los autores priorizan siete áreas para cerrar la brecha entre prototipos y herramientas clínicamente integradas:

1. **Ensayos clínicos rigurosos**: Priorizar estudios prospectivos en entornos operacionales reales sobre evaluaciones simuladas, con endpoints de seguridad y eficacia clínica a largo plazo.

2. **Marcos de evaluación armonizados**: Establecer métricas estandarizadas para usabilidad, seguridad del paciente y efectividad clínica comparables entre sistemas.

3. **Gobernanza ética y regulatoria**: Desarrollar modelos de responsabilidad (*liability*) claros para acciones autónomas en entornos de alto riesgo; establecer estándares para sistemas adaptativos.

4. **Integración seamless**: Desarrollar APIs estandarizadas para interoperabilidad con EHR y flujos de trabajo clínicos existentes, reduciendo la carga cognitiva del clínico.

5. **Mitigación de alucinaciones**: Implementar "Verifier Agents" dedicados a auditar razonamiento y hacer cumplir políticas de seguridad determinísticas antes de la ejecución.

6. **Tecnologías emergentes**: Explorar agentes de monitoreo continuo con datos de wearables, gemelos digitales (*digital twins*) para simulación de tratamientos, y sistemas de Explainable AI para transparencia.

7. **Infraestructura de privacidad**: Promover el desarrollo de LLMs open-source desplegados localmente (*on-premises*) para mitigar riesgos de transferencia de datos sensibles.

## Fuentes
- [[sources/19-01-artificial-intelligence-agents-in-healthcare-research-a-scoping-review]]