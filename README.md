# Observatorio Ciudadano de Arbolado Urbano de Temuco

Herramienta abierta y gratuita para **documentar la pérdida de arbolado urbano en Temuco
(2005-2024)**, vincularla con la expansión inmobiliaria y vial, y con el aumento de calor
superficial. Nace de una idea ciudadana y se apoya en la campaña de la ONG Verde Urbano
(presentada ante el Senado de Chile, Boletín N°14.214-12).

🌐 **Dashboard en vivo:** https://mendozavolcanic.github.io/observatorio-arbolado-temuco/
🗺️ **Mapa interactivo:** https://mendozavolcanic.github.io/observatorio-arbolado-temuco/mapa.html

> Herramienta de análisis ciudadano independiente. Los datos satelitales de media resolución
> muestran tendencias de cobertura, no un censo de árboles individuales (ver *Limitaciones*).

---

## 1. La idea (por qué existe)

Daniela, activista de Temuco, quería saber **cuánto arbolado se perdió, dónde, y si fue por
obras** (inmobiliarias o viales) — con un caso testigo: los árboles del bandejón de Av.
Caupolicán y la apertura hacia Pablo Neruda. Y llevarlo a un **observatorio ciudadano** que
sume las denuncias de podas y talas de la comunidad.

La transcripción original de la idea está en [`transcripcion.txt`](transcripcion.txt).

## 2. La verdad que ordena el método

**No existe ningún dato gratuito que dé "árbol por árbol" en serie temporal larga.**
- Lo gratuito que llega a 2005 vive a 30 m/píxel (Landsat) → ve *parches* de verde, no
  ejemplares. A esa escala un árbol de calle es más chico que un píxel.
- Lo que resuelve el árbol individual (Meta canopy 1 m) es de *una sola época*, no serie.
- Google Earth Pro tiene la imagen fina histórica, pero su licencia permite solo **conteo
  manual**, no alimentar una IA.

Por eso el diseño es de **tres capas**: un radar satelital automatizado (tendencia), un
conteo manual de detalle en corredores clave (la cifra irrebatible), y un observatorio
ciudadano que junta todo.

## 3. Metodología — las tres capas

### Capa 1 — Radar satelital (automatizado, Google Earth Engine)
Mide *dónde y cuándo* cambió el verde y *cuánto se calentó* la ciudad.
- **NDVI** (índice de vegetación) anual 2005-2024, con **Landsat 5/8 Colección 2 Nivel 2**
  (superficie), composites de **verano** (dic-feb) por mediana para sortear la nubosidad de
  la Araucanía. Bandas armonizadas entre sensores (Roy et al. 2016).
- **Pérdida de verde**: ΔNDVI respecto a 2005; se marcan en rojo los píxeles con caída
  fuerte (< −0.15).
- **Tipo de vegetación** (árbol vs pasto/arbusto): **Google Dynamic World** (10 m) para
  separar la clase "trees", ya que el NDVI solo no distingue un árbol de un pasto.
- **Altura de dosel**: mapa global de **Meta/WRI** (1 m) como referencia estructural.
- **Calor**: temperatura de superficie (**LST**) desde la banda térmica de Landsat
  (método de Ermida et al. 2020). Cruzada con el NDVI muestra la correlación
  árbol ↔ temperatura.
- **Años sin dato**: 2012-2013 quedan como hueco real (fin de Landsat 5, arranque de
  Landsat 8). El slider del mapa los salta automáticamente.

### Capa 2 — Detalle en corredores piloto (semi-manual)
La cifra "había N árboles y hoy quedan M", con área de sombra perdida.
- Corredores: **Av. Olimpia** (23 árboles ya documentados por la ONG = validación de
  terreno) y **Av. Caupolicán** (el caso emblemático).
- Imagen histórica de alta resolución en **Google Earth Pro** → conteo manual de copas
  (antes/después) → exportar a GeoJSON → validar contra el dato de la ONG → cruzar con el
  permiso de obra responsable.

### Capa 3 — Observatorio ciudadano (en construcción)
Sitio público (este repo, GitHub Pages) que integra los resultados + denuncias ciudadanas
de podas/talas con foto y GPS + árboles patrimoniales (catastro UFRO).

## 4. El código

Todo en Python + Google Earth Engine. Módulos en [`src/gee/`](src/gee/):

