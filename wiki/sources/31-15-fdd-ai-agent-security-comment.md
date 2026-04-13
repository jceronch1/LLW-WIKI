# 31 - 15_FDD_AI_agent_security_comment

## Resumen
La emergencia de la inteligencia artificial agéntica (IA agéntica) representa un punto de inflexión para el gobierno federal de los Estados Unidos. Si se integra adecuadamente, esta tecnología puede expandir la productividad y acelerar los procesos burocráticos; sin embargo, su implementación sin considerar los riesgos potenciales puede socavar la confianza pública e institucional. Los sistemas de agentes de IA actúan de manera autónoma para lograr objetivos específicos utilizando modelos de lenguaje grande (LLMs) integrados en software de andamiaje, lo que les permite ejecutar tareas de múltiples pasos sin supervisión humana continua. Es esta capacidad de acción autónoma, y no el modelo subyacente, lo que distingue a los agentes de las aplicaciones de IA convencionales y los hace particularmente desafiantes de asegurar.

Los riesgos estratégicos asociados incluyen vectores de ataque como puertas traseras (backdoors), inyección de prompts indirecta y envenenamiento de datos, tácticas que Rusia, China e Irán ya han empleado en el contexto de LLMs convencionales. La IA agéntica amplifica el impacto y la sigilo de estos ataques. Por ejemplo, las puertas traseras pueden incrustarse en las habilidades de los agentes, y la inyección de prompts puede obligar a los agentes a tomar acciones maliciosas sin necesidad de acceder a los sistemas gubernamentales, siguiendo principios de control reflexivo de la era soviética. Además, el envenenamiento de datos se agrava en sistemas agénticos, ya que las fuentes envenenadas pueden ser amplificadas y reintroducidas de manera autónoma.

Los marcos de ciberseguridad federales actuales de NIST (SP 800-160, SP 800-218 y SP 800-53) fueron diseñados para software determinista y no abordan la naturaleza autónoma de la IA agéntica, dejando brechas en la integridad del tiempo de ejecución, la identidad, la procedencia y la cadena de suministro. El documento argumenta que, en lugar de simplemente catalogar vulnerabilidades, el diseño de seguridad debe comenzar considerando los resultados inaceptables que no deben permitirse bajo ninguna circunstancia, utilizando metodologías como la Ingeniería Cibernética Impulsada por Consecuencias (CCE) del Laboratorio Nacional de Idaho.

Finalmente, la Fundación para la Defensa de las Democracias (FDD) presenta siete recomendaciones clave para el gobierno de EE. UU.: actualizar los estándares de ingeniería de NIST, establecer infraestructura de pruebas específica para IA agéntica, acelerar la iniciativa COSAiS, expandir MITRE ATLAS, lanzar un Centro de Análisis e Intercambio de Información de IA (AI-ISAC), requerir una Lista de Materiales de IA (AIBOM) en las adquisiciones, y mantener a los humanos en el ciclo con un grupo de trabajo interagencial y expertos internos. La urgencia es crítica, ya que las brechas de control pueden ser explotadas rápidamente por adversarios extranjeros.

## Datos clave
- **Fecha del documento:** 9 de marzo de 2026.
- **Organización autora:** Foundation for Defense of Democracies (FDD).
- **Destinatario:** U.S. Department of Commerce / National Institute of Standards and Technology (NIST), Center for AI Standards and Innovation.
- **Número de referencia:** XRIN 0693-XA002.
- **Caso ClawHub:** Se detectaron 824 capacidades no autorizadas o maliciosas ("malicious skills") de aproximadamente 10,700 en el mercado de código abierto para agentes de IA, según análisis de la firma de seguridad Koi.ai en febrero de 2026.
- **Caso BRICKSTORM:** Actores estatales de la República Popular China crearon una puerta trasera para infraestructura empresarial ampliamente utilizada, que permaneció indetectada por un largo periodo.
- **Red Pravda:** Red de desinformación masiva desplegada por Rusia para manipular los entornos de información y envenenar los modelos de IA.
- **Marcos de NIST con brechas identificadas:** SP 800-160, SP 800-218, SP 800-218A, SP 800-53 y SP 800-53A.
- **Principio OWASP mencionado:** "Least agency" (mínima autonomía), que dicta que los agentes solo deben recibir la autonomía mínima requerida para su tarea autorizada.

