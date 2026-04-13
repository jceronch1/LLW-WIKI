# 28 - 04 - METHOD AND SYSTEM FOR LOCAL AUTONOMOUS INTERNAL PENETRATION TESTING USING RETRIEVAL-AUGMENTED ARTIFICIAL INTELLIGENCE AGENTS

## Resumen

Este documento presenta la especificación técnica y la divulgación de invención para L-PentAI, un agente de Inteligencia Artificial autónomo y local diseñado para realizar pruebas de penetración internas. El sistema combina el Aprendizaje por Refuerzo (RL) con la Generación Aumentada por Recuperación (RAG) y la Búsqueda de Vecinos Aproximados (ANN) para automatizar el descubrimiento de configuraciones incorrectas, vulnerabilidades y oportunidades de exfiltración de datos dentro de redes empresariales. Su objetivo principal es mejorar la postura de seguridad ejerciendo continuamente las defensas internas, respetando siempre las restricciones de seguridad y las políticas de privacidad.

La arquitectura de L-PentAI se compone de seis módulos principales: un recuperador (retriever), un indexador, una base de datos vectorial, un agente de política (policy agent), un planificador y un Modelo de Lenguaje Grande (LLM). El agente opera en pasos de tiempo discretos: observa el estado del entorno, recupera contexto relevante de la base de datos vectorial mediante algoritmos ANN (como HNSW o IVF), forma un estado aumentado y selecciona una acción basada en una política estocástica optimizada por métodos de gradiente de política (como PPO o MAPPO). Este enfoque permite al agente tomar decisiones informadas y contextualizadas en tiempo real.

Un aspecto diferenciador de L-PentAI es su compromiso con la privacidad y la seguridad operativa. Todo el procesamiento, recuperación de datos y registro de logs se ejecuta de forma local (on-premises), sin enviar información sensible fuera de la organización. El sistema incluye un "kill switch" y un componente de monitoreo que audita las acciones del agente y finaliza su ejecución si detecta un comportamiento anómalo, integrándose además con plataformas SIEM para reportar anomalías.

El documento detalla el rigor matemático del sistema, formalizando el entorno como un Proceso de Decisión de Markov (MDP) y derivando las actualizaciones del gradiente de política. También se analizan métricas de evaluación como precisión, recall y F1-score, junto con métricas de RL como la recompensa promedio por episodio. Los resultados experimentales en redes sintéticas demuestran que el agente aprende de manera efectiva, aumentando la recompensa promedio de 0.2 a 1.8, y mejorando la precisión de 0.3 a 0.85.

Finalmente, la invención explora la coordinación multi-agente bajo el paradigma de Entrenamiento Centralizado con Ejecución Descentralizada (CTDE), donde agentes especializados (escáner, explotación, movimiento lateral) colaboran compartiendo observaciones. Los estudios de ablación confirman que la eliminación de RAG reduce la precisión en un 15%, y la eliminación de la cooperación multi-agente disminuye el recall, validando la arquitectura híbrida propuesta como superior frente a enfoques de RL aislados o basados en reglas estáticas.

## Datos clave
- **Inventor/Autor**: Ruslan Tiahniienko (Investigador Independiente)
- **Fecha de Presentación (Filing Date)**: 11 de febrero de 2026
- **Algoritmos de RL principales**: REINFORCE, PPO (Proximal Policy Optimization), MAPPO (Multi-Agent PPO), DDPG (Deep Deterministic Policy Gradient)
- **Algoritmos de Búsqueda Vectorial (ANN)**: LSH (Locality Sensitive Hashing), HNSW (Hierarchical Navigable Small World), IVF (Inverted File)
- **Complejidad de búsqueda**: HNSW logra complejidad logarítmica O(log n), IVF opera en O(√n) con clústeres balanceados, y LSH tiene una complejidad aproximada de O(n^{1/ρ})
- **Lenguajes de implementación**: Go (plano de control/API), Rust (índice ANN y concurrencia segura), Python (bucles de entrenamiento RL y PyTorch)
- **Resultados experimentales (Red sintética 100 hosts)**: Recompensa promedio aumentó de 0.2 a 1.8; Precisión mejoró de 0.3 a 0.85; Recall de 0.25 a 0.8; F1-score de 0.28 a 0.82.
- **Impacto de ablación**: Sin RAG, la precisión cae un 15%. Sin cooperación multi-agente, el recall disminuye. La búsqueda por fuerza bruta aumenta el tiempo de recuperación en un orden de magnitud frente a HNSW.
- **Tiempo de entrenamiento**: Promedio de 0.5 segundos por episodio, donde la recuperación vectorial representa el 10% del tiempo total.