| Archivo | Qué hace |
|---|---|
| `_init.py` | Inicializa y autentica Google Earth Engine (`init_ee()`) |
| `aoi_temuco.py` | Área de estudio: límite comunal oficial de Temuco (`get_aoi_temuco()`) |
| `ndvi_series.py` | Serie NDVI anual con Landsat armonizado (`ndvi_anual_landsat(anio)`) |
| `lst_series.py` | Temperatura de superficie anual (`lst_anual(anio)`) |
| `dynamicworld.py` | Clase "trees" y máscara de árboles con Dynamic World |
| `rgb.py` | Composiciones de color real (Sentinel-2 / Landsat) por año |
| `change_correlacion.py` | ΔNDVI (pérdida/ganancia) y correlación NDVI↔LST |
| `export.py` | Exporta las imágenes GEE a PNG para el dashboard |

Scripts de orquestación en [`scripts/`](scripts/):

| Script | Qué produce |
|---|---|
| `generar_dashboard.py` | Los mapas del panel principal (`docs/img/`) y las cifras titulares |
| `generar_overlays.py` | La serie anual de capas superponibles del mapa + `anios.json` |
| `cruce_expansion.py` | Cruce de la pérdida de verde con los loteos/obras oficiales |

El frontend es estático: [`docs/index.html`](docs/index.html) (panel) y
[`docs/mapa.html`](docs/mapa.html) (mapa interactivo Leaflet con slider anual y capas
conmutables). Se publica solo con **GitHub Pages** (carpeta `docs/`).

## 5. Cómo reproducirlo

### Requisitos
```bash
pip install earthengine-api geemap rasterio geopandas numpy pandas matplotlib python-dotenv pytest
```
- **Cuenta de Google Earth Engine** (gratis, uso no comercial): registrarse en
  https://code.earthengine.google.com y crear un Cloud Project.

### Pasos
```bash
# 1. Autenticar Earth Engine (una vez)
earthengine authenticate

# 2. Generar los mapas del panel y las cifras
python scripts/generar_dashboard.py

# 3. Generar la serie anual de capas del mapa interactivo
python scripts/generar_overlays.py

# 4. (opcional) Cruce con expansión inmobiliaria
python scripts/cruce_expansion.py

# 5. Publicar: commit + push; GitHub Pages sirve la carpeta docs/
git add docs/ && git commit -m "update overlays" && git push
```

## 6. Fuentes de datos (todas gratuitas)

| Fuente | Uso | Acceso |
|---|---|---|
| Landsat 5/8 C2 L2 | NDVI y LST 2005-2024 | Google Earth Engine |
| Sentinel-2 | Color real reciente (2015+) | Google Earth Engine |
| Google Dynamic World | Clase "trees" 10 m | Google Earth Engine |
| Meta/WRI Canopy Height | Altura de dosel 1 m | Google Earth Engine |
| IDE Temuco | Loteos, permisos de edificación, límite comunal | ide-munitemuco.hub.arcgis.com |
| Google Earth Pro | Conteo manual de copas (Capa 2) | earth.google.com |

## 7. Limitaciones (honestas)

- **Resolución**: 30 m (Landsat) no resuelve el árbol de calle individual; la Capa 1 mide
  tendencia de parches, no un censo. El conteo exacto es la Capa 2 (manual).
- **Nubosidad**: Temuco es lluvioso; se usan composites de verano por mediana, pero algunos
  años quedan más ruidosos. 2012-2013 no tienen dato satelital confiable.
- **NDVI ≠ árboles**: se complementa con Dynamic World para separar árbol de pasto.
- **Correlación calor**: en clima húmedo puede ser más débil que en Santiago; se trata como
  hallazgo, no como resultado forzado.

## 8. Documentación y bibliografía

- **Plan maestro**: [`docs/plans/2026-07-15-observatorio-arbolado-temuco.md`](docs/plans/2026-07-15-observatorio-arbolado-temuco.md)
- **Síntesis de investigación**: [`bibliografia/SINTESIS_INVESTIGACION.md`](bibliografia/SINTESIS_INVESTIGACION.md)
- **Fichas por tema**: [`bibliografia/`](bibliografia/) (00-06 + fichas)
- **Skills de Claude Code usadas**: [`SKILLS_PROYECTO.md`](SKILLS_PROYECTO.md)

Papers clave: Ermida et al. 2020 (LST GEE) · Brown et al. 2022 (Dynamic World) ·
Weinstein et al. 2019 (DeepForest) · Sarricolea 2014 (ICU Santiago) · Zamorano 2011/2015
(Araucaria) · Lezano/ONG Verde Urbano 2024 (Senado). Los PDFs no se versionan por copyright.

## 9. Créditos

Idea: **Daniela** (Temuco). Campaña: **Angélica Lezano / ONG Verde Urbano**. Árboles
patrimoniales: **Laboratorio de Ecosistemas y Bosques, Universidad de La Frontera (UFRO)**.
Desarrollo técnico: Nicolás Mendoza + Claude Code. Datos: NASA/USGS, ESA, Google, Meta/WRI,
Municipalidad de Temuco.
