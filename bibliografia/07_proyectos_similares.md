# Proyectos y estudios similares al observatorio ciudadano de arbolado urbano (Temuco)

**Objetivo de esta ficha:** no metodología genérica de NDVI (ya cubierta en `02_satelite_plataformas_gratuitas.md`), sino **proyectos/estudios que hagan el CONJUNTO**: (a) detección temporal de pérdida de dosel urbano con satélite, (b) cruce con temperatura de superficie/isla de calor, (c) cruce con expansión inmobiliaria, (d) dashboard web público con enfoque de ciencia ciudadana.
**Fecha de compilación:** 2026-07-15. **Metodología:** WebSearch/WebFetch (Crossref/S2 ya explotados en fichas 02–04; para "conjunto de 4 piezas" el material vive sobre todo en papers de caso-de-ciudad y en plataformas, no en bases bibliográficas puras).

Formato: **nombre · tipo · qué hace · qué se parece a Temuco · qué copiar/aprender · ¿open? · URL/cita.**

---

## 1. Observatorios/plataformas operativas de arbolado urbano con teledetección

### 1.1 Tree Equity Score (American Forests) — el modelo a seguir más de cerca
- **Tipo:** plataforma/observatorio público (web-app + API + metodología documentada).
- **Qué hace:** puntaje 0–100 por barrio que combina % de dosel arbóreo (satélite/LiDAR), temperatura de superficie, densidad poblacional e indicadores socioeconómicos (ingreso, salud, empleo, edad, raza) para priorizar dónde plantar. Serie temporal año a año desde 2021, con "National Explorer" que permite comparar cambio de dosel entre ciudades EEUU.
- **Similitud con Temuco:** es exactamente el ensamble (a)+(b)+cruce socioeconómico que Daniela quiere, ya con dashboard público y metodología publicada.
- **Qué copiar:** (1) la **fórmula del puntaje** (dosel + calor + prioridad social, ponderada) es pública y replicable con datos gratis (INE en vez de censo EEUU); (2) el patrón de **"national/city explorer" con swipe por barrio**; (3) su justificación narrativa ("equidad de sombra") es un argumento político fuerte, útil para el Senado/Muni de Temuco.
- **¿Open?** Metodología abierta (treeequityscore.org/methodology) y hay repo parcial en GitHub (`american-forests/tree-equity-score`), pero el dato subyacente y el hosting son de American Forests; **NO cubre Chile**. Lo replicable es el método, no el dato.
- **URL:** https://www.treeequityscore.org · https://www.treeequityscore.org/methodology

### 1.2 Google Environmental Insights Explorer (EIE) — Tree Canopy Lab
- **Tipo:** plataforma web de Google (parte de Sustainability/Insights).
- **Qué hace:** estima % de dosel por manzana con imágenes aéreas + IA, identifica zonas con déficit de sombra y "dónde plantar" para +40.000 ciudades a nivel mundial (Tree Canopy Lab en cientos de ciudades).
- **Similitud:** dashboard público gratis con capa de dosel a escala de manzana, gratuito, sin backend propio para el usuario final.
- **Qué copiar:** la UI de "antes/después + potencial de plantación" es un buen patrón de dashboard aunque el dato de Temuco haya que generarlo con Landsat/Sentinel propio en vez del pipeline interno de Google.
- **¿Open?** Gratis para consultar, no código abierto, no API pública documentada para bajar el raster. Cobertura de Temuco **sin confirmar** (hay que revisar el listado de ciudades).
- **URL:** https://insights.sustainability.google/labs/treecanopy

### 1.3 Treepedia (MIT Senseable City Lab) — Green View Index a nivel de calle
- **Tipo:** metodología + código abierto (ya documentado en ficha 04, aquí en el contexto de "conjunto").
- **Qué hace:** mide verdor visible desde la perspectiva del peatón (Green View Index) sobre panoramas de calle en decenas de ciudades del mundo, con mapa público comparativo entre ciudades.
- **Similitud:** aporta la pieza "percepción ciudadana a nivel de calle" que complementa el satélite top-down — mismo espíritu de "mostrarle al público cuánto verde ve al caminar".
- **Qué copiar:** el concepto de comparar Temuco con otras ciudades chilenas/mundiales en un único índice divulgativo (aunque haya que sustituir Google Street View por Mapillary, ver ficha 04 §2–3).
- **¿Open?** Código sí (GitHub), pero depende de imágenes de calle con licencia variable.
- **URL:** https://senseable.mit.edu/treepedia · https://github.com/mittrees/Treepedia_Public

