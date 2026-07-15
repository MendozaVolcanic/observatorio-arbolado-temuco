# Calor urbano y arbolado — plataformas y estudios GRATIS/open

Investigación para observatorio ciudadano de Temuco (Chile). Objetivo: demostrar, solo con recursos gratuitos/abiertos, que **perder árboles = más calor / menos sombra**.
Metodología de búsqueda: Crossref (mailto=cvivallos@gmail.com), Semantic Scholar, SciELO/Dialnet (LATAM), luego WebSearch para plataformas. Fecha: 2026-07-15.

Formato por hallazgo: **nombre · tipo · qué hace · dato gratis · resolución · gratis/open + link · ¿cubre Chile? · cifra clave · cita/URL**.

---

## 0. El fenómeno físico (para el observatorio, en lenguaje de terreno)

Un árbol enfría por dos mecanismos: **sombra** (intercepta la radiación solar antes de que caliente el suelo/pavimento) y **evapotranspiración** (transpira agua, y evaporar agua consume calor — enfriamiento evaporativo, como el sudor). El pavimento y el hormigón, en cambio, absorben radiación de día y la liberan de noche: eso es la **isla de calor urbana (ICU)**. Perder dosel arbóreo quita ambos servicios a la vez, por eso el efecto es fuerte y medible desde satélite.

La variable que un satélite mide directamente NO es la temperatura del aire, sino la **temperatura de superficie (LST, Land Surface Temperature)** — la temperatura de la "piel" del terreno (techos, calles, copas). LST y cobertura verde están inversamente correlacionadas: donde hay árboles/pasto (NDVI alto), la LST baja. Esta correlación negativa LST↔NDVI es exactamente lo que el observatorio puede mapear gratis.

---

## 1. Temperatura de superficie (LST) desde Landsat — gratis

### Cómo se calcula (banda térmica)
Landsat 8/9 llevan el sensor térmico **TIRS** (bandas 10 y 11, ~10.9 y 12 µm). El flujo típico:
1. Banda térmica → radiancia → **temperatura de brillo (BT)**.
2. Se calcula **NDVI** (bandas roja e infrarroja cercana) y de ahí la **fracción de vegetación** y la **emisividad de superficie (LSE)** (método NDVI-thresholds de Sobrino et al. 2008 / SNDVI).
3. Se corrige BT por emisividad (y opcionalmente vapor de agua atmosférico) → **LST**. Algoritmos: Single-Channel (SC), Mono-Window (MW), Radiative Transfer Equation (RTE).

- **Resolución**: banda térmica Landsat 8/9 se entrega remuestreada a **30 m** (nativa TIRS ~100 m). Revisita 16 días (8 días combinando L8+L9). Serie desde 1982 con Landsat 5/7 (banda térmica 120/60 m).
- **Alternativa lista para usar**: producto **Landsat Collection 2 Level-2 Surface Temperature** (USGS ya entrega LST calibrada, sin que uno calcule nada) — 30 m, gratis en EarthExplorer y en GEE.

### Herramientas / tutoriales GEE (todos gratis)
- **Ermida et al. (2020), "GEE Open-Source Code for LST Estimation from the Landsat Series"** · paper + código GEE · calcula LST L4/5/7/8 con SMW y emisividad ASTER-GED · open access · MDPI Remote Sensing 12(9):1471 · https://www.mdpi.com/2072-4292/12/9/1471 · código: `users/sofiaermida/landsat_smw_lst`. **Es el punto de partida recomendado**: pegás un polígono de Temuco y sale la LST.
- **leonsnill/lst_landsat** · repo GitHub · implementación GEE de LST Landsat · open (MIT) · https://github.com/leonsnill/lst_landsat
- **Improving Landsat LST in GEE using NDVI-based emissivity (2026)** · paper · mejora la emisividad NDVI vs ASTER-GED · Advances in Space Research · DOI 10.1016/j.asr.2025.11.085
- Tutoriales paso a paso gratis (Medium/TechGEO) para Landsat 8 LST en GEE (código copy-paste): buscar "Analyzing LST with Landsat 8 in Google Earth Engine".
- **NASA ARSET** · capacitación gratis · "Satellite Remote Sensing for Measuring Urban Heat Islands and Constructing Heat Vulnerability Indices" y "Introduction to Thermal Remote Sensing and UHI Mapping" · https://appliedsciences.nasa.gov (buscar ARSET urban heat).
- **Esri Learn** · lección gratis "Learn to map urban heat with Landsat" · https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/imagery/learn-to-map-urban-heat-with-landsat

