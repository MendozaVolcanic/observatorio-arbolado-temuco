"""Serie NDVI anual sobre Temuco (Landsat Collection 2 Nivel 2, superficie).

Decisión de sensores (evita Landsat 7 SLC-off, que mete franjas sin dato):
  - año <= 2012  -> Landsat 5 TM   (LT05)
  - año >= 2013  -> Landsat 8 OLI  (LC08)
Cubre 2005-2025 con óptica gratuita. Composite de verano austral por defecto
(dic del año anterior a mar), la ventana menos nublada en La Araucanía.
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee._init import init_ee


def _mask_l2_c2(img: "ee.Image") -> "ee.Image":
    """Enmascara nube y sombra de nube usando QA_PIXEL (Collection 2 L2)."""
    qa = img.select("QA_PIXEL")
    cloud = qa.bitwiseAnd(1 << 3).eq(0)        # bit 3: cloud
    shadow = qa.bitwiseAnd(1 << 4).eq(0)       # bit 4: cloud shadow
    return img.updateMask(cloud.And(shadow))


def _scale_sr(img: "ee.Image", bands: list) -> "ee.Image":
    """Aplica el factor de escala de reflectancia de superficie C2 L2."""
    return img.select(bands).multiply(0.0000275).add(-0.2)


def _rango_verano(anio: int):
    """Verano austral: 1-dic del año previo a 1-mar del año dado."""
    return f"{anio - 1}-12-01", f"{anio}-03-01"


def ndvi_anual_landsat(anio: int, temporada: str = "verano") -> "ee.Image":
    """NDVI compuesto (mediana) sobre Temuco para un año.

    temporada: 'verano' (dic-feb, default) o 'anual' (todo el año).
    Devuelve ee.Image con banda 'NDVI'.
    """
    init_ee()
    aoi = get_aoi_temuco()

    if anio <= 2012:
        col_id, nir, red = "LANDSAT/LT05/C02/T1_L2", "SR_B4", "SR_B3"
    else:
        col_id, nir, red = "LANDSAT/LC08/C02/T1_L2", "SR_B5", "SR_B4"

    if temporada == "verano":
        d0, d1 = _rango_verano(anio)
    else:
        d0, d1 = f"{anio}-01-01", f"{anio}-12-31"

    col = (
        ee.ImageCollection(col_id)
        .filterBounds(aoi)
        .filterDate(d0, d1)
        .map(_mask_l2_c2)
    )

    def _ndvi(img: "ee.Image") -> "ee.Image":
        sr = _scale_sr(img, [nir, red])
        return sr.normalizedDifference([nir, red]).rename("NDVI")

    return col.map(_ndvi).median().clip(aoi).rename("NDVI")