### 1.4 EU Urban Atlas / Copernicus Land Monitoring — referencia de land cover urbano serie
- **Tipo:** producto institucional europeo de cobertura de suelo urbano de alta resolución (incluye clase de vegetación) para +788 ciudades europeas, con actualizaciones periódicas (2006, 2012, 2018, 2021) que permiten **detectar cambio** de forma comparable entre fechas.
- **Similitud:** es el ejercicio de "serie temporal de cobertura urbana comparable" al que aspira Temuco, aunque a escala continental y con financiamiento institucional (no ciencia ciudadana).
- **Qué copiar:** la lógica de **clases y umbrales estandarizados entre fechas** (para que el cambio sea comparable y no artefacto de metodología, el mismo problema que ya se documentó con ESA WorldCover v100 vs v200 en ficha 02) es la lección metodológica más útil de este caso.
- **¿Open?** Sí, datos abiertos (land.copernicus.eu), pero **no cubre Chile** (solo UE) — sirve como referencia de diseño, no como fuente de datos.
- **URL:** https://land.copernicus.eu/en/products/urban-atlas

### 1.5 UK Canopy Cover Webmap — ciencia ciudadana + webmap público (Reino Unido)
- **Tipo:** estudio + plataforma web pública, resultado de un proyecto de ciencia ciudadana.
- **Qué hace:** más de 400 voluntarios entre 2018–2022 recolectaron muestras de cobertura de dosel por barrio ("ward") en ciudades y pueblos del Reino Unido; los resultados se publican en un **webmap público** comparable entre localidades.
- **Similitud:** es de los pocos casos documentados donde la **ciencia ciudadana alimenta directamente un mapa público de dosel**, el mismo patrón que Daniela busca (voluntarios → dato → mapa).
- **Qué copiar:** el protocolo de muestreo por voluntarios (compatible con i-Tree Canopy, ya en ficha 02 §4) y la publicación agregada por barrio en vez de por punto individual (protege privacidad y es más fácil de mantener).
- **¿Open?** El estudio es de acceso restringido en Tandfonline (paywall parcial); el webmap resultante es público. **Peer J / RICS journal, 2023.**
- **Cita:** "The canopy cover Webmap of the United Kingdom's towns and cities" (2023), *Land International/RICS*, DOI vía https://www.tandfonline.com/doi/full/10.1080/03071375.2023.2233864

---

## 2. Papers de "urban tree canopy change detection" con serie temporal Landsat/Sentinel — casos de una ciudad

### 2.1 Ontario (Canadá) — casi 50 años de cambio de dosel con Landsat
- **Qué hace:** construye una serie de % de cobertura arbórea (TCC) **1972–2020** para un paisaje urbano-rural del sur de Ontario, entrenando modelos random forest con TCC interpretado visualmente sobre imagen de alta resolución y propagándolo sobre el archivo Landsat completo.
- **Similitud directa:** es el ejercicio metodológico más parecido al objetivo "serie 2005–2025" de Temuco — mismo problema (resolución Landsat gruesa vs. necesidad de serie larga), misma solución (fotointerpretación de puntos de entrenamiento + modelo + Landsat histórico).
- **Qué copiar:** el flujo entero es replicable en GEE: puntos de entrenamiento por fotointerpretación (o i-Tree Canopy) en 2–3 fechas ancla, random forest sobre bandas Landsat, y extrapolación a toda la serie 1984+.
- **¿Open?** Publicado en *Canadian Journal of Remote Sensing* (Taylor & Francis, acceso mixto — verificar OA).
- **Cita:** "Using Landsat time-series to investigate nearly 50 years of tree canopy cover change across an urban-rural landscape in southern Ontario" (2024). DOI 10.1080/07038992.2024.2445836. https://www.tandfonline.com/doi/full/10.1080/07038992.2024.2445836

