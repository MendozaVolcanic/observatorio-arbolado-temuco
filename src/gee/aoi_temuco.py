"""AOI de la comuna de Temuco para GEE.

Fuente oficial: capa DPA_COMUNAS_2023 (División Político-Administrativa de Chile),
comuna cut_com=09101 (Temuco), descargada a datos/limite_comunal_temuco.geojson.
Superficie oficial ~466.78 km².

Si el GeoJSON no está disponible, cae a un bbox urbano provisional.
"""
import json
import os
import ee
from src.gee._init import init_ee

_GEOJSON = os.path.join(
    os.path.dirname(__file__), "..", "..", "datos", "limite_comunal_temuco.geojson"
)

# Fallback: bbox aproximado del área urbana de Temuco [W, S, E, N]
TEMUCO_BBOX = [-72.68, -38.78, -72.53, -38.68]

_aoi_cache = None


def get_aoi_temuco() -> "ee.Geometry":
    """Devuelve el límite comunal oficial de Temuco como ee.Geometry.

    Cae al bbox provisional si falta el GeoJSON.
    """
    global _aoi_cache
    init_ee()
    if _aoi_cache is not None:
        return _aoi_cache
    if os.path.exists(_GEOJSON):
        with open(_GEOJSON, encoding="utf-8") as f:
            fc = json.load(f)
        geom = fc["features"][0]["geometry"]
        _aoi_cache = ee.Geometry(geom, "EPSG:4326", geodesic=False)
    else:
        _aoi_cache = ee.Geometry.Rectangle(TEMUCO_BBOX)
    return _aoi_cache
