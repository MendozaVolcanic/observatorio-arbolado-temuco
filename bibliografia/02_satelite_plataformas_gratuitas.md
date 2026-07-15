# Plataformas y métodos satelitales GRATUITOS para monitoreo de arbolado urbano

**Proyecto:** Observatorio ciudadano de pérdida de arbolado urbano — Temuco, Chile (serie 2005–2025)
**Restricción dura:** solo GRATIS/open. GEE gratis para investigación/no-comercial cuenta como gratis. Imágenes comerciales de pago (Maxar, Planet full, etc.) NO.
**Fecha de compilación:** 2026-07-15
**Metodología:** APIs gratis (Crossref con mailto) → WebSearch/WebFetch para docs de plataformas y catálogos GEE.

> Nota de honestidad metodológica de entrada: **ningún dataset global gratuito resuelve el árbol de calle individual de forma fiable en serie temporal larga.** Todo lo gratis-y-reproducible-2005→2025 vive a 10–30 m (Landsat/Sentinel). Lo que sí resuelve el árbol individual (Maxar 0.5 m, WorldView) o es de pago, o es un snapshot puntual (Meta 1 m, un solo año). El diseño realista para Temuco combina: (a) **backbone de tendencia** a 30 m con Landsat en GEE (única fuente que llega a 2005), y (b) **validación puntual** por fotointerpretación humana sobre imagen de alta resolución gratuita (i-Tree Canopy / Google satellite). Detalle abajo.

---

## 1. Google Earth Engine (GEE) + geemap — BACKBONE RECOMENDADO

