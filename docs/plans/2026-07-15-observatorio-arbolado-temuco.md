# Observatorio Ciudadano de Arbolado Urbano de Temuco — Plan Maestro

> **Para trabajadores agénticos:** este es un PLAN MAESTRO de proyecto (roadmap de 3 subsistemas). La Capa 1 está detallada a nivel de tareas ejecutables. Las Capas 2 y 3 están a nivel de fase/entregable y se convertirán en planes TDD propios cuando se aborden. Steps con checkbox (`- [ ]`).

**Goal:** Construir un observatorio ciudadano, gratuito y reproducible, que documente la pérdida de arbolado urbano en Temuco (2000-2025), la vincule con la expansión inmobiliaria/vial y con el aumento de calor superficial, y sirve de evidencia a la campaña ciudadana ya activa.

**Architecture:** Tres capas independientes que se pueden construir y mostrar por separado. (1) **Radar** satelital automatizado en Google Earth Engine: NDVI + temperatura de superficie (LST) a escala de ciudad, para responder *dónde/cuándo* se perdió verde y *cuánto se calentó*. (2) **Detalle** en corredores piloto (Caupolicán, Imperial, Av. Olimpia): conteo de árboles antes/después con evidencia irrebatible. (3) **Observatorio vivo** en GitHub Pages: mapa + denuncias ciudadanas + capas oficiales de causa (permisos de edificación, loteos) + árboles patrimoniales.

**Tech Stack:** Python 3.12 (Anaconda) · Google Earth Engine (`earthengine-api` + `geemap`) · Sentinel Hub CDSE y USGS M2M (reutilizados del workspace) · rasterio/numpy · Leaflet + GitHub Pages · KoBoToolbox · i-Tree Canopy (manual) · QGIS (opcional).

**Restricción dura:** solo herramientas y datos GRATUITOS/open. GEE es gratis para uso no comercial (el observatorio califica).

---

## Contexto que el implementador necesita saber

- **El proyecto no parte de cero políticamente.** Angélica Lezano Vidal (ONG Verde Urbano), amiga de la clienta Daniela, ya presentó ante el Senado el problema (Boletín N°14.214-12, jul-2024). Casos con cifra ya documentados: Arboleda de Fresnos Av. Olimpia (23 árboles), calle Imperial por SERVIU (>20 árboles). El observatorio es la herramienta de evidencia de esa campaña.
- **La verdad técnica que ordena el diseño:** no existe dato gratuito que dé "árbol por árbol" en serie 2000-2025. Lo gratuito que llega a 2005 vive a 30 m (Landsat) → ve parches de verdor, no ejemplares. Por eso el radar (Capa 1) mide tendencia, y el conteo de ejemplares (Capa 2) es manual sobre imagen histórica de Google Earth Pro.
- **Restricción verificada:** IDE Chile solo tiene ortofoto fina gratis para regiones norte/centro; Temuco (sur) queda fuera. Google Earth Pro histórico permite solo conteo *manual* (su licencia prohíbe descargar rasters para IA). → nada de DeepForest sobre ortofoto en Temuco hasta que haya imagen propia (dron/celular).
- Detalle de fuentes y decisiones en `../bibliografia/SINTESIS_INVESTIGACION.md` y `../bibliografia/06_verificacion_fuentes.md`.

## Reutilización del workspace (no reinventar)

| Necesidad | Reutilizar de | Qué |
|---|---|---|
| Descarga Sentinel-2 vía CDSE | `Copernicus-v1/sentinel2_downloader.py`, `VegStress-v1/ndvi_analyzer.py` | Credenciales `SH_CLIENT_ID`/`SH_CLIENT_SECRET`, evalscript NDVI, auth CDSE |
| Landsat (térmico + histórico) | `Landsat-v1/landsat_downloader.py` | Auth USGS M2M (gratis sin tarjeta), bandas térmicas |
| Detección de cambio | `Copernicus-v1/change_detector.py`, `change_analysis.py` | Lógica de diff de píxeles |
| Dashboard GitHub Pages | `VegStress-v1/dashboard_generator.py`, `Copernicus-v1/docs/` | Patrón `generator.py → docs/index.html`, calendario, mapa |
| AOIs Chile | `Copernicus-v1/config_sentinel2.py` | Patrón de definición de geometrías/buffers |

**Prerequisito Capa 1:** cuenta Google Earth Engine (gratis) — registrarse en code.earthengine.google.com y crear un cloud project. Sin esto, camino alternativo = pipeline de descarga local reutilizando Copernicus-v1/Landsat-v1 (más pesado).

