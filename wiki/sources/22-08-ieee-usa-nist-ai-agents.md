# 22 - 08_IEEE_USA_NIST_AI_agents

## Resumen
El documento "22 - 08_IEEE_USA_NIST_AI_agents" aborda los riesgos y vulnerabilidades en sistemas de agentes de inteligencia artificial (IA), enfatizando la necesidad de una seguridad robusta para maximizar el potencial de estos sistemas. Se discuten aspectos como la robustez frente a ataques, problemas emergentes en nuevas versiones, dependencias del ecosistema de herramientas y desafíos de implementación.

## Datos clave
- **Fecha:** 9 de marzo de 2026
- **Autor:** Peter Cihon, Senior Advisor, Center for AI Standards and Innovation (CAISI), NIST, U.S. Department of Commerce

## Temas principales
1. Robustez frente a ataques y problemas emergentes en nuevas versiones.
2. Dependencias del ecosistema de herramientas y tecnologías.
3. Desafíos de implementación, incluyendo internalización vs externalización y edge/cloud hosting.
4. Comparación entre modelos de código abierto y propietario.
5. Barriers to adoption and compliance issues.

## Actores y entidades mencionadas
- **Organizaciones:** IEEE-USA, NIST (National Institute of Standards and Technology), CAISI (Center for AI Standards and Innovation)
- **Personas:** Peter Cihon

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/seguridad-cibernetica|seguridad-cibernética]]

## Citas textuales relevantes
> "La seguridad en agentes de IA requiere un enfoque proporcional a la autonomía, los privilegios y el entorno operativo. La falta de una gobernanza adecuada puede introducir riesgos significativos."

## Notas
- El documento destaca la necesidad de implementar controles adecuados para agentes de IA en función de su nivel de autonomía y entorno operativo.
- Se recomienda la adopción de guías, marcos de trabajo y mejores prácticas para mejorar la seguridad.

---

# 22 - 08_IEEE_USA_NIST_AI_agents

## Resumen del Documento

**Fecha:** 9 de marzo de 2026  
**Autor:** Peter Cihon, Senior Advisor, Center for AI Standards and Innovation (CAISI), National Institute of Standards and Technology (NIST), U.S. Department of Commerce  

### Contexto
IEEE-USA presenta una respuesta a la RFI (Request for Information) del CAISI sobre consideraciones de seguridad para agentes de IA. Se destaca el potencial y los riesgos asociados con estos sistemas.

### Potencial de los Agentes de IA
- **Aplicaciones:** Diagnóstico temprano de enfermedades, descubrimiento de terapias, educación personalizada, agricultura más eficiente, avances científicos.
- **Safeguards necesarios:** Protección adecuada y contextual para maximizar el potencial.

### Categorización de Riesgos
- **Tipos de Agentes de IA:** Se distinguen según su nivel de autonomía, alcance de privilegios y entorno operativo.
- **Riesgos:** Diferentes entre agentes limitados a procesamiento de información (riesgo de integridad y privacidad) e integrados con sistemas digitales (riesgos cibernéticos).

### Riesgos Específicos
1. **Threats, Risks, and Vulnerabilities**
   - **Prompt Injection:** Inyección deliberada o indirecta de comandos.
   - **Escalado de Privilegios:** Falta de control de acceso fino para agentes de IA.
   - **Falta de Guardrails:** Dificultad en detectar solicitudes maliciosas.
   - **Espionaje Cibernético:** Agentes pueden exponer información sensible interna.
   - **Amplificación de Acciones:** Impacto multiplicado de una entrada comprometida.
   - **Confianza Confusa:** Riesgo de confundir sistemas confiables y no confiables.
   - **Consecuencias Físicas:** Daños físicos en entornos físico-cibernéticos.
   - **Vulnerabilidades No Deterministas:** Salidas probabilísticas que dificultan pruebas exhaustivas.
   - **Bypass Estocástico:** Ataques iterativos para evadir guardrails.
   - **Cadenas de Razonamiento:** Inyección en etapas intermedias del razonamiento.

2. **Riesgos Fundamentales**
   - **Vagancia Gubernamental e Invisible Superficie de Ataque:** Agentes operan invisiblemente hasta que se detecta una brecha.
   - **Ataques Automáticos a Máquina Velocidad:** Operación rápida sin fatiga, comprimiendo atacantes humanos en horas.
   - **Compromiso de Cadena de Suministro:** Riesgo de cascada en sistemas integrados.
   - **Riesgos de Datos:** Exposición accidental de datos sensibles.
   - **Riesgos Adjacentes Técnicos:** Vulnerabilidades transferidas entre componentes.
   - **Riesgos Específicos de IA:** Emergencia de comportamientos, sesgo amplificado.

