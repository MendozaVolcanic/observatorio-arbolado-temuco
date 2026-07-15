# Síntesis de investigación — Observatorio Ciudadano de Arbolado Urbano de Temuco

**Fecha:** 2026-07-15 · **Restricción dura:** solo herramientas y datos GRATUITOS/open.
**Pregunta:** ¿qué métodos y plataformas gratuitas y reproducibles existen para detectar/cuantificar pérdida de arbolado urbano en el tiempo (copas individuales, dosel, verdor a nivel calle) y vincularla con islas/olas de calor, y qué casos/observatorios similares existen (Chile/LATAM)?

Detalle por hilo en: `00_senado_temuco_verde_urbano.md`, `01_copas_dosel_altares.md`, `02_satelite_plataformas_gratuitas.md`, `03_calor_urbano_arbolado.md`, `04_ciencia_ciudadana_chile.md`, `05_busqueda_propia.md`.

---

## 1. La verdad incómoda (define todo el diseño)

**No existe ningún atajo gratuito que dé "árbol por árbol" en serie temporal larga (2005→2025).**
- Lo gratis-y-reproducible que llega a 2005 vive a 10–30 m (Landsat/Sentinel vía Google Earth Engine): sirve para verdor y pérdida de *parches*, no para censar ejemplares. A esa escala el árbol de calle es sub-píxel.
- Lo que resuelve el ejemplar (Meta canopy 1 m; imágenes Maxar) es **una sola época** (~2018-2020) o **de pago**.
- Google Earth Pro tiene imagen histórica alta-res navegable, pero su licencia permite **solo inspección/conteo manual**, no descargar rasters para alimentar IA.

→ **Diseño realista = backbone satelital de tendencia (automatizable) + validación humana puntual en corredores + capa ciudadana.** No un censo automático de árboles.

---

## 2. Recopilación por enfoque (solo lo gratis/reproducible)

### A. Radar satelital de escala-ciudad (backbone)
| Herramienta | Qué aporta | Dato | Resol. | Chile |
|---|---|---|---|---|
| **Google Earth Engine + geemap** | Única vía gratis al archivo Landsat (1984+, cubre 2005) + Sentinel-2 (2015+). NDVI, ΔNDVI, tendencia Theil-Sen, LandTrendr/CCDC para fechar pérdidas | Landsat/S2 | 30/10 m | ✅ |
| **Dynamic World** | Clase "trees" 10 m probabilística 2015+ (GEE) | S2 | 10 m | ✅ |
| **ESRI Land Cover** | 10 m anual 2017+, visor swipe no-código | S2 | 10 m | ✅ |
| **i-Tree Canopy (USDA)** | % dosel por fotointerpretación humana (resuelve ejemplar), no-código, funciona en Chile | Google img | visual | ✅ |
| Hansen/Global Forest Watch | Pérdida dosel anual 2000+, **pero 30 m subestima árbol urbano disperso**; solo periferia | Landsat | 30 m | ⚠️ |
| ESA WorldCover | Solo snapshots 2020/2021, versiones no comparables | S2 | 10 m | ⚠️ |
| Meta/WRI Canopy Height 1 m | Única capa gratis que resuelve ejemplar, **pero snapshot único ~2019**; sirve de máscara estructural | Maxar+IA | 1 m | ✅ |

**Separar árbol de pasto (NDVI no basta):** fenología / series temporales de NDVI en GEE + red-edge (S2 b5-7) + textura GLCM.

### B. Detección de copas / dosel de detalle (corredores piloto)
| Herramienta | Qué aporta | Estado |
|---|---|---|
| **DeepForest** (Weecology) | Cajas de copas individuales en RGB. Open 100%. Modelo base = bosque natural → **re-entrenar** con copas urbanas locales | Necesita RGB ~10 cm |
| **detectree2** (PatBall1) | Copas como **polígonos** (mide área) → mejor para cuantificar pérdida. Requiere GPU + fine-tuning | Necesita RGB fino + GPU |
| **i-Tree Canopy / conteo manual** | Ruta gratis+legal para el histórico: puntos aleatorios o conteo visual sobre Google Earth Pro 2005 vs 2025 | Listo, manual |

### C. Calor urbano / la consecuencia medible (el hilo más "vendible")
| Herramienta | Qué aporta | Chile |
|---|---|---|
| **LST Landsat** (USGS ST L2 ó código GEE **Ermida et al. 2020** `users/sofiaermida/landsat_smw_lst`) | Temperatura de superficie 30 m gratis; cruzada con NDVI muestra correlación negativa árbol↔calor | ✅ |
| **ERA5 (Copernicus)** | Fechar olas de calor y bajar la escena Landsat de esos días → barrios sin árboles varios °C más calientes | ✅ |
| **Yale Global Surface UHI Explorer** | Intensidad isla de calor >10.000 ciudades, **incluye Temuco**, listo para usar | ✅ |
| Tree Equity Score (metodología) | No opera fuera EEUU/UK → **replicar lógica en QGIS**: dosel + LST + censo INE = qué barrios tienen menos árboles y más calor | replicable |

