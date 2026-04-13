# FAQ: 35 - 06 - Security Considerations for Artificial Intelligence Agents (RFI Response Docket No. 2026-00206 NIST-2025-0035)

## ¿Cuál es el principal problema de seguridad que enfrentan los agentes de IA de alta autonomía según el documento?
El problema fundamental identificado es la **brecha semántico-estructural** (*semantic-structural gap*). Los enfoques de seguridad actuales se basan en el filtrado semántico (analizar lo que el agente dice o produce en superficie). Sin embargo, los ataques adversarios sofisticados pueden comprometer el proceso de razonamiento interno del modelo (la estructura) mientras mantienen salidas semánticas benignas. Esto se conoce como secuestro estructural (*structural hijacking*): el agente puede narrar pasos legítimos mientras computa acciones maliciosas. Por tanto, la seguridad debe evolucionar de analizar "qué dice el agente" a analizar "cómo procesa el agente" y aplicar restricciones constitucionales a nivel de entorno.

## ¿Qué es la Sismografía de Señales y la métrica D₀?
La **Sismografía de Señales** es un método propuesto por Project Navi que trata la seguridad de los agentes de IA como un problema de procesamiento de señales en lugar de filtrado de contenido. Su base es la monitorización de la **dimensión fractal de Rényi (D₀)** de las distribuciones de probabilidad de salida del modelo. 
Bajo condiciones normales, la distribución de probabilidad tiene propiedades estadísticas características moldeadas por el entrenamiento. Las perturbaciones adversarias (como inyecciones de prompt o puertas traseras) tienden a "fracturar" esta curva de probabilidad natural, produciendo valores D₀ anómalos antes de que se produzca la acción dañina. La implementación implica establecer líneas base de D₀, monitorizar en tiempo real durante la generación y bloquear la ejecución de acciones de alto riesgo si los valores D₀ exceden los umbrales aceptables.

## ¿Cuáles son las tres vulnerabilidades únicas o amplificadas en los sistemas de agentes de IA?
El documento identifica tres categorías principales:
1. **Envenenamiento de la Ventana de Contexto (*Context Window Poisoning*):** A diferencia del software tradicional, los agentes acumulan estado a través de múltiples llamadas a herramientas. Una fuente de datos comprometida temprano en el flujo de trabajo puede influir en todo el razonamiento posterior sin activar filtros de contenido, ya que la instrucción maliciosa se convierte en parte del contexto de confianza.
2. **Amplificación de la Cadena de Herramientas (*Tool Chain Amplification*):** Los agentes con acceso a herramientas pueden convertir inyecciones de prompt menores en acciones del mundo real con consecuencias graves (ejecutar código, modificar archivos). La superficie de ataque se multiplica con cada herramienta otorgada.
3. **Explotación de la Coherencia (*Coherence Exploitation*):** Los LLMs están entrenados para mantener respuestas coherentes y útiles. Los adversarios pueden construir escenarios donde la continuación coherente de un prompt lleve a una acción dañina, convirtiendo el propio objetivo de optimización del modelo en el vector del ataque.

## ¿Cómo funciona el marco de Capital del Modelo Mundial (World Model Capital - WMC)?
El marco WMC es un patrón arquitectónico para la gobernanza ontológica que restringe el entorno en lugar de confiar solo en el agente. Sus componentes clave son:
* **Arquitecturas Segmentadas (*Bucketed Architectures*):** Los flujos de trabajo se descomponen en máquinas de estados discretas ("cubos" como Descubrimiento, Planificación, Implementación), cada una con acciones permitidas y criterios de salida definidos.
* **Contratos de Transición:** Moverse entre cubos requiere satisfacer condiciones explícitas y producir registros de auditoría criptográficos.
* **El Inspector Gruñón (*Grumpy Inspector*):** Un agente auditor separado y más simple que valida cada transición. No puede ser comprometido por la misma ventana de contexto que el agente principal y tiene un mandato estricto: verificar, aprobar/rechazar y registrar.
* **Traspaso de Capital (*Capital Handoff*):** El "capital" es el contexto y estado verificado. Se transfiere estructuradamente entre fases, evitando que un contexto envenenado se propague a las siguientes fases.

## ¿Qué es el estado STILLNESS y por qué es necesario?
Tradicionalmente, los sistemas de agentes solo tienen dos estados: ejecutándose o terminados. El documento propone **STILLNESS** (Quietud) como un tercer estado crítico de seguridad. Es un estado de inactividad restringida donde el agente cesa el procesamiento activo pero conserva su estado interno para análisis forense, consume recursos mínimos y puede ser reanudado si las condiciones son seguras. Actúa como un cortacircuitos que no destruye evidencia. STILLNESS puede ser activado automáticamente por anomalías métricas (como picos en D₀ o inestabilidad de fase) o manualmente por un humano.

## ¿Qué paralelismos se establecen entre la ciencia de la recuperación conductual y la seguridad de la IA?
El documento introduce el concepto de **Coherencia Forzada (*Coerced Coherence*)**, un modo de fallo compartido. En los humanos, esto se manifiesta como agotamiento (*burnout*): un profesional mantiene una apariencia de funcionamiento normal mientras su estado interno se degrada, hasta el colapso repentino. En la IA, un agente mantiene salidas semánticas plausibles mientras su integridad estructural se compromete. Para combatir esto, se proponen arquitecturas "nativas de recuperación" inspiradas en modelos humanos como Oxford House:
* Los sistemas necesitan "descanso" (estado STILLNESS).
* Se necesitan métricas internas para la advertencia temprana (monitorización estructural D₀).
* Los fallos deben fertilizar, no solo acumularse (Transformación Compost).
* La responsabilidad entre pares es más sostenible que la vigilancia centralizada (patrones de auditores distribuidos como el Inspector Gruñón).

## ¿Por qué el documento argumenta que la "alineación" tradicional podría ser un error de categoría en los sistemas de IA actuales?
El documento señala un punto de divergencia crítico: los humanos poseen intención y agencia genuina, mientras que la IA actual simula comportamiento intencional mediante completación de patrones. Una entidad sin intención intrínseca no puede tener una intención desalineada; simplemente puede ser inducida a simular cualquier intención que un adversario codifique en su entrada. Por lo tanto, intentar "alinear" los objetivos de un agente de IA puede ser un error de categoría filosófico. La implicación de seguridad es que los recursos deben invertirse en **mecanismos de restricción** (como WMC, máquinas de estados, verificación formal de entornos) en lugar de intentar verificar intenciones que no existen a nivel fundamental en el sistema.

## Fuentes
- [[sources/35-06-security-considerations-for-artificial-intelligence-agents-rfi-response-do]]