## Temas principales
1. **Definición y naturaleza de la IA Agéntica:** Sistemas autónomos que utilizan LLMs para planificar y ejecutar acciones en sistemas externos sin supervisión humana continua.
2. **Vectores de ataque y riesgos estratégicos:** Puertas traseras (backdoors), inyección de prompts indirecta y envenenamiento de datos (data poisoning).
3. **Amenazas de adversarios extranjeros:** Uso de doctrinas de guerra de sistemas por parte de China y tácticas de control reflexivo por parte de Rusia.
4. **Riesgos de interacción multi-agente:** Fallos en cascada, auto-replicación de agentes y dificultad de atribución en ecosistemas interconectados.
5. **Obsolescencia de los marcos de ciberseguridad actuales:** Brechas en los estándares de NIST diseñados para software determinista y no para sistemas autónomos.
6. **Ingeniería basada en consecuencias (CCE):** Cambio de paradigma para asegurar sistemas enfocado en eliminar los resultados inaceptables por diseño.
7. **Políticas de adquisición y transparencia:** Necesidad de Listas de Materiales de IA (AIBOM) y cumplimiento normativo en la compra de tecnología.
8. **Supervisión humana y talento gubernamental:** Importancia de mantener humanos en el ciclo, grupos de trabajo interagenciales y auditorías de "sombreros blancos".

## Actores y entidades mencionadas
- **Foundation for Defense of Democracies (FDD)** y su Center on Cyber and Technology Innovation
- **U.S. Department of Commerce**
- **National Institute of Standards and Technology (NIST)** / Center for AI Standards and Innovation
- **Autores:** Leah Siskind, Dr. Georgianna Shea, Marina Chernin
- **Koi.ai** (Firma de ciberseguridad)
- **OpenAI**
- **UK’s National Cyber Security Center (NCSC)**
- **Cybersecurity and Infrastructure Security Agency (CISA)**
- **Idaho National Laboratory (INL)**
- **OWASP** (Open Worldwide Application Security Project)
- **MITRE** (Adversarial Threat Landscape for Artificial Intelligence Systems - ATLAS)
- **Department of Energy national laboratories**
- **Defense Advanced Research Projects Agency (DARPA)**
- **National Science Foundation**
- **Office of Science and Technology Policy (White House)**
- **U.S. Digital Service, 18F, Presidential Innovation Fellowship**
- **Grupos de hackers estatales chinos** (ej. BRICKSTORM)
- ** Rusia** (Red Pravda, control reflexivo)

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/ia-agentica|ia-agéntica]]
- [[concepts/seguridad-informatica|seguridad-informática]]
- [[concepts/modelos-de-lenguaje-grandes|modelos-de-lenguaje-grandes]] (LLMs)
- [[concepts/inyeccion-de-prompt|ataques-de-inyección-de-prompt]]
- [[envenenamiento-de-datos]]
- [[concepts/marcos-normativos-nist|marcos-normativos-nist]]
- [[concepts/guerra-hibrida|guerra-híbrida]]
- [[concepts/transparencia-algoritmica|transparencia-algorítmica]]
- [[concepts/cadena-de-suministro|cadena-de-suministro]]
- [[concepts/ciberseguridad-defensiva|ciberseguridad-defensiva]]

## Citas textuales relevantes
> "The emergence of agentic artificial intelligence (AI) represents an inflection point for the federal government."

> "It is this capacity for autonomous action, rather than the underlying model itself, that distinguishes agent systems from conventional AI applications. That capacity for autonomous action makes agentic AI powerful and uniquely challenging to secure."

> "Unlike traditional cyberattacks, prompt injection requires no access to government systems. A malicious instruction embedded in an external document or an email is sufficient. By the time the compromise is detected, the damage would already be underway."

> "Where Russia seeks to manipulate what AI systems believe, China seeks to control what they can do."

> "Most agentic failures are not model failures. They are authority failures, in which the agent was permitted to do something it should never have been allowed to do."

> "The core security question is therefore: under any failure scenario, what is the worst this agent could do, and have we engineered that outcome out of the system?"

> "A federal government that deploys agentic AI without closing existing control gaps is one that has handed adversaries a significant and unnecessary advantage."

## Notas
- El documento es un comentario público oficial presentado ante el gobierno de los Estados Unidos, específicamente en respuesta a una solicitud del NIST sobre consideraciones de seguridad para agentes de IA.
- Aunque la wiki se centra en el ecosistema de la Inteligencia Artificial en Colombia, este documento proporciona un marco técnico y normativo avanzado (estándares NIST, AIBOM, CCE) que sirve como referencia internacional para la regulación y aseguramiento de sistemas autónomos de IA en cualquier contexto nacional.
- Las fechas referenciadas en el documento (ej. marzo 2026, febrero 2026, diciembre 2025) sitúan el contexto del documento en un escenario prospectivo o de política futurista hipotética/deliberativa.