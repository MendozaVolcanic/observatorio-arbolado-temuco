# Copas individuales, altura de dosel y cambio arbóreo — métodos gratis/open-source

Investigación para observatorio ciudadano de pérdida de árboles en Temuco (Chile).
Fecha: 2026-07-15 · Metodología: Crossref + Semantic Scholar + WebSearch/WebFetch.
RESTRICCIÓN: solo gratis / open-source. Escéptico: se distingue lo REALMENTE reproducible de lo que "suena bien".

---

## Tabla resumen

| # | Nombre | Tipo | Qué hace (1 frase) | Dato gratis que usa | Resolución | ¿Open source? + link | ¿Sirve árbol de calle urbano? | ¿Cubre Chile/SA? | Cita/URL |
|---|--------|------|--------------------|---------------------|-----------|----------------------|-------------------------------|------------------|----------|
| 1 | **DeepForest** (Weecology) | Herramienta (Python) + modelo | Detección de copas individuales (bounding boxes) en RGB aéreo con RetinaNet preentrenado en NEON | RGB aéreo propio (~10 cm) | Óptimo ~10 cm/px | Sí, MIT — github.com/weecology/DeepForest | Parcial: modelo base es de bosque NEON; en calle urbana **requiere re-entrenar** con copas etiquetadas | Modelo global, no específico Chile | Weinstein et al. 2020, Methods Ecol Evol, DOI 10.1111/2041-210X.13472 |
| 2 | **detectree2** (Ball/PatBall1) | Herramienta (Python) + modelos | Segmentación de copas (polígonos, no cajas) con Mask R-CNN / Detectron2 | RGB/multiespectral aéreo o dron | Aéreo/dron alta res | Sí — github.com/PatBall1/detectree2 | Parcial: entrenado en trópico denso; urbano posible re-entrenando; necesita GPU | Modelo global; probado en trópico, no Chile | Ball et al. 2023, Remote Sens Ecol Conserv, DOI 10.1002/rse2.332 |
| 3 | **Meta/WRI Global Canopy Height 1 m** | Dataset + modelo | Mapa global de altura de dosel a 1 m; detecta árboles individuales por altura | Imagen Maxar (procesada por Meta; el usuario NO paga) | 1 m | Modelo y datos CC-BY 4.0; en GEE y AWS | Sí como capa de altura de línea base; NO da copa individual delineada por sí solo | **Sí, global incluye Chile** | Tolan et al. 2024, Remote Sens Environ; arXiv 2204.08322 |
| 4 | **Meta CHM v2 (DINOv3)** | Dataset/modelo (nuevo) | Mejora del CHM 1 m con backbone DINOv3 | Idem Maxar procesada | ~1 m | Open (preprint 2026) | Igual que #3, mejor calidad | Global | arXiv 2603.06382 (CHMv2) |
| 5 | **DeepTreeAttention** (Weecology) | Repo/modelo | Predicción de especie de copa (attention CNN, Hang et al. 2020) sobre copas ya detectadas | Hiperespectral/RGB NEON | Aéreo | Sí — github.com/weecology/DeepTreeAttention | Solo si querés especie; requiere hiperespectral tipo NEON (no hay en Temuco) | No datos para Chile | Marconi et al. 2024, PMC11251727 |
| 6 | **Hansen Global Forest Change (UMD/GLAD)** | Dataset | Cobertura y **pérdida** de dosel anual 2000–presente | Landsat (gratis) | **30 m** | Sí, en GEE (UMD/hansen) | NO para árbol de calle (30 m es muy grueso para copa urbana); sí para contexto peri-urbano | Sí, global | Hansen et al. 2013, Science |
| 7 | **Global 30 m Landsat Tree Canopy Cover v4** | Dataset | % cobertura de dosel | Landsat | 30 m | Sí, GEE community catalog | NO copa individual urbana; contexto | Sí | gee-community-catalog.org/projects/global_tcc |
| 8 | **segment-geospatial (samgeo) + SAM** | Herramienta | Segmentación genérica (SAM) de objetos incl. árboles; wrapper integra detectree2 | Cualquier RGB del usuario | Depende de la imagen | Sí — samgeo.gishub.org | Experimental para copas; útil como asistente de etiquetado | Global | Wu 2023 |
| 9 | **Google Earth Pro (imágenes históricas)** | Fuente de imagen | Visor de imagen histórica alta res (clock icon) | Mosaicos históricos (visualización) | Alta (variable) | No — **licencia restrictiva** | Solo para inspección visual/conteo manual; NO redistribuir ni derivar rasters georref. | Cobertura Temuco variable por fecha | earth.google.com |
| 10 | **OpenAerialMap** | Fuente de imagen | Repositorio de imagen aérea abiertamente licenciada | Imagen aérea CC | Alta (dron/avión) | Sí, abierto | Sí si hay cobertura; **cobertura de Chile escasa** | Parcial/escasa Chile | openaerialmap.org |
| 11 | **IGM Chile / aerofotogramétrico** | Fuente de imagen | Archivo de vuelos aéreos históricos de todo Chile | Fotos aéreas históricas | Alta | No abierto (solicitud/pago) | Sí para líneas base 2005/2010 si se consigue | Sí, Chile | Instituto Geográfico Militar |