## Temas principales
1. Arquitectura híbrida RL-RAG para ciberseguridad ofensiva autónoma.
2. Formalización matemática del entorno como Proceso de Decisión de Markov (MDP) y Gradiente de Política.
3. Búsqueda de Vecinos Aproximados (ANN) y bases de datos vectoriales para recuperación de contexto en tiempo real.
4. Entrenamiento Centralizado con Ejecución Descentralizada (CTDE) para sistemas multi-agente en pentesting.
5. Privacidad y seguridad en despliegue local (on-premises) de agentes de IA.
6. Métricas de evaluación y funciones de recompensa en RL para detección de vulnerabilidades.
7. Teoría de la información aplicada al RL (Entropía, Entropía Cruzada, Divergencia KL y JS).
8. Casos de uso específicos: Detección de desviación de configuración, higiene de credenciales, arquitectura Zero-Trust y cumplimiento normativo.

## Actores y entidades mencionadas
- **Ruslan Tiahniienko**: Inventor principal e investigador independiente.
- **Milvus**: Documentación de referencia citada para análisis de complejidad de algoritmos ANN.
- **xOffense**: Framework previo de RL multi-agente citado como estado del arte.
- **Sutton & Barto (2018)**: Referencia estándar de texto citada para la derivación del teorema del gradiente de política.

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/aprendizaje-por-refuerzo|aprendizaje-por-refuerzo]]
- [[concepts/generacion-aumentada-por-recuperacion-para-agentes|generación-aumentada-por-recuperación]]
- [[concepts/pruebas-de-penetracion|pruebas-de-penetración]]
- [[concepts/bases-de-datos-vectoriales|bases-de-datos-vectoriales]]
- [[concepts/optimizacion-de-politica-proximal|optimización-de-política-proximal]]
- [[concepts/ciberseguridad-ofensiva|ciberseguridad-ofensiva]]
- [[concepts/procesos-de-decision-de-markov|procesos-de-decisión-de-markov]]
- [[concepts/busqueda-de-vecinos-aproximados-para-agentes|búsqueda-de-vecinos-aproximados]]

## Citas textuales relevantes
> "The goal is to automate discovery of misconfigurations, vulnerabilities and data exfiltration opportunities inside enterprise networks while respecting safety constraints and privacy policies."

> "All data (vector index, retrieved documents, logs) remains on-premises, preserving confidentiality. Only anonymized metrics may leave the system."

> "Ablation studies indicate that removing RAG reduces precision by 15%, as the agent lacks context about which hosts are likely vulnerable. Removing multi-agent cooperation decreases recall, indicating the importance of specialized agents."

> "The system includes a monitoring component that audits agent actions and terminates misbehavior. Additionally, a 'kill switch' can stop the agent if unusual activity is detected."

> "In zero-trust environments, agents attempt lateral movement and resource access across micro-segments. The reward is based on whether micro-segmentation controls prevent unauthorized access."

## Notas
- La fecha de presentación de la patente (11 de febrero de 2026) es futura respecto al momento actual, lo que indica que el documento funciona como una divulgación técnica prospectiva o un borrador de especificación de patente.
- El sistema está diseñado estrictamente para despliegue local, lo cual es una restricción crítica para entornos empresariales donde la exfiltración de datos hacia APIs externas de LLMs es inaceptable.
- La función de recompensa penaliza al agente si es detectado por los defensores y si viola restricciones de seguridad, lo que fomenta un comportamiento furtivo y合规 (cumplimiento de políticas) durante el pentesting.
- Se sugieren direcciones futuras como la integración de RLHF (Reinforcement Learning from Human Feedback), entrenamiento adversario, y la aplicación de Redes Neuronales de Grafos (GNN) para la priorización de rutas de ataque.