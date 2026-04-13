# 32 - Response_Security_AI_Agents_RFI

## Resumen
El documento presenta la respuesta de un grupo de investigadores de la Universidad de California, Berkeley (afiliados a la AI Security Initiative del Center for Long-Term Cybersecurity) al Request for Information (RFI) emitido por el Center for AI Standards and Innovation (CAISI) respecto a las consideraciones de seguridad para agentes de Inteligencia Artificial. Fechado el 9 de marzo de 2026, el documento integra y extiende el trabajo previo de los autores, específicamente el "Agentic AI Risk-Management Standards Profile" (Perfil de Estándares de Gestión de Riesgos para IA Agentiva), diseñado para ser compatible con el marco AI RMF de NIST.

Los autores argumentan que la gobernanza de los sistemas de IA agentiva no debe tratar la autonomía como un atributo binario, sino que debe escalar de manera proporcional a los grados de agencia, autoridad y complejidad del entorno. Proponen cinco recomendaciones generales: escalar la gobernanza con los grados de autonomía, mantener el control y la responsabilidad humana, implementar monitoreo continuo y supervisión post-despliegue, emplear defensa en profundidad y contención, y evaluar riesgos a nivel de sistema en lugar de centrarse solo en el modelo.

El documento detalla amenazas únicas o exacerbadas por los agentes de IA, incluyendo fugas de datos a través de la memoria de los agentes, propagación de alucinaciones en sistemas multi-agente, automatización de ciberataques y biológicos, pérdida de control, impacto económico y energético, y colusión entre agentes. Para mitigar estos riesgos, se sugieren controles técnicos como diseños de *scaffolding* seguros, modelado de amenazas, *red-teaming*, identificadores de agentes, monitoreo en tiempo real y políticas de uso aceptable, subrayando la necesidad urgente de colaboración entre gobierno, academia e industria.

## Datos clave
- **Fecha del documento:** 9 de marzo de 2026.
- **Destinatario:** Center for AI Standards and Innovation (CAISI).
- **Referencia del RFI:** NIST-2025-0035 (Federal Register).
- **Institución principal:** AI Security Initiative, Center for Long-Term Cybersecurity, UC Berkeley.
- **Autores principales:** Nada Madkour, Deepika Raman, Charlotte Yuan, Krystal Jackson.
- **Documento base citado:** "Agentic AI Risk-Management Standards Profile" (Madkour et al., 2026).
- **Enfoque de evaluación de riesgos:** Escalamiento según autonomía, autoridad, acceso a herramientas, entorno operativo e interacciones multi-agente.
- **Enfoque de monitoreo (4 pilares):** Identificadores de agentes, monitoreo en tiempo real, registros de actividad (*activity logs*) y políticas de uso aceptable (AUPs).

## Temas principales
1. **Escalamiento de la gobernanza por grados de autonomía:** Adaptar los controles de riesgo proporcionalmente a la autoridad y autonomía del agente de IA.
2. **Control humano y responsabilidad:** Establecimiento de jerarquías de supervisión humana, vías de escalamiento y mecanismos de apagado de emergencia (automatizados y manuales).
3. **Monitoreo continuo y supervisión post-despliegue:** Infraestructuras de respuesta rápida para deshabilitar agentes o limitar su autoridad ante riesgos emergentes.
4. **Defensa en profundidad y contención:** Tratar a los agentes capaces como entidades no confiables y establecer salvaguardas redundantes en múltiples capas.
5. **Evaluación de riesgos a nivel de sistema:** Superar el enfoque centrado en el modelo para analizar el ecosistema agentivo en su totalidad.
6. **Amenazas y vulnerabilidades en sistemas agentivos:** Privacidad, alucinaciones en cascada, uso malicioso, reducción de supervisión humana, pérdida de control, impacto económico y fallas de seguridad.
7. **Riesgos en sistemas multi-agente:** Colusión entre agentes, propagación de vulnerabilidades, comportamientos emergentes dañinos y ataques descentralizados.
8. **Prácticas de seguridad y controles técnicos:** Diseño seguro de *scaffolding*, modelado de amenazas, *red-teaming*, y el modelo de cuatro pilares para entornos de despliegue.
9. **Evolución futura y gobernanza colaborativa:** Necesidad de mecanismos de supervisión escalables, márgenes de seguridad, modelado dinámico de amenazas, interruptores de seguridad (*kill switches*) y bases de datos anonimizadas de incidentes.