---

## Notas por hilo

### 1. DeepForest
- Modelo "release" preentrenado en NEON: **precision 0.66, recall 0.79** (bosque natural). En ambiente urbano de calle, el propio paper reconoce que urbano "es muy distinto" y usaron re-entrenamiento. Necesita RGB aéreo fino (~10 cm); con imagen satelital de 30–50 cm el desempeño cae.
- Realmente gratis y reproducible. Pero **el dato de entrada (RGB ~10 cm sobre Temuco) es el cuello de botella**, no el software.

### 2. detectree2
- Da polígonos de copa (mejor que cajas para medir área de copa y pérdida). Detectron2/Mask R-CNN, **requiere GPU**. Modelos del "model garden" entrenados en trópico → para Temuco conviene fine-tuning con copas etiquetadas locales.

### 3–4. Meta/WRI Canopy Height 1 m — CLAVE, pero con asterisco
- **Gratis, CC-BY 4.0, global (incluye Chile), 1 m, MAE 2.8 m.** Acceso GEE: `ee.ImageCollection("projects/sat-io/open-datasets/facebook/meta-canopy-height")`; también AWS (dataforgood-fb-forests) como GeoTIFF COG.
- **Advertencia dura (escéptico):** es **una sola época compuesta**, ~2009–2020 con ~80% de la imagen de 2018–2020. **NO es serie temporal** → **no sirve por sí solo para cambio 2005–2025**. Sirve como **línea base de altura ~2019** y para detectar árboles altos individuales. MAE 2.8 m implica que árboles jóvenes/bajos y separar copas contiguas es incierto.
- CHM v2 (DINOv3, 2026) mejora calidad pero sigue siendo mosaico, no anual.

### 5. Métodos UTC (Urban Tree Canopy assessment)
- Flujo estándar municipal: clasificación de cobertura (árbol/no árbol) sobre imagen alta res + LiDAR cuando existe. Reproducible con datos gratis **solo si hay imagen alta res gratis**; el estándar US (i-Tree Canopy) usa fotointerpretación de puntos sobre imagen — gratis y muy reproducible para **estimar % cobertura**, no copa individual.
- Papers de referencia (Crossref): "Urban Tree Canopy Mapping ... Double-Branch CNN & Multi-Temporal HSR" (DOI 10.3390/rs15030765); "Urban Tree Mapping and Individual Canopy Demarcation ... UAV" (10.1109/ingarss61818.2024.10984067).

### 6. Cambio de dosel 2005–2025
- No hay un producto gratis 1 m multi-fecha listo. Opciones reales:
  - **Peri-urbano/grueso:** Hansen GFC 30 m (2000+) — pérdida anual, gratis en GEE. Insuficiente para copa de calle.
  - **Fino:** construir 2 fechas propias (foto histórica ~2005/2010 vs. imagen reciente) y correr DeepForest/detectree2 en ambas → diferencia de copas. Depende 100% de conseguir imagen histórica alta res.
- Paper útil de límites: "Difficulties with estimating city-wide urban forest cover change from national, remotely-sensed tree canopy maps" (10.1007/s11252-007-0040-9) — advierte que mapas nacionales fallan a escala ciudad.

### 7. Imagen histórica alta res gratis para 2005/2010
- **Google Earth Pro:** tiene imagen histórica de alta resolución navegable gratis (icono reloj). Límite duro: **licencia** prohíbe redistribuir/derivar rasters georreferenciados; uso legítimo = **conteo/inspección manual** en pantalla (captura visual), no descarga de raster para procesar con IA a escala.
- **OpenAerialMap:** abierto (CC) pero cobertura de Chile escasa/nula para Temuco 2005–2010.
- **USGS EarthExplorer:** Landsat gratis pero 30 m (grueso) y CORONA/aéreo de alta res casi solo USA — no Temuco.
- **IGM Chile:** archivo aerofotogramétrico nacional histórico; alta res real para 2005/2010 pero **no open** (solicitud formal, posible costo).

---

## Recomendación para el corredor piloto (Av. Caupolicán)

Para **conteo de copas en un corredor piloto**, priorizar (todo gratis):
1. **Base de altura hoy:** Meta/WRI CHM 1 m en GEE como capa de contexto (árboles altos existentes ~2019).
2. **Conteo de copas fino:** conseguir RGB de dron/aéreo del corredor (o el mosaico reciente disponible) y correr **DeepForest** para conteo rápido; si se necesita **área de copa** (para cuantificar pérdida), usar **detectree2** (polígonos). Ambos probablemente requieran **etiquetar ~50–100 copas locales** para fine-tuning por el sesgo urbano.
3. **Cambio 2005→2025:** correr el mismo detector sobre una imagen histórica (Google Earth Pro para inspección/validación manual; IGM si se consigue raster procesable) vs. reciente. Reconocer que la fecha histórica es la mayor limitación reproducible.

**Lo que NO es reproducible barato:** una serie temporal automática 1 m 2005–2025 lista para usar — no existe gratis; hay que construirla por fechas.
