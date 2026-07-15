"""Temperatura de superficie (LST) anual sobre Temuco.

Usa el producto oficial Surface Temperature de Landsat Collection 2 Nivel 2
(banda ST_B*), ya calibrado y validado por USGS (corrección atmosférica de
single-channel). No requiere portar el algoritmo SMW de Ermida: para C2 L2 el
producto ST oficial es la vía más robusta y sin riesgo de traducción.

Escala C2 L2 ST -> Kelvin:  DN * 0.00341802 + 149.0  (luego -273.15 = °C)

Sensores (mismo criterio que ndvi_series):
  - año <= 2012  -> Landsat 5 TM   (banda ST_B6)
  - año >= 2013  -> Landsat 8 OLI  (banda ST_B10)
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee._init import init_ee
from src.gee.ndvi_series import _mask_l2_c2, _rango_verano


def lst_anual(anio: int, temporada: str = "verano") -> "ee.Image":
    """LST compuesta (mediana) sobre Temuco para un año, en °C. Banda 'LST'."""
    init_ee()
    aoi = get_aoi_temuco()

    if anio <= 2012:
        col_id, st_band = "LANDSAT/LT05/C02/T1_L2", "ST_B6"
    else:
        col_id, st_band = "LANDSAT/LC08/C02/T1_L2", "ST_B10"

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

    def _to_celsius(img: "ee.Image") -> "ee.Image":
        kelvin = img.select(st_band).multiply(0.00341802).add(149.0)
        return kelvin.subtract(273.15).rename("LST")

    return col.map(_to_celsius).median().clip(aoi).rename("LST")
