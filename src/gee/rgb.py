"""Composiciones de color real (true color) por año sobre Temuco.

Para "ver los cambios como en Google Earth". Combina dos fuentes según el año,
priorizando el mejor detalle disponible:
  - año >= 2016  -> Sentinel-2 (10 m, nítido)   B4-B3-B2
  - año <  2016  -> Landsat 5/8 (30 m)          SR_B(3/4)-B(2/3)-B(1/2)

Ambas se devuelven como reflectancia 0-1 en bandas [R, G, B] para visualizar
con el mismo estiramiento, de modo que la serie sea comparable a la vista.
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee._init import init_ee
from src.gee.ndvi_series import _mask_l2_c2, _rango_verano

S2 = "COPERNICUS/S2_SR_HARMONIZED"


def _s2_true_color(anio: int, aoi: "ee.Geometry") -> "ee.Image":
    d0, d1 = _rango_verano(anio)

    def _mask(img):
        scl = img.select("SCL")
        keep = (scl.neq(3).And(scl.neq(8)).And(scl.neq(9))
                .And(scl.neq(10)).And(scl.neq(11)))  # sombra, nubes, cirros
        return img.updateMask(keep)

    col = (ee.ImageCollection(S2)
           .filterBounds(aoi)
           .filterDate(d0, d1)
           .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 60))
           .map(_mask))
    rgb = col.select(["B4", "B3", "B2"]).median().multiply(1 / 10000)
    return rgb.rename(["R", "G", "B"]).clip(aoi)


def _landsat_true_color(anio: int, aoi: "ee.Geometry") -> "ee.Image":
    if anio <= 2012:
        col_id, bands = "LANDSAT/LT05/C02/T1_L2", ["SR_B3", "SR_B2", "SR_B1"]
    else:
        col_id, bands = "LANDSAT/LC08/C02/T1_L2", ["SR_B4", "SR_B3", "SR_B2"]
    d0, d1 = _rango_verano(anio)
    col = (ee.ImageCollection(col_id).filterBounds(aoi).filterDate(d0, d1)
           .map(_mask_l2_c2))

    def _sr(img):
        return img.select(bands).multiply(0.0000275).add(-0.2)

    rgb = col.map(_sr).median()
    return rgb.rename(["R", "G", "B"]).clip(aoi)


def rgb_anual(anio: int) -> "ee.Image":
    """Color real por año. Bandas [R, G, B] en reflectancia 0-1."""
    init_ee()
    aoi = get_aoi_temuco()
    if anio >= 2016:
        return _s2_true_color(anio, aoi)
    return _landsat_true_color(anio, aoi)