### Relación LST vs cobertura arbórea / NDVI (evidencia)
- **Effects of urban tree canopy loss on LST magnitude and timing (2017)** · Zhou et al. · ISPRS J. Photogrammetry & Remote Sensing · DOI 10.1016/j.isprsjprs.2017.04.011 · demuestra que la pérdida de dosel eleva la LST y adelanta el pico térmico diario. **Clave para el argumento "cortar árboles = más calor".**
- **Urban Landscape Heterogeneity Influences the Relationship between Tree Canopy and LST (2021)** · Urban Forestry & Urban Greening · DOI 10.1016/j.ufug.2020.126930.
- Regla empírica repetida en la literatura: **por cada +10% de cobertura vegetal, la LST baja ~0.6–1.2 °C** (varía por clima/método). Trees bajan LST **2–12 °C** según densidad de copa. (Ver secciones 2 y sources.)

---

## 2. Efecto de enfriamiento de árboles urbanos — CIFRAS concretas

> Distinguir siempre: **temperatura del AIRE** (efecto menor, ~fracciones de °C) vs **temperatura de SUPERFICIE/LST** (efecto grande, varios °C). El satélite mide LST.

- **WRI — "Cooling Potential of Urban Trees"** (meta-síntesis) · **cada +10% de dosel baja la temperatura del aire ~0.3 °C**; en general trees bajan aire 0.5–5.8 °C y superficie **2–12 °C** · https://www.wri.org/insights/urban-trees-cooling-potential
- **"Increasing tree canopy lowers urban air temperature by up to 1.5 °C in heat-prone areas" (2025)** · npj Urban Sustainability 5:92 · **+30% de dosel → −1.5 °C de aire en promedio; +10% en hotspots → −0.8 °C** · https://www.nature.com/articles/s42949-025-00277-x
- **"Trees halve urban heat island effect globally…" (2026)** · Nature Communications · los árboles reducen ~a la mitad la intensidad de la ICU, con beneficios desiguales entre barrios · https://www.nature.com/articles/s41467-026-71825-x
- **"A Systematic Review of the Cooling Effects of Urban Forests" (2026)** · Arboriculture & Urban Forestry · revisión metodológica · https://auf.isa-arbor.com
- **"A scaling law for predicting urban trees canopy cooling efficiency"** · PMC11572964 · hay un umbral: el enfriamiento crece con el dosel hasta saturar · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11572964/
- **Shade-tree planting Downtown LA (2024)** · Sustainability 16(20):8768 · descompone sombra vs transpiración vs estacionalidad · DOI 10.3390/su16208768.
- **Tree canopy vs building shade in urban heat mitigation using LST (2025)** · Urban Climate · DOI 10.1016/j.uclim.2025.102522.
- **Neighbourhood tree canopy cover & heat-related ambulance calls (2016)** · Urban Forestry & Urban Greening · DOI 10.1016/j.ufug.2016.08.005 · liga menos dosel con más emergencias por calor (salud).

**Cifra "titular" recomendada para Temuco:** *"Cada 10% de dosel que perdemos sube la temperatura de superficie del orden de 0.6–1.2 °C y la del aire ~0.3 °C"* (WRI + literatura LST).

---

## 3. Plataformas web ya hechas sobre calor urbano (gratis, ¿usables en Chile?)

| Plataforma | Tipo | Qué hace | Gratis/open | ¿Chile? | Link |
|---|---|---|---|---|---|
| **Global Surface UHI Explorer (Yale YCEO)** | Web-app + dataset GEE | Intensidad de ICU (día/noche, verano/invierno) para **>10.000 ciudades del mundo**, 2003–2018, base MODIS | Sí, open (NASA SEDAC + GEE `YALE/YCEO/UHI/...`) | **SÍ — cobertura global, incluye Temuco/Santiago** | https://geospatial.yale.edu/global-surface-uhi-explorer |
| **Google Environmental Insights Explorer — Tree Canopy** | Web-app | Estima % de dosel por manzana con imágenes aéreas + IA; identifica dónde plantar | Gratis | Preview para +40.000 ciudades; Tree Canopy en cientos de ciudades (verificar Temuco) | https://insights.sustainability.google/labs/treecanopy |
| **WRI OpenUrban / Urban Land use-cover** | Dataset + framework | Uso/cobertura de suelo urbano 1 m (OSM+Overture+ESA WorldCover) + albedo, altura de copa, LST, sombra modelada | Open, fuentes globales gratis | **SÍ (global, 83% precisión fuera de EEUU)** | https://www.wri.org (buscar OpenUrban / heat-resilient infrastructure) |
| **NASA Earthdata / ARSET UHI** | Datos + capacitación | Productos LST (Landsat, MODIS, ECOSTRESS) e índices de vulnerabilidad al calor | Gratis | SÍ (global) | https://www.earthdata.nasa.gov |
| **ECOSTRESS (ISS)** | Dataset | LST a ~70 m, varias horas del día (capta el calor de la tarde) | Gratis (Earthdata / AppEEARS) | SÍ (según pasadas ISS) | Earthdata "ECOSTRESS LST" |
| **American Forests Tree Equity Score** | Web-app | Puntaje de equidad de dosel por barrio (dosel + salud + calor + demografía) | Gratis | **NO fuera de EEUU/UK/Toronto** — pero el *método* es replicable | https://www.treeequityscore.org |
| **Global Forest Watch (WRI)** | Web-app + API | Pérdida/ganancia de cobertura arbórea (Hansen, 30 m, anual) | Gratis/open + API | **SÍ (global)** — sirve para "cuánto dosel perdió Temuco año a año" | https://www.globalforestwatch.org |
| **Copernicus / C3S (ver sección 4)** | Datos + web-apps | ERA5, estrés térmico, atlas climático | Gratis | SÍ (global; UrbClim solo 100 ciudades EU) | https://climate.copernicus.eu |

