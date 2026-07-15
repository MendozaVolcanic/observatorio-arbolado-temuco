"""Genera capas superponibles (overlays PNG) para el mapa interactivo, AÑO POR AÑO.

Todas en Web Mercator (EPSG:3857) sobre el bbox urbano, alineadas con OSM.
Serie anual 2005-2024 (Landsat 5/8 + Sentinel-2), NDVI armonizado (Roy 2016).
Años sin datos de satélite (gap Landsat 5→8, ~2012-2013) se saltan automáticamente.

Por cada año con datos:
  rgb_{a}.png · ndvi_{a}.png · perdida_2005_{a}.png · arboles_perdida_{a}.png
Fijas: ganancia_2005_2024.png · tipo_veg_2024.png · canopy_height.png
Escribe docs/overlays/anios.json con la lista de años disponibles (para el slider).

Uso: python scripts/generar_overlays.py
"""
import os
import sys
import json
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
PAL_LOSS = ["#ff5a36", "#7a0000"]
BASE = 2005
ANIOS = list(range(2005, 2025))


def _thumb(img_vis, path):
    url = img_vis.getThumbURL({"region": urbano, "dimensions": DIM, "format": "png", "crs": CRS})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)


def _tiene_datos(img):
    """True si la imagen tiene al menos una banda (composite no vacío)."""
    try:
        return img.bandNames().size().getInfo() > 0
    except Exception:
        return False


ndvi_base = ndvi_anual_landsat(BASE)
arboles_ref = mascara_arboles(2016, umbral=0.5)
disponibles = []

for a in ANIOS:
    ndvi = ndvi_anual_landsat(a)
    if not _tiene_datos(ndvi.select("NDVI")):
        print(f"  {a}: sin datos, se salta")
        continue
    try:
        _thumb(rgb_anual(a).visualize(min=0.0, max=0.30), f"docs/overlays/rgb_{a}.png")
        _thumb(ndvi.visualize(min=0, max=0.85, palette=PAL_NDVI), f"docs/overlays/ndvi_{a}.png")
        if a > BASE:
            delta = ndvi.subtract(ndvi_base).rename("dNDVI")
            perd = delta.updateMask(delta.lt(-0.15))
            _thumb(perd.visualize(min=-0.5, max=-0.15, palette=PAL_LOSS), f"docs/overlays/perdida_2005_{a}.png")
            _thumb(perd.updateMask(arboles_ref).visualize(min=-0.5, max=-0.15, palette=PAL_LOSS),
                   f"docs/overlays/arboles_perdida_{a}.png")
        disponibles.append(a)
        print(f"  {a}: ok")
    except Exception as e:
        print(f"  {a}: error ({str(e)[:60]}), se salta")

# Capas fijas
delta_full = ndvi_anual_landsat(2024).subtract(ndvi_base)
_thumb(delta_full.updateMask(delta_full.gt(0.15)).visualize(min=0.15, max=0.5, palette=["#78c679", "#00441b"]),
       "docs/overlays/ganancia_2005_2024.png")
label = clase_dominante(2024)
tipos = label.remap([1, 2, 4, 5], [0, 1, 2, 3]).updateMask(
    label.eq(1).Or(label.eq(2)).Or(label.eq(4)).Or(label.eq(5)))
_thumb(tipos.visualize(min=0, max=3, palette=["#1a6b34", "#cfe08a", "#e0a458", "#7a9e3c"]),
       "docs/overlays/tipo_veg_2024.png")
try:
    canopy = ee.ImageCollection("projects/meta-forest-monitoring-okw37/assets/CanopyHeight").mosaic().clip(urbano)
    _thumb(canopy.updateMask(canopy.gt(1)).visualize(min=0, max=25, palette=["#f7fcb9", "#41ab5d", "#004529"]),
           "docs/overlays/canopy_height.png")
except Exception as e:
    print(f"  [canopy omitido: {e}]")

with open("docs/overlays/anios.json", "w", encoding="utf-8") as f:
    json.dump(disponibles, f)
print(f"\nAños disponibles ({len(disponibles)}): {disponibles}")
print("Overlays generados en docs/overlays/")
