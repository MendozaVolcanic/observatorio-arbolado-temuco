"""Genera el primer dashboard visual del observatorio (mapas NDVI + cambio).

Produce PNGs estáticos en docs/img/ y no depende de tokens GEE en vivo,
así que la página resultante la puede ver cualquiera sin login ni cuota.

Uso: python scripts/generar_dashboard.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ee
from src.gee._init import init_ee
from src.gee.aoi_temuco import get_aoi_temuco, TEMUCO_BBOX
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.lst_series import lst_anual
from src.gee.change_correlacion import correlacion_ndvi_lst
from src.gee.export import thumb_png, con_borde

init_ee()
aoi = get_aoi_temuco()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)  # recorte del área urbana

# Paletas
PAL_NDVI = ["#c8b18f", "#f7f7c8", "#a6d96a", "#1a9641", "#006837"]  # suelo→bosque
PAL_DELTA = ["#8c1515", "#d73027", "#ffffbf", "#1a9850", "#006837"]  # pérdida→ganancia

ANIO_BASE, ANIO_ACT = 2014, 2024  # mismo sensor (L8) para el cambio

ndvi_base = ndvi_anual_landsat(ANIO_BASE)   # L8
ndvi_act = ndvi_anual_landsat(ANIO_ACT)     # L8
delta = ndvi_act.subtract(ndvi_base).rename("dNDVI")

# 1) NDVI actual, área urbana
thumb_png(
    con_borde(ndvi_act.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
    urbano, {}, "docs/img/ndvi_2024_urbano.png",
)
# 2) NDVI base, área urbana
thumb_png(
    con_borde(ndvi_base.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
    urbano, {}, "docs/img/ndvi_2013_urbano.png",
)
# 3) Cambio ΔNDVI 2013→2024, área urbana (rojo = pérdida de verde)
thumb_png(
    con_borde(delta.visualize(min=-0.3, max=0.3, palette=PAL_DELTA), aoi),
    urbano, {}, "docs/img/delta_ndvi_urbano.png",
)
# 4) Contexto: NDVI comuna completa
thumb_png(
    con_borde(ndvi_act.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
    aoi, {}, "docs/img/ndvi_2024_comuna.png",
)

# 5) Temperatura de superficie (LST) verano 2024, área urbana
PAL_LST = ["#2166ac", "#67a9cf", "#fddbc7", "#ef8a62", "#b2182b"]  # frío→caliente
lst_act = lst_anual(ANIO_ACT)
thumb_png(
    con_borde(lst_act.visualize(min=18, max=42, palette=PAL_LST), aoi),
    urbano, {}, "docs/img/lst_2024_urbano.png",
)

# Cifra: fracción de píxeles urbanos con pérdida marcada (ΔNDVI < -0.1)
perdida = delta.lt(-0.1)
frac = perdida.reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["dNDVI"]
print(f"Fracción área urbana con pérdida NDVI marcada (<-0.1) {ANIO_BASE}->{ANIO_ACT}: {frac*100:.1f}%")

# Cifra: correlación vegetación-temperatura (área urbana)
corr = correlacion_ndvi_lst(ANIO_ACT, urbano)["correlation"]
print(f"Correlación NDVI-LST área urbana {ANIO_ACT}: {corr:.2f}")
print("Mapas generados en docs/img/")