---

## CAPA 1 — Radar satelital (detallada)

**Objetivo de la capa:** mapa reproducible de Temuco con (a) pérdida de verdor 2000→2025, (b) temperatura de superficie y su correlación negativa con el verde, (c) fechado del año de pérdida por parche. Salidas: GeoTIFF + GeoJSON + PNGs + un notebook reproducible.

**Archivos:**
- Crear: `src/gee/aoi_temuco.py` — define el AOI comunal de Temuco
- Crear: `src/gee/ndvi_series.py` — serie NDVI anual Landsat/Sentinel
- Crear: `src/gee/lst_series.py` — serie LST anual (Ermida 2020)
- Crear: `src/gee/change_correlacion.py` — ΔNDVI, tendencia, correlación NDVI↔LST
- Crear: `src/gee/export.py` — exporta rasters/mapas
- Crear: `notebooks/capa1_radar_temuco.ipynb` — flujo reproducible y visual
- Crear: `tests/test_capa1.py` — verificaciones de sanity
- Crear: `requirements.txt`, `.env.example`, `README.md`

### Task 1: Entorno y autenticación GEE

- [ ] **Step 1: Crear `requirements.txt`**

```
earthengine-api>=1.0
geemap>=0.32
rasterio>=1.3
numpy>=1.26
pandas>=2.0
matplotlib>=3.8
python-dotenv>=1.0
```

- [ ] **Step 2: Instalar y autenticar**

Run: `pip install -r requirements.txt && earthengine authenticate`
Expected: navegador abre flujo OAuth de Google; al terminar, token guardado localmente.

- [ ] **Step 3: Configurar el project ID y un helper de init**

GEE ya exige el Cloud Project en `ee.Initialize`. La cuenta ya existe (project **`earnest-beacon-488902-k9`**). Guardar el ID en `.env` (no es secreto, pero fuera del código para portabilidad):

```
# .env
GEE_PROJECT=earnest-beacon-488902-k9
```

```python
# src/gee/_init.py  — usar init_ee() en todos los módulos en vez de ee.Initialize()
import ee, os
from dotenv import load_dotenv
load_dotenv()
def init_ee():
    ee.Initialize(project=os.getenv("GEE_PROJECT"))
```
> En Task 2-6, reemplazar cada `ee.Initialize()` por `from src.gee._init import init_ee; init_ee()`.

- [ ] **Step 4: Verificar acceso**

Run: `python -c "from src.gee._init import init_ee; import ee; init_ee(); print(ee.Number(1).add(1).getInfo())"`
Expected: imprime `2`. Si falla con "not registered"/"project not found", verificar el ID en el selector de proyecto del Code Editor (arriba a la derecha).

### Task 2: AOI comunal de Temuco

**Files:** Create `src/gee/aoi_temuco.py`, Test `tests/test_capa1.py`

- [ ] **Step 1: Escribir test de sanity del AOI**

```python
# tests/test_capa1.py
from src.gee.aoi_temuco import get_aoi_temuco

def test_aoi_temuco_bounds():
    aoi = get_aoi_temuco()  # ee.Geometry
    c = aoi.centroid(1).coordinates().getInfo()  # [lon, lat]
    assert -72.8 < c[0] < -72.4, f"lon fuera de Temuco: {c[0]}"
    assert -38.9 < c[1] < -38.6, f"lat fuera de Temuco: {c[1]}"
```

- [ ] **Step 2: Ejecutar y ver que falla**

Run: `pytest tests/test_capa1.py::test_aoi_temuco_bounds -v`
Expected: FAIL (módulo no existe).

- [ ] **Step 3: Implementar el AOI**

```python
# src/gee/aoi_temuco.py
"""AOI de la comuna de Temuco para GEE.
Bbox urbano provisional; reemplazar por el límite comunal oficial
descargado del Visor de Límites de IDE Temuco cuando esté disponible.
"""
import ee

# Bbox aproximado del área urbana de Temuco (lon/lat)
TEMUCO_BBOX = [-72.68, -38.78, -72.53, -38.68]  # [W, S, E, N]

def get_aoi_temuco() -> "ee.Geometry":
    ee.Initialize()
    return ee.Geometry.Rectangle(TEMUCO_BBOX)
```

- [ ] **Step 4: Ejecutar y ver que pasa**

