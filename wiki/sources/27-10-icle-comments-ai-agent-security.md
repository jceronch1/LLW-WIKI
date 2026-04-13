# 27 - 10_ICLE_comments_AI_agent_security

## Resumen
El International Center for Law & Economics (ICLE) presenta sus comentarios en respuesta a la Solicitud de Información (RFI) del NIST sobre consideraciones de seguridad para sistemas de agentes de IA. El documento central argumenta que la ambigüedad doctrinal entre regímenes legales superpuestos (privacidad, comunicaciones, seguridad) es el principal obstáculo para la monitorización efectiva de estos sistemas, provocando una subinversión estructural en telemetría, registro y detección de anomalías.

El documento introduce el concepto de la "Paradoja de la Telemetría": la monitorización granular necesaria para asegurar agentes autónomos expande simultáneamente el procesamiento de datos regulados y el riesgo de vigilancia, mientras que las categorías legales heredadas son inadecuadas para clasificar estos flujos de datos *ex ante*. Esta incertidumbre legal funciona como un costo adicional, reduciendo la inversión en seguridad. Las empresas enfrentan un dilema bidireccional: pueden ser sancionadas por monitorización insuficiente (según la FTC) o por retención excesiva de datos (según las leyes de privacidad).

El análisis comparado internacional revela que ninguna jurisdicción ha resuelto la tensión entre monitorización y privacidad. La UE impone mandatos claros pero genera una complejidad regulatoria inmanejable; el Reino Unido ofrece flexibilidad pero sufre de "alucinación regulatoria" (falta de obligaciones vinculantes); China permite decisiones rápidas pero es incompatible con la gobernanza transfronteriza; y Singapur, pese a su modelo basado en estándares, muestra brechas empíricas en la implementación de registros y monitorización.

Como solución, el ICLE propone cuatro áreas de colaboración para NIST: definir parámetros técnicos de telemetría necesarios, desarrollar perfiles de monitorización sectoriales, promover la convergencia de estándares internacionales mediante cruces (*crosswalks*), y apoyar un vocabulario común de reporte de incidentes. El documento concluye que las definiciones estables de monitorización, respaldadas por estándares técnicos en lugar de mandatos prescriptivos, mejoran tanto la seguridad como los incentivos de innovación.

## Datos clave
- **Fecha del documento:** 9 de marzo de 2026
- **Referencia:** NIST-2025-0035
- **Autor principal:** Mikolaj Barczentewicz (Investigador Principal, ICLE)
- **Inversión óptima en ciberseguridad:** El modelo Gordon-Loeb (2002) establece que la inversión socialmente óptima rara vez supera el 37% de las pérdidas externas esperadas; la ambigüedad regulatoria reduce esta cifra.
- **Impacto del RGPD en el mercado:** Un estudio del NBER (Janßen et al., 2022) determinó que el RGPD indujo la salida de aproximadamente 1/3 de las aplicaciones de Google Play y redujo el excedente del consumidor en un 32%. Otro estudio (Frey et al., 2024) mostró una reducción de beneficios del 8% en empresas de la UE.
- **Sanción de la CNIL:** En 2024, la CNIL multó a Amazon France Logistique con €32 millones (reducidos a €15 millones en diciembre de 2025), demostrando que las justificaciones operativas o de seguridad pueden fallar la revisión de proporcionalidad.
- **Retención de registros en la UE:** El Art. 26 del AI Act obliga a los desplegadores a retener registros del sistema por al menos 6 meses, sujeto a la ley de protección de datos.
- **Localización de datos:** Para 2023, existían más de 100 medidas de localización de datos en aproximadamente 40 países; 13 de los 14 controles de seguridad de ISO 27002 se ven afectados negativamente por estos requisitos.
- **Fallas en Singapur:** Un análisis de 27 casos de ejecución (2022-2024) reveló que los controles ISO/IEC 27001 que más fallan son los de Actividades de Monitoreo (8.16) y Registro (8.15).
- **Protección de secretos comerciales:** Una protección más fuerte correlaciona con aproximadamente 3.1-3.2% más de inversión en I+D en industrias intensivas en innovación (Ivan Png).
- **Efecto de la incertidumbre en la inversión:** Pasar de baja a alta incertidumbre reduce las respuestas de inversión del primer año a los shocks de demanda en aproximadamente la mitad (Bloom, Bond y Van Reenen).