3. **Vulnerabilidades del Código**
   - **Sugerencias de Códigos Obsoletos:** Riesgos de introducir vulnerabilidades en código generado rápidamente.
   - **Insuficiencia de Guardrails:** Falta de detección de entradas maliciosas.

4. **Vulnerabilidades del Protocolo**
   - **Riesgos en la Cadena de Agentes (A2A):** Riesgo en bibliotecas abiertas que pueden propagar vulnerabilidades.

### Variación de Riesgos
- **Capacidad del Modelo:** Modelos más fuertes y con horizonte a largo plazo presentan riesgos mayores.
- **Ecosistema de Herramientas:** Ecosistema en evolución, con riesgos potenciales.
- **Método de Implementación:** Diferentes riesgos según si se implementa internamente o externamente.
- **Contexto de Hospedaje:** Riesgos variados dependiendo del entorno (premises, nube, borde).
- **Caso de Uso:** Riesgos específicos según el caso de uso.

### Conclusión
La seguridad en agentes de IA requiere un enfoque proporcional a la autonomía, los privilegios y el entorno operativo. La falta de una gobernanza adecuada puede introducir riesgos significativos.

---

**Referencias:**
1. Russell, Stuart, Peter Norvig, and Artificial Intelligence. "A modern approach." Artificial Intelligence. Prentice-Hall, Englewood Cliffs 25.27 (1995): 79-80.
2. Identity and Access Management.
3. OAuth 2.0.
4. Role-Based Access Control (RBAC).
5. https://arxiv.org/abs/2307.15043
6. https://arxiv.org/abs/2211.09527
7. Cost of Data Breach Report, IBM, 2025.
8. https://www.anthropic.com/news/disrupting-AI-espionage
9. An API token is a unique, secure credential used to authenticate and authorize a user or application when accessing an API.
10. International AI Safety Report 2026.
11. EUREKA: Evaluating and Understanding Large Foundation Models - Microsoft Research.

---

**Contacto:** Erica Wissolik  
e.wissolik@ieee.org | (202) 360-5023

---

## Desarrollo y Seguridad de Agentes de Inteligencia Artificial (IA)

### Aspectos Relevantes

1. **Desempeño en Tareas de Generación de Código**
   - Los agentes de IA se recomienda que no se utilicen para la identificación de errores.

2. **Adopción de Guías y Marco de Trabajo de Seguridad Cibernética**
   - Existe una falta generalizada de conciencia sobre la seguridad de los sistemas de agente de IA entre desarrolladores, emplazadores y usuarios.
   - La adopción de guías, marcos de trabajo y mejores prácticas es lenta.

3. **Impedimentos en la Adopción**
   - Los desarrolladores a menudo no consideran la seguridad durante el desarrollo de soluciones.
   - La cultura debe cambiar para que la seguridad sea una función de diseño, no solo de aprobación.

4. **Marco de Trabajo Relevantes**
   - **NIST SP 800-53 Rev. 517**: Proporciona controles directamente aplicables a la seguridad del agente.
   - **OWASP Top 10 para Aplicaciones Agenticas (2025)**: Identifica 10 riesgos específicos de agentes.
   - **MITRE ATLAS**: Ofrece técnicas y tácticas adversarias específicas para agentes de IA.

5. **Evaluación de Seguridad Durante el Desarrollo**
   - Se pueden anticipar amenazas, riesgos y vulnerabilidades mediante modelado de amenazas específico del agente.
   - Métodos como la evaluación segura por diseño, pruebas adversarias y análisis estático e dinámico.

6. **Detección de Incidentes Seguros**
   - Registros de seguridad y rutas de auditoría capturan prompts, outputs del modelo, llamadas a herramientas, decisiones de política.
   - Monitoreo en tiempo real y detección de anomalías alertan sobre uso inusual de herramientas.

7. **Comparación con Prácticas de Seguridad Tradicionales**
   - Las prácticas de seguridad para agentes de IA se alinean con las tradicionales, pero incluyen nuevas amenazas como la inyección de prompts y riesgos en el plano de ejecución.

8. **Madurez de Métodos**
   - Prácticas maduras incluyen NIST SSDF, evaluaciones de riesgo, monitoreo y respuesta a incidentes.
   - Áreas emergentes incluyen pruebas seguras para agentes/LLMs y detección robusta de inyecciones de prompts.

