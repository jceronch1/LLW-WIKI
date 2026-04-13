# 33 - 04_NIST_security_AI_agents

## Resumen
El documento constituye la respuesta de la Computing Research Association (CRA) y el Computing Community Consortium (CCC) a la Solicitud de Información del NIST sobre Consideraciones de Seguridad para Agentes de Inteligencia Artificial. En él, se advierte que los modelos de seguridad actuales son inadecuados para hacer frente a la naturaleza adaptativa y autónoma de los agentes de IA, señalando que la depuración de estos sistemas es extremadamente difícil y que su capacidad para aprender de los errores puede amplificar cualquier fallo subyacente en su código.

Se identifican desafíos críticos específicos de los agentes autónomos, como la delegación incierta de credenciales, el riesgo dependiente del contexto, la dificultad para atribuir responsabilidades cuando el código es generado por IA, y el peligro de fallas en cascada en sistemas multi-agente, donde un solo agente comprometido puede envenenar la toma de decisiones de otros en cuestión de horas. Además, se subrayan los riesgos de las acciones de alta velocidad y alto riesgo ejecutadas sin aprobación humana inmediata.

El texto también aborda la amenaza que representa el desequilibrio en la fuerza laboral si se reemplaza a expertos humanos por IA en la codificación y auditoría sin mantener un enfoque de "human-in-the-loop" (humano en el ciclo). Se insta al NIST a publicar guías de implementación que definan roles humanos responsables, puertas de aprobación para código generado por IA y métricas de supervisión. Asimismo, se alerta sobre la necesidad de equilibrar la regulación para no sofocar la investigación académica frente a la opacidad de la industria.

Finalmente, el documento enfatiza que el ritmo de desarrollo de ataques está superando a las capacidades de los modelos de IA y que las barreras de seguridad comerciales actuales no funcionarán contra agentes maliciosos de autoaprendizaje. Se aboga por un cambio radical hacia la "seguridad por diseño" (Security by Design), la creación de incentivos industriales, la conexión entre investigadores y profesionales de la ciberseguridad, y el desarrollo de protocolos para verificar si una entidad que interactúa con un agente de IA es humana o una IA.

## Datos clave
- **Fecha del documento:** 11 de marzo de 2026.
- **Autores:** Rachel Greenstadt (NYU), Michela Taufer (UTK), Ming Lin (UMD), Manish Parashar (University of Utah), David Jensen (UMass Amherst), Brian Mosley (CRA).
- **Representación:** La CRA es una asociación de más de 270 organizaciones de investigación en computación de América del Norte.
- **Financiamiento del CCC:** Patrocinado por la National Science Foundation (NSF), aunque las opiniones del documento no reflejan necesariamente las de la NSF.
- **Fallas en cascada:** Un solo agente comprometido puede envenenar la toma de decisiones de agentes descendentes en un sistema multi-agente en cuestión de horas.
- **Aprendizaje por refuerzo:** Los agentes de IA utilizan funciones de recompensa para distinguir entre ataques exitosos y fallidos, creando una memoria que mejora su efectividad pero amplifica errores de código.
- **Guía propuesta para NIST:** Se sugiere definir (i) roles humanos responsables, (ii) puertas de revisión/aprobación, (iii) requisitos de documentación de procedencia, y (iv) métricas de supervisión humana para agentes de codificación de IA.
- **Brecha de seguridad:** La interpretabilidad de la IA está muy por detrás de sus capacidades, y el ritmo de desarrollo de ataques supera a los modelos de IA actuales.

## Temas principales
1. Desafíos de seguridad específicos en agentes de IA (depuración, imprevisibilidad, amplificación de errores).
2. Limitaciones de los modelos de seguridad tradicionales frente a la autonomía (delegación de credenciales, riesgo contextual, responsabilidad, fallas en cascada).
3. Riesgos del desequilibrio de la fuerza laboral y la necesidad de experiencia humana en el ciclo ("human-in-the-loop").
4. Alineación regulatoria y cumplimiento del comportamiento agéntico, con equilibrio entre la industria y la academia.
5. Vulnerabilidades introducidas por nuevas capas de abstracción (de lenguajes de programación a prompts en lenguaje natural) y la falta de pruebas verticales de extremo a extremo.
6. Dinámicas de interacción y conflicto en sistemas multi-agente.
7. Estrategias de seguridad y detección frente a ataques automatizados y maliciosos a gran escala.
8. La necesidad imperativa de "Seguridad por Diseño" y la verificación de identidad en interacciones agénticas.

## Actores y entidades mencionadas
- Computing Research Association (CRA)
- Computing Community Consortium (CCC)
- National Institute of Standards and Technology (NIST)
- National Science Foundation (NSF)
- New York University (NYU)
- University of Tennessee, Knoxville (UTK)
- University of Maryland, College Park (UMD)
- University of Utah
- University of Massachusetts Amherst (UMass Amherst)
- Rachel Greenstadt
- Michela Taufer
- Ming Lin
- Manish Parashar
- David Jensen
- Brian Mosley

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/sistemas-agentivos-ia|agentes-de-ia]]
- [[concepts/seguridad-informatica|seguridad-informatica]]
- [[concepts/sistemas-multi-agente|sistemas-multi-agente]]
- [[concepts/aprendizaje-por-refuerzo|aprendizaje-por-refuerzo]]
- [[concepts/regulacion-de-ia|regulacion-de-ia]]
- [[concepts/seguridad-por-diseno|seguridad-por-diseno]]
- [[concepts/interpretabilidad|interpretabilidad]]
- [[concepts/human-in-the-loop|human-in-the-loop]]
- [[concepts/ciberseguridad|ciberseguridad]]

## Citas textuales relevantes
> "There are serious security threats and vulnerabilities specific to AI agent systems. One of the most significant is that debugging an AI agent is incredibly difficult."

> "The attribute that makes AI agents so useful is their ability to learn from mistakes, often utilizing techniques such as reinforcement learning. [...] But that increased effectiveness will amplify any errors caused by faults in the agent’s code."

> "cascading failures in Multi-Agent Systems can occur, where a single compromised agent can quickly poison the decision-making of downstream agents within hours"

> "Crucially, the immediate future still demands human expertise in complex coding and a deep understanding of these AI agents. [...] the field faces serious dangers if AI adoption accelerates."

> "Imposing excessive constraints on academic researchers prematurely risks stifling innovation, yet a lack of regulation could lead to the exploitation of the general public by opaque black-box systems offered by industry."

> "more often than not, securing a system happens after the design or even deployment, meaning the security community is routinely playing catch-up and attempting to patch vulnerabilities that could be exploited any minute."

> "A significant concern is the current inability to verify if a human, or even another AI agent, is interacting with an AI agent. This lack of verification poses serious security risks, especially for commercial applications."

## Notas
- El documento está fechado en el futuro (11 de marzo de 2026), lo cual es un dato factual del texto proporcionado y debe ser tratado como tal en el contexto de la wiki.
- El documento sirve como una recomendación directa al NIST, proponiendo la creación de marcos de implementación específicos para agentes de IA en lugar de depender de las directrices generales actuales.
- Se hace referencia a un documento previo, el CCC White Paper "A Research Ecosystem for Secure Computing", como base para el argumento de la seguridad por diseño.
- Se critica explícitamente un ejemplo real (aunque no identificado por nombre) de un sistema universitario que está considerando crear el rol de "Oficial de Riesgo de IA" que requeriría aprobación previa para investigaciones, considerándolo perjudicial para la libertad académica y el progreso del campo.