### 2.2 Portland, Oregon (EEUU) — drivers de pérdida de dosel en ciudad en crecimiento
- **Qué hace:** cuantifica pérdida de UTC 2014–2020 con NAIP 1 m + random forest, y la explica con modelos espaciales autorregresivos cruzando variables demográficas, biofísicas y **de política urbana** (zonificación, permisos).
- **Similitud:** es el paper que más se acerca a la pieza "(c) expansión inmobiliaria" del pedido — mide directamente qué variables de desarrollo urbano predicen dónde se pierde dosel.
- **Qué copiar:** el diseño de modelo (regresión espacial con variable de "permiso de construcción/subdivisión" como predictor de pérdida de dosel) es trasladable a Temuco cruzando el catastro de permisos del MINVU/Observatorio Urbano (ya identificado en ficha 04 §5) con la capa de pérdida de dosel Landsat.
- **¿Open?** Sí, MDPI *Sustainability* 16(5):1803, open access.
- **Cita:** "Drivers of Tree Canopy Loss in a Mid-Sized Growing City: Case Study in Portland, OR (USA)" (2024). DOI 10.3390/su16051803. https://www.mdpi.com/2071-1050/16/5/1803

### 2.3 Christchurch, Nueva Zelanda — pérdida de dosel por intensificación residencial
- **Qué hace:** mide pérdida de dosel urbano 2016–2021 y muestra que la **redensificación de propiedades residenciales** (subdivisión de sitios, "housing intensification") explica más pérdida de árboles que la reconstrucción simple tras terremoto.
- **Similitud:** es el caso más directo de "pérdida de arbolado ligada a expansión/densificación inmobiliaria", con relevancia directa para el argumento de Temuco sobre loteos y subdivisión de sitios con árboles patrimoniales.
- **Qué copiar:** el marco conceptual "green vs growth" (tensión entre normativa de densificación y retención de dosel) es el mismo que se puede argumentar con la Ordenanza de Temuco 2021 y el Observatorio Urbano MINVU.
- **¿Open?** ScienceDirect (*Urban Forestry & Urban Greening*), verificar acceso — DOI 10.1016/j.ufug.2025.128123 (ver enlace).
- **Cita:** "Green vs growth: The effect of residential intensification on urban tree canopy loss in Christchurch, New Zealand" (2025). https://www.sciencedirect.com/science/article/pii/S2210670725005529

### 2.4 Beijing (China) — fenología urbana a escala de calle con Landsat+Sentinel+PlanetScope
- **Qué hace:** combina tres sensores (Landsat-8 30 m, Sentinel-2 10 m, PlanetScope 3 m) para reconstruir la fenología del arbolado de calle en el centro de Beijing, resolviendo mejor el problema de "árbol de calle sub-píxel" que documentamos en ficha 02.
- **Similitud:** ataca exactamente la limitación honesta que ya identificamos (30 m no resuelve el árbol individual) fusionando resoluciones — un camino a evaluar si Temuco consigue acceso a PlanetScope (Planet ofrece licencias gratis para investigación/no-comercial via NICFI/Education & Research).
- **¿Open?** MDPI *Remote Sensing*, open access.
- **Cita:** DOI 10.3390/rs16132351. https://www.mdpi.com/2072-4292/16/13/2351

---

## 3. Papers que combinan pérdida de dosel urbano CON temperatura de superficie/isla de calor en una ciudad concreta

### 3.1 Worcester, Massachusetts (EEUU) — "experimento natural" de pérdida y ganancia de dosel y LST
- **Qué hace:** aprovecha que Worcester perdió y ganó dosel de forma abrupta 2008–2015 (por plaga del escarabajo asiático) como "experimento natural" para medir el efecto causal sobre LST: **picos de LST de +1 a +6 °C** en zonas de pérdida de dosel, y **extensión del período cálido de verano hasta 15 días** donde se perdió el dosel.
- **Similitud:** exactamente el diseño (a)+(b) del pedido — serie temporal de dosel cruzada con LST Landsat en una sola ciudad, con causa identificable (aquí plaga; en Temuco sería tala/subdivisión).
- **Qué copiar:** el uso de LST **por fecha/estación** (no solo promedio anual) para mostrar que el efecto de pérdida de dosel es más fuerte en pico de verano — mensaje divulgativo potente para Temuco en enero-febrero.
- **¿Open?** US Forest Service (dominio público), ya referenciado parcialmente en ficha 03 (Zhou et al. 2017 es de este mismo grupo/dataset).
- **Cita:** Elmes, A. et al., "Effects of urban tree canopy loss on land surface temperature magnitude and timing" — ver también https://research.fs.usda.gov/treesearch/54836 (USDA, público) y https://www.fs.usda.gov/nrs/pubs/jrnl/2017/nrs_2017_elmes_001.pdf (PDF público).