Run: `pytest tests/test_capa1.py::test_aoi_temuco_bounds -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add requirements.txt src/gee/aoi_temuco.py tests/test_capa1.py
git commit -m "feat(capa1): AOI comunal de Temuco para GEE"
```

### Task 3: Serie NDVI anual (Landsat armonizado 2000-2025 + Sentinel-2 2015+)

**Files:** Create `src/gee/ndvi_series.py`, Modify `tests/test_capa1.py`

- [ ] **Step 1: Escribir test de rango físico de NDVI**

```python
# añadir a tests/test_capa1.py
import ee
from src.gee.ndvi_series import ndvi_anual_landsat

def test_ndvi_en_rango_fisico():
    img = ndvi_anual_landsat(2020)  # ee.Image, banda 'NDVI'
    stats = img.reduceRegion(
        reducer=ee.Reducer.minMax(),
        geometry=get_aoi_temuco(),
        scale=30,
        maxPixels=int(1e9),
    ).getInfo()
    assert -1.0 <= stats["NDVI_min"] <= stats["NDVI_max"] <= 1.0
```

- [ ] **Step 2: Ejecutar y ver que falla**

Run: `pytest tests/test_capa1.py::test_ndvi_en_rango_fisico -v`
Expected: FAIL (módulo no existe).

- [ ] **Step 3: Implementar NDVI anual con máscara de nubes**

```python
# src/gee/ndvi_series.py
"""Serie NDVI anual sobre Temuco.
Landsat Collection 2 L2 armonizado (5/7/8/9) para 2000-2025.
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco

def _mask_l2(img):
    qa = img.select("QA_PIXEL")
    # bits 3 (cloud) y 4 (cloud shadow)
    mask = qa.bitwiseAnd(1 << 3).eq(0).And(qa.bitwiseAnd(1 << 4).eq(0))
    return img.updateMask(mask)

def _scale_l2(img):
    optical = img.select("SR_B.").multiply(0.0000275).add(-0.2)
    return img.addBands(optical, None, True)

def ndvi_anual_landsat(anio: int) -> "ee.Image":
    ee.Initialize()
    aoi = get_aoi_temuco()
    # Selección de sensor por año
    if anio <= 2011:
        col_id, nir, red = "LANDSAT/LT05/C02/T1_L2", "SR_B4", "SR_B3"
    elif anio <= 2013:
        col_id, nir, red = "LANDSAT/LE07/C02/T1_L2", "SR_B4", "SR_B3"
    else:
        col_id, nir, red = "LANDSAT/LC08/C02/T1_L2", "SR_B5", "SR_B4"
    col = (ee.ImageCollection(col_id)
           .filterBounds(aoi)
           .filterDate(f"{anio}-01-01", f"{anio}-12-31")
           .map(_mask_l2).map(_scale_l2))
    def _ndvi(img):
        return img.normalizedDifference([nir, red]).rename("NDVI")
    return col.map(_ndvi).median().clip(aoi).rename("NDVI")
```

- [ ] **Step 4: Ejecutar y ver que pasa**

Run: `pytest tests/test_capa1.py::test_ndvi_en_rango_fisico -v`
Expected: PASS (min/max dentro de [-1, 1]).

- [ ] **Step 5: Commit**

```bash
git add src/gee/ndvi_series.py tests/test_capa1.py
git commit -m "feat(capa1): serie NDVI anual Landsat sobre Temuco"
```

### Task 4: Serie LST anual (temperatura de superficie, Ermida 2020)

**Files:** Create `src/gee/lst_series.py`, Modify `tests/test_capa1.py`

- [ ] **Step 1: Escribir test de rango físico de LST**

```python
from src.gee.lst_series import lst_anual

def test_lst_en_kelvin_razonable():
    img = lst_anual(2020)  # banda 'LST' en °C
    import ee
    stats = img.reduceRegion(ee.Reducer.minMax(), get_aoi_temuco(), 100, maxPixels=1e9).getInfo()
    assert -20 <= stats["LST_min"] <= stats["LST_max"] <= 70  # °C plausibles
```

- [ ] **Step 2: Ejecutar y ver que falla**

Run: `pytest tests/test_capa1.py::test_lst_en_kelvin_razonable -v`
Expected: FAIL.

- [ ] **Step 3: Implementar LST reutilizando el módulo validado de Ermida et al. 2020**