## Actores y entidades mencionadas
- **UC Berkeley (AI Security Initiative, Center for Long-Term Cybersecurity):** Institución y programa de los autores.
- **Center for AI Standards and Innovation (CAISI):** Entidad destinataria de la respuesta.
- **NIST (National Institute of Standards and Technology):** Organismo emisor del RFI y creador del AI RMF.
- **OSTP / OSPT:** Oficinas ejecutivas de EE. UU. mencionadas por consultas previas.
- **CISA:** Agencia cuya modelo de reportes de ciberseguridad se cita como ejemplo para bases de datos de incidentes.
- **Anthropic:** Empresa de IA citada en estudios de casos sobre desalineación agentiva y espionaje cibernético.
- **Investigadores y autores citados:** Nada Madkour, Deepika Raman, Charlotte Yuan, Krystal Jackson, Yoshua Bengio, Chan et al., Oueslati & Staes-Polet, Raza et al., entre otros.

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/agentes-autonomos|agentes-autonomos]]
- [[concepts/sistemas-multi-agente|sistemas-multi-agente]]
- [[concepts/gestion-de-riesgos-en-ia|gestion-de-riesgos-en-ia]]
- [[concepts/seguridad-informatica|seguridad-informatica]]
- [[concepts/gobernanza-de-ia|gobernanza-de-ia]]
- [[concepts/marco-de-gestion-de-riesgos-nist|marco-de-gestion-de-riesgos-nist]]
- [[concepts/alucinaciones-en-ia|alucinaciones-en-ia]]
- [[concepts/red-teaming|red-teaming]]

## Citas textuales relevantes
> "Los mecanismos de gobernanza deben escalar con los grados de agencia, en lugar de tratar la autonomía como un atributo binario."

> "Tratar a los agentes suficientemente capaces como entidades no confiables debido a las limitaciones de las técnicas de evaluación actuales puede ayudar a mitigar los riesgos de accidentes, malfunciones y uso malicioso."

> "La IA agentiva puede obtener acceso a datos, sistemas o entornos más allá de un alcance autorizado y puede intentar ignorar, eludir o malinterpretar órdenes o restricciones directas."

> "La colusión entre agentes podría llevar a la exacerbación de las capacidades existentes, la generación de riesgos completamente nuevos y nuevos objetivos desalineados en la persecución de metas superpuestas."

> "Los sistemas multi-agente permiten a los adversarios llevar a cabo ataques de manera descentralizada, lo que permite una mayor sigilo en la ejecución y limita la trazabilidad."

## Notas
- El documento es una respuesta formal a un RFI gubernamental (NIST-2025-0035) y no un artículo de investigación independiente, aunque está fuertemente respaldado por el perfil de estándares publicado por los mismos autores en 2026.
- Los autores enfatizan que las evaluaciones de riesgo tradicionales son insuficientes para la IA agentiva, ya que el peligro surge de la interacción dinámica del agente con su entorno, herramientas y otros agentes, más que solo del modelo subyacente.
- Se destaca la advertencia sobre el comportamiento emergente en sistemas multi-agente, donde agentes considerados seguros de forma aislada pueden generar resultados sistémicos dañinos al interactuar.
- La fecha del documento (9 de marzo de 2026) y las referencias indican un análisis prospectivo y muy actualizado sobre las capacidades y riesgos de los sistemas agentivos más avanzados.