### 3.2 Columbia, Carolina del Sur (EEUU) — machine learning + LST, 14 años
- **Qué hace:** mapea dosel con ML sobre imagen satelital y LST derivada de Landsat térmico durante 14 años, mostrando que **la temperatura sube donde el dosel se pierde y continúa el desarrollo urbano** — casi el mismo enunciado que el pedido de Daniela.
- **Similitud:** metodología de bajo costo (ML + Landsat gratis) aplicable 1:1 en GEE para Temuco.
- **¿Open?** MDPI (revista *Geomatics* 3(2):19), open access.
- **Cita:** "Machine Learning in Urban Tree Canopy Mapping: A Columbia, SC Case Study for Urban Heat Island Analysis" (2023). https://www.mdpi.com/2673-7086/3/2/19

### 3.3 Aarhus, Dinamarca — LST + índices espectrales tipo NDVI
- **Qué hace:** estima LST desde Landsat 8 térmico y prueba combinaciones de bandas tipo-NDVI para explicar la LST; diferencia rural-urbana hasta 3.96 °C, diferencia entre zonas cálidas/frías hasta 13.26 °C dentro de la misma ciudad.
- **Similitud:** buen ejemplo de reporte de cifras "de titular" (igual a las que ya reunimos en ficha 03 §2) pero con metodología reproducible expuesta paso a paso.
- **¿Open?** Verificar (no confirmado en esta pasada).

### 3.4 Bogotá norte (Colombia) — LST + EVI 22 años, ¿la normativa protege el verde?
- **Qué hace:** analiza **22 años (2000–2021)** de EVI y LST con MODIS (1 km, compuestos anuales, 1.004 imágenes de temperatura y 496 de vegetación) sobre 6.930 ha del norte de Bogotá, comparando una zona con plan de manejo urbano y una reserva natural protegida (Reserva Thomas van der Hammen). Con regresión pixel a pixel y test de Mann-Kendall encuentra que **ambas zonas muestran la misma tendencia de más calor y menos vegetación** (correlación 0.92 temperatura, 0.87 vegetación) pese a la protección legal — conclusión: la urbanización sobrepasa la normativa.
- **Similitud:** es el caso LATAM más cercano al conjunto completo (a)+(b)+(c): serie satelital larga de vegetación+calor cruzada explícitamente con la pregunta "¿la normativa de protección funciona frente a la expansión urbana?" — la misma pregunta política que puede hacerse en Temuco respecto a ordenanzas de arbolado vs. permisos de edificación.
- **Qué copiar:** el diseño comparativo "zona protegida vs. zona sin protección" como forma de aislar el efecto normativo, y el uso de Mann-Kendall (test no paramétrico de tendencia, gratis en Python/R) para probar significancia estadística de la tendencia de pérdida — más riguroso que solo "ΔNDVI entre dos años".
- **¿Open?** SÍ, acceso abierto CC BY-NC 4.0, *Investigaciones Geográficas* (UNAM, México — revista SciELO).
- **Cita:** "¿Es detectable empíricamente la protección normativa del territorio? Análisis de las tendencias de temperatura y vegetación del área norte de Bogotá con sensores remotos" (2024). https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-46112024000100104

---

## 4. Casos en Chile y LATAM de monitoreo de arbolado urbano con satélite (complemento a ficha 04 §6)

### 4.1 Bogotá — Arbolapp + Geoportal de Bosques Urbanos + mapa interactivo ciudadano ⭐ (modelo LATAM más completo)
- **Tipo:** conjunto de 3 piezas públicas del Distrito + un mapa hecho por un ciudadano independiente sobre datos abiertos.
- **Qué hace:** (1) **Geoportal de Datos Abiertos de los Bosques Urbanos** (bogota.gov.co) — permite a la ciudadanía ver zonas de conservación y **proponer nuevas**; (2) **Arbolapp Bogotá** — app con conteo de árboles plantados por localidad e identificación de zonas con déficit de cobertura; (3) **mapa interactivo de arbolado** hecho por un usuario (@jupaneira) sobre datos del Jardín Botánico de Bogotá publicados en IDECA (infraestructura de datos abierta distrital), con ~1.5 millones de árboles geolocalizados, filtro por especie/localidad y capa de intensidad de cobertura (datos de 2005 a 2022, no todos actualizados).
- **Similitud:** es el ejemplo LATAM que más se parece en espíritu al objetivo de Daniela — dato oficial abierto (censo, no necesariamente satelital) + posibilidad de participación ciudadana ("proponer zonas de conservación") + mapa público reutilizado por un tercero fuera del gobierno.
- **Qué copiar:** (1) el patrón "gobierno publica el dato crudo en un portal de datos abiertos (IDECA≈IDE Temuco) y un tercero construye el mapa bonito encima" — Daniela puede hacer exactamente esto si logra que la Muni de Temuco publique su catastro de arbolado (pendiente, ver ficha 04 §5); (2) el mecanismo de "proponer nueva zona de conservación" como forma de participación ciudadana más allá de solo mirar el mapa.
- **¿Open?** Sí — datos abiertos del Distrito vía IDECA; el mapa de terceros usa Leaflet/herramientas estándar.
- **URL:** https://bogota.gov.co/mi-ciudad/ambiente/bogota-cuenta-con-geoportal-de-datos-abiertos-de-los-bosques-urbanos · https://www.ideca.gov.co · mapa ciudadano: https://cambiocolombia.com/medio-ambiente/articulo/2023/3/asi-es-el-mapa-interactivo-del-arbolado-urbano-de-bogota

