# 06 — Resultados de verificación de fuentes (navegador + búsqueda), 2026-07-15

Verificación de los 5 puntos pendientes de la síntesis, para fijar arquitectura.

## 1. IDE Temuco (ide-munitemuco.hub.arcgis.com) — VERIFICADO ✅/❌
Hub municipal ArcGIS **vivo**. Descarga en CSV/KML/Zip/GeoJSON/GeoTIFF/PNG.
- ❌ **NO tiene** (visiblemente) catastro de arbolado urbano ni ortofoto de alta resolución.
- ✅ **SÍ tiene las capas de la CAUSA** que Daniela quiere cruzar, con dato **oficial municipal**:
  - **Visor de Carpetas de Edificación** — permisos de construcción + recepción definitiva (histórico).
  - **Visor de Loteos** — registros históricos de loteos (incl. irregulares).
  - **Visor de Fusiones y Subdivisiones** — historial predial.
  - **Visor de Zonificación / Plan Regulador** — uso de suelo, qué se puede construir.
  - **Macrosectores y Unidades Vecinales con censo 2024** — base para justicia ambiental / equidad de sombra.
  - **Humedales Urbanos** (Ley 21.202), Ciclovías, Cortafuegos.
→ **Implicancia:** el cruce "pérdida de árboles ↔ expansión inmobiliaria/vial" es MÁS fuerte de lo previsto: datos oficiales, no inferidos. Pero para detección de copas no hay imagen fina aquí.

## 2. Ortofoto fina nacional (IDE Chile / ide.cl) — VERIFICADO ⚠️
- ide.cl reestructurado (URLs viejas dan 404). Existe centro de descarga con +100 capas y ortofotos.
- **Fotografías aéreas de alta resolución IDE Chile disponibles solo para comunas de regiones NORTE y CENTRO.** Temuco está en el SUR (Araucanía, 38°S) → **probablemente SIN cobertura de ortofoto fina gratis nacional.** (Confirmar en centro de descarga cuando esté operativo, u oficina regional IDE Araucanía: Arturo Prat 535, Temuco.)
- IGM Chile tiene ortofotos pero archivo NO open (solicitud/costo) — coincide con agente A.
→ **Implicancia CLAVE:** la **Capa 2 (detección de copas) NO puede asumir imagen fina gratis descargable para IA (DeepForest)** en Temuco. Camino gratis+legal: conteo manual asistido sobre Google Earth Pro histórico + i-Tree Canopy, o **generar imagen propia** (dron / celular / Mapillary) en corredores piloto.

## 3. Calor urbano — VERIFICADO ✅✅ (el hilo más sólido)
- **Yale Global Surface UHI** disponible como dataset en **Google Earth Engine** (`YALE/YCEO/UHI/...v4`), 2003-2018, 1 km, MODIS día/noche, >10.000 ciudades incl. Temuco → consultable programáticamente. Explorer web: geospatial.yale.edu/global-surface-uhi-explorer.
- **HALLAZGO NUEVO — paper local:** "Heat on the Move: Contrasting Mobile and Fixed Insights into Temuco's Urban Heat Islands" (PMC11860384, 2024-25). Estudio específico de islas de calor de Temuco con transectos móviles + estaciones fijas. **Referencia local directa** para validar/anclar el análisis.
- LST propio a 30 m con código GEE Ermida 2020 sigue siendo el método fino (Yale a 1 km es contexto grueso).

## 4. Catastro de arbolado Temuco — no público confirmado
No aparece capa pública. Pedir a SECPLA / Unidad de Parques y Arbolado Urbano vía Ley de Transparencia. UFRO (Laboratorio de Ecosistemas y Bosques) tiene el catastro de patrimoniales.

## 5. Mapillary corredores piloto — no confirmado por búsqueda
Cobertura específica de Caupolicán/Alemania no confirmada vía web; verificar directo en app Mapillary al abordar Capa 2. Alternativa robusta: generar cobertura propia con celular.

---

## Conclusión para la arquitectura (confirma las 3 capas, con ajustes)
1. **Capa 1 (radar GEE) — confirmada y reforzada.** NDVI + LST 2000-2025 + dataset Yale UHI. El hilo calor es el más sólido y tiene paper local de anclaje.
2. **Capa 2 (detalle en corredores) — ajuste importante:** NO hay ortofoto fina gratis para IA en Temuco → arranca con **conteo manual asistido (Google Earth Pro histórico) + i-Tree Canopy**, con opción de imagen propia (dron/celular) para automatizar después. DeepForest queda para cuando exista imagen fina local.
3. **Capa 3 (observatorio ciudadano) — confirmada y potenciada:** además de denuncias, integrar capas oficiales de causa de IDE Temuco (edificación, loteos, zonificación) → el "por qué se perdieron" con dato oficial. GitHub Pages + Leaflet + KoBoToolbox.