**Decisión (confirmada por el paper `bibliografia/pdfs/Ermida_2020_LST_GEE.pdf`):** no reimplementar el algoritmo. Ermida publicó el algoritmo Statistical Mono-Window (SMW) con emisividad ASTER-GED como código GEE abierto. El módulo original es JavaScript (`users/sofiaermida/landsat_smw_lst`), pero su repositorio **tiene un port de Python** — usar ese.

Sub-pasos:
1. Clonar el repo: `git clone https://github.com/sofiaermida/landsat_smw_lst.git vendor/landsat_smw_lst` (verificar que trae `Landsat_LST.py` y los módulos `compute_*`; si solo trae JS, portar las 5 funciones SMW a Python siguiendo el paper §2).
2. Envolver su función principal en nuestro `lst_anual`:

```python
# src/gee/lst_series.py
import ee, sys, os
from src.gee.aoi_temuco import get_aoi_temuco
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "vendor", "landsat_smw_lst"))
from Landsat_LST import fetch_landsat_collection_LST  # nombre real según el repo; ajustar al importar

def lst_anual(anio: int) -> "ee.Image":
    ee.Initialize()
    aoi = get_aoi_temuco()
    sat = "L5" if anio <= 2011 else ("L7" if anio <= 2013 else "L8")
    col = fetch_landsat_collection_LST(sat, f"{anio}-01-01", f"{anio}-12-31", aoi, use_ndvi=True)
    # el módulo entrega LST en Kelvin en la banda 'LST'
    return col.select("LST").median().subtract(273.15).clip(aoi).rename("LST")
```
> El nombre exacto de la función del módulo se confirma al clonar (el repo expone una colección con banda `LST`). Citar Ermida et al. 2020 (Remote Sensing 12(9):1471) en el README. Ventaja: emisividad y ventana ya calibradas y validadas — ahorra semanas.

- [ ] **Step 4: Ejecutar y ver que pasa**

Run: `pytest tests/test_capa1.py::test_lst_en_kelvin_razonable -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gee/lst_series.py tests/test_capa1.py
git commit -m "feat(capa1): serie LST anual sobre Temuco"
```

### Task 5: Cambio y correlación NDVI↔LST

**Files:** Create `src/gee/change_correlacion.py`, Modify `tests/test_capa1.py`

- [ ] **Step 1: Test — ΔNDVI define zonas de pérdida**

```python
from src.gee.change_correlacion import delta_ndvi, correlacion_ndvi_lst

def test_delta_ndvi_signo():
    d = delta_ndvi(2005, 2024)  # banda 'dNDVI' = NDVI_2024 - NDVI_2005
    import ee
    s = d.reduceRegion(ee.Reducer.mean(), get_aoi_temuco(), 30, maxPixels=1e9).getInfo()
    assert -2.0 <= s["dNDVI"] <= 2.0

def test_correlacion_es_negativa():
    r = correlacion_ndvi_lst(2020)  # float: Pearson NDVI vs LST
    assert r < 0, "se espera correlación negativa árbol-calor"
```

- [ ] **Step 2: Ejecutar y ver que falla**

Run: `pytest tests/test_capa1.py -k "delta or correlacion" -v`
Expected: FAIL.

- [ ] **Step 3: Implementar**

```python
# src/gee/change_correlacion.py
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.lst_series import lst_anual

def delta_ndvi(a0: int, a1: int) -> "ee.Image":
    ee.Initialize()
    return ndvi_anual_landsat(a1).subtract(ndvi_anual_landsat(a0)).rename("dNDVI").clip(get_aoi_temuco())

def correlacion_ndvi_lst(anio: int) -> float:
    ee.Initialize()
    aoi = get_aoi_temuco()
    stack = ndvi_anual_landsat(anio).addBands(lst_anual(anio))
    r = stack.reduceRegion(ee.Reducer.pearsonsCorrelation(), aoi, 30, maxPixels=1e9).getInfo()
    return r["correlation"]
```

- [ ] **Step 4: Ejecutar y ver que pasa**

Run: `pytest tests/test_capa1.py -k "delta or correlacion" -v`
Expected: PASS. (Si la correlación no diera negativa, es un hallazgo real a investigar, no un bug del test — anotarlo.)

- [ ] **Step 5: Commit**

```bash
git add src/gee/change_correlacion.py tests/test_capa1.py
git commit -m "feat(capa1): delta NDVI y correlacion NDVI-LST"
```

### Task 5b: Validación cruzada del verdor con Dynamic World

