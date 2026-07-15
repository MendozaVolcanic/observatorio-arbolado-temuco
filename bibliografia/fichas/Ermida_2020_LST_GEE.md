# Ermida, S.L.; Soares, P.; Mantas, V.; Göttsche, F.-M.; Trigo, I.F. (2020)

**"Google Earth Engine Open-Source Code for Land Surface Temperature Estimation from the Landsat Series."** *Remote Sensing* 12(9), 1471. DOI: 10.3390/rs12091471. MDPI, open access (CC BY).

## Qué aporta al proyecto

Es la referencia metodológica CENTRAL de la capa 1 (el plan ya la cita explícitamente). Los autores publican un repositorio de código GEE (JavaScript, módulo reutilizable) que calcula LST directamente en Google Earth Engine para Landsat 4, 5, 7 y 8, sin necesitar descargar ni almacenar datos localmente — encaja perfecto con la restricción de "solo gratis" del proyecto.

## Dato / cifra clave

- Algoritmo: Statistical Mono-Window (SMW), calibrado con simulaciones de transferencia radiativa, simple de implementar y computacionalmente liviano.
- Usa emisividad de superficie derivada del producto ASTER GED (Global Emissivity Database) como insumo adicional al canal térmico de Landsat.
- El código está empaquetado como "GEE module" (import directo vía `require()` en el Code Editor de GEE), no como script suelto — se importa con una sola línea.

## Cómo se usa en el observatorio — impacto de implementación

**Esto sí es accionable de inmediato**: en vez de reimplementar el algoritmo LST desde cero, la capa 1 del observatorio debería **importar directamente el módulo GEE de Ermida et al.** (repositorio público enlazado en el paper, sección de "Data Availability") y aplicarlo sobre Landsat 5/7/8 para la serie 2000–2025 de Temuco. Esto ahorra semanas de calibración propia del algoritmo SMW y da trazabilidad académica al método usado (citable, peer-reviewed, validado contra estaciones terrestres en el propio paper). Es el único de los 5 papers con un detalle de implementación directamente reutilizable en el pipeline técnico.
