"""Cambio de vegetación y relación vegetación↔calor sobre Temuco.

- delta_ndvi: diferencia de NDVI entre dos años (mapa de pérdida/ganancia).
- correlacion_ndvi_lst: correlación de Pearson NDVI vs temperatura de superficie.
  Se espera NEGATIVA: donde hay más vegetación, la superficie está más fría
  (el efecto de enfriamiento del arbolado — la base del "menos árboles = más calor").
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.lst_series import lst_anual
from src.gee._init import init_ee


def delta_ndvi(anio_base: int, anio_act: int) -> "ee.Image":
    """NDVI(anio_act) - NDVI(anio_base). Banda 'dNDVI'. Negativo = pérdida de verde."""
    init_ee()
    d = ndvi_anual_landsat(anio_act).subtract(ndvi_anual_landsat(anio_base))
    return d.rename("dNDVI").clip(get_aoi_temuco())


def correlacion_ndvi_lst(anio: int, region: "ee.Geometry" = None) -> dict:
    """Correlación de Pearson NDVI vs LST en un año. Devuelve {correlation, p_value}."""
    init_ee()
    if region is None:
        region = get_aoi_temuco()
    stack = ndvi_anual_landsat(anio).addBands(lst_anual(anio))
    r = stack.reduceRegion(
        reducer=ee.Reducer.pearsonsCorrelation(),
        geometry=region,
        scale=30,
        maxPixels=int(1e9),
    ).getInfo()
    return {"correlation": r.get("correlation"), "p_value": r.get("p-value")}
