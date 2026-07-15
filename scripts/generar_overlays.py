"""Genera capas superponibles (overlays PNG) para el mapa interactivo.

Todas en Web Mercator (EPSG:3857) sobre el mismo bbox urbano, alineadas con OSM.
Serie 2005-2024 (Landsat 5/8 + Sentinel-2), NDVI armonizado (Roy 2016).

Produce por año {2005,2010,2015,2020,2024}:
  - rgb_{año}.png          color real (Sentinel-2 10 m desde 2020, Landsat 30 m antes)
  - ndvi_{año}.png         índice de vegetación
  - perdida_2005_{año}.png pérdida de verde acumulada desde 2005 (dinámica)
  - arboles_perdida_{año}.png  pérdida acumulada solo donde había árboles
Además:
  - ganancia_2005_2024.png, tipo_veg_2024.png, canopy_height.png (altura de dosel, Meta)

Uso: python scripts/generar_overlays.py
"""
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ee
from src.gee._init import init_ee
from src.gee.aoi_temuco import TEMUCO_BBOX
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.rgb import rgb_anual
from src.gee.dynamicworld import clase_dominante, mascara_arboles

init_ee()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)
DIM = 1400
CRS = "EPSG:3857"

PAL_NDVI = ["#c8b18f", "#f7f7c8", "#a6d96a", "#1a9641", "#006837"]
BASE = 2005
ANIOS = [2005, 2010, 2015, 2020, 2024]
ANIOS_CAMBIO = [2010, 2015, 2020, 2024]  # 2005 = base


def _thumb(img_vis, path):
    url = img_vis.getThumbURL({"region": urbano, "dimensions": DIM, "format": "png", "crs": CRS})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)


ndvi_base = ndvi_anual_landsat(BASE)
arboles_ref = mascara_arboles(2016, umbral=0.5)  # DW arranca 2015 -> proxy arbolado

# 1) Color real + 2) NDVI por año
for a in ANIOS:
    _thumb(rgb_anual(a).visualize(min=0.0, max=0.30), f"docs/overlays/rgb_{a}.png")
    _thumb(ndvi_anual_landsat(a).visualize(min=0, max=0.85, palette=PAL_NDVI),
           f"docs/overlays/ndvi_{a}.png")
    print(f"  rgb_{a}.png + ndvi_{a}.png")

# 3) Pérdida acumulada desde 2005 (dinámica) + filtrada a árboles
for a in ANIOS_CAMBIO:
    delta = ndvi_anual_landsat(a).subtract(ndvi_base).rename("dNDVI")
    perdida = delta.updateMask(delta.lt(-0.15))
    _thumb(perdida.visualize(min=-0.5, max=-0.15, palette=["#ff5a36", "#7a0000"]),
           f"docs/overlays/perdida_2005_{a}.png")
    _thumb(perdida.updateMask(arboles_ref).visualize(min=-0.5, max=-0.15, palette=["#ff5a36", "#7a0000"]),
           f"docs/overlays/arboles_perdida_{a}.png")
    print(f"  perdida_2005_{a}.png + arboles_perdida_{a}.png")

# 4) Ganancia y 5) Tipo de vegetación
delta_full = ndvi_anual_landsat(2024).subtract(ndvi_base)
_thumb(delta_full.updateMask(delta_full.gt(0.15)).visualize(min=0.15, max=0.5, palette=["#78c679", "#00441b"]),
       "docs/overlays/ganancia_2005_2024.png")
label = clase_dominante(2024)
tipos = label.remap([1, 2, 4, 5], [0, 1, 2, 3]).updateMask(
    label.eq(1).Or(label.eq(2)).Or(label.eq(4)).Or(label.eq(5)))
_thumb(tipos.visualize(min=0, max=3, palette=["#1a6b34", "#cfe08a", "#e0a458", "#7a9e3c"]),
       "docs/overlays/tipo_veg_2024.png")
print("  ganancia_2005_2024.png + tipo_veg_2024.png")

# 6) Altura de dosel (Meta/WRI ~1 m) — distingue árbol por altura
try:
    canopy = ee.ImageCollection("projects/meta-forest-monitoring-okw37/assets/CanopyHeight").mosaic().clip(urbano)
    _thumb(canopy.updateMask(canopy.gt(1)).visualize(min=0, max=25, palette=["#f7fcb9", "#41ab5d", "#004529"]),
           "docs/overlays/canopy_height.png")
    print("  canopy_height.png (altura de dosel Meta)")
except Exception as e:
    print(f"  [canopy_height omitido: {e}]")

# --- Cifras para el dashboard ---
delta24 = ndvi_anual_landsat(2024).subtract(ndvi_base)
perd = delta24.lt(-0.15)
frac_urb = perd.reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["NDVI"]
frac_arb = perd.updateMask(arboles_ref).reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["NDVI"]
print(f"\nPérdida de verde 2005->2024 (área urbana): {frac_urb*100:.1f}%")
print(f"Pérdida de verde en zonas ARBÓREAS 2005->2024: {frac_arb*100:.1f}%")

W, S, E, N = TEMUCO_BBOX
print(f"BOUNDS Leaflet: [[{S}, {W}], [{N}, {E}]]")
print("Overlays generados en docs/overlays/")