9. **Documentación y Datos Upstream**
   - Paquetes de datos de seguridad upstream: resúmenes de la proveniencia del entrenamiento, comportamientos no seguros conocidos.
   - Disclosures públicos podrían crear nuevas vulnerabilidades si se publican detalles sensibles.

10. **Documentación de Despliegue Seguro**
    - La documentación actual es inconsistente; NIST podría definir un "Hoja de Seguridad de Despliegue del Agente" (1 página).

11. **Constricción y Monitoreo de Entornos de Despliegue**
    - Métodos técnicos para restringir el acceso a los entornos de despliegue.
    - Modificaciones virtuales o físicas para mitigar amenazas, incluyendo rollback y negaciones.

12. **Interacciones con Counterpartes**
    - Prácticas variadas según el tipo de interacción (humanos, sistemas digitales, mecánicos, etc.).

13. **Monitoreo de Entornos de Despliegue**
    - Monitoreo continuo mediante registros de acciones del agente y detección de anomalías.
    - Retos en la implementación de métodos tradicionales de monitoreo.

## Referencias

- Pruet, J., Makanju, A., Reiber, J., & Achiam, J. (2026, February 6). *AI and international security: Pathways of impact and key uncertainties*. OpenAI.
- [Enlaces a documentos y recursos](https://cdn.openai.com/pdf/international-security.pdf)

---

# Seguridad de los Agentes de Inteligencia Artificial (IA)

## Monitoreo y Alertas

Los agentes de IA pueden generar alertas basadas en la frecuencia de uso de herramientas, volúmenes anormales de acceso a datos, o secuencias de acciones inesperadas. El cumplimiento de políticas durante el tiempo de ejecución incluye listas blanqueadas para herramientas y acciones, límites de tasa, interruptores de circuito, y mecanismos automatizados de cierre que detienen la ejecución del agente en caso de violación.

## Análisis de Secuencia y Trajectoria

El análisis de secuencias y trayectorias monitorea cadenas de acciones en lugar de eventos aislados para detectar ataques lentos o multistep, como el abuso gradual de privilegios o la exfiltración de datos en etapas.

## Telemetría del Entorno

La telemetría del entorno incluye monitoreo de tráfico de red, rastreo de utilización de recursos y registros de acceso a sistemas con los que interactúa el agente.

### Desafíos Legales y de Privacidad

Los desafíos legales y de privacidad incluyen la exposición de datos empresariales sensibles a los agentes; prompts y outputs generados por usuarios podrían contener información personal o confidencial; y telemetría cruzada que podría caer bajo marcos regulatorios como requisitos de protección de datos y cumplimiento.

### Madurez de Métodos

La madurez de estos métodos en la investigación y la práctica requiere continuo desarrollo para establecer mejores prácticas para el monitoreo en tiempo real, escalable y preservador de privacidad. Herramientas observables específicas del agente, marcos de monitoreo de comportamiento y auditorías automatizadas de acciones autónomas están emergiendo con investigación activa y adopción temprana en la industria.

## Despliegue Abierto en Internet

El despliegue abierto en internet está aumentando. Se propone utilizar attestaciones criptográficas firmadas para contar y filtrar el tráfico de agentes de manera confiable. También se sugiere publicar indicadores agregados como la capacidad nacional de inferencia y la latencia de mobilización computacional, junto con estándares de identidad del agente.

## Consideraciones Adicionales

### Fomento de Prácticas Seguras

Un "kit inicial" de NIST para agentes incluye arquitecturas de referencia, baselines de control mínimas por nivel de riesgo y test harnesses que las startups/SME pueden adoptar en pocos días. Plantillas de adquisición listas para uso: hojas de seguridad de una página y requisitos de registros de auditoría que los compradores federales y empresas pueden reutilizar.

### Colaboración Gubernamental

La colaboración gubernamental con el ecosistema de IA es urgente, especialmente en áreas de alta consecuencia. Se recomienda la evaluación compartida y el intercambio seguro de incidentes (lo que falló, cómo se detectó, mitigaciones), así como la adopción de operadores entrenados.

### Enfoques de Investigación Prioritarios

La investigación debe enfocarse en defensas robustas contra la inyección indirecta de prompts en agentes que usan herramientas (no solo chat). Se deben asegurar la seguridad a través de todos los modos: analizar información sensible en todos los modos antes de enviar datos a los modelos. Se deben detectar backdoors/poisoning para modelos de base, fortaleciendo las pruebas pre-deploy so que los gatilladores ocultos sean menos probables.

### Enfoques Internacionales

**Estados Unidos**: El AI Act crea obligaciones armonizadas y claridad en el mercado pero puede aumentar la carga de cumplimiento para innovadores pequeños (SME) si no se rigen bien. Crea un régimen vinculante, basado en el riesgo, que moldeará los defectos de proveedores globales.

**Singapur**: Aborda la seguridad de agentes de IA con una pila pro-innovación que urge a las organizaciones a delimitar explícitamente la autonomía del agente (herramientas/permisos), asignar responsabilidad humana clara y gestionar controles a lo largo del ciclo de vida. Beneficios: guía rápida que se mantiene al ritmo de la tecnología; menor fricción de adopción, especialmente para SMEs; mayor garantía medible en compras y regulaciones.

**India**: Fortalece las reglas de privacidad sobre minimización de datos empujados y notificación de violaciones—mejora la confianza, pero las empresas solicitan un despliegue gradual para evitar interrupciones. Su modelo de gobierno es "ligero" y basado en riesgos, combinando medidas voluntarias con un enfoque "tecnológico-legal" que embedde legalidad en el diseño del sistema (cumplimiento por diseño) usando la Infraestructura Pública Digital (DPI). Propone una coordinación gubernamental a través de un Grupo de Gobierno para IA (AIGG) y evaluaciones técnicas/evaluaciones a través de un Instituto de Seguridad de IA (AISI), junto con responsabilidades graduadas basadas en riesgo y diligencia debida.

**Arabia Saudita**: Su política nacional de IA se asienta en los Principios Éticos de la Autoridad de Datos e IA (SDAIA) y orientaciones gubernamentales sobre GenAI, mientras que su postura cibernética nacional está configurada a través del Control de Seguridad Cibernética Esencial (ECC-2:2024). También tiene una Ley de Protección de Datos Personales (PDPL) que moldea las condiciones de manejo y transferencia transfronteriza.

**Israel**: Publicó una política gubernamental sobre regulación y ética de IA (2023) y ejecuta un Programa Nacional de IA con pilares en infraestructura, talento y gobierno. Beneficios: un diseño de programa interministerial apoya la rápida traducción de políticas a implementaciones (sandbox, adopción pública, accesibilidad de datos).

**China**: Tiene una pila regulatoria multilayer para salidas AI online e influencias sistémicas: Medidas Temporales Generativas de IA (2023), Reglas de Recomendación de Algoritmos (2022) y Reglas de Síntesis Profunda (efectivas 2023). Beneficios: la centralización de la aplicación puede rápidamente exigir la identificación del origen, etiquetado visible y obligaciones de plataforma.

**Rusia**: Tiene una estrategia nacional a largo plazo para IA hasta 2030 con movimientos reportados para restringir el uso de generativos AI en áreas administrativas públicas sensibles (proyecto de regulación). Beneficios: prohibiciones explícitas en contextos gubernamentales sensibles pueden reducir el riesgo de uso accidental de alto impacto.

**Reino Unido**: Renombró su Instituto de Seguridad de IA hacia un Instituto de Seguridad de IA con un mayor énfasis en la seguridad nacional y los riesgos cibernéticos; también firmó una asociación con OpenAI que incluye el intercambio de datos para investigaciones de seguridad. Beneficios: un modelo de instituto dedicado mejora la capacidad de medición y acelera métodos prácticos de evaluación para sistemas de vanguardia.

**Japón**: Enfatiza el gobierno suave, el gobierno a lo largo del ciclo de vida mediante las Directrices de IA para Negocios (actualizadas hasta diciembre 2024) y estableció el Instituto de Seguridad de IA de Japón (J-AISI) en febrero de 2024 como un centro de evaluación e información. Beneficios: orientaciones voluntarias, prácticas de gobierno bajan la fricción de adopción mientras impulsan prácticas de gobierno consistentes a través del sector.

### Enfoques Externos

**Pensamiento de la "Envelope" Aérea**: Definir límites operativos duros; tratar las violaciones como eventos de seguridad con respuesta obligatoria—simple para líderes y auditores entender. **Disciplina de Sistemas Distribuidos**: Compensar/undo es un enfoque probado para transacciones multistep, directamente relevante a revertir trayectorias de acción del agente.

Los puntos de vista expresados en este documento representan las opiniones del IEEE-USA. Los miembros del IEEE que contribuyeron a esta respuesta son Harish Babu Arunachalam, Biju Baburajan, Maulik Bhatt, Amit Chaudhary, Ramakrishna Garine, Dev Gupta, Nipun Joshi, Shankar Krishnan, Olivera Kotevska, Aditya Mehra, Siddharth Nandagopal, Tarun Reddy Nukala, Srinivasan Parthasarathy, Francesca Rossi, Abhinavdutt Singh y Akshay Sonawane.