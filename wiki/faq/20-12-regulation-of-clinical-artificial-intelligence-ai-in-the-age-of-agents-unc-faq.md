# FAQ: 20 - 12 - Regulation of clinical Artificial Intelligence (AI) in the Age of Agents Unconfined Non-Deterministic Clinical Software (UNDCS) systems for healthcare

## ¿Qué es el software clínico no determinado y no confinado (UNDCS)?
El UNDCS (*Unconfined Non-Deterministic Clinical Software*) se refiere a una nueva categoría de sistemas de inteligencia artificial, como los modelos de lenguaje extensos (LLMs) basados en transformadores, que operan en un espacio semántico abierto y sin límites. A diferencia de los sistemas anteriores, el UNDCS responde a instrucciones (*prompts*) no estructuradas y puede presentar un comportamiento no determinista, lo que significa que la misma entrada puede producir diferentes salidas debido a factores como el parámetro de "temperatura" o errores en cálculos de punto flotante.

## ¿Cuál es la diferencia entre los sistemas de IA "confinados" y "no confinados"?
La distinción radica en la predictibilidad y el alcance de sus salidas:
*   **Sistemas Confinados:** Incluyen el software clínico determinista (DCS), con relaciones fijas entre entrada y salida, y el software clínico confinado (CCS), que utiliza técnicas como el aprendizaje profundo (*deep learning*) pero mantiene un espectro de etiquetas de salida predefinido y predecible.
*   **Sistemas No Confinados (UNDCS):** Utilizan modelos como los LLMs que operan en un espacio semántico abierto, lo que introduce riesgos únicos como "alucinaciones" (errores semánticos inherentes a la compresión de datos del modelo) y una variabilidad difícil de evaluar mediante métodos tradicionales de conjuntos de datos exhaustivos.

## ¿Por qué los marcos regulatorios actuales (como SaMD) son insuficientes para los LLM?
Los marcos actuales, como el de *Software as a Medical Device* (SaMD) de la FDA, son principalmente "basados en etiquetas" (*label-driven*), lo que significa que la regulación se centra en el uso previsto designado por el fabricante. Sin embargo, los LLM modernos (como ChatGPT o Claude) se distribuyen directamente al consumidor por proveedores tecnológicos que controlan toda la cadena de suministro, pero que a menudo no detallan sus fuentes de entrenamiento ni se registran como fabricantes de dispositivos médicos. Estos modelos suelen utilizar descargos de responsabilidad genéricos para evitar el uso clínico, lo que deja un vacío regulatorio que desprotege a los usuarios finales.

## ¿Qué riesgos específicos presentan los sistemas UNDCS en el entorno clínico?
Los principales riesgos identificados son:
1.  **Alucinaciones:** Errores semánticos donde el modelo genera información que parece creíble pero es incorrecta.
2.  **Falta de protección al consumidor:** La ausencia de procesos de vigilancia de eventos adversos y la falta de selección adecuada de usuarios (basada en alfabetización tecnológica y sanitaria).
3.  **Errores en situaciones de alto riesgo:** La capacidad de proporcionar recomendaciones erróneas pero convincentes ante información clínica incompleta.
4.  **Consecuencias indirectas:** El uso de herramientas no clínicas (como escribas de IA) puede causar errores en la documentación, diagnósticos erróneos en procesos posteriores y problemas en las reclamaciones de seguros médicos.

## ¿Qué estrategias de mitigación de riesgos se proponen para el UNDCS?
Se sugieren varias técnicas para alinear el comportamiento de estos sistemas con su uso previsto:
*   **Red Teaming:** Pruebas de estrés mediante simulaciones de ataques adversarios, inyección de *prompts* y *jailbreaking*.
*   **Guardrails (Barreras de seguridad):** Algoritmos para filtrar salidas inapropiadas.
*   **RAG (Generación Aumentada por Recuperación):** Integrar la recuperación de información de fuentes de conocimiento confiables para fundamentar las respuestas.
*   **Moderación Agente-Agente:** Uso de arquitecturas de Sistemas Multi-Agente (MAS) para lograr consenso y reducir errores.
*   **Modelos Neuro-simbólicos:** Combinar la capacidad generativa con razonamiento determinístico basado en guías validadas.
*   **LLM-as-a-Judge:** Implementar bucles de evaluación donde un modelo califica y verifica la validez de las salidas agregadas.

## ¿Qué es la moderación agente-agente y cómo ayuda en la regulación?
La moderación agente-agente utiliza arquitecturas de Sistemas Multi-Agente (MAS) para que múltiples agentes de IA interactúen entre sí. Este proceso permite buscar el consenso entre diferentes instancias del modelo, lo que ayuda a reducir la frecuencia de errores y mitigar los sesgos de autorreferencia (donde un modelo tiene un sesgo positivo hacia modelos de su propio tipo). Al combinar esto con RAG y modelos neuro-simbólicos, se puede asegurar que las salidas del sistema de soporte a la decisión clínica (CDSS) se alineen con las guías médicas establecidas.

## Fuentes
- [[sources/20-12-regulation-of-clinical-artificial-intelligence-ai-in-the-age-of-agents-unc]]