**Justificación (paper `bibliografia/pdfs/Brown_2022_DynamicWorld.pdf`):** Dynamic World da una probabilidad de clase "trees" a 10 m desde 2015, gratis en GEE. Sirve para chequear que las zonas que el NDVI marca como pérdida de verde son efectivamente *árboles* y no pasto — el punto débil del NDVI. Solo aplica 2015→2025 (no llega a 2005).

**Files:** Create `src/gee/dynamicworld.py`, Modify `tests/test_capa1.py`

- [ ] **Step 1: Test — fracción de árboles en [0,1]**

```python
from src.gee.dynamicworld import trees_prob_anual

def test_trees_prob_rango():
    img = trees_prob_anual(2020)  # banda 'trees' probabilidad media anual
    import ee
    s = img.reduceRegion(ee.Reducer.minMax(), get_aoi_temuco(), 10, maxPixels=int(1e9)).getInfo()
    assert 0.0 <= s["trees_min"] <= s["trees_max"] <= 1.0
```

- [ ] **Step 2: Ejecutar y ver que falla.** Run: `pytest tests/test_capa1.py::test_trees_prob_rango -v` → FAIL.

- [ ] **Step 3: Implementar**

```python
# src/gee/dynamicworld.py
import ee
from src.gee.aoi_temuco import get_aoi_temuco

def trees_prob_anual(anio: int) -> "ee.Image":
    ee.Initialize()
    aoi = get_aoi_temuco()
    col = (ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")
           .filterBounds(aoi).filterDate(f"{anio}-01-01", f"{anio}-12-31")
           .select("trees"))
    return col.mean().clip(aoi).rename("trees")
```

- [ ] **Step 4: Ejecutar y ver que pasa.** Run: `pytest tests/test_capa1.py::test_trees_prob_rango -v` → PASS.

- [ ] **Step 5: Commit** `feat(capa1): validacion verdor con Dynamic World trees`

### Task 6: Exportar mapas y notebook reproducible

- [ ] **Step 1:** Crear `src/gee/export.py` con `export_geotiff(img, nombre)` (a Google Drive via `ee.batch.Export.image.toDrive`) y `mapa_png(img, vis, nombre)` con `geemap`.
- [ ] **Step 2:** Crear `notebooks/capa1_radar_temuco.ipynb` que: inicializa GEE, muestra NDVI 2005 vs 2024 lado a lado, el mapa ΔNDVI (rojo=pérdida), la capa `trees` de Dynamic World 2020 (validación de que la pérdida es de árboles, no pasto), el mapa LST 2024, imprime la correlación NDVI↔LST y la capa Yale UHI (`YALE/YCEO/UHI` para Temuco). **Validación de terreno:** superponer las estaciones/zonas del estudio local (`bibliografia/pdfs/HeatOnTheMove_2024_Temuco_UHI.pdf`, 23 estaciones, zonas Z-1 a Z-4) y comparar cualitativamente contra nuestro LST satelital.
- [ ] **Step 3:** Ejecutar el notebook de punta a punta; verificar que los 4 mapas renderizan y la correlación se imprime.
- [ ] **Step 4:** Escribir `README.md` de la Capa 1 (prerequisito GEE, cómo correr, qué produce).
- [ ] **Step 5:** Commit `feat(capa1): export + notebook radar reproducible`.

**Entregable Capa 1:** notebook + mapas de pérdida de verde y de calor de Temuco 2005→2024, con la correlación árbol↔calor cuantificada. Esto ya es demostrable ante la campaña.

---

## CAPA 2 — Detalle en corredores piloto (roadmap)

**Objetivo:** la cifra irrebatible "en Caupolicán/Imperial/Av. Olimpia había N árboles en 20XX y hoy quedan M", con área de sombra perdida.

**Fases (se detallará como plan TDD propio al abordarla):**
1. Selección de 1 corredor piloto (empezar por Av. Olimpia: 23 árboles ya documentados por ONG Verde Urbano → verdad de terreno para validar el método).
2. Conteo manual asistido sobre **Google Earth Pro** histórico (imagen cenital 2005/2010/2015/2020/2025): marcar cada copa como punto en un KML, exportar a GeoJSON. Registrar la licencia (uso manual permitido).
3. Estimar % dosel con **i-Tree Canopy** (puntos aleatorios) por corredor y año → cobertura con intervalo de confianza.
4. Área de sombra: aproximar copa→m² sombreados; sumar pérdida.
5. (Opcional/futuro) Imagen propia de dron o recorrido con celular → cuando exista, correr **DeepForest**/**detectree2** para automatizar y **Green View Index** con **Mapillary**/ZenSVI.
6. Cruce con causa: superponer el corredor con permisos de edificación / loteos descargados de **IDE Temuco** y con la obra vial responsable.