**Lectura clave para Temuco:**
- **Tree Equity Score NO cubre Chile** (solo EEUU, y versiones UK/Toronto). El observatorio debe **replicar su lógica** con datos globales gratis (dosel + LST + índice socioeconómico del INE/censo).
- **Yale Global Surface UHI Explorer** y **Global Forest Watch** son los dos que funcionan *out-of-the-box* en Temuco.
- **"A global downstream approach to mapping surface UHI using open data" (2025)** · ScienceDirect S2950492925000057 · workflow open-source automatizado (Landsat + SRTM) — plantilla replicable.

---

## 4. Olas de calor — datasets/plataformas gratuitas

- **ERA5 (Copernicus C3S / CDS)** · reanálisis climático global · temperatura del aire horaria, ~31 km (0.25°), 1940–presente · **gratis** vía Climate Data Store (`cds.climate.copernicus.eu`, API `cdsapi` en Python) · **SÍ Chile**. Sirve para definir **olas de calor** (percentiles de Tmax) y dar contexto temporal a la LST satelital.
- **ERA5-HEAT / UTCI** · índice de estrés térmico (Universal Thermal Climate Index) derivado de ERA5, near-real-time (~5 días de latencia) · gratis · global.
- **C3S "Thermal Trace"** · web-app · >80 años de datos de estrés por calor y frío · gratis · global · https://climate.copernicus.eu/thermal-trace-decades-heat-and-cold-stress-data-your-fingertips
- **Copernicus Interactive Climate Atlas** · web-app · clima pasado y proyecciones · gratis · https://climate.copernicus.eu/copernicus-interactive-climate-atlas-guide-powerful-new-c3s-tool
- **Copernicus "Climate Variables for cities in Europe 2008–2017" (UrbClim, VITO)** · 100 m, ICU y estrés térmico · gratis · **solo 100 ciudades europeas** (no Chile, pero referencia metodológica).
- **DGAC/Meteochile** · datos nacionales de estaciones · gratis · Chile · blog divulgativo "Islas de Calor ¡Ciudades en llamas!" (2025) · https://blog.meteochile.gob.cl/2025/03/20/islas-de-calor-ciudades-en-llamas/
- **Observatorios de calor ciudadano (crowdsourced)**: campañas tipo **NOAA/CAPA Urban Heat Watch** (voluntarios con sensores en autos/bici) — modelo replicable por el observatorio para medir **temperatura del aire a nivel de calle** (complementa la LST satelital).

**Cómo se cruza con vegetación:** ERA5 da *cuándo* ocurre la ola de calor (fechas); en esas fechas se descarga la escena Landsat/ECOSTRESS y se mapea LST vs dosel/NDVI. Así se muestra que en plena ola de calor los barrios sin árboles están varios °C más calientes.

---

## 5. Justicia ambiental / equidad de sombra (herramientas open)

- **Concepto**: cruzar mapa de dosel (o LST) con mapa socioeconómico (censo/INE) → mostrar que los barrios pobres tienen **menos árboles y más calor**. Es el corazón del "Tree Equity Score".
- **Herramientas replicables gratis**:
  - Dosel: Google EIE Tree Canopy / ESA WorldCover (10 m) / Global Forest Watch / dosel propio desde NDVI Landsat/Sentinel-2.
  - Calor: LST Landsat (sección 1) o Yale UHI Explorer.
  - Demografía: **Censo Chile / INE** (manzanas censales), gratis.
  - SIG: **QGIS** (open) o GEE para superponer capas y correlacionar.