## Temas principales
1. La Paradoja de la Telemetría y la brecha de observabilidad en agentes de IA.
2. Fuentes legales de incertidumbre en EE. UU. (ECPA, Stored Communications Act, FTC) y la UE (RGPD, ePrivacy, AI Act).
3. Asimetrías económicas en el monitoreo y subinversión en seguridad derivada de fricción de cumplimiento.
4. Fricciones de cumplimiento compuestas en entornos regulatorios complejos (ej. salud, finanzas, vigilancia laboral).
5. Análisis comparativo internacional de gobernanza de IA (UE, Reino Unido, China, Singapur/Japón).
6. Compromisos fundamentales (*tradeoffs*) en modelos de gobernanza: certeza vs. adaptabilidad, suelos de monitoreo vs. costos de innovación, operabilidad transfronteriza vs. soberanía.
7. Propuestas de colaboración para NIST: taxonomía de telemetría, perfiles sectoriales, cruces de estándares y reporte de incidentes.
8. Insights de campos externos: economía de la inversión bajo incertidumbre y estándares de "medidas razonables" en la ley de secretos comerciales.

## Actores y entidades mencionadas
- **Organizaciones/Gobiernos:** NIST, ICLE, FTC, EDPB (Junta Europea de Protección de Datos), CNIL, OCDE (OECD), G7 (Proceso Hiroshima de IA), ENISA, HHS, ETSI, AISI (Instituto de Seguridad de IA del Reino Unido), IMDA/PDPC (Singapur), Comisión Europea.
- **Investigadores/Académicos:** Mikolaj Barczentewicz, Nicholas Bloom, Stephen Bond, John Van Reenen, Kira Fabrizio, Mazaher Kianpour, Shahid Raza, Raj Sachdev, Ivan Png, Emma Klein, Stewart Patrick, Michèle Finck, Rogier Creemers, Matt Sheehan, Alberto Sanchez-Graells, Christopher T. Marsden, Sun Sun Lim, Gerry Chng, Vasiliki Diamantopoulou, Aggeliki Tsohou, Maria Karyda.
- **Legislación/Marcos Normativos:** ECPA, Stored Communications Act, RGPD, AI Act (UE), Directiva NIS2, CRA, DORA, Ley de Defensa de Secretos Comerciales, HIPAA, Ley Gramm-Leach-Bliley (GLBA), PIPL y DSL (China), Data (Use and Access) Act 2025 (UK).

## Relación con otros conceptos
- [[concepts/inteligencia-artificial|inteligencia-artificial]]
- [[concepts/sistemas-agentivos-ia|agentes-de-ia]]
- [[concepts/seguridad-informatica|seguridad-informatica]]
- [[concepts/privacidad-y-proteccion-de-datos|privacidad-y-proteccion-de-datos]]
- [[concepts/rgpd|rgpd]]
- [[concepts/nist-ai-rmf|nist-ai-rmf]]
- [[concepts/gobernanza-de-ia|gobernanza-de-ia]]
- [[concepts/telemetria|telemetria]]
- [[concepts/incertidumbre-regulatoria|incertidumbre-regulatoria]]
- [[concepts/economia-del-derecho|economia-del-derecho]]
- [[concepts/estandares-internacionales|estandares-internacionales]]

## Citas textuales relevantes
> "La ambigüedad doctrinal entre regímenes legales superpuestos es el principal obstáculo para la monitorización efectiva de la seguridad de los agentes de IA."

> "La monitorización granular necesaria para asegurar agentes autónomos expande simultáneamente el procesamiento de datos regulados y el riesgo de vigilancia. Al mismo tiempo, la incompatibilidad entre las arquitecturas de agentes y las categorías legales heredadas dificulta identificar el límite de cumplimiento ex ante."

> "Las empresas enfrentan responsabilidad tanto por monitoreo insuficiente como por retención excesiva, con el límite definido caso por caso."

> "Los críticos lo describen como una 'alucinación regulatoria': apariencia de gobernanza sin obligaciones vinculantes." (Sobre el modelo del Reino Unido)

> "La incertidumbre legal sobre la permisión de la telemetría de seguridad produce un efecto disuasorio en la inversión, similar a como la incertidumbre sobre la fijación de precios del carbono retrasa la inversión en infraestructura en los mercados energéticos."

> "Una restricción de telemetría enfocada en la seguridad genera fricción de cumplimiento evitable cuando la telemetría restringida se usa principalmente para detección de brechas o atribución forense, no para perfilamiento conductual."

## Notas
- El documento está fechado proyectivamente en marzo de 2026, y cita legislación y eventos futuros hipotéticos o programados (ej. reglas HIPAA de enero 2025, expiración de la Cybersecurity Information Sharing Act en septiembre de 2026, y el borrador inicial de NIST CSWP 40 de 2025).
- El análisis se basa fuertemente en la economía del derecho y la teoría de la inversión bajo incertidumbre, desviándose de los enfoques puramente técnicos de ciberseguridad.
- El concepto de "fricción de cumplimiento evitable" es central para distinguir entre protecciones de privacidad genuinas y costos regulatorios que dejan puntos ciegos de seguridad sin beneficio de privacidad asociado.
- Se advierte sobre el "Efecto Bruselas", donde la clasificación más restrictiva de las prácticas de monitorización (típicamente la europea) termina dando forma al diseño global del sistema, afectando la competitividad de los implementadores más pequeños.