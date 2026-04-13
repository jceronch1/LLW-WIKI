# busqueda-de-vecinos-aproximados-para-agentes

## Definición
Uso de algoritmos como HNSW (Hierarchical Navigable Small World), IVF o LSH para permitir que los agentes de IA recuperen contexto relevante de bases de datos vectoriales en tiempo real. Esta técnica reduce la complejidad temporal de búsqueda de fuerza bruta a logarítmica O(log n), haciendo viable la generación aumentada por recuperación en pasos de decisión rápidos.

## Ideas clave
- Esencial para la viabilidad en tiempo real de arquitecturas RAG en agentes
- HNSW ofrece complejidad O(log n) con buen equilibrio calidad/velocidad
- IVF ofrece complejidad O(sqrt(n)) en clusters balanceados
- Permite consultas de similitud del coseno en millones de vectores
- Implementado en componentes de alto rendimiento como Rust

## Relación con otros conceptos
- [[concepts/generacion-aumentada-por-recuperacion-para-agentes|generacion-aumentada-por-recuperacion-para-agentes]]
- [[concepts/memoria-persistente-agentiva|memoria-a-largo-plazo-en-agentes]]

## Fuentes relacionadas
- [[sources/28-04-method-and-system-for-local-autonomous-internal-penetration-testing-using-]]

## Preguntas abiertas
- (pendiente de desarrollo)