- **Método "Tree Equity" replicable**: (1) unidad = manzana/barrio; (2) variables = % dosel, LST/ICU, densidad poblacional, indicador de vulnerabilidad; (3) puntaje que prioriza dónde plantar. La metodología de American Forests es pública: https://www.treeequityscore.org/methodology
- **Evidencia de inequidad (Chile)**: en Santiago, *"los parques más frescos de las comunas más calurosas son al menos 0.6 °C más cálidos que cualquier área verde de las comunas del sector oriente"* — diferencia estructural en calidad/diseño del verde entre barrios ricos y pobres (ver sección 6).

---

## 6. Casos en Chile y LATAM (calor urbano + arbolado)

- **ICU de superficie del Área Metropolitana de Santiago con Terra-MODIS y ACP (2014)** · Sarricolea & Martín-Vide · Revista de Geografía Norte Grande (SciELO Chile) · DOI 10.4067/s0718-34022014000100009 · variables clave: **NDVI y albedo (relación negativa)**, densidad construida (positiva); ICU >5 °C en comunas centrales · **open access SciELO** · https://www.scielo.cl/scielo.php?pid=S0718-34022014000100009
- **Tesis "La isla de calor urbana de superficie y sus factores condicionantes: Santiago" (Sarricolea)** · TDX/UB · open · https://www.tdx.cat/handle/10803/86936 · **cifra clave: implementar áreas verdes donde no hay vegetación reduciría la ICU entre 1.2 y 5.5 °C**; +10.000 m² construidos/ha suben 1–2 °C.
- **Estudio "77 zonas frías" en comunas con mayores olas de calor (2025, Chile)** · las zonas frías (verde/agua) **reducen hasta 5.5 °C la temperatura superficial** · divulgación: https://www.cienciaenchile.cl/estudio-identifica-77-zonas-frias-en-comunas-con-mayores-olas-de-calor-reducen-hasta-55-c-la-temperatura-superficial/
- **"Isla de calor urbana de Santiago y microclima en el espacio público"** · Repositorio U. de Chile · open PDF · https://repositorio.uchile.cl/bitstream/handle/2250/170696/isla-de-calor-urbana-de-santiago.pdf
- **Romero et al. — patrones de crecimiento espacial y clima urbano de ciudades chilenas** · AEC · https://aeclim.org/wp-content/uploads/2016/02/0074_PU-SA-V-2006-H_ROMERO.pdf
- **Parque urbano Isla Cautín, Temuco (2023)** · Revista ARQ / SciELO Chile · DOI 10.4067/s0717-69962023000200070 · infraestructura hidroecológica y resiliencia — **caso local de Temuco** (verde urbano).
- **LATAM**: ICU en el entorno andino de **Cuenca-Ecuador** (2018, DOI 10.14198/ingeo2018.70.08); **Campeche, México** (SciELO Chile, DOI 10.4067/S0718-36072024000100008); **Puebla, México — barrio "Arboledas"** (2026, DOI 10.18537/est.v015.n029.a04); cubiertas vegetales para mitigar ICU (2024, ACE, DOI 10.5821/ace.19.56.12581).

---

## Fuentes / URLs consultadas
- Crossref API (mailto=cvivallos@gmail.com), SciELO/Dialnet, WebSearch (julio 2026).
- WRI Cooling Potential: https://www.wri.org/insights/urban-trees-cooling-potential
- npj Urban Sustainability 2025: https://www.nature.com/articles/s42949-025-00277-x
- Nature Comms 2026 (trees halve UHI): https://www.nature.com/articles/s41467-026-71825-x
- Yale Global Surface UHI Explorer: https://geospatial.yale.edu/global-surface-uhi-explorer
- Google EIE Tree Canopy: https://insights.sustainability.google/labs/treecanopy
- Global Forest Watch: https://www.globalforestwatch.org
- Tree Equity Score + método: https://www.treeequityscore.org/methodology
- Copernicus C3S / CDS: https://cds.climate.copernicus.eu · https://climate.copernicus.eu
- Ermida et al. 2020 GEE LST: https://www.mdpi.com/2072-4292/12/9/1471
- Sarricolea 2014 Santiago (SciELO): https://www.scielo.cl/scielo.php?pid=S0718-34022014000100009
- Zonas frías Chile 2025: https://www.cienciaenchile.cl/estudio-identifica-77-zonas-frias-en-comunas-con-mayores-olas-de-calor-reducen-hasta-55-c-la-temperatura-superficial/
