"""Genera capas superponibles (overlays PNG transparentes) para el mapa interactivo.

Cada capa se renderiza en Web Mercator (EPSG:3857) sobre el mismo bbox urbano,
para que se alinee con el callejero OpenStreetMap en Leaflet. Las zonas sin dato
quedan transparentes (dejan ver las calles debajo).

Uso: python scripts/generar_overlays.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ee
from src.gee._init import init_ee
from src.gee.aoi_temuco import TEMUCO_BBOX
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.export import thumb_png

init_ee()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)
DIM = 1400
CRS = "EPSG:3857"  # Web Mercator: alinea con OSM/Leaflet

PAL_NDVI = ["#c8b18f", "#f7f7c8", "#a6d96a", "#1a9641", "#006837"]

ANIOS = [2014, 2016, 2018, 2020, 2022, 2024]


def _thumb(img_vis, path):
    """Thumbnail en Web Mercator sobre el bbox urbano (con transparencia por máscara)."""
    url = img_vis.getThumbURL({
        "region": urbano, "dimensions": DIM, "format": "png", "crs": CRS,
    })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    import urllib.request
    urllib.request.urlretrieve(url, path)


# NDVI por año (para el control temporal) — opaco, se regula con opacidad en Leaflet
for a in ANIOS:
    ndvi = ndvi_anual_landsat(a).visualize(min=0, max=0.85, palette=PAL_NDVI)
    _thumb(ndvi, f"docs/overlays/ndvi_{a}.png")
    print(f"  ndvi_{a}.png")

# Capa PÉRDIDA destacada: solo píxeles donde el NDVI cayó (2014->2024), en rojo.
delta = ndvi_anual_landsat(2024).subtract(ndvi_anual_landsat(2014)).rename("dNDVI")
perdida = delta.updateMask(delta.lt(-0.15))  # transparente salvo pérdida marcada
perdida_vis = perdida.visualize(min=-0.5, max=-0.15, palette=["#ff5a36", "#7a0000"])
_thumb(perdida_vis, "docs/overlays/perdida_2014_2024.png")
print("  perdida_2014_2024.png")

# Capa GANANCIA (contrapunto): píxeles donde el NDVI subió
ganancia = delta.updateMask(delta.gt(0.15))
ganancia_vis = ganancia.visualize(min=0.15, max=0.5, palette=["#78c679", "#00441b"])
_thumb(ganancia_vis, "docs/overlays/ganancia_2014_2024.png")
print("  ganancia_2014_2024.png")

# Bounds para Leaflet: [[sur, oeste], [norte, este]]
W, S, E, N = TEMUCO_BBOX
print(f"\nBOUNDS Leaflet: [[{S}, {W}], [{N}, {E}]]")
print("Overlays generados en docs/overlays/")