**Cifras citables:** +10% dosel → −0.6 a −1.2 °C LST (WRI). **Chile (Sarricolea, Santiago): reverdecer reduce isla de calor 1.2–5.5 °C**; estudio 2025 "zonas frías" hasta −5.5 °C superficie. Caso local: Parque Isla Cautín, Temuco (ARQ 2023).

### D. Nivel calle / Green View Index
- **Treepedia (MIT)** depende de Google Street View → API masiva **paga**. Histórico solo visible manual.
- **Ruta gratis real: Mapillary** (imágenes de calle abiertas + API gratis) procesado con **AmericanRedCross/street-view-green-view** o **ZenSVI** → Green View Index.
- **Ventaja ciudadana:** si falta cobertura Mapillary en Temuco, Daniela y voluntarios **generan la suya** recorriendo Caupolicán/Alemania con el celular → registro abierto "antes/después" propio.

### E. Stack del observatorio ciudadano (todo gratis, sin backend)
- **GitHub Pages + Leaflet + tiles OpenStreetMap** para el mapa.
- Denuncias con foto+GPS: **KoBoToolbox** (open AGPL, offline, API) — o **Google Forms** para mínima fricción.
- Capa colaborativa sin programar: **uMap** (embebible).
- Árboles como GeoJSON propio o vía OSM/iNaturalist API.
- ❌ OpenTreeMap descartado: exige servidor PostGIS (no corre en Pages) y su SaaS pasó a pago.

### F. Contexto y fuentes locales (Chile / Temuco) — el ancla del proyecto
- **Angélica Lezano Vidal / ONG Verde Urbano** ("la Angélica" del audio) ya presentó ante el **Senado** ("Deforestación del arbolado urbano en Temuco", Boletín N°14.214-12, jul-2024). Casos con cifra: Arboleda de Fresnos Av. Olimpia (23 árboles), Barrio Coilaco, ampliación calle Imperial por SERVIU (>20 árboles). +1000 firmas ciudadanas.
- **Árboles patrimoniales** ya identificados por el **Laboratorio de Ecosistemas y Bosques, Universidad de La Frontera (UFRO)**.
- **IDE Temuco** (ide-munitemuco.hub.arcgis.com) — hub municipal VIVO con descarga GeoJSON/KML/GeoTIFF y WMS/WFS. **Posible fuente gratis de ortofoto fina — verificar años/resolución.**
- **IDE Chile** (ide.cl) — ortofotos alta-res descargables gratis. **IDE MINVU, INE geodatos, CONAF SIT** vivos.
- **SAF/FACh** (saf.cl) — archivo de fotografía aérea histórica (clave para 2005-2015) pero **gratuidad NO confirmada** (cotizar).
- Catastro de arbolado de Temuco: no confirmado público → pedir a SECPLA/transparencia. Referentes: Providencia (60.000 árboles), La Reina (35.995), Buenos Aires/Bogotá (datos abiertos).
- Marco político: **Estrategia Nacional de Infraestructura Verde 2025 (MMA-MINVU-FAO)** menciona atenuar islas de calor. Normas NCh 3524/3525/3701.
- Marco conceptual análogo: arXiv 2508.17648 "Citizen Centered Climate Intelligence" (ciencia ciudadana + árboles + LST + cooling metrics).

---

## 3. Arquitectura recomendada — "Observatorio de tres capas"

**Capa 1 — Radar (automatizable, 100% gratis, GEE):** NDVI + LST sobre Temuco 2000-2025. Mapa de pérdida de verdor y de calentamiento por sector; LandTrendr/CCDC para fechar el año de pérdida de cada parche. *Entrega el "dónde/cuándo" + la correlación árbol↔calor con cifra en °C.* Reutiliza pipeline CDSE de VegStress-v1 y térmico de Landsat-v1.

**Capa 2 — Evidencia de detalle (semi-manual, gratis) en corredores piloto** (Caupolicán, Imperial, Av. Olimpia): conteo de copas antes/después sobre Google Earth Pro histórico + i-Tree Canopy; si IDE Temuco/IDE Chile tienen ortofoto fina reciente → DeepForest para el estado actual; Green View Index con Mapillary/celular. *Entrega el "perdimos N árboles / X m² de sombra" irrebatible.*

**Capa 3 — Observatorio ciudadano vivo:** GitHub Pages + Leaflet; denuncias de podas/talas con foto+GPS vía KoBoToolbox; capa de patrimoniales (UFRO); integración del material que ya tienen.

**Giro estratégico:** liderar por el golpe demostrable (Capa 2 en un corredor + la cifra de calor de Capa 1), no por cubrir toda la ciudad.

---

## 4. Verificaciones pendientes antes de fijar arquitectura (candidatas a hacer con navegador)
1. **IDE Temuco / IDE Chile:** ¿qué ortofotos y de qué años/resolución? → decide si la Capa 2 puede usar IA (DeepForest) o queda en conteo manual.
2. **Google Earth Pro histórico sobre Temuco:** qué fechas cenital hay para 2005/2010/2015 en Caupolicán/Imperial.
3. **Yale UHI Explorer:** confirmar el dato de intensidad para Temuco.
4. **Catastro de arbolado Temuco:** pedir a SECPLA / vía Ley de Transparencia.
5. **Cobertura Mapillary** en corredores piloto.
