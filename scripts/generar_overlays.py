"""Genera capas superponibles (overlays PNG transparentes) para el mapa interactivo.

Cada capa se renderiza en Web Mercator (EPSG:3857) sobre el mismo bbox urbano,
para que se alinee con el callejero OpenStreetMap en Leaflet.

Produce:
  - ndvi_{año}.png            vegetación (NDVI) por año
  - perdida_2014_{año}.png    pérdida de verde acumulada desde 2014 (dinámica)
  - arboles_perdida_{año}.png pérdida acumulada SOLO donde había árboles (Dynamic World)
  - ganancia_2014_2024.png    ganancia de verde
  - tipo_veg_2024.png         tipo de cobertura: árboles/pasto/arbustos/cultivos

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
from src.gee.dynamicworld import clase_dominante, mascara_arboles

init_ee()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)
DIM = 1400
CRS = "EPSG:3857"

PAL_NDVI = ["#c8b18f", "#f7f7c8", "#a6d96a", "#1a9641", "#006837"]
BASE = 2014
ANIOS = [2014, 2016, 2018, 2020, 2022, 2024]
ANIOS_CAMBIO = [2016, 2018, 2020, 2022, 2024]  # 2014 = base, sin pérdida


def _thumb(img_vis, path):
    url = img_vis.getThumbURL({"region": urbano, "dimensions": DIM, "format": "png", "crs": CRS})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)


ndvi_base = ndvi_anual_landsat(BASE)
# Máscara de arbolado de referencia (DW no cubre 2014 -> usa 2016, el más cercano)
arboles_ref = mascara_arboles(2016, umbral=0.5)

# 1) NDVI por año
for a in ANIOS:
    _thumb(ndvi_anual_landsat(a).visualize(min=0, max=0.85, palette=PAL_NDVI),
           f"docs/overlays/ndvi_{a}.png")
    print(f"  ndvi_{a}.png")

# 2) Pérdida de verde acumulada 2014->año (dinámica) y 3) filtrada a árboles
for a in ANIOS_CAMBIO:
    delta = ndvi_anual_landsat(a).subtract(ndvi_base).rename("dNDVI")
    perdida = delta.updateMask(delta.lt(-0.15))
    _thumb(perdida.visualize(min=-0.5, max=-0.15, palette=["#ff5a36", "#7a0000"]),
           f"docs/overlays/perdida_2014_{a}.png")
    # solo donde había árboles
    perdida_arb = perdida.updateMask(arboles_ref)
    _thumb(perdida_arb.visualize(min=-0.5, max=-0.15, palette=["#ff5a36", "#7a0000"]),
           f"docs/overlays/arboles_perdida_{a}.png")
    print(f"  perdida_2014_{a}.png + arboles_perdida_{a}.png")

# 4) Ganancia acumulada 2014->2024
delta_full = ndvi_anual_landsat(2024).subtract(ndvi_base).rename("dNDVI")
ganancia = delta_full.updateMask(delta_full.gt(0.15))
_thumb(ganancia.visualize(min=0.15, max=0.5, palette=["#78c679", "#00441b"]),
       "docs/overlays/ganancia_2014_2024.png")
print("  ganancia_2014_2024.png")

# 5) Tipo de vegetación (Dynamic World 2024): árboles / pasto / cultivos / arbustos
label = clase_dominante(2024)
tipos = label.remap([1, 2, 4, 5], [0, 1, 2, 3])  # solo clases vegetales
tipos = tipos.updateMask(label.eq(1).Or(label.eq(2)).Or(label.eq(4)).Or(label.eq(5)))
_thumb(tipos.visualize(min=0, max=3, palette=["#1a6b34", "#cfe08a", "#e0a458", "#7a9e3c"]),
       "docs/overlays/tipo_veg_2024.png")
print("  tipo_veg_2024.png  (arboles=verde oscuro, pasto=amarillo, cultivos=naranja, arbustos=oliva)")

W, S, E, N = TEMUCO_BBOX
print(f"\nBOUNDS Leaflet: [[{S}, {W}], [{N}, {E}]]")
print("Overlays generados en docs/overlays/")
