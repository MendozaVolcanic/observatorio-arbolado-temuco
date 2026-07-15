"""Tests de sanity de la Capa 1 (radar GEE) — observatorio arbolado Temuco.

Requieren conexión a Earth Engine (cuenta autenticada + GEE_PROJECT en .env).
"""
import ee
from src.gee.aoi_temuco import get_aoi_temuco


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
