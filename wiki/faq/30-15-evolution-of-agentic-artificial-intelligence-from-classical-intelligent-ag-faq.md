# FAQ: 30 - 15 - Evolution of Agentic Artificial Intelligence From Classical Intelligent Agents to LLM-Based Autonomous Systems

## ¿Qué es la Inteligencia Artificial Agentic (Agentic AI) y cómo ha evolucionado hasta los sistemas actuales?
La Inteligencia Artificial Agentic (IA Agentic) se refiere a sistemas de IA capaces de planificar, realizar acciones y adaptar su comportamiento para alcanzar objetivos con una supervisión humana limitada. Su evolución se divide en tres eras principales:
1. **Era I - IA Simbólica y agentes basados en planificación:** Sistemas tempranos que usaban representaciones simbólicas y razonamiento basado en reglas. Eran interpretables pero frágiles en entornos complejos del mundo real.
2. **Era II - IA Estadística y agentes basados en aprendizaje:** La aparición del aprendizaje automático y el aprendizaje por refuerzo (RL) permitió agentes más adaptables, aunque su entrenamiento era costoso, exigente en datos y específico de cada dominio.
3. **Era III - Modelos fundacionales y agencia centrada en el lenguaje:** Los Modelos de Lenguaje Grande (LLMs) transformaron el campo al permitir que el lenguaje natural sirva como interfaz general para objetivos, planes, herramientas y entornos. Los LLMs actuales pueden interpretar instrucciones, descomponer tareas y usar herramientas, dando lugar a los sistemas autónomos modernos.

## ¿Cuáles son las diferencias clave entre los sistemas de IA tradicionales y los sistemas de IA Agentic?
Según el documento, las diferencias fundamentales entre la IA tradicional y la IA Agentic se resumen en seis dimensiones:
*   **Tipo de salida:** La IA tradicional produce una única predicción o clasificación, mientras que la Agentic ejecuta acciones multi-paso orientadas a un objetivo.
*   **Autonomía:** Mínima en la tradicional frente a de moderada a alta en la Agentic.
*   **Memoria:** La tradicional no tiene memoria persistente; la Agentic utiliza memoria externa estructurada.
*   **Uso de herramientas:** No integrado en la tradicional frente a capacidades integradas de llamada a herramientas (APIs) en la Agentic.
*   **Planificación:** No es explícita en la tradicional frente a una planificación explícita de múltiples pasos en la Agentic.
*   **Perfil de riesgo:** La tradicional presenta errores a nivel de salida (output), mientras que la Agentic introduce riesgos a nivel de sistema debido a las acciones que ejecuta.

## ¿Cuáles son los componentes fundamentales de la arquitectura de un sistema de IA Agentic moderno basado en LLMs?
La arquitectura moderna de IA Agentic no es solo un modelo, sino un sistema estructurado que sigue un flujo de trabajo iterativo (pensar-actuar-observar-reflexionar). Sus componentes principales son:
1.  **Interpretación de objetivos:** Convertir la intención del usuario en objetivos claros.
2.  **Planificación:** Crear o refinar un plan de múltiples pasos.
3.  **Uso de herramientas (Tool use):** Invocar APIs, motores de búsqueda, ejecución de código o bases de datos.
4.  **Memoria y recuperación:** Almacenar y buscar contexto relevante e historial de tareas.
5.  **Reflexión y autocorrección:** Aprender del feedback y mejorar sin necesidad de reentrenamiento (ej. Reflexion).
6.  **Monitoreo de ejecución:** Detectar errores, revisar planes y continuar o escalar.

## ¿Qué patrones arquitectónicos existen para los sistemas de IA Agentic?
El documento clasifica las arquitecturas modernas en tres categorías principales:
*   **Agentes únicos y arquitecturas modulares:** Un controlador LLM centralizado gestiona la interpretación, planificación y ejecución, apoyado en componentes especializados (ej. solvers simbólicos, calculadoras). El marco MRKL es un ejemplo de este enfoque neuro-simbólico híbrido.
*   **Arquitecturas colaborativas multi-agente:** Dividen responsabilidades entre agentes especializados (planificador, codificador, crítico) que colaboran mediante protocolos de comunicación estructurados. Ejemplos incluyen AutoGen (conversaciones coordinadas) y SWE-agent (interacción directa con entornos de software).
*   **Agentes autónomos generativos e incorporados (Embodied):** Operan en entornos interactivos o simulados, mantienen memoria a largo plazo, reflexionan y acumulan habilidades. Ejemplos incluyen los Agentes Generativos para simulaciones sociales y Voyager para entornos abiertos como Minecraft.

## ¿Cómo se evalúa la eficacia y seguridad de un sistema de IA Agentic?
La evaluación de la IA Agentic es más compleja que la de modelos de un solo turno, ya que depende de la ejecución de múltiples pasos y la interacción con herramientas. Las dimensiones centrales de evaluación son:
*   **Éxito de la tarea (Task success):** Precisión en la consecución del objetivo (tasa de éxito).
*   **Eficiencia:** Utilización de recursos (pasos, tiempo, llamadas a API, costo).
*   **Robustez:** Capacidad de recuperación ante errores (tasa de recuperación).
*   **Fundamentación (Groundedness):** Fiabilidad factual (soporte de citas/evidencia).
*   **Seguridad:** Cumplimiento de políticas (tasa de violación).
*   **Supervisión humana:** Necesidad de intervención (frecuencia de aprobación).

## ¿Qué riesgos específicos introduce la IA Agentic y cómo se pueden mitigar?
Al poder tomar acciones e interactuar con sistemas externos, la IA Agentic introduce riesgos más allá de los chatbots tradicionales:
*   **Riesgos:** Acciones alucinadas (comandos inseguros), inyección de prompts o manipulación de herramientas, exceso de autonomía (actuar fuera del alcance previsto) y brechas de responsabilidad (falta de claridad sobre quién es culpable si el flujo causa daño).
*   **Controles prácticos:** Permisos de herramientas y principio de mínimo privilegio, aprobación humana en el bucle (human-in-the-loop) para acciones de alto impacto, auditoría y trazabilidad de decisiones, verificación mediante recuperación (RAG) y ejecución en entornos aislados (sandboxing) para código y acciones de sistema.

## ¿Cuáles son los dominios de aplicación principales de la IA Agentic?
Las aplicaciones se agrupan en dos grandes dominios:
1.  **Automatización de tareas cognitivas y empresariales:** Agentes que operan en ecosistemas digitales para automatizar revisiones bibliográficas, síntesis de investigación, generación y prueba de código (ej. SWE-agent), orquestación de flujos de trabajo y operaciones empresariales. Su principal contribución es la eficiencia, pero su riesgo principal son las acciones incorrectas a escala sin verificación.
2.  **Simulación, entrenamiento y autonomía incorporada (Embodied):** Agentes que operan en entornos interactivos que requieren razonamiento a largo plazo y comportamiento adaptativo, como el modelado de dinámicas sociales (Agentes Generativos) o la exploración y acumulación de habilidades en entornos abiertos (Voyager). Su desafío principal es la seguridad y la incertidumbre ambiental en el mundo real.

## Fuentes
- [[sources/30-15-evolution-of-agentic-artificial-intelligence-from-classical-intelligent-ag]]