**Entregable Capa 2:** ficha por corredor con antes/después, cifra de árboles y m² de sombra perdidos, y la obra/permiso asociado.

---

## CAPA 3 — Observatorio ciudadano vivo (roadmap)

**Objetivo:** sitio público donde vive el análisis y la comunidad reporta podas/talas.

**Fases (plan TDD propio al abordarla):**
1. Repo GitHub + GitHub Pages con **Leaflet** + tiles OSM, mapa centrado en Temuco.
2. Capas base: resultados Capa 1 (GeoJSON de pérdida/calor), corredores Capa 2, árboles patrimoniales (UFRO), capas de causa (edificación/loteos de IDE Temuco vía WMS/GeoJSON).
3. Denuncias ciudadanas: formulario **KoBoToolbox** (foto + GPS + tipo: poda/tala/pérdida), API que vuelca a GeoJSON, marcador en el mapa. Alternativa mínima: Google Forms + `uMap`.
4. Integrar el material existente de la comunidad (fotos/denuncias) como capa inicial.
5. Ficha "cuánta sombra/patrimonio en riesgo" por sector.

**Entregable Capa 3:** observatorio público en `usuario.github.io/observatorio-arbolado-temuco`.

---

## Datos y fuentes (todas gratis)
- **Satélite:** Landsat C2 L2 (1984+) y Sentinel-2 (2015+) vía GEE; Sentinel-2 vía CDSE (reuso Copernicus-v1) como alternativa.
- **Calor:** LST Landsat (Ermida 2020); dataset Yale UHI (`YALE/YCEO/UHI`).
- **Causa (oficial):** IDE Temuco — carpetas de edificación, loteos, zonificación, macrosectores+censo 2024.
- **Patrimoniales:** Laboratorio de Ecosistemas y Bosques, UFRO (solicitar).
- **Imagen histórica de detalle:** Google Earth Pro (conteo manual).
- **Street-level:** Mapillary (+ generación propia con celular).

## Riesgos y mitigaciones
| Riesgo | Mitigación |
|---|---|
| Alta nubosidad de Temuco degrada la serie NDVI/LST | Composites anuales por mediana; usar verano (dic-feb); reportar % píxeles válidos |
| Landsat 30 m no resuelve árbol de calle | Es esperado: la Capa 1 mide tendencia de parches, no ejemplares; el ejemplar lo da la Capa 2 |
| GEE requiere registro/curva de aprendizaje | Documentar alta paso a paso; fallback pipeline local con Copernicus-v1/Landsat-v1 |
| Google Earth Pro prohíbe descarga de rasters para IA | Conteo manual (permitido); IA solo sobre imagen propia |
| Correlación NDVI↔LST podría ser débil en zona lluviosa | Tratar como hallazgo, no forzar; anclar con el paper local de Temuco (PMC11860384) |
| Falta de imagen fina histórica en Araucanía | Aceptado; Capa 2 se apoya en Google Earth Pro + validación de terreno ONG |

## Secuencia recomendada
1. **Capa 1 (piloto radar GEE)** — próxima; entrega algo mostrable rápido.
2. **Capa 2 corredor Av. Olimpia** — la cifra irrebatible con verdad de terreno ya conocida (23 árboles).
3. **Capa 3 observatorio** — junta todo en público.
Giro estratégico: liderar comunicacionalmente con Capa 2 + el mapa de calor de Capa 1.

## Decisiones tomadas (2026-07-15, Nicolás)
- **Backbone:** Google Earth Engine, con **cuenta nueva** (registro gratis). Pipeline local descartado (fallback).
- **AOI:** **límite comunal oficial** descargado del Visor de Límites de IDE Temuco (no bbox provisional). → La Task 2 se ajusta: en vez del bbox, descargar el polígono comunal (GeoJSON/KML) de IDE Temuco y cargarlo como `ee.Geometry`. El bbox queda solo como fallback si la descarga falla.
- **Corredores piloto Capa 2:** **ambos** — Av. Olimpia (validación con verdad de terreno: 23 árboles ONG) primero, Caupolicán (emblemático del audio) segundo.
- **Denuncias Capa 3:** pendiente de explicación a Nicolás (KoBoToolbox vs Google Forms+uMap).
