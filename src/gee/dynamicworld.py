"""Tipo de cobertura vegetal con Google Dynamic World (10 m, 2015+).

Dynamic World clasifica cada píxel en 9 clases con una probabilidad por clase.
Nos interesa distinguir árboles de pasto/arbusto/cultivo — el punto ciego del NDVI.

Clases (banda 'label', valor entero):
  0 agua · 1 árboles · 2 pasto · 3 veg. inundada · 4 cultivos
  5 arbustos/matorral · 6 construido · 7 suelo desnudo · 8 nieve
Solo disponible desde jun-2015.
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee._init import init_ee
from src.gee.ndvi_series import _rango_verano

DW = "GOOGLE/DYNAMICWORLD/V1"


def trees_prob_anual(anio: int) -> "ee.Image":
    """Probabilidad media de 'árboles' (0-1) en verano. Banda 'trees'."""
    init_ee()
    aoi = get_aoi_temuco()
    d0, d1 = _rango_verano(max(anio, 2016))  # DW arranca jun-2015
    col = ee.ImageCollection(DW).filterBounds(aoi).filterDate(d0, d1).select("trees")
    return col.mean().clip(aoi).rename("trees")


def clase_dominante(anio: int) -> "ee.Image":
    """Clase de cobertura dominante del año (moda de 'label'). Banda 'label'."""
    init_ee()
    aoi = get_aoi_temuco()
    d0, d1 = _rango_verano(max(anio, 2016))
    col = ee.ImageCollection(DW).filterBounds(aoi).filterDate(d0, d1).select("label")
    return col.mode().clip(aoi).rename("label")


def mascara_arboles(anio: int, umbral: float = 0.5) -> "ee.Image":
    """Máscara booleana: 1 donde la probabilidad de árbol supera el umbral."""
    return trees_prob_anual(anio).gte(umbral)