### 4.2 CEDEUS (Centro de Desarrollo Urbano Sustentable, Chile) — Observatorio con dashboard de indicadores
- **Tipo:** observatorio universitario (PUC + otras) con dashboard de indicadores urbanos para la Región Metropolitana.
- **Qué hace:** publica indicadores urbanos (incluye componentes de sustentabilidad/verde) en formato dashboard público.
- **Similitud:** referencia de "cómo se ve un observatorio académico chileno con dashboard", aunque no está confirmado que tenga capa satelital de dosel específica — **verificar contenido exacto en el sitio antes de citarlo como equivalente**.
- **¿Open?** Público, gratis. URL: https://observatorio.cedeus.cl

### 4.3 Santiago — monitoreo de catastros de áreas verdes urbanas (ya en ficha 04, contexto ampliado aquí)
- **Qué hace:** (SciELO 2019) analiza catastros de áreas verdes del Área Metropolitana de Santiago combinando fotointerpretación sobre ortofoto/satélite + polígonos de instrumentos de planificación urbana — mismo tipo de fuente dual (satélite + normativa) que se sugiere para Temuco.
- **URL:** https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-83582019000200129

---

## 5. Proyectos de ciencia ciudadana + árboles urbanos con componente satelital/tecnológico

### 5.1 GreenScan (TU Delft / IEEE, 2024) — sensado móvil ciudadano + LLM
- **Tipo:** plataforma de investigación (no aún un producto público desplegado a escala de ciudad) que combina participación ciudadana, sensores térmicos/multiespectrales de bajo costo y modelos de lenguaje (LLM) con recuperación aumentada.
- **Qué hace:** ciudadanos envían fotos/descripciones de árboles vía web/móvil; el sistema fusiona datos de sensores baratos (térmico + multiespectral) montados en peatones o vehículos (taxis, camiones de basura — "drive-by sensing") para calcular **NDVI** (capacidad fotosintética) y **CTD, Canopy Temperature Depression** (estrés hídrico) por árbol, en tiempo casi real y a bajo costo.
- **Similitud:** es el proyecto más innovador encontrado que junta explícitamente "ciencia ciudadana" + "sensado tipo satélite pero a pie de calle" — resuelve el problema de resolución sub-píxel que Landsat/Sentinel no resuelven, con hardware barato en vez de imagen comercial.
- **Qué copiar:** la idea de **CTD (temperatura de copa − temperatura del aire)** como proxy de estrés hídrico/salud por árbol individual es trasladable con una cámara térmica de bajo costo (~100-300 USD) operada por voluntarios, complementando el satélite (que da tendencia de área) con datos puntuales de salud de ejemplares.
- **¿Open?** Investigación académica (arXiv/IEEE), sin producto público desplegado; el código no está confirmado como liberado en esta pasada — **verificar repo antes de asumir reutilización**.
- **Cita:** "GreenScan: Toward Large-Scale Terrestrial Monitoring the Health of Urban Trees Using Mobile Sensing" (2024). arXiv 2312.14364. https://arxiv.org/html/2312.14364v2 · IEEE: https://ieeexplore.ieee.org/document/10529969/

### 5.2 "Citizen-Centered Climate Intelligence" (India, arXiv 2025) — dato de árbol abierto para enfriamiento urbano
- **Tipo:** paper/propuesta de arquitectura (India) que "operacionaliza" datos abiertos de árboles para enfriamiento urbano y ruteo peatonal ("eco-routing") con participación ciudadana.
- **Similitud:** aborda directamente la pregunta "cómo un dato de árbol abierto y ciudadano se traduce en una herramienta de enfriamiento urbano usable por la gente" — el mismo puente (a)+(b)+ciudadanía que busca Temuco, pero orientado a app de navegación en vez de solo mapa de denuncia.
- **Nota de honestidad:** el PDF no pudo procesarse completo en esta pasada (binario); **recomendado leerlo directo con markitdown** antes de citarlo con detalle metodológico.
- **URL:** https://arxiv.org/pdf/2508.17648 (arXiv 2508.17648)

