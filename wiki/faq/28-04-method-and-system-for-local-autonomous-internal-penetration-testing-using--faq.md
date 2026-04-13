# FAQ: 28 - 04 - METHOD AND SYSTEM FOR LOCAL AUTONOMOUS INTERNAL PENETRATION TESTING USING RETRIEVAL-AUGMENTED ARTIFICIAL INTELLIGENCE AGENTS

## ¿Qué es L-PentAI y cuál es su propósito principal?
L-PentAI (Local Autonomous AI Agent for Internal Penetration Testing) es un sistema de ciberseguridad basado en Inteligencia Artificial diseñado para realizar pruebas de penetración internas de manera continua y autónoma. Su propósito es automatizar el descubrimiento de configuraciones incorrectas, vulnerabilidades y oportunidades de exfiltración de datos dentro de las redes corporativas. Opera completamente de forma local (on-premises) sin enviar datos sensibles fuera de la organización, combinando Aprendizaje por Refuerzo (RL) con Generación Aumentada por Recuperación (RAG) para mejorar la postura de seguridad evaluando constantemente las defensas internas.

## ¿Cómo integra L-PentAI la Generación Aumentada por Recuperación (RAG) con el Aprendizaje por Refuerzo (RL)?
L-PentAI fusiona RL y RAG creando un bucle de interacción híbrido. En cada paso de tiempo, el agente observa el estado del entorno de red y consulta una base de datos vectorial mediante algoritmos de búsqueda de vecinos más cercanos aproximados (ANN). Los documentos recuperados (como detalles de CVE, políticas y configuraciones) se utilizan para aumentar (augment) la representación del estado antes de que la red de políticas (policy network) seleccione una acción. Además, el contexto recuperado se inyecta en los prompts de un Modelo de Lenguaje Grande (LLM) que guía la planificación de alto nivel y se utiliza para dar forma a la señal de recompensa (por ejemplo, mayor recompensa si el agente hace referencia a una vulnerabilidad crítica real).

## ¿Qué algoritmos de búsqueda vectorial utiliza el sistema y por qué?
El sistema emplea algoritmos de Búsqueda de Vecinos Más Cercanos Aproximados (ANN) para permitir la recuperación de contexto en tiempo real sin los costos computacionales de una búsqueda exhaustiva (fuerza bruta). Específicamente, utiliza:
*   **HNSW (Hierarchical Navigable Small World):** Preferido para índices de tamaño medio, ya que ofrece una complejidad logarítmica $O(\log n)$, logrando un equilibrio ideal entre velocidad y calidad de búsqueda.
*   **IVF (Inverted File):** Utilizado para conjuntos de datos extremadamente grandes o dinámicos, ofreciendo una complejidad de $O(\sqrt{n})$ cuando los clústeres están bien equilibrados.
*   **LSH (Locality Sensitive Hashing):** Con una complejidad aproximada de $O(n^{1/\rho})$, es otra alternativa mencionada, aunque HNSW e IVF son las opciones principales en la implementación.

## ¿Cómo se garantiza la privacidad y seguridad de los datos en L-PentAI?
La privacidad y la seguridad son fundamentales en el diseño de L-PentAI. El sistema opera bajo un despliegue local seguro donde todos los datos (índices vectoriales, documentos recuperados y registros) permanecen en los servidores de la organización; no se realizan llamadas externas y el LLM se ejecuta localmente o mediante una API interna segura. Además, implementa cifrado en reposo, listas de control de acceso para restringir qué agentes pueden consultar qué colecciones, y registros de auditoría seguros (usando hashing SHA-256 para las acciones). También incluye un "kill switch" o interruptor de emergencia para terminar comportamientos inusuales y puede integrarse con plataformas SIEM para reportar anomalías, cumpliendo con normativas como el GDPR.

## ¿Qué métodos de Aprendizaje por Refuerzo (RL) se aplican para el entrenamiento de los agentes?
El agente de políticas (policy agent) se entrena utilizando métodos de gradiente de políticas. El sistema formaliza el entorno como un Proceso de Decisión de Markov (MDP) y utiliza principalmente:
*   **PPO (Proximal Policy Optimization):** Utiliza un objetivo sustituto recortado (clipped surrogate objective) para garantizar que las nuevas políticas no se desvíen demasiado de las antiguas, estabilizando el entrenamiento.
*   **Actor-Critic:** Combina una red de políticas (actor) que selecciona acciones y una red de valor (crítico) que estima la ventaja.
*   **MAPPO (Multi-Agent PPO):** Para la coordinación de múltiples agentes, utilizando el paradigma de Entrenamiento Centralizado con Ejecución Descentralizada (CTDE).
*   **Regularización de Entropía:** Se añade un bonus de entropía a la función objetivo para fomentar la exploración y evitar la convergencia prematura a políticas deterministas.

## ¿Cómo funciona la coordinación multiagente en la arquitectura de L-PentAI?
L-PentAI soporta múltiples agentes especializados (por ejemplo, escáner, explotación, movimiento lateral, auditoría) coordinados por un planificador (planner). Para abordar los desafíos de entornos multiagente como la no-estacionariedad y la asignación de crédito, utiliza el marco **CTDE (Centralized Training with Decentralized Execution)**. Durante el entrenamiento, todos los agentes comparten observaciones y contexto, permitiendo que el crítico tenga acceso a información global. Durante la ejecución, cada agente actúa de forma descentralizada utilizando su propia política y observaciones locales. Los estudios de ablación demuestran que esta cooperación multiagente mejora el recall en la detección de vulnerabilidades.

## ¿Cuáles son los principales casos de uso de L-PentAI en una red corporativa?
El documento detalla cinco casos de uso principales:
1.  **Detección de Desviación de Configuración (Configuration Drift):** Escaneo periódico de archivos para compararlos con plantillas base y alertar sobre puertos no autorizados, usando RAG para determinar si la desviación está permitida.
2.  **Higiene de Credenciales:** Pruebas de contraseñas débiles o por defecto, donde la recuperación de políticas de contraseñas aumenta la recompensa si se descubre una violación.
3.  **Pruebas de Arquitectura Zero-Trust:** Simulación de movimiento lateral para verificar si las reglas de microsegmentación bloquean adecuadamente el acceso no autorizado.
4.  **Simulación de Respuesta a Incidentes:** Emulación de patrones de ataque (phishing, malware) enriquecidos con inteligencia de amenazas recuperada, para evaluar tiempos de detección y respuesta.
5.  **Auditoría de Cumplimiento (Compliance):** Verificación contra marcos regulatorios como PCI-DSS e ISO 27001, mapeando observaciones a estados de cumplimiento mediante recuperación de requisitos.

## ¿Qué tecnologías y lenguajes de programación componen la implementación de L-PentAI?
La implementación del sistema está estructurada en microservicios que utilizan diferentes lenguajes optimizados para tareas específicas:
*   **Go:** Utilizado para el plano de control (control-plane), exponiendo endpoints REST/gRPC para programar pruebas, recuperar métricas y gestionar configuraciones, aprovechando su concurrencia.
*   **Rust:** Empleado para componentes críticos de rendimiento como el índice ANN (HNSW/IVF), aprovechando su seguridad de memoria y concurrencia segura. Se comunica mediante FFI o gRPC.
*   **Python:** Utilizado para los componentes de aprendizaje automático, albergando el bucle de entrenamiento RL, integración con PyTorch, y el planificador que usa el LLM y RAG.
*   **Almacenamiento:** Usa bases de datos clave-valor como SQLite o Postgres para embeddings, metadatos y registros.

## Fuentes
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]