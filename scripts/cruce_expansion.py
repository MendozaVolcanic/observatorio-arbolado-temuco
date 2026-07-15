"""Cruce entre pérdida de verde y expansión inmobiliaria (loteos oficiales).

Compara la pérdida de NDVI 2005->2024 DENTRO de los loteos aprobados/recibidos
desde 2005 (dato oficial IDE Temuco) vs. el resto del área urbana. Si la pérdida
es mayor dentro de los loteos, la urbanización explica parte de la pérdida.

También escribe docs/data/loteos_recientes.geojson (loteos 2005+) para el mapa.

Uso: python scripts/cruce_expansion.py
"""
import os
import sys
import json
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ee
from src.gee._init import init_ee
from src.gee.aoi_temuco import TEMUCO_BBOX
from src.gee.ndvi_series import ndvi_anual_landsat

init_ee()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)


def _year(p):
    for campo in ("ap_fresol", "ru_frecep", "p_fresol"):
        v = p.get(campo)
        if v:
            try:
                return datetime.fromtimestamp(v / 1000, timezone.utc).year
            except Exception:
                pass
    v = p.get("l_ado")
    try:
        return int(str(v)[:4])
    except Exception:
        return None


src = json.load(open("datos/loteos_temuco.geojson", encoding="utf-8"))
recientes = []
for f in src["features"]:
    y = _year(f["properties"])
    if y and 2005 <= y <= 2024 and f["geometry"]:
        p = f["properties"]
        recientes.append({
            "type": "Feature", "geometry": f["geometry"],
            "properties": {"nombre": p.get("l_nombre"), "anio": y,
                           "viviendas": p.get("l_num_vivi"), "barrio": p.get("l_barrios")},
        })
print(f"Loteos 2005-2024 con geometría: {len(recientes)}")

# Guardar para el mapa
os.makedirs("docs/data", exist_ok=True)
json.dump({"type": "FeatureCollection", "features": recientes},
          open("docs/data/loteos_recientes.geojson", "w", encoding="utf-8"))

# Construir FeatureCollection en GEE y rasterizar (dentro de loteo = 1)
feats = [ee.Feature(ee.Geometry(f["geometry"]), {}) for f in recientes]
fc = ee.FeatureCollection(feats)
mask_loteo = ee.Image(0).paint(fc, 1).clip(urbano).selfMask()

delta = ndvi_anual_landsat(2024).subtract(ndvi_anual_landsat(2005)).rename("d")
perd = delta.lt(-0.15)

# Pérdida media dentro de loteos nuevos vs fuera (en área urbana)
dentro = perd.updateMask(mask_loteo).reduceRegion(
    ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["d"]
fuera = perd.updateMask(mask_loteo.unmask(0).Not()).reduceRegion(
    ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["d"]

print(f"Pérdida de verde DENTRO de loteos 2005+: {dentro*100:.1f}%")
print(f"Pérdida de verde FUERA de loteos:        {fuera*100:.1f}%")
if fuera:
    print(f"Los loteos nuevos perdieron {dentro/fuera:.1f}x más verde que el resto")