### 5.3 Tree-quest — app de ciencia ciudadana para inventario de árbol individual
- **Tipo:** app de ciencia ciudadana (ScienceDirect 2026) para recolectar información de árboles individuales.
- **Similitud:** complementa el patrón "app simple para que cualquiera reporte un árbol", en la misma línea que OpenTreeMap/iNaturalist ya cubiertos en ficha 04, pero más reciente — **revisar si aporta algo nuevo sobre esas dos** antes de invertir tiempo (baja prioridad).
- **URL:** https://www.sciencedirect.com/science/article/pii/S1574954126003043

---

## 6. "Urban forest observatory" / "observatorio de arbolado" documentado — hallazgo honesto

**No se encontró un proyecto único, documentado y con ese nombre exacto ("urban forest observatory"), que integre las 4 piezas (satélite + calor + expansión inmobiliaria + dashboard ciudadano público) en una sola plataforma operativa para una ciudad.** Lo que existe es **descompuesto en piezas** entre distintos proyectos:
- La pieza de **dosel + equidad social + dashboard** la resuelve mejor **Tree Equity Score** (EEUU, sección 1.1).
- La pieza de **serie temporal Landsat + LST en una ciudad** la resuelven mejor los papers de caso (sección 3): Worcester, Columbia SC, Bogotá norte.
- La pieza de **dosel + expansión inmobiliaria** la resuelve mejor Christchurch NZ y Portland OR (sección 2).
- La pieza de **datos abiertos + participación ciudadana + mapa público** la resuelve mejor **Bogotá** (Arbolapp + Geoportal + mapa ciudadano, sección 4.1) y el **UK Canopy Cover Webmap** (sección 1.5).

**Conclusión para el proyecto de Daniela:** el observatorio de Temuco, si junta las 4 piezas en un solo sitio con GitHub Pages + Leaflet, **sería genuinamente novedoso** — no hay un competidor directo documentado que haga exactamente eso para una ciudad chilena/latinoamericana de tamaño intermedio. Esto es un argumento de valor para el proyecto, no solo un hallazgo bibliográfico.

---

## Fuentes / URLs consultadas (WebSearch, 2026-07-15)
- Tree Equity Score: https://www.treeequityscore.org/methodology
- Google EIE Tree Canopy: https://insights.sustainability.google/labs/treecanopy
- Treepedia MIT: https://senseable.mit.edu/treepedia
- EU Urban Atlas: https://land.copernicus.eu/en/products/urban-atlas
- UK Canopy Cover Webmap: https://www.tandfonline.com/doi/full/10.1080/03071375.2023.2233864
- Ontario Landsat 50 años: https://www.tandfonline.com/doi/full/10.1080/07038992.2024.2445836
- Portland OR: https://www.mdpi.com/2071-1050/16/5/1803
- Christchurch NZ: https://www.sciencedirect.com/science/article/pii/S2210670725005529
- Beijing fenología multi-sensor: https://www.mdpi.com/2072-4292/16/13/2351
- Worcester MA / Elmes et al.: https://research.fs.usda.gov/treesearch/54836
- Columbia SC: https://www.mdpi.com/2673-7086/3/2/19
- Bogotá norte LST+EVI 22 años: https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-46112024000100104
- Bogotá Geoportal Bosques Urbanos: https://bogota.gov.co/mi-ciudad/ambiente/bogota-cuenta-con-geoportal-de-datos-abiertos-de-los-bosques-urbanos
- Mapa ciudadano arbolado Bogotá: https://cambiocolombia.com/medio-ambiente/articulo/2023/3/asi-es-el-mapa-interactivo-del-arbolado-urbano-de-bogota
- CEDEUS: https://observatorio.cedeus.cl
- Santiago catastros áreas verdes (SciELO 2019): https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-83582019000200129
- GreenScan: https://arxiv.org/html/2312.14364v2
- Citizen-Centered Climate Intelligence (India): https://arxiv.org/pdf/2508.17648
- Tree-quest: https://www.sciencedirect.com/science/article/pii/S1574954126003043
