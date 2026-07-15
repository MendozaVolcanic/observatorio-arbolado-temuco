"""Tests de sanity de la Capa 1 (radar GEE) — observatorio arbolado Temuco.

Requieren conexión a Earth Engine (cuenta autenticada + GEE_PROJECT en .env).
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.lst_series import lst_anual
from src.gee.change_correlacion import correlacion_ndvi_lst


def test_aoi_temuco_bounds():
    """El AOI debe estar geográficamente sobre Temuco."""
    aoi = get_aoi_temuco()  # ee.Geometry
    c = aoi.centroid(1).coordinates().getInfo()  # [lon, lat]
    assert -72.8 < c[0] < -72.4, f"lon fuera de Temuco: {c[0]}"
    assert -38.9 < c[1] < -38.6, f"lat fuera de Temuco: {c[1]}"


def test_aoi_temuco_superficie():
    """El área del AOI debe rondar los 467 km² oficiales de la comuna."""
    aoi = get_aoi_temuco()
    area_km2 = aoi.area(maxError=10).divide(1e6).getInfo()
    assert 400 < area_km2 < 520, f"superficie inesperada: {area_km2:.1f} km²"


def test_ndvi_en_rango_fisico():
    """El NDVI debe estar en el rango físico [-1, 1]."""
    img = ndvi_anual_landsat(2020)  # ee.Image, banda 'NDVI'
    stats = img.reduceRegion(
        reducer=ee.Reducer.minMax(),
        geometry=get_aoi_temuco(),
        scale=30,
        maxPixels=int(1e9),
    ).getInfo()
    assert stats["NDVI_min"] is not None, "sin datos NDVI (¿todo enmascarado?)"
    assert -1.0 <= stats["NDVI_min"] <= stats["NDVI_max"] <= 1.0


def test_ndvi_vegetacion_positiva():
    """La mediana de NDVI en Temuco (ciudad arbolada) debe ser claramente positiva."""
    img = ndvi_anual_landsat(2020)
    med = img.reduceRegion(
        reducer=ee.Reducer.median(),
        geometry=get_aoi_temuco(),
        scale=30,
        maxPixels=int(1e9),
    ).getInfo()["NDVI"]
    assert med > 0.2, f"NDVI mediano inesperadamente bajo: {med}"


def test_lst_en_rango_razonable():
    """La temperatura de superficie (°C) debe estar en un rango físico plausible."""
    img = lst_anual(2020)  # banda 'LST' en °C
    stats = img.reduceRegion(
        reducer=ee.Reducer.minMax(),
        geometry=get_aoi_temuco(),
        scale=100,
        maxPixels=int(1e9),
    ).getInfo()
    assert stats["LST_min"] is not None, "sin datos LST"
    assert -20 <= stats["LST_min"] <= stats["LST_max"] <= 70, f"LST fuera de rango: {stats}"


def test_correlacion_ndvi_lst_negativa():
    """Más vegetación debe implicar superficie más fría (correlación negativa)."""
    r = correlacion_ndvi_lst(2024)
    assert r["correlation"] < -0.3, f"correlación no negativa: {r}"