- **Nombre:** Google Earth Engine (plataforma de cómputo geoespacial en la nube) + `geemap` (librería Python de Qiushi Wu para GEE con mapas interactivos).
- **Tipo:** Plataforma de análisis en la nube (JavaScript Code Editor + API Python) / librería open-source.
- **Qué hace:** Da acceso y cómputo sobre petabytes de archivo satelital sin descargar nada; permite construir composites, índices (NDVI/EVI), clasificaciones y detección de cambio a escala de ciudad/barrio con unos pocos scripts.
- **Dato gratuito:** SÍ. GEE es gratis para uso académico, de investigación y sin fines de lucro (registro en https://earthengine.google.com; el observatorio ciudadano califica). Uso comercial requiere plan de pago, pero el observatorio NO es comercial.
- **Archivos clave accesibles gratis dentro de GEE:**
  - **Landsat Collection 2** (L4/5 TM 1984+, L7 ETM+ 1999+, L8 OLI 2013+, L9 2021+): **30 m**, revisita 16 días. **Es la ÚNICA fuente óptica gratuita que cubre 2005** con continuidad → imprescindible para la serie 2005–2025.
  - **Sentinel-2 MSI** (2015-06+): **10 m** en bandas visibles/NIR, revisita ~5 días. Mejor resolución pero sólo desde 2015 → cubre la mitad reciente de la serie.
  - **Sentinel-2 red-edge** (bandas 5,6,7 a 20 m): útil para vigor/tipo de vegetación.
- **Resolución:** 30 m (Landsat) / 10 m (Sentinel-2).
- **Cobertura temporal:** 1984→presente (Landsat) / 2015→presente (Sentinel-2).
- **Código abierto / no-código:** Código (JS o Python). `geemap` es open-source (MIT) en https://github.com/gee-community/geemap con libro y tutoriales reproducibles (https://geemap.org, https://book.geemap.org). El Code Editor JS también sirve sin instalar nada.
- **¿Cubre Chile / Temuco?** SÍ. Cobertura global; Temuco (~38.7°S) perfectamente cubierto por Landsat y Sentinel-2.
- **Cómo se usa para change detection de dosel urbano:** (1) construir composites anuales/estacionales libres de nube por mediana; (2) calcular NDVI por año; (3) diferencia NDVI entre años (ΔNDVI) o regresión temporal de tendencia (pixel-wise trend / Theil-Sen) para mapear pérdida de verdor; (4) opcional: clasificación supervisada árbol/pasto/impermeable con Random Forest. Para roturas abruptas existe **LandTrendr** y **CCDC** (algoritmos de segmentación temporal implementados nativamente en GEE), ideales para fechar el año de pérdida de un parche arbóreo.
- **Limitación honesta para árbol de calle:** a 30 m un píxel Landsat mezcla techo+calle+vereda+copa; un árbol de calle aislado (copa 4–8 m) es sub-píxel y se pierde. Sentinel-2 a 10 m detecta agrupaciones/plazas pero aún no el individuo. Sirve para **tendencia de verdor y pérdida de parches**, no para censo de ejemplares.
- **Cita/URL:** Gorelick, N. et al. (2017). "Google Earth Engine: Planetary-scale geospatial analysis for everyone." *Remote Sensing of Environment* 202:18–27. https://doi.org/10.1016/j.rse.2017.06.031 · Catálogo: https://developers.google.com/earth-engine/datasets · geemap: Wu, Q. (2020). *JOSS* 5(51):2305. https://doi.org/10.21105/joss.02305

---

## 2. Google Dynamic World V1 — land cover 10 m near-real-time con clase "trees"

- **Nombre:** Dynamic World V1 (Google + WRI).
- **Tipo:** Dataset de land cover probabilístico near-real-time (deep learning sobre cada escena Sentinel-2).
- **Qué hace:** Clasifica cada píxel Sentinel-2 en 9 clases (incluida **"trees"**) con probabilidades continuas, casi en tiempo real por cada pasada del satélite.
- **Dato gratuito:** SÍ, alojado abiertamente en GEE (`GOOGLE/DYNAMICWORLD/V1`).
- **Resolución:** 10 m.
- **Cobertura temporal:** **2015-06-27 → presente** (una predicción por cada escena S2 L1C con nubes ≤35%). Confirmado en el Earth Engine Data Catalog.
- **Código abierto / no-código:** Código vía GEE. También visor no-código en https://dynamicworld.app.
- **¿Cubre Chile?** SÍ, global.
- **¿Sirve para cambio de árboles urbanos?** Parcialmente. La clase "trees" tiene buena exactitud (los estudios reportan mejor precisión para clases estables como agua y árboles). Como es por-escena y probabilístico, se puede construir la **probabilidad media anual de "trees"** por píxel y comparar entre años → mapa de ganancia/pérdida de dosel a 10 m desde 2015. **Limitación:** empieza en 2015 (no llega a 2005); a 10 m sigue sin resolver el árbol de calle individual y la clase "trees" en tejido urbano denso se confunde con "grass"/"shrub" en píxeles mixtos.
- **Cita/URL:** Brown, C.F. et al. (2022). "Dynamic World, Near real-time global 10 m land use land cover mapping." *Scientific Data* 9:251. https://doi.org/10.1038/s41597-022-01307-4 · Catálogo: https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1

---

## 3. Land cover globales de referencia (ESA WorldCover, ESRI, tree-canopy layers)

### 3a. ESA WorldCover 10 m
- **Tipo:** Mapa global de cobertura de suelo (Sentinel-1+2), clase "Tree cover".
- **Gratuito:** SÍ (CC-BY 4.0). En GEE (`ESA/WorldCover/v100`, `v200`), AWS Open Data y https://esa-worldcover.org.
- **Resolución:** 10 m.
- **Cobertura temporal:** **snapshot de 2 años**: 2020 (v100) y 2021 (v200). **v100 y v200 usan algoritmos distintos → NO comparar directamente para detectar cambio** (el propio ESA advierte que las diferencias mezclan cambio real y cambio de algoritmo).
- **No-código:** visor web en esa-worldcover.org.
- **¿Cubre Chile?** SÍ, global.
- **Utilidad para Temuco:** mapa base/máscara de "dónde hay árbol" en 2020–21, no serie de cambio.
- **Cita:** Zanaga, D. et al. (2021/2022) ESA WorldCover. Zenodo https://doi.org/10.5281/zenodo.7254221

### 3b. ESRI 10 m Annual Land Cover (Impact Observatory / Esri / Microsoft)
- **Gratuito:** SÍ. Basado en Sentinel-2, clase "Trees". En GEE community catalog y https://livingatlas.arcgis.com/landcover.
- **Resolución:** 10 m. **Cobertura temporal:** **anual 2017→presente** (ventaja: es serie anual, mejor para cambio que WorldCover).
- **No-código:** visor "Sentinel-2 Land Cover Explorer" (ArcGIS Living Atlas), con swipe temporal — un ciudadano puede ver cambio sin código.
- **¿Cubre Chile?** SÍ, global.
- **Limitación:** 10 m, clase árbol genérica; buen tamiz de cambio de dosel a nivel barrio, no ejemplar.

### 3c. Google/WRI + Meta High-Resolution Canopy Height (canopy layers)
- Ver sección 6 (altura de dosel). Son capas de **altura**, no de land cover; el Meta 1 m es la única capa gratis que insinúa el árbol individual (pero es snapshot, no serie).

---

## 4. i-Tree (USDA Forest Service) — GRATIS, fotointerpretación humana

- **Nombre:** i-Tree Canopy (y i-Tree Landscape) — suite del USDA Forest Service.
- **Tipo:** Herramienta web de estimación de cobertura por **muestreo aleatorio + fotointerpretación manual** sobre imagen aérea de Google.
- **Qué hace:** El usuario clasifica a mano N puntos aleatorios (árbol / pasto / impermeable / etc.) sobre Google Maps satelital; la herramienta calcula % de cobertura de dosel con intervalos de confianza estadísticos.
- **Dato gratuito:** SÍ, 100% gratis, sin instalación (https://canopy.itreetools.org).
- **Resolución:** la de la imagen de Google (submétrica donde exista) → **resuelve el árbol individual** porque lo interpreta un humano.
- **Cobertura temporal:** la que ofrezca el histórico de imágenes de Google Earth para el área (variable; en Temuco suele haber varias fechas 2005–2025 vía Google Earth Pro histórico). i-Tree Canopy en sí no maneja series; se corre una vez por fecha.
- **Código abierto / no-código:** **NO-CÓDIGO** (ideal para ciudadanos). No es open-source pero es gratuito y web.
- **¿Cubre Chile / funciona fuera de EEUU?** SÍ para i-Tree Canopy: funciona en cualquier parte del mundo porque sólo necesita la imagen de Google y puntos aleatorios; se puede cargar un shapefile del área o dibujar el polígono. **Matiz importante:** las herramientas de i-Tree que estiman beneficios ecosistémicos con especies/clima (i-Tree Eco, Landscape) están *adaptadas* sólo a un set de países (Canadá, Colombia, México, Australia, Europe/UK, etc.) — **Chile NO está en la lista de adaptaciones oficiales**, así que i-Tree Eco/Landscape corren con clima "internacional" limitado. Pero **i-Tree Canopy (solo % cobertura) sí sirve en Temuco sin restricción**.
- **Utilidad para el observatorio:** es el **método de validación estándar-oro barato**: fotointerpretación estratificada de puntos en dos fechas (p.ej. 2005 vs 2025) da un % de dosel comparable con IC — defendible ante autoridades y reproducible por voluntarios.
- **Cita/URL:** i-Tree Canopy, USDA Forest Service. https://canopy.itreetools.org · Internacional: https://www.itreetools.org/support/resources-overview/i-tree-international · Nowak, D.J. et al. metodología en itreetools.org.

---

## 5. Global Forest Watch / Hansen Global Forest Change — ¿sirve para árbol urbano?

- **Nombre:** Hansen Global Forest Change (UMD) + plataforma Global Forest Watch (WRI).
- **Tipo:** Dataset global de cobertura arbórea 2000 y pérdida/ganancia anual + visor web.
- **Qué hace:** Mapea "tree cover" 2000 y **pérdida bruta anual 2001→presente** a partir de Landsat.
- **Dato gratuito:** SÍ. En GEE (`UMD/hansen/global_forest_change`), en GFW (https://globalforestwatch.org) y descarga directa.
- **Resolución:** **30 m** (Landsat).
- **Cobertura temporal:** cobertura 2000; pérdida anual 2001→~2023 (se actualiza).
- **Código abierto / no-código:** ambos — GEE (código) y GFW (visor no-código con alertas y descarga por polígono).
- **¿Cubre Chile?** SÍ, global.
- **¿Sirve para pérdida de árbol URBANO?** **Limitado / mayormente NO para la ciudad.** Diseñado para **bosque de dosel cerrado**: define pérdida como remoción de rodal a 30 m. En tejido urbano subestima fuerte el arbolado disperso: un árbol de calle o una plaza pequeña rara vez supera el umbral de "forest" ni el tamaño mínimo detectable a 30 m. El propio WRI reconoce que las evaluaciones globales **subestiman la cobertura arbórea dispersa en entornos urbanos**. Puede detectar la tala de un paño arbolado grande (parque, cerro, remoción por proyecto inmobiliario) en la periferia de Temuco, pero **no el goteo de pérdida de árboles de calle**.
- **Alternativa WRI para árbol disperso:** **Tropical Tree Cover** (WRI/Land & Carbon Lab), Sentinel-2 a **10 m**, año 2020, disponible en GFW y GEE, pensado justamente para árbol fuera de bosque (drylands, urbano, riparian). Mejor que Hansen para lo urbano, pero es snapshot 2020 y cubre trópicos/subtrópicos — **verificar cobertura a 38°S (Temuco queda en el límite sur de la máscara "tropical"; probablemente fuera).**
- **Cita/URL:** Hansen, M.C. et al. (2013). "High-Resolution Global Maps of 21st-Century Forest Cover Change." *Science* 342:850–853. https://doi.org/10.1126/science.1244693 · GFW blog comparación datasets: https://www.globalforestwatch.org/blog/data-and-tools/tree-cover-data-comparison/

---

## 6. Índices y métodos para distinguir ÁRBOL de PASTO con satélite

El problema central del observatorio: NDVI alto lo tienen **tanto el árbol como el pasto/césped**. Métodos gratuitos para separarlos:

- **NDVI solo → insuficiente.** No distingue árbol de pasto (ambos verdes). Sirve para "hay/no hay vegetación" y para tendencia de verdor total, no para tipo.
- **Fenología / series temporales (el método más potente y gratis):** el pasto/césped y los cultivos tienen ciclo estacional marcado (verde en primavera-verano, seco en otoño-invierno o tras siega), mientras el **árbol perennifolio mantiene NDVI alto todo el año** y el árbol caducifolio tiene una fenología distinta y más amplia que el pasto. Construir el **perfil temporal intra-anual de NDVI** (amplitud, mínimo invernal, integral) con Landsat/Sentinel-2 en GEE separa árbol de pasto mucho mejor que una sola imagen. **Es la técnica recomendada** dado que es gratis y reproducible con el archivo temporal.
- **Textura (GLCM):** las copas arbóreas dan textura rugosa/sombreada; el césped es liso. Métricas GLCM (varianza, homogeneidad) sobre Sentinel-2 10 m ayudan, aunque a 10 m la textura del árbol individual es débil.
- **Red-edge (Sentinel-2 bandas 5–7, 20 m):** índices red-edge (NDRE, IRECI) y contenido de clorofila/estructura foliar aportan separación adicional árbol vs herbáceo.
- **Altura del dosel (la señal más limpia, pero cara de obtener gratis):** un árbol tiene altura (>2–3 m) y el pasto no. Fuentes gratuitas de altura:
  - **Meta/WRI High-Resolution Canopy Height, 1 m**: la única capa gratis que resuelve el árbol individual. En GEE y AWS Open Data. **PERO es snapshot (2020, actualizado 2026), no serie temporal** → sirve como capa de "dónde hay árbol y qué alto" para enmascarar/validar, no para el cambio 2005–2025. https://gee-community-catalog.org/projects/meta_trees/
  - **Global canopy height 10 m (Lang et al. 2023, ETH)**: GEDI+Sentinel-2, año 2020, gratis en GEE. https://doi.org/10.1038/s41559-023-02206-6
  - **GEDI L2A** (footprints LiDAR espaciales, 25 m, 2019+): altura real pero muestreo disperso, no cobertura continua; útil para calibrar.
  - **Fotogrametría propia (drone/imagen histórica):** un DSM propio da altura y resuelve el árbol de calle, pero requiere procesamiento y no cubre 2005 retroactivamente salvo con pares estéreo de imagen aérea histórica.
- **Limitación real de 10 m / 30 m para árbol de calle:** un árbol urbano típico (copa 3–8 m de diámetro, 7–50 m² de área) es **sub-píxel a 10 m** (píxel S2 = 100 m²) y muy sub-píxel a 30 m (píxel Landsat = 900 m²). En calles arboladas la señal se mezcla con asfalto y techos. Conclusión honesta: **para inventario de ejemplares hace falta imagen submétrica + fotointerpretación/deep learning; los índices a 10–30 m sólo dan agregados de dosel a nivel de manzana/barrio.**

---

## 7. Plataformas web LISTA-PARA-USAR (no-código) para ciudadanos

Ordenadas por utilidad para que un vecino de Temuco vea cambio de verdor sin programar:

1. **i-Tree Canopy** (sección 4) — no-código, gratis, resuelve árbol individual por fotointerpretación humana, funciona en Temuco. **La más recomendada para el componente ciudadano.** https://canopy.itreetools.org
2. **ESRI Sentinel-2 Land Cover Explorer** (ArcGIS Living Atlas) — swipe temporal 2017→presente a 10 m, clase "Trees", global, gratis, navegador. https://livingatlas.arcgis.com/landcoverexplorer
3. **Global Forest Watch** — visor no-código con pérdida anual por polígono y descarga; útil para paños grandes en la periferia, limitado en calle. https://globalforestwatch.org
4. **Dynamic World app** — visor no-código de la clase "trees" a 10 m desde 2015. https://dynamicworld.app
5. **Google Earth Pro (histórico)** — gratis, imágenes históricas submétricas con línea de tiempo; permite **comparación visual 2005 vs 2025 de una cuadra** y es la fuente de imagen para i-Tree Canopy. No cuantifica solo, pero es potentísimo para evidencia visual ciudadana. https://www.google.com/earth/versions/
6. **ESA WorldCover viewer** — snapshot 2020/2021, base de referencia. https://esa-worldcover.org
7. **Copernicus Browser (Sentinel Hub / EO Browser)** — gratis, permite ver Sentinel-2 histórico 2015+, calcular NDVI on-the-fly y comparar fechas sin código. Muy usable por ciudadanos. https://browser.dataspace.copernicus.eu

---

## SÍNTESIS: qué es realmente gratis + reproducible + llega a 2005

| Necesidad | Herramienta gratis | Llega a 2005 | Resuelve árbol de calle |
|---|---|---|---|
| Tendencia de verdor/dosel serie larga | **GEE + Landsat 30 m** | **SÍ (1984+)** | No (agregado barrio) |
| Cambio dosel 10 m reciente | GEE + Sentinel-2 / Dynamic World / ESRI | No (2015/2017+) | No |
| Validación puntual árbol individual | **i-Tree Canopy + Google Earth histórico** | Sí (según imagen) | **SÍ (humano)** |
| Capa "dónde/qué alto" | Meta 1 m / Lang 10 m canopy height | No (snapshot 2020) | Sí (1 m), snapshot |
| Pérdida de paño grande | Hansen/GFW 30 m | Sí (2001+) | No (solo bosque) |
| Separar árbol de pasto | **Series temporales NDVI + red-edge + textura en GEE** | Sí | Parcial |

**Recomendación de arquitectura:** GEE (Landsat backbone 2005–2025 + Sentinel-2/Dynamic World refuerzo 2015–2025, con fenología para separar árbol/pasto) como motor cuantitativo, y **i-Tree Canopy sobre Google Earth histórico** como capa de validación y componente ciudadano/participativo. Meta 1 m como referencia estructural puntual. Hansen/GFW solo para eventos de tala grandes en